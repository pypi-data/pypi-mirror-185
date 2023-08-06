import torch
from weathon.utils import conlleval
from weathon.nlp.factory.metric import SpanMetrics
from weathon.nlp.task import TokenClassificationTask


class SpanNERTask(TokenClassificationTask):
    """
    Span模式的命名实体识别Task
    
    Args:
        module: 深度学习模型
        optimizer: 训练模型使用的优化器名或者优化器对象
        loss_function: 训练模型使用的损失函数名或损失函数对象
        class_num (:obj:`int` or :obj:`None`, optional, defaults to None): 标签数目
        scheduler (:obj:`class`, optional, defaults to None): scheduler对象
        n_gpu (:obj:`int`, optional, defaults to 1): GPU数目
        device (:obj:`class`, optional, defaults to None): torch.device对象，当device为None时，会自动检测是否有GPU
        cuda_device (:obj:`int`, optional, defaults to 0): GPU编号，当device为None时，根据cuda_device设置device
        ema_decay (:obj:`int` or :obj:`None`, optional, defaults to None): EMA的加权系数
        **kwargs (optional): 其他可选参数
    """  # noqa: ignore flake8"

    def _get_train_loss(
            self,
            inputs,
            outputs,
            **kwargs
    ):
        loss = self._compute_loss(inputs, outputs, **kwargs)

        self._compute_loss_record(**kwargs)

        return outputs, loss

    def _get_evaluate_loss(
            self,
            inputs,
            outputs,
            **kwargs
    ):
        loss = self._compute_loss(inputs, outputs, **kwargs)
        self._compute_loss_record(**kwargs)

        return outputs, loss

    def _compute_loss(
            self,
            inputs,
            logits,
            verbose=True,
            **kwargs
    ):
        start_logits = logits[0]
        end_logits = logits[1]

        start_logits = start_logits.view(-1, len(self.id2cat))
        end_logits = end_logits.view(-1, len(self.id2cat))

        active_loss = inputs['attention_mask'].view(-1) == 1

        active_start_logits = start_logits[active_loss]
        active_end_logits = end_logits[active_loss]

        active_start_labels = inputs['start_label_ids'].long().view(-1)[active_loss]
        active_end_labels = inputs['end_label_ids'].long().view(-1)[active_loss]

        start_loss = self.loss_function(
            active_start_logits,
            active_start_labels
        )
        end_loss = self.loss_function(
            active_end_logits,
            active_end_labels
        )

        loss = start_loss + end_loss

        return loss

    def _on_evaluate_epoch_begin(self, **kwargs):

        self.metric = SpanMetrics(self.id2cat)

        if self.ema_decay:
            self.ema.store(self.model.parameters())
            self.ema.copy_to(self.model.parameters())

        self._epoch_begin_record(**kwargs)

    def _evaluate_step_end(self, inputs, logits, **kwargs):

        with torch.no_grad():
            # compute loss
            logits, loss = self._get_evaluate_loss(inputs, logits, **kwargs)

        length = inputs['attention_mask'].cpu().numpy().sum() - 2

        S = []
        start_logits = logits[0]
        end_logits = logits[1]

        start_score_list = torch.argmax(start_logits, -1).cpu().numpy()
        end_score_list = torch.argmax(end_logits, -1).cpu().numpy()

        for index, (start_score, end_score) in enumerate(zip(start_score_list, end_score_list)):
            start_score = start_score[1:length + 1]
            end_score = end_score[1:length + 1]

            S = []
            for i, s_l in enumerate(start_score):
                if s_l == 0:
                    continue
                for j, e_l in enumerate(end_score[i:]):
                    if s_l == e_l:
                        S.append((s_l, i, i + j))
                        break

            self.metric.update(true_subject=inputs['label_ids'][index], pred_subject=S)

        self.metric.update(true_subject=inputs['label_ids'][0], pred_subject=S)

        self.evaluate_logs['eval_example'] += len(inputs['label_ids'])
        self.evaluate_logs['eval_step'] += 1
        self.evaluate_logs['eval_loss'] += loss.item()

    def _on_evaluate_epoch_end(
            self,
            validation_data,
            epoch=1,
            is_evaluate_print=True,
            id2cat=None,
            **kwargs
    ):

        if id2cat is None:
            id2cat = self.id2cat

        with torch.no_grad():
            eval_info, entity_info = self.metric.result()

        if is_evaluate_print:
            print('eval_info: ', eval_info)
            print('entity_info: ', entity_info)

    def _train_collate_fn(self, batch):
        """将InputFeatures转换为Tensor"""

        input_ids = torch.tensor([f['input_ids'] for f in batch], dtype=torch.long)
        attention_mask = torch.tensor([f['attention_mask'] for f in batch], dtype=torch.long)
        token_type_ids = torch.tensor([f['token_type_ids'] for f in batch], dtype=torch.long)
        start_label_ids = torch.cat([f['start_label_ids'] for f in batch])
        end_label_ids = torch.cat([f['end_label_ids'] for f in batch])
        label_ids = [f['label_ids'] for f in batch]

        tensors = {
            'input_ids': input_ids,
            'attention_mask': attention_mask,
            'token_type_ids': token_type_ids,
            'start_label_ids': start_label_ids,
            'end_label_ids': end_label_ids,
            'label_ids': label_ids
        }

        return tensors

    def _evaluate_collate_fn(self, batch):
        return self._train_collate_fn(batch)
