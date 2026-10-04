---
title: 'Stochastic Rounding in Low-Precision Transformer Inference: A Variable-Precision
  Emulation Study of a Small GPT-2'
title_zh: 低精度 Transformer 推理中的随机舍入：小 GPT-2 变精度仿真研究
authors:
- Yohan Chatelain
- Pablo de Oliveira Castro
affiliations:
- Krembil Centre for Neuroinformatics, Centre for Addiction and Mental Health
- Université Paris-Saclay, UVSQ, LI-PaRAD
arxiv_id: '2610.01889'
url: https://arxiv.org/abs/2610.01889
pdf_url: https://arxiv.org/pdf/2610.01889
published: '2026-10-01'
collected: '2026-10-04'
category: LLM
direction: 低精度推理 · 随机舍入策略
tags:
- stochastic rounding
- low-precision inference
- quantization
- transformer
- mixed-precision
- round-to-nearest
one_liner: 系统研究低精度 Transformer 中随机舍入与就近舍入的逐位置权衡，发现 MLP 输出宜用 SR、LM head 宜用 RN，混合配置可显著降低困惑度损失
practical_value: '- 在低比特部署 LLM 时，不要全局统一舍入策略：对长 reduction 的 MLP 输出（尤其 down-projection）优先尝试随机舍入
  SR，可显著抑制误差累积；而在 LM head 保留就近舍入 RN，避免引入非均匀 logit 方差导致 softmax 损失增加。

  - 混合精度方案可将 SR 用于 MLP、RN 用于 head，实验中在 t=6 时把 perplexity 损失从等位 RN 的约 2.21x 降至 1.10x，减少约
  28%，这对电商搜索/推荐中的文案生成、query 改写等低比特小模型很实用。

  - 借助 PRISM 变精度随机舍入（VPSR）算法可离线评估不同层/操作的舍入策略，无需真实低精度硬件即可进行 what-if 分析，适合在量化工具链中作为
  auto-tuning 组件。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：低精度 Transformer 推理中，随机舍入（SR）与就近舍入（RN）的选择缺乏逐站点指导，现有量化方案通常全局采用一种舍入规则，忽视网络不同位置对噪声的敏感度差异。

**方法关键点**：扩展 PRISM 库支持任意虚拟精度，提出变精度随机舍入（VPSR）算法并证明其舍入决策可在硬件浮点中精确评估。通过两个互补分析解释逐站点权衡：线性投影概率前向误差界显示 SR 误差包络为 O(√n u)，优于 RN 的 O(n u)，在长 MLP 下投影中差距最大；对输出 softmax 交叉熵损失做二阶分解，将期望损失变化拆成有符号漂移、漂移曲率和 Fisher 加权方差惩罚，揭示 MLP 噪声近似均匀 logit 平移（softmax 不变），而 head 噪声非均匀导致方差惩罚。

**关键结果**：在 DistilGPT-2 上 t=6 位尾数，MLP 处 SR 的 perplexity 为全精度 1.15x，显著优于 RN 的 2.21x；LM head 处 SR 因非均匀方差劣于 RN；混合配置（MLP 输出用 SR，head 用 RN）达到 1.10x，比等位 RN 减少 28% 的 perplexity 损失。
