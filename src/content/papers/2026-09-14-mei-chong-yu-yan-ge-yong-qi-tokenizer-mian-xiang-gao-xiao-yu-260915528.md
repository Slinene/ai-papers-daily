---
title: 'To Each Language Its Tokenizer: Modular Tokenizers for Efficient Multilingual
  LLMs'
title_zh: 每种语言各用其 tokenizer：面向高效多语言 LLM 的模块化 tokenizer
authors:
- Franck Signe
- Hippolyte Pilchen
- François Yvon
- Édouard Grave
affiliations:
- Kyutai
- Sorbonne Université
- CNRS
- Univ. Grenoble Alpes
- Grenoble INP
arxiv_id: '2609.15528'
url: https://arxiv.org/abs/2609.15528
pdf_url: https://arxiv.org/pdf/2609.15528
published: '2026-09-14'
collected: '2026-09-15'
category: Training
direction: 多语言模块化 tokenizer 与高效训练
tags:
- tokenizer
- multilingual
- LLM
- BPE
- Unigram
- efficient inference
one_liner: 提出模块化多语言 tokenizer 与预训练策略，可按语言子集提取子词表并动态使用，降低内存并加速推理
practical_value: '- 部署多语言 LLM 服务（国际化电商搜索、海外广告文案生成）时，可为高频语言子集抽取轻量 subtokenizer，只保留对应子词表，大幅缩小
  embedding / output 矩阵，降低内存占用与推理延迟，尤其适合小模型或边缘场景。

  - 模块化 tokenizer 思路可迁移到多领域/多场景文本：按业务类目、品牌、商品描述等定制子词表，训练或推理时动态激活子 vocab，减少大而全词表的冗余计算。

  - 预训练中按 batch 采样 subtokenizer 并将预测限制在相关词汇子集，既能保持大词表覆盖，又能降低 softmax 开销；可参考用于多任务、多场景
  LLM 的训练优化。

  - 该方法本质是 tokenizer 与 embedding 层的基础优化，若你的业务使用 LLM 做生成式推荐或 QueryRec，且面临多语言、大词表成本问题，可借鉴其模块化设计；否则业务可借鉴点有限。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：多语言 LLM 传统上使用单一共享词表，导致跨语言压缩率不均；大 embedding 和输出矩阵增加内存并拖慢推理，对小模型尤其浪费，而实际模型往往只用少量语言子集。

方法关键点：论文提出模块化多语言训练框架。首先学习大型模块化 BPE / Unigram tokenizer，能提取面向任意语言子集的 subtokenizer；这些 subtokenizer 实现与单语 tokenizer 相当的压缩率，并改善跨语言公平性。其次设计预训练策略：按 batch 采样 subtokenizer，将预测限制在对应的词汇子集上，从而在大词表下也能高效训练；推理时可按任意语言组合使用子词表，减少内存并加速，且不牺牲性能。

关键结果：摘要未给具体数值，但展示 subtokenizer 的压缩率与单语 tokenizer 相当、公平性提升；在支持高效推理的同时保持模型性能，代码已开源。
