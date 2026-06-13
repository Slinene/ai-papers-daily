---
title: 'Influcoder: Distilling Decoders'' Gradient Influence Rankings into an Encoder
  for Data Attribution'
title_zh: Influcoder：将解码器梯度影响排名蒸馏至编码器以加速数据归因
authors:
- Dimitri Kachler
- Damien Sileo
- Pascal Denis
affiliations:
- Centre Inria de l'Université de Lille
- CRIStAL
- Université de Lille
arxiv_id: '2606.13668'
url: https://arxiv.org/abs/2606.13668
pdf_url: https://arxiv.org/pdf/2606.13668
published: '2026-06-11'
collected: '2026-06-13'
category: Other
direction: 数据归因 · 影响函数加速
tags:
- Data Attribution
- Influence Functions
- Knowledge Distillation
- LLM Training
- Model Efficiency
one_liner: 通过将解码器梯度影响排名蒸馏为编码器直接输出，实现大规模数据归因的快速近似。
practical_value: '- **大规模数据排查加速**：在推荐/Agent 模型出现异常行为（如偏见、违规输出）时，需快速定位有害训练样本。Influcoder
  用轻量编码器替代逐样本梯度计算，可在电商场景中用于快速检索“中毒”样本，大幅缩短排查周期。

  - **训练数据在线过滤**：若已有标注的好/坏样本集，可参照 Influcoder 的排名蒸馏思想，训练一个小型影响评分模型，实时判断新采集的日志样本是否值得加入训练，避免离线全量重算影响函数。

  - **蒸馏目标的迁移**：方法中的 pairwise 排名损失（使编码器输出排序与真实影响排序一致）可借鉴到其他需要“排序替代计算”的场景，例如召回阶段对候选
  item 的重要性排序、特征选择或数据增强样本的优先级评估。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：传统基于影响函数（Influence Functions）的数据归因方法需要为每个训练样本计算梯度，难以扩展至海量数据，无法用于大规模预训练数据的快速筛选与审计。

**方法**：提出 Influcoder，将解码器（LLM）的梯度影响排名蒸馏到一个轻量编码器中。训练时，先用解码器对部分样本计算精确的影响分数，然后训练一个编码器（如 BERT）以 pairwise 排名损失模仿这些影响排序。推理时，编码器可直接输出任意样本的影响估计，无需重复梯度计算。

**关键结果**：在检测有害训练样本等任务上，Influcoder 的排序相关性（如 Spearman ρ）可达到原始影响函数的 80%~90%，但计算速度提升数个数量级，模型存储仅需编码器参数，无需保存海量梯度。方法在跨模型迁移中亦表现稳健，蒸馏出的编码器可用于不同于原解码器的模型。
