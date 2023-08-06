# -*- coding: utf-8 -*-
# @Time    : 2022/10/3 16:26
# @Author  : LiZhen
# @FileName: bert.py
# @github  : https://github.com/Lizhen0628
# @Description:


import torch
from torch import nn
from torch import Tensor
from transformers import BertPreTrainedModel, AutoModel, AutoConfig, BertConfig, BertModel, PretrainedConfig


class Bert(BertPreTrainedModel):
    """
    原始的BERT模型

    Args:
        transformer_model_name: transformers 模型名称 或 模型路径
        num_labels: 标签数量
        encoder_trained (:obj:`bool`, optional, defaults to True):
            bert参数是否可训练，默认可训练
        pooling (:obj:`str`, optional, defaults to "cls"):
            bert输出的池化方式，默认为"cls_with_pooler"，
            可选有["cls", "cls_with_pooler", "first_last_avg", "last_avg", "last_2_avg"]

    Reference:
        [1] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding  
    """  # noqa: ignore flake8"

    def __init__(self, config: PretrainedConfig, encoder_trained=True, pooling='cls_with_pooler'):
        super(Bert, self).__init__(config)
        self.bert = BertModel(config) if 'albert' in config.name_or_path.lower() else AutoModel.from_pretrained(
            config=config)
        self.pooling = pooling
        for param in self.bert.parameters():
            param.requires_grad = encoder_trained

        self.num_labels = config.num_labels
        self.dropout = nn.Dropout(config.hidden_dropout_prob)
        self.classifier = nn.Linear(config.hidden_size, self.num_labels)

        self.init_weights()

    def mask_pooling(self, x: Tensor, attention_mask=None):
        if attention_mask is None:
            return torch.mean(x, dim=1)
        return torch.sum(x * attention_mask.unsqueeze(2), dim=1) / torch.sum(attention_mask, dim=1, keepdim=True)

    def sequence_pooling(self, sequence_feature, attention_mask, pooling):

        if pooling is None:
            pooling = self.pooling

        if pooling == 'cls_with_pooler':
            return sequence_feature.pooler_output
        sequence_feature = sequence_feature.hidden_states
        if pooling == 'first_last_avg':
            sequence_feature = sequence_feature[-1] + sequence_feature[1]
        elif pooling == 'last_avg':
            sequence_feature = sequence_feature[-1]
        elif pooling == 'last_2_avg':
            sequence_feature = sequence_feature[-1] + sequence_feature[-2]
        elif pooling == 'cls':
            return sequence_feature[-1][:, 0, :]
        else:
            raise Exception("unknown pooling {}".format(pooling))

        return self.mask_pooling(sequence_feature, attention_mask)

    def get_encoder_feature(self, encoder_output, attention_mask, pooling=None):
        if self.task == 'SequenceLevel':
            return self.sequence_pooling(encoder_output, attention_mask, pooling)
        elif self.task == 'TokenLevel':
            return encoder_output['last_hidden_state']
        else:
            return encoder_output.last_hidden_state[:, 0, :]

    def forward(
            self,
            input_ids=None,
            attention_mask=None,
            token_type_ids=None,
            position_ids=None,
            **kwargs
    ):

        outputs = self.bert(input_ids, attention_mask=attention_mask, token_type_ids=token_type_ids,
                            position_ids=position_ids, return_dict=True, output_hidden_states=True)
        encoder_feature = self.get_encoder_feature(outputs, attention_mask)
        encoder_feature = self.dropout(encoder_feature)
        out = self.classifier(encoder_feature)
        return out


class BertForSequenceClassification(Bert):

    def __init__(self, config: PretrainedConfig, encoder_trained: bool = True, pooling='cls_with_pooler'):
        super(BertForSequenceClassification, self).__init__(config, encoder_trained=encoder_trained, pooling=pooling)
        self.task = 'SequenceLevel'


class BertForTokenClassification(Bert):
    """
    Args:
        config: 模型的配置对象
        encoder_trained (:obj:`bool`, optional, defaults to True): bert参数是否可训练，默认可训练
    Reference:
        [1] BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding  
    """  # noqa: ignore flake8"

    def __init__(self, config: PretrainedConfig, encoder_trained: bool = True):
        super(BertForTokenClassification, self).__init__(config, encoder_trained=encoder_trained)
        self.task = 'TokenLevel'
