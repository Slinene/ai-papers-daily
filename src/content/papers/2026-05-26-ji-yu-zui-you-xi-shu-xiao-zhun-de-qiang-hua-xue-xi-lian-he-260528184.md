---
title: Joint Training of Multi-Token Prediction in Reinforcement Learning via Optimal
  Coefficient Calibration
title_zh: 基于最优系数校准的强化学习联合多Token预测
authors:
- Zili Wang
- Jiajun Chai
- Lin Chen
- Xiaohan Wang
- Shiming Xiang
- Guojun Yin
affiliations:
- 中国科学院大学
- 中国科学院自动化研究所
- 美团
arxiv_id: '2605.28184'
url: https://arxiv.org/abs/2605.28184
pdf_url: https://arxiv.org/pdf/2605.28184
published: '2026-05-26'
collected: '2026-05-28'
category: Training
direction: 训练优化·多Token预测联合RL
tags:
- MTP
- RLVR
- gradient alignment
- coefficient calibration
- log-probability proxy
- LLM post-training
one_liner: 提出在线自适应系数调整方法OCC，通过log概率代理动态平衡RL与MTP梯度，使联合训练稳定超越detach基线
practical_value: '- **辅助损失动态加权**：在推荐模型联合训练主任务（如CTR）与辅助任务（如多样性、长尾覆盖）时，可借鉴OCC的廉价梯度对齐代理，在线校准辅助任务系数，避免固定权重导致的后期性能退化。

  - **多步奖励预测的RL优化**：在强化学习推荐或Agent策略优化中，若使用多步奖励预测头（类似MTP），可利用OCC思想根据梯度方向一致性自适应调节多步预测损失的权重，防止后期扰动损害主策略。

  - **多目标策略梯度平衡**：对于多Agent协作或联合策略学习，不同智能体的梯度可能存在冲突，可通过一阶相关与二阶扰动的分解分析有益与有害信号，动态分配更新强度，替代常规的固定比例调度。

  - **轻量级实现**：OCC仅需计算小批量内的log概率变化向量内积，无需全模型梯度，计算开销可忽略，易于在分布式训练框架中实现。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多Token预测（MTP）在预训练中有效，但在RL后训练阶段联合训练MTP和主模型常导致严重的性能下降，迫使业界采用梯度分离（detach）的妥协方案，牺牲了多token监督的潜在收益。论文旨在从优化角度解释联合训练失败的原因，并提出可行方案。

**方法关键点**
- **理论分解**：基于L-smooth假设，将MTP对RL目标的影响分解为一阶相关项（RL与MTP梯度内积）和二阶扰动项（MTP梯度范数），统一解释了三种训练策略：Detach（梯度无关）、交叉熵损失（相关项期望为零，纯扰动）、策略损失（初期相关主导，后期相关衰减而扰动持续）。
- **退化机制**：策略损失虽初期可提升性能，但随着训练进入平坦区域，梯度对齐下降而扰动项不减，导致增益由正转负，出现“先升后降”现象。
- **OCC方法**：推导出每步最优MTP系数应为 λ* ∝ c / v²（c为梯度内积，v²为MTP梯度范数）。为避免高成本的全梯度计算，采用 log 概率变化的向量内积 ĉ 与范数平方 v̂² 作为廉价代理，在线计算自适应系数 λ_t = λ_+ · ĉ_t / (v̂²_t + ε)，并允许系数为负以翻转有害梯度方向。

**关键实验结果**
- **设置**：训练数据 DAPO-Math-17k，评估基准 AIME24/25、AMC、MATH、Minerva、OlympiadBench；模型 MiMo-7B-RL、GLM-4.5-Air (106B MoE)；RL 算法 DAPO 和 GSPO。
- **结果**：在 MiMo-7B-RL + DAPO 上，OCC 平均准确率 61.7%，相比 Detach 的 58.9% 提升 2.8 点，远超 CE Loss 的 47.7% 和 Policy Loss 的 57.4%。Policy Loss 随训练衰退，而 OCC 始终稳定超越 Detach。OCC 系数自适应衰减，计算开销仅约 8.07 秒/步（Detach 8.11 秒），远低于全梯度计算的 45 秒。方法在不同模型尺度和 RL 算法下均保持优势。

**一句话核心**：通过跟踪 RL 与 MTP 梯度的在线对数概率对齐，OCC 以可忽略的计算代价动态校准多 token 损失系数，首次使 MTP 安全地融入 RL 训练并获得稳定提升。
