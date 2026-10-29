---
title: 'Follow the Gradient: Tracing Safety Degradation Back to Training Data'
title_zh: 跟随梯度：将安全退化追溯到训练数据
authors:
- Saket Reddy
- Amro Abbas
- Anshuman Suri
- Ari Morcos
- David Schwab
- Pratyush Maini
affiliations:
- DatologyAI
- University of Illinois Urbana-Champaign (UIUC)
arxiv_id: '2610.37481'
url: https://arxiv.org/abs/2610.37481
pdf_url: https://arxiv.org/pdf/2610.37481
published: '2026-10-27'
collected: '2026-10-29'
category: Training
direction: LLM 微调数据安全筛选
tags:
- gradient attribution
- data filtering
- safety alignment
- LoRA
- training data
one_liner: SimpleLoRIF 将低秩梯度归因扩至百万级数据，过滤梯度对齐不安全的样本，攻击成功率最高降22%
practical_value: '- 在微调推荐/Agent LLM 时，可用“梯度方向对齐目标/非目标行为”的分数筛选训练样本，去除与广告合规违规、品牌安全、诱导点击等不良输出梯度对齐的隐式风险数据，不依赖文本表面。

  - 工程实现上，只对最后 4 个 transformer blocks 回传并配合低秩投影计算梯度 embedding，可处理百万级样本；推荐团队可用类似方法对商品/query
  日志做安全与质量滤除，无需全模型回传。

  - 过滤比例与能力存在平衡：删除 top 20% 最对齐样本可显著降低攻击成功率且能力保持或提升；业务上可扫描过滤比例阈值，评估线上指标。

  - 可构建定制化数据过滤 pipeline，按比例或子集过滤风险数据；类似思路可迁移到搜索词改写、推荐理由生成等场景的合规性治理。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：指令微调数据即使表面良性也可能侵蚀模型安全，传统内容过滤难以识别这类安全退化样本。

方法关键点：SimpleLoRIF 简化低秩归因，仅对最后 4 层 transformer blocks 回传梯度，能够对百万级样本生成梯度 embedding；用样本梯度与不安全响应的对齐分数排序数据，删除 Tulu 3 中 top 20% 最对齐样本，构建 SafeTulu。

关键结果：在 emergent misalignment 场景，梯度可把不安全代码与有害输出聚在一起，AUC 最高 0.865；在 Qwen、Llama、Olmo 上训练 SafeTulu 使 GCG 攻击成功率最高下降 22%，优于 LLM-as-a-judge 与既有梯度过滤，同时能力基本保持或提升；删除数据还揭示工具执行失败、叙事算术等潜在不安全来源，并发布 SafeTulu 数据集与 HuggingFace Space。
