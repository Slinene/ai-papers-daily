---
title: Towards interpreting any residual stream direction by scaling activation inversion
title_zh: 通过扩展激活反演解释任意残差流方向
authors:
- Celeste De Schamphelaere
- Juan J. Vazquez
- Ari Spiesberger
- Tomáš Gavenčiak
- Gavin Leech
- Euan Ong
- Jiahai Feng
affiliations:
- MATS
- Arb Research
- Charles University
- Anthropic
arxiv_id: '2611.08465'
url: https://arxiv.org/abs/2611.08465
pdf_url: https://arxiv.org/pdf/2611.08465
published: '2026-11-05'
collected: '2026-11-08'
category: LLM
direction: LLM 可解释性 · 激活方向反演
tags:
- LLM interpretability
- activation inversion
- metamodel
- RL
- SAE
- steering vectors
one_liner: 训练元模型将残差流方向映射为最大化激活的文本，实现可验证的方向解释
practical_value: '- 在电商/推荐场景中，用户与商品 embedding 常被当作黑箱表示。可将 MAEM 思路迁移：训练一个小型生成模型，输入某个
  embedding 或方向向量，输出能强烈激活该向量的商品描述、用户评论或搜索词，从而解释 embedding 维度背后的语义（如价格敏感、品牌偏好、品类意图）。

  - 工程实现上，MAEM 采用无标签 RL 目标，最大化生成文本与目标方向在 frozen 模型各层激活的最大 cosine 相似度，不依赖人工标注。推荐系统中有大量未标注的行为序列向量、隐状态，可用类似目标训练从向量到文本的生成器，用于特征可视化和模型调试。

  - 验证方式值得借鉴：生成的解释文本可通过原模型 forward 计算真实激活相似度，提供 grounded 的可信度指标。在 Agent 系统中，可将模型决策点的残差方向转换为自然语言描述，辅助审计与人工校验，尤其适用于高风险推荐或合规审查。

  - 注意该方法需要训练较大规模的元模型，计算成本较高，且主要针对 LLM 内部表征。如果业务资源有限，可先用语料搜索作为 baseline，只在需要解释开放域方向时引入
  MAEM。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：解释语言模型残差流方向通常依赖在语料中搜索最大激活文本，但受限于语料内容；自然语言自编码器（NLA）生成的解释又无法直接验证。需要一种能生成任意方向对应文本、且可验证的方法。

**方法关键点**：提出最大激活示例元模型（MAEM），一个独立的语言模型，输入目标模型的残差流方向向量 v，输出文本 x。训练目标为无标签 RL：奖励是 v 与 x 在目标模型各层激活向量的最大余弦相似度。该方法不依赖标注数据，可扩展到多种来源的方向（steering vectors、SAE 特征、激活等）。生成文本可通过冻结目标模型 forward 验证真实性。

**关键结果**：训练 Qwen3.6-27B MAEM 后：在反演 held-out activations 上优于语料搜索和 NLA；在多数 held-out 语言/领域上超过 10M tokens 的语料搜索；激活了 89% 的 held-out SAE 特征；识别 steering vectors 概念与 NLA 相当；恢复 LoRA 后门 payload 优于语料搜索；能 verbalise 部分模型 workspace 内部独白。
