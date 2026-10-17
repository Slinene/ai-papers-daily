---
title: 'Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored
  Noise for LLM RLVR'
title_zh: 锚定噪声驱动的嵌入空间定向探索：改进 LLM RLVR
authors:
- Daijiao Liu
- Huiyi Wang
- Lina Yao
- Dong Gong
affiliations:
- University of New South Wales (UNSW Sydney)
arxiv_id: '2610.16105'
url: https://arxiv.org/abs/2610.16105
pdf_url: https://arxiv.org/pdf/2610.16105
published: '2026-10-11'
collected: '2026-10-17'
category: Training
direction: RLVR 训练探索增强
tags:
- RLVR
- GRPO
- Exploration
- Embedding Perturbation
- LLM
- Reasoning
one_liner: 在 GRPO rollout 中用少量锚定噪声扰动嵌入位置替代标准采样，以极低成本提升探索多样性，优于 GRPO。
practical_value: '- 在电商/搜索/生成式推荐模型的 RLVR/GRPO 训练中，可在 prompt embedding 后追加一个带共享锚点和高斯噪声的扰动位置，按
  10%–20% 比例替换标准 rollout，低成本增加组内 reward 方差，改善优势信号。

  - 对扰动 rollout 使用降权优势参与更新，可防止噪声过度干扰策略；该方法不改模型结构、解码和线上推理，适合作为现有 GRPO 训练管道的即插即用探索插件。

  - 当业务需要提高生成多样性（如推荐理由、搜索建议、自动文案）时，可借鉴“锚点+噪声”的定向探索思路，让同一 prompt 的候选沿共同方向发散，提升采样覆盖，而非仅依赖调高温度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RLVR 通常每个 prompt 采样 8–16 条轨迹，小预算下同一策略采样高度相似，导致组内 reward 变化小，削弱 group-relative advantage 信号。提高温度、熵奖励、非对称裁剪和增大预算等方法均未改变 rollout 条件。

**方法**：EDEN 在 rollout 源头做锚定输入扰动。在相同预算内，用少量标准 rollout 替换为“prompt + 单个追加的扰动 embedding 位置”生成的轨迹。高斯噪声驱动变化，共享锚点提供组内公共条件方向。选中的扰动 rollout 以降低的优势权重参与 GRPO 更新；模型架构、离散解码、测试推理不变。

**结果**：在多个模型规模和数学推理基准上，EDEN 优于 GRPO 和同管道探索控制，采样解覆盖提升最大；分析显示更多 prompt 组获得非零组相对学习信号，噪声与锚定互补。
