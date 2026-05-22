---
title: 'DelTA: Discriminative Token Credit Assignment for Reinforcement Learning from
  Verifiable Rewards'
title_zh: DelTA：通过判别性Token信用分配提升可验证奖励的强化学习
authors:
- Kaiyi Zhang
- Wei Wu
- Yankai Lin
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Ant International
arxiv_id: '2605.21467'
url: https://arxiv.org/abs/2605.21467
pdf_url: https://arxiv.org/pdf/2605.21467
published: '2026-05-19'
collected: '2026-05-22'
category: Training
direction: 强化学习训练优化 · Token级信用分配
tags:
- RLVR
- Token Credit Assignment
- Discriminator View
- Policy Gradient
- DAPO
- Mathematical Reasoning
one_liner: 将RLVR更新视为隐式线性判别器，通过重加权token梯度向量增强正负侧质心的区分度，提升数学推理等任务表现。
practical_value: '- 将策略梯度更新解构为隐式判别器的方法可用于诊断线上RL模型训练中的token偏向问题，尤其适合电商推荐中奖励信号稀疏的长序列生成（如自动文案、对话）场景。

  - 通过对比正负优势响应的token梯度质心并重加权token贡献，可以兼容大部分序列级RL目标（如GRPO、DAPO），工程实现可插入现有RLHF训练流程。

  - 系数计算采用最后一层隐藏状态或输出行梯度代理，无需全参梯度，开销可控，适合大规模LLM训练的在线重加权。

  - 在电商Agent的推理规划中，可借鉴基于判别性信号重新分配token信用，提升模型在长推理链上的一致性和正确率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：RLVR 用序列级可验证奖励优化 LLM 推理能力，但奖励与 token 更新间存在粒度错配。标准策略梯度更新如何将序列奖励转换为 token 概率变化并不透明。研究发现 RLVR 更新方向隐含地充当了 token 梯度向量的线性判别器，但现有方法中正负侧质心易被高频共享模式（如格式 token）主导，稀释了能区分高低奖励响应的判别方向。

**方法关键点**：
- 将 DAPO 等序列级 RLVR 的局部更新分解为优势加权正负侧 token 梯度质心之差，推导出更新方向等价于 token 梯度空间中的隐式线性判别器。
- 提出 DelTA，通过对比正负侧质心为每个 token 分配判别性得分，得分高的 token 梯度方向更代表自身侧而远于对侧。
- 使用得分重加权 RLVR 代理损失，并引入自归一化，塑造更具判别力的更新方向，抑制共享方向。
- 系数计算采用冻结 token 梯度代理（LM-head 行向量或 top-K 隐藏梯度），避免全参梯度开销，且不向优化过程回传梯度。

**关键实验**：
- 在 Qwen3-8B/14B-Base 上使用 DeepMath-103K 训练，在 AIME24-26、HMMT25 等七个数学基准上评估。
- DelTA 较 DAPO、SAPO、FIPO 等最强同尺寸基线平均提升 8B 上 3.26 分、14B 上 2.62 分。
- 额外验证了代码生成和不同 backbone 的泛化性，消融实验显示去掉对侧比较或系数映射均导致显著下降。

**最值得记住的一句话**：RLVR 的更新方向可以被视为一个隐式线性判别器，通过重塑正负侧质心来调整 token 概率的增减，DelTA 以判别性 token 信用分配让模型更关注能区分好答案与坏答案的关键 token。
