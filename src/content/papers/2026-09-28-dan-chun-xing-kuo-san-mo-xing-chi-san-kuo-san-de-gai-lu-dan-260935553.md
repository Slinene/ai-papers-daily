---
title: Simplex Diffusion Models
title_zh: 单纯形扩散模型：离散扩散的概率单纯形框架
authors:
- Justin Deschenaux
- Alexandre Galashov
- Andrew Campbell
- Li Kevin Wenliang
- James Thornton
- Arnaud Doucet
- Valentin De Bortoli
affiliations:
- Google DeepMind
- EPFL
- UCL Gatsby
arxiv_id: '2609.35553'
url: https://arxiv.org/abs/2609.35553
pdf_url: https://arxiv.org/pdf/2609.35553
published: '2026-09-28'
collected: '2026-09-29'
category: Other
direction: 离散扩散 · 概率单纯形
tags:
- Discrete Diffusion
- Simplex
- DDIM
- Language Modeling
- Code Generation
- Information Collapse
one_liner: 提出在概率单纯形上扩散的 SDM，保留中间不确定性，用 DDIM 式采样统一离散与连续扩散
practical_value: '- 生成式推荐/ Semantic ID 生成中，离散扩散每一步仅采样一个 token 会丢失分布，SDM 用单纯形上的分布作为中间状态，可保留候选
  item 的不确定性，减少误差累积；无需 Self-Conditioning 的额外前向。

  - 大词表场景（如 item ID 词表很大）可以用 argmax embedding 替代期望 embedding，避免 O(V*d) 矩阵乘法，同时保持推理连续状态；这是工程上可落地的
  trick。

  - DDIM-like 采样器有 churn 参数，可调节随机性（实验中 κ=1 通常最好），且支持蒸馏到极低步数（8 步），有利于在线生成式推荐的低延迟部署。

  - 用 normalized variance ν_t 调度浓度比直接调 c_t 更直观，便于在不同任务上快速调参；自适应时间采样也能提升性能。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：离散扩散模型在中间步对 categorical 采样，丢失不确定性（信息坍缩），依赖 Self-Conditioning 或 loopholing 弥补；连续松弛在嵌入空间扩散，但类别身份破坏突然；直接在概率单纯形上建模可保留分布。现有 Dirichlet Flow Matching 需 ODE 积分，大词表扩展差。

**方法关键点**：
- 前向过程：用 Dirichlet 分布，均值 = α_t P0 + (1-α_t)π，浓度参数 c_t 独立控制 variance；t→1 时退化为 Dir(c_1 π)。
- 反向桥：闭式 reverse transition，用 Beta/Dirichlet 随机变量构造，churn κ∈[0,1] 控制随机性，无需数值积分；κ=0 低随机，κ=1 高随机。
- 训练：交叉熵损失，denoiser 输入可用期望嵌入 P_t E 或 argmax 嵌入 E_{argmax P_t}（大词表高效）。
- 浓度调度用 normalized variance ν_t 参数化更直观；高温度极限退化为离散扩散，低温度极限确定性，存在高斯涨落，统一离续。

**关键实验**：
- TinyGSM 代码生成：无 SC 的 SDM（期望嵌入）T=0.1 512 NFE 达 49.0%，超过 MDM+SC 45.8%；Argmax+SC 在 8k NFE 达 57.0%。蒸馏到 8 步解 GSM8K 32.1%，超过 128 步蒸馏离散扩散 21.4%。
- Sudoku：SDM+SC 达 99.1%，接近最佳 MDM+SC 99.3%，远超 DFM 76.7%。
- OWT：64 步 SDM 经 logit shaping 达 GenPPL 17.0, entropy 5.46，接近真实数据，同时候揭示了 OWT 评测局限。

**最值得记住的一句话**：离散与连续扩散不是对立的，SDM 在单纯形上保留分布，避免信息坍缩，并通过 temperature/churn 统一两者。
