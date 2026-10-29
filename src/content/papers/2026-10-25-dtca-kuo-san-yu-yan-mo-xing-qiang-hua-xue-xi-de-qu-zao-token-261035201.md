---
title: 'DTCA: Denoising Token Credit Assignment for Reinforcement Learning in Diffusion
  Language Models'
title_zh: DTCA：扩散语言模型强化学习的去噪 Token 信用分配
authors:
- Hongze Chen
- Miao Pan
- Lizhou Liang
- Qinfeng Li
- Xinyin Ma
- Yongliang Shen
- Weishi Wang
- Daniel Dahlmeier
- Xuhong Zhang
- Wenqi Zhang
affiliations:
- Zhejiang University
- National University of Singapore
- SAP
arxiv_id: '2610.35201'
url: https://arxiv.org/abs/2610.35201
pdf_url: https://arxiv.org/pdf/2610.35201
published: '2026-10-25'
collected: '2026-10-29'
category: Training
direction: 扩散语言模型 RL 训练 · 信用分配
tags:
- Diffusion Language Models
- Reinforcement Learning
- Credit Assignment
- Token-level Signal
- LLaDA
- Mathematical Reasoning
one_liner: 提出 DTCA，按去噪 token 置信度增益估计贡献并分组，用于扩散语言模型 RL 的 token 级信用分配。
practical_value: '- 面向文案/query 生成的 RL 训练：若用 RL 优化广告文案、搜索词或商品标题生成，稀疏 outcome reward
  会导致 credit assignment 困难。可借鉴 DTCA 的 token 贡献估计，用生成过程中 token 置信度增益作为细粒度奖励塑形，加速收敛。

  - 按语言单元分组校准信号：DTCA 按 POS 分组贡献。在电商场景中，可对商品标题/query 中的品牌词、类目词、属性词分别设定权重，让 RL 更关注关键信息
  token，减少语义噪声干扰。

  - 熵变化校准避免过优化：策略更新引起的 token 熵变化被用于校准学习信号。实际 RL 训练生成模型时，可监控 token 级熵，抑制高熵 token 的过大梯度，提升训练稳定性。

  - 筛选 informative 去噪 timesteps：DTCA 选择关键去噪步骤参与 RL 训练。若业务中采用扩散或非自回归生成模型，可减少无效训练步，节省算力并提升信号质量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：扩散语言模型（DLM）通过迭代去噪生成文本，但将其用于 RL 时，最终 outcome reward 难以区分不同 token 的贡献，credit assignment 比自回归生成更困难。

**方法关键点**：DTCA 在 token 承诺后，测量剩余 masked 位置预测置信度的提升，作为该 token 的贡献估计；按词性（POS）对贡献信号分组归一化，得到 token-level 权重。这些权重用于：1）选择 informative denoising timesteps，只在高贡献步骤采样；2）在 RL 训练中为每个 token 分配学习信号，替代稀疏 trajectory 奖励。此外，DTCA 根据策略更新引起的 token-level 熵变化对学习信号进一步校准，防止过优化高熵 token。

**结果**：在 LLaDA-8B-Instruct 上，DTCA 在不同生成预算下均稳定提升数学推理能力：MATH500 最多提升 9.0 分，GSM8K 最多提升 5.3 分，超过基线和现有 RL 方法。
