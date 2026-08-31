---
title: When Linguistic and Internal Confidence Diverge in Large Language Models
title_zh: 大语言模型中语言置信度与内部置信度的分歧
authors:
- Hefan Zhang
- Bingquan Zhang
- Ming Cheng
- Saeed Hassanpour
- Weicheng Ma
- Soroush Vosoughi
affiliations:
- Dartmouth College
- Oakland University
arxiv_id: '2608.28382'
url: https://arxiv.org/abs/2608.28382
pdf_url: https://arxiv.org/pdf/2608.28382
published: '2026-08-28'
collected: '2026-08-31'
category: Eval
direction: LLM 置信度评估与校准
tags:
- LLM
- confidence calibration
- uncertainty estimation
- verbalized confidence
- logits
- selective prediction
one_liner: 系统评估 30 个 LLM 的语言置信度与内部置信度在分类/生成任务上的关联、量级和校准分歧
practical_value: '- 在电商/Agent 流程中若使用 LLM 自报置信度做拒答、路由或加权，不要默认其与内部概率一致；先做多轴诊断：实例级 Spearman/关联、平均置信度差异、ECE/校准曲线。尤其指令调优模型可能高报置信度且校准更差。

  - 如果只能拿到语言置信度，优先用“分数示例”prompt 且避免置信度值塌缩（如全 5 分或全高），这样能保留一定 rank-order 信息用于排序/过滤；纯态度引导（“请更谨慎”）只会抬高/降低数值，不改善与真实质量的
  alignment。

  - 在生成式推荐或文案生成场景，可以用 semantic entropy 或多次采样一致性作为内部不确定性替代语言置信度；若不能用 logits，可让模型输出
  1-5 分而非自然语言模糊词，并做分布检查。

  - 工程上按 task difficulty/基座能力分层：简单样本或强 base 模型的置信度更有参考价值；复杂长尾商品/query 不要依赖语言置信度做硬过滤。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
LLM 经常被要求报告置信度，但语言层面的自我置信是否忠实反映内部置信度并不清楚。这直接影响下游是否能用它做选择性预测、拒答或加权融合。  

**方法与关键结果**  
在 8 个分类任务、2 个生成任务和 30 个模型（三个家族）上，将语言置信度与 logits 置信度沿三个轴比较：实例级关联、量级一致性和校准；生成任务则用 semantic entropy 作为内部不确定性。结果发现各轴经常分歧：实例级关联平均较弱，但在简单样本和更强基座模型上有所改善；指令调优模型报告的置信度更高，有时关联也更高，但置信度差距更大、校准更差。Prompt 设计主要改变语言置信度的分布：态度提示会膨胀置信度却不改善对齐；分数示例如果避免数值塌缩，能保留一定秩序信号。回归分析显示置信度分数的分布属性解释了大部分观测到的对齐模式，模型元数据在控制后作用较小。  

**结论**  
支持“有损信道”观点：更分散的语言置信度分布可以携带有用的秩信息，但不会使其校准。语言置信度用于可靠性流水线前，必须用多轴诊断评估。
