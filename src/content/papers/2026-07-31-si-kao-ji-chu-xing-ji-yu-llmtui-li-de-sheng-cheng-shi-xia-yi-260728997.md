---
title: 'Think2Go: Generative Next POI Recommendation with LLM Reasoning'
title_zh: 思考即出行：基于LLM推理的生成式下一兴趣点推荐
authors:
- Zhuang Zhuang
- Shanshan Feng
- Hangwei Qian
- Mingqi Yang
- Heng Qi
- Yanming Shen
- Baocai Yin
affiliations:
- Dalian University of Technology
- Wuhan University
- A*STAR
- South China University of Technology
arxiv_id: '2607.28997'
url: https://arxiv.org/abs/2607.28997
pdf_url: https://arxiv.org/pdf/2607.28997
published: '2026-07-31'
collected: '2026-08-03'
category: GenRec
direction: 生成式推荐 · 语义ID + 推理增强
tags:
- Generative Recommendation
- Next POI
- LLM Reasoning
- Semantic ID
- Advantage Calibration
- GRPO
one_liner: 统一SFT与RL推理，用时空不确定性校准优势估计，大幅提升LLM对语义ID的理解和跨域泛化
practical_value: '- **SFT与RL统一训练范式**：在自回归生成中同时保留记忆和推理探索，避免LLM灾难性遗忘，可直接用于商品标题、推荐理由等的生成式推荐系统。

  - **难度感知的优势估计**：通过核密度估计用户行为时空分布，量化当前请求的认知不确定性，动态调整RL更新幅度——电商中可对冷门/长尾用户加大探索，对高频行为保持保守。

  - **奖励重标定避免难度信号丢失**：用样本奖励相对于组内最大值的缩放替代纯中心化，防止GRPO在易/难样本上产生相同的优势值，可迁移至推荐策略的在线强化学习调优。

  - **Token级熵作为探索奖励**：防止推理token熵塌缩，维持策略多样性，在生成式排序或创意文案生成中有助于避免模式崩溃。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现有LLM用于POI推荐时，语义ID（SID）通常独立训练，导致LLM对SID理解不足、泛化差，尤其用户行为稀疏且时空复杂。推理方法（如GRPO）存在优势估计偏差：不同难度样本更新力度一致，且SFT与RL分阶段训练造成遗忘。本文提出Think2Go，将推理过程融入生成式推荐，通过校准优势估计提升探索效率和SID理解。

### 方法关键点
- **统一SFT-RL架构**：生成输出结构为`Think→Go→Self-Correct→Answer`，`Think`和`Go`段用RL优化策略，`Answer`段做SFT监督，`Self-Correct`桥接两者，避免遗忘。
- **校准优势策略优化（CAPO）**：融合两种校准系数：
  - *时空认知不确定性（STEU）*：用高斯核密度估计查询时刻与历史签到的时空相似度，高不确定性时放大优势，鼓励探索。
  - *难度感知奖励缺口（DRG）*：用当前奖励与组内最大奖励的相对值重新缩放优势，恢复被中心化抹除的难度信号。
- **渐进式奖励**：格式奖励（部分格式0.5，完整格式1.0+长度门限）防止奖励黑客；评估奖励按SID单元分解，部分正确也给分。
- **Token级熵奖励**：在优势中加入token熵项，维持推理token多样性，缓解熵塌缩。

### 关键实验结果
- 三个数据集（NYC, TKY, CA）上全面超越基线：Acc@1分别比最强LLM基线GNPR提高6.33%、5.78%、7.49%，比传统最强ROTAN提高23.86%、31.77%、17.47%。
- 消融显示STEU、DRG、熵奖励均带来显著增益；训练过程中熵值稳定、奖励提升快，未出现熵塌缩。
- SID类别预测任务中准确率远超SFT基线（如NYC: 0.3024 vs 0.1241），验证推理训练加深了LLM对SID的语义理解。
- 跨域迁移性能明显更好，证明泛化能力提升。

一句话：**时空核密度估计的认知不确定性校准，让LLM在RL推理中更聪明地探索，从而大幅提升语义ID的生成质量。**
