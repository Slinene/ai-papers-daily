---
title: On the Difficulty of Sequence-Level Supervised Learning for Autoregressive
  Language Models
title_zh: 自回归语言模型序列级监督学习的困难性
authors:
- Mathieu Blondel
- Michaël E. Sander
- Germain Vivier-Ardisson
- Tianlin Liu
- Vincent Roulet
affiliations:
- Google DeepMind
arxiv_id: '2611.16736'
url: https://arxiv.org/abs/2611.16736
pdf_url: https://arxiv.org/pdf/2611.16736
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: 自回归模型序列级训练目标分析
tags:
- Sequence-Level Training
- Teacher Forcing
- Exposure Bias
- Autoregressive Models
- Gumbel
- Optimization
one_liner: 证明两种序列级损失无下界，stop-gradient 方向是 NLL 的有效下降方向但方差大，认为 teacher forcing 可能已足够
practical_value: '- **不要盲目用序列级损失替代 token-level NLL**：在生成式推荐/LLM 微调中，基于贪心解码或采样的序列级损失理论上可能无下界，会导致训练不稳定。若要引入序列级信号，应优先考虑奖励加权或
  RL 框架，而不是直接作为可微损失。

  - **对采样/解码过程 stop gradient 是一个可用的 trick**：论文证明对采样过程做 stop gradient 得到的 moment matching
  更新方向是 NLL 的有效下降方向。业务中若想在生成式 item 排序或文案生成中利用序列级反馈，可以对采样部分截断梯度，仅用其信号构造更新方向，避免无界损失。

  - **注意 moment matching 方向的高方差问题**：该方向理论上合法但实际方差很大，直接使用需要增大 batch size、引入 baseline
  或 variance reduction 技巧。业务落地时若发现训练不稳定，可回到 teacher forcing 的监督学习阶段，把序列级优化放到后续 RL
  微调阶段。

  - **Gumbel 重参数化连接采样与贪心解码**：论文用 autoregressive Gumbel tricks 揭示采样损失是贪心损失在 Gumbel
  扰动下的期望，这为设计可微生成推荐目标提供理论提醒：基于采样的优化本质上是在噪声下贪心，需谨慎评估其优化性质。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**  
自回归语言模型监督学习阶段通常采用 teacher forcing 下的 token-level NLL，训练与推理存在 exposure bias：训练时以 ground-truth prefix 为条件，推理时依赖自身预测，导致误差累积。为缓解这一问题，研究者提出序列级训练目标，但这类目标的理论性质缺乏系统分析。

**方法关键点**  
论文分析两种自然的序列级损失：基于贪心解码序列的损失，以及基于自回归采样序列的损失。核心结论是这两种损失均无下界（unbounded below），因此不能作为合法损失函数使用。进一步利用 autoregressive Gumbel tricks，证明采样损失是贪心损失在 Gumbel 扰动下的期望。由于病理源于解码序列对模型参数的依赖，作者转向分析对采样过程施加 stop gradient 后得到的更新方向，称之为 moment matching 方向。虽然该方向不是任何损失函数的梯度，但证明它在函数空间中是自回归 NLL 的合法下降方向。

**关键结果**  
两种序列级损失无下界，不能直接优化；stop-gradient 的 moment matching 方向是 NLL 的有效下降方向，但实际方差很高。最终结论：在自回归模型的监督学习阶段，teacher forcing 可能已经足够，序列级优化应审慎对待。
