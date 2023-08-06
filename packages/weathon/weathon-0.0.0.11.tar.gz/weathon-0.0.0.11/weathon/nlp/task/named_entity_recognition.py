

import torch

from weathon.utils import conlleval
from weathon.nlp.factory.metric import SpanMetrics,BiaffineSpanMetrics
from weathon.nlp.task.token_classification import TokenClassificationTask


class BIONERTask(TokenClassificationTask):
    """
    BIO序列分类任务的Task
    
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

    def __init__(self, *args, **kwargs):

        super(BIONERTask, self).__init__(*args, **kwargs)

    def _evaluate_step_end(self, inputs, outputs, **kwargs):

        with torch.no_grad():
            # compute loss
            logits, loss = self._get_evaluate_loss(inputs, outputs, **kwargs)
            self.evaluate_logs['eval_loss'] += loss.item()

        self.evaluate_logs['labels'].append(inputs['label_ids'].cpu())
        self.evaluate_logs['logits'].append(logits.cpu())
        self.evaluate_logs['input_lengths'].append(inputs['input_lengths'].cpu())

        self.evaluate_logs['eval_example'] += len(inputs['label_ids'])
        self.evaluate_logs['eval_step'] += 1

    def _on_evaluate_epoch_end(
        self,
        validation_data,
        epoch=1,
        is_evaluate_print=True,
        id2cat=None,
        markup='bio',
        **kwargs
    ):

        if id2cat is None:
            id2cat = self.id2cat

        self.ner_metric = conlleval.SeqEntityScore(id2cat, markup=markup)
        preds_ = torch.argmax(torch.cat(self.evaluate_logs['logits'], dim=0), -1).numpy().tolist()
        labels_ = torch.cat(self.evaluate_logs['labels'], dim=0).numpy().tolist()
        input_lens_ = torch.cat(self.evaluate_logs['input_lengths'], dim=0).numpy()

        for index_, label_ in enumerate(labels_):
            label_list_ = []
            pred_list_ = []
            for jndex_, _ in enumerate(label_):
                if jndex_ == 0:
                    continue
                elif jndex_ == input_lens_[index_]-1:
                    self.ner_metric.update(
                        pred_paths=[pred_list_],
                        label_paths=[label_list_]
                    )
                    break
                else:
                    label_list_.append(labels_[index_][jndex_])
                    pred_list_.append(preds_[index_][jndex_])

        eval_info, entity_info = self.ner_metric.result()

        if is_evaluate_print:
            print('eval loss is {:.6f}, precision is:{}, recall is:{}, f1_score is:{}'.format(
                self.evaluate_logs['eval_loss'] / self.evaluate_logs['eval_step'],
                eval_info['acc'],
                eval_info['recall'],
                eval_info['f1'])
            )


class CRFNERTask(TokenClassificationTask):
    """
    +CRF命名实体模型的Task
    
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

    def _compute_loss(
        self,
        inputs,
        logits,
        verbose=True,
        **kwargs
    ):
        loss = -1 * self.model.crf(
            emissions=logits,
            tags=inputs['label_ids'].long(),
            mask=inputs['attention_mask']
        )

        return loss

    def _evaluate_step_end(self, inputs, outputs, **kwargs):

        with torch.no_grad():
            # compute loss
            logits, loss = self._get_evaluate_loss(inputs, outputs, **kwargs)

            tags = self.model.crf.decode(logits, inputs['attention_mask'])
            tags = tags.squeeze(0)

        self.evaluate_logs['labels'].append(inputs['label_ids'].cpu())
        self.evaluate_logs['logits'].append(tags.cpu())
        self.evaluate_logs['input_lengths'].append(inputs['input_lengths'].cpu())

        self.evaluate_logs['eval_example'] += len(inputs['label_ids'])
        self.evaluate_logs['eval_step'] += 1
        self.evaluate_logs['eval_loss'] += loss.item()

    def _on_evaluate_epoch_end(
        self,
        validation_data,
        epoch=1,
        is_evaluate_print=True,
        id2cat=None,
        markup='bio',
        **kwargs
    ):

        if id2cat is None:
            id2cat = self.id2cat

        self.ner_metric = conlleval.SeqEntityScore(id2cat, markup=markup)

        preds_ = torch.cat(self.evaluate_logs['logits'], dim=0).numpy().tolist()
        labels_ = torch.cat(self.evaluate_logs['labels'], dim=0).numpy().tolist()
        input_lens_ = torch.cat(self.evaluate_logs['input_lengths'], dim=0).numpy()

        for index_, label_ in enumerate(labels_):
            label_list_ = []
            pred_list_ = []
            for jndex_, _ in enumerate(label_):
                if jndex_ == 0:
                    continue
                elif jndex_ == input_lens_[index_]-1:
                    self.ner_metric.update(
                        pred_paths=[pred_list_],
                        label_paths=[label_list_]
                    )
                    break
                else:
                    label_list_.append(labels_[index_][jndex_])
                    pred_list_.append(preds_[index_][jndex_])

        eval_info, entity_info = self.ner_metric.result()

        if is_evaluate_print:
            print('eval loss is {:.6f}, precision is:{}, recall is:{}, f1_score is:{}'.format(
                self.evaluate_logs['eval_loss'] / self.evaluate_logs['eval_step'],
                eval_info['acc'],
                eval_info['recall'],
                eval_info['f1'])
            )


class BiaffineNERTask(TokenClassificationTask):
    """
    Biaffine命名实体模型的Task
    
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

    def _compute_loss(
        self,
        inputs,
        logits,
        verbose=True,
        **kwargs
    ):

        span_label = inputs['label_ids'].view(size=(-1,))
        span_logits = logits.view(size=(-1, self.class_num))

        span_loss = self.loss_function(span_logits, span_label.long())

        span_mask = inputs['span_mask'].view(size=(-1,))

        span_loss *= span_mask
        loss = torch.sum(span_loss) / inputs['span_mask'].size()[0]

        return loss

    def _evaluate_step_end(self, inputs, outputs, **kwargs):

        with torch.no_grad():
            # compute loss
            logits, loss = self._get_evaluate_loss(inputs, outputs, **kwargs)
            logits = torch.nn.functional.softmax(logits, dim=-1)
            self.evaluate_logs['eval_loss'] += loss.item()

        self.evaluate_logs['labels'].append(inputs['label_ids'].cpu())
        self.evaluate_logs['logits'].append(logits.cpu())

        self.evaluate_logs['eval_example'] += len(inputs['label_ids'])
        self.evaluate_logs['eval_step'] += 1

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

        biaffine_metric = BiaffineSpanMetrics()

        preds_ = torch.cat(self.evaluate_logs['logits'], dim=0)
        labels_ = torch.cat(self.evaluate_logs['labels'], dim=0)

        with torch.no_grad():
            recall, precise, span_f1 = biaffine_metric(preds_, labels_)

        if is_evaluate_print:
            print('eval loss is {:.6f}, precision is:{}, recall is:{}, f1_score is:{}'.format(
                self.evaluate_logs['eval_loss'] / self.evaluate_logs['eval_step'],
                precise,
                recall,
                span_f1)
            )


class GlobalPointerNERTask(TokenClassificationTask):
    """
    GlobalPointer命名实体模型的Task
    
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

    def _compute_loss(
        self,
        inputs,
        logits,
        verbose=True,
        **kwargs
    ):
        loss = self.loss_function(logits, inputs['label_ids'])

        return loss

    def _evaluate_begin_record(self, **kwargs):

        self.evaluate_logs['eval_loss'] = 0
        self.evaluate_logs['eval_step'] = 0
        self.evaluate_logs['eval_example'] = 0

        self.evaluate_logs['labels'] = []
        self.evaluate_logs['logits'] = []
        self.evaluate_logs['input_lengths'] = []

        self.evaluate_logs['numerate'] = 0
        self.evaluate_logs['denominator'] = 0

    def _evaluate_step_end(self, inputs, outputs, **kwargs):

        with torch.no_grad():

            # compute loss
            logits, loss = self._get_evaluate_loss(inputs, outputs, **kwargs)

            numerate, denominator = conlleval.global_pointer_f1_score(
                inputs['label_ids'].cpu(),
                logits.cpu()
            )
            self.evaluate_logs['numerate'] += numerate
            self.evaluate_logs['denominator'] += denominator

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

        if is_evaluate_print:
            print('eval loss is {:.6f}, precision is:{}, recall is:{}, f1_score is:{}'.format(
                self.evaluate_logs['eval_loss'] / self.evaluate_logs['eval_step'],
                self.evaluate_logs['numerate'],
                self.evaluate_logs['denominator'],
                2*self.evaluate_logs['numerate']/self.evaluate_logs['denominator'])
            )


class SpanNERTask(TokenClassificationTask):
    """
    Span模式的命名实体模型的Task
    
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
            start_score = start_score[1:length+1]
            end_score = end_score[1:length+1] 
            
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
