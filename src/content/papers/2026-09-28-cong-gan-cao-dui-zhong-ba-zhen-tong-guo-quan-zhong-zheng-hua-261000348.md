---
title: 'Removing the NEEDLE in the Haystack: Backdoor Removal in LLMs via Weight Orthogonalisation'
title_zh: 从干草堆中拔针：通过权重正交化移除 LLM 后门
authors:
- Minoo Kim
- Vasileios Lampos
- George Drayson
affiliations:
- Locai Labs
- Centre for AI, Computer Science, UCL
arxiv_id: '2610.00348'
url: https://arxiv.org/abs/2610.00348
pdf_url: https://arxiv.org/pdf/2610.00348
published: '2026-09-28'
collected: '2026-10-03'
category: LLM
direction: LLM 安全防御 · 权重正交化
tags:
- backdoor defense
- weight orthogonalisation
- LLM safety
- activation steering
- training-free
one_liner: 训练免清洗方法估计后门方向与拒绝子空间，对权重正交化，在保持安全能力的同时实现最低 ASR
practical_value: '- 若业务中微调或使用开源 LLM 作为导购/客服/推荐 Agent，上游权重可能被投毒；NEEDLE 提供一种无需干净基线和原始训练数据的应急修复手段，适合已上线模型的后门摘除。

  - 其“估计激活方向 → 权重正交投影”的思路可推广到业务中的模型行为纠正：例如用少量对比样本估计生成式推荐模型中的偏见、幻觉或不合规输出方向，通过投影移除，无需全量微调。

  - 保留拒绝子空间的做法可作为模型编辑的约束：在修改推荐/Agent 模型权重时，显式保持安全对齐相关表示不变，降低对拒绝、安全审核、对话质量等下游能力的附带损害。

  - 评估体系可借鉴：线上模型任何补丁/编辑/校准，除了效果指标，应同时监控 ASR、KL 散度与能力基准，避免治好后门却牺牲推荐/对话质量。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM 后门攻击隐蔽，训练数据被投毒后模型在特定 trigger 下产生恶意行为。现有防御在移除后门时往往会偏移模型对良性输入的输出分布，导致基础能力与安全性下降。

方法：NEEDLE 是一种训练免清洗（training-free）的定向后门移除方法。在 trigger 已识别的前提下，它通过激活向量估计后门方向与拒绝子空间；然后对权重执行顺序正交化（sequential weight orthogonalisation），抑制后门相关表示，同时保留拒绝相关表示不被改变。整个过程不需要干净参考模型，也不需要原始被投毒的训练数据。

结果：在多个模型家族和多种攻击类型上评估，NEEDLE 取得所有防御方法中最低的平均 Attack Success Rate (ASR)，在具有挑战性的代码注入攻击上达到 0% ASR；同时 KL 散度最低，模型能力和安全性变化最小。
