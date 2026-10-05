---
title: 'Pivot-SD: Efficient Self-Distillation for Masked Diffusion Language Models'
title_zh: Pivot-SD：掩码扩散语言模型的高效自蒸馏
authors:
- Seo Hyun Kim
- Sunwoo Hong
- Younwoo Choi
- Chen-Hao Chao
- Se-Young Yun
- Rahul G. Krishnan
affiliations:
- KAIST AI
- University of Toronto
- Vector Institute
arxiv_id: '2610.03665'
url: https://arxiv.org/abs/2610.03665
pdf_url: https://arxiv.org/pdf/2610.03665
published: '2026-10-02'
collected: '2026-10-05'
category: Training
direction: 掩码扩散 LM 后训练 · 自蒸馏
tags:
- diffusion language models
- self-distillation
- credit assignment
- reasoning
- post-training
one_liner: 用信息增益筛选高影响力掩码 token 进行自蒸馏，提升扩散语言模型推理性能
practical_value: '- 在生成式推荐或 Agent 训练中，可用信息增益等指标识别对最终结果影响最大的中间决策 token（如商品属性、工具调用参数），只对关键
  token 做监督，降低训练噪声和计算开销。

  - 对失败轨迹不要整条丢弃，定位导致失败的 pivot token 使用 targeted unlikelihood，其余 token 保持原样，可以保留有效探索、避免过度惩罚。

  - 自蒸馏/离线 RL 中只需少量 query（200 个）和 rollout（每个 4 次）即可达到超过全序列 SFT 和预算匹配 RL 的效果，适合标注和算力受限的业务场景。

  - 掩码扩散模型在生成式推荐（如 Semantic ID 生成）中逐步填充 token，可将每一步的 uncertainty reduction 作为信号，动态决定训练重点或推理早停条件。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：掩码扩散语言模型（dLMs）作为自回归模型的并行替代，在复杂推理上展现出潜力，但面临信用分配难题——去噪过程中少数 token 的“承诺”会大幅降低剩余 mask 位置的不确定性，并塑造最终回复。现有后训练方法（SFT 或 RL）通常训练最终文本或对整个去噪步骤赋奖励，未识别这些关键 token，导致训练效率低且容易受无关 token 干扰。

**方法关键点**：Pivot-SD 是一种离线自蒸馏框架，只监督高影响力的“pivot” token。它利用信息增益度量计算每个 token 承诺对剩余 mask 位置不确定性的减少，选择 top pivots。成功轨迹中的 pivot 用交叉熵训练；失败轨迹中的 pivot 用 targeted unlikelihood 训练，其余 token 保持原样。这种选择性策略聚焦决策关键点，同时避免失败轨迹的噪声覆盖有效探索。

**关键结果**：仅使用 200 个问题、每个问题 4 次 rollout，Pivot-SD 在 LLaDA-8B-Instruct 上超越了全序列 SFT 和预算匹配的 diffusion RL 基线，在数学和代码基准上取得一致提升，展示了极高的数据效率。
