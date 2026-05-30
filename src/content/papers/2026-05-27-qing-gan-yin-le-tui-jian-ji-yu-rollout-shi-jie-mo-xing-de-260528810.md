---
title: 'Affective Music Recommendation: A Rollout-Based World Model for Offline Preference
  Optimization'
title_zh: 情感音乐推荐：基于 rollout 世界模型的离线偏好优化
authors:
- Audrey Chan
- Aaron Labbé
- Jacob Lavoie
- Jordan Bannister
- Arsène Fansi Tchango
- Guillaume Lajoie
- Laurent Charlin
affiliations:
- LUCID Inc.
- Mila — Québec AI Institute
arxiv_id: '2605.28810'
url: https://arxiv.org/abs/2605.28810
pdf_url: https://arxiv.org/pdf/2605.28810
published: '2026-05-27'
collected: '2026-05-30'
category: RecSys
direction: 世界模型 · 离线偏好优化 · 情感计算
tags:
- World Model
- Offline RL
- DPO
- Affective Computing
- Music Recommendation
- Cold-Start
one_liner: 用因果 Transformer 世界模型联合预测行为与情感反馈，并通过 DPO 优化策略，在伦理约束下实现情感导向的音乐推荐。
practical_value: '- **世界模型作为离线模拟器与安全闸门**：当在线实验受伦理或合规限制时（如电商中的高风险推荐、医疗健康推荐），可训练一个因果
  Transformer 预测用户多维反馈（点击、评分、情感），完全在模拟器中训练和压力测试策略，上线前用对抗历史探测策略鲁棒性。

  - **DPO + 行为克隆做受控探索**：用行为克隆初始化策略，再通过 DPO 微调，KL 散度惩罚项可约束策略偏离已验证的基准，适合在已有生产策略基础上渐进优化，避免灾难性遗忘。偏好对可基于“负反馈纠正采样”构造，即针对历史负反馈样本搜索高效用替代，形成有监督改进信号。

  - **因子化 Transformer 架构便于并行打分**：世界模型采用因子化设计，先对用户历史编码得到表示向量，再与候选物品 embedding 拼接后通过轻量
  MLP 预测反馈，可实现一次历史编码、批量候选评分的并行化，大幅降低实时推理成本，适合库存量大的电商场景。

  - **多目标效用函数融合异质反馈**：将点击、评分、情感等多维信号加权合成为标量效用，且权重可配置，方便根据业务阶段动态调整优化目标（如先提转化再控多样性），同时监控覆盖率、熵、Gini
  等多样性指标防止策略坍缩。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：功能型音乐平台（如助眠、专注）的成功取决于用户情感状态而非简单点击，但直接在线实验影响情感状态存在严重伦理风险，尤其对临床脆弱人群。传统推荐依赖行为反馈，情感信号仅在会话级稀疏标注，且数据来自固定生产策略，存在曝光偏差。如何在无在线交互的条件下，训练出提升用户情感目标的推荐策略，是核心挑战。

**方法关键点**：
- **世界模型**：基于因果 Transformer，用历史序列联合预测歌曲级的播放进度、二元评分以及会话级的效价和唤醒度。采用因子化架构：用户历史经 causal transformer 编码为表示向量，再与候选歌曲 embedding 拼接，用 MLP 头输出四维预测，支持并行评分。使用 MERT 声学嵌入，无位置编码即达最优。
- **策略优化**：先用行为克隆（InfoNCE 损失）模仿生产策略得到 Copycat 基准，再用 DPO 在世界模型数据上进行离线微调。偏好对构建采用“负反馈纠正采样”：对历史中获得负面反馈的歌曲，从其近邻和随机探索中选出世界模型预测效用最高的候选作为正样本，原曝光歌曲为负样本。效用函数可配置，本文采用效价和唤醒度各 0.5 的权值，行为和评分信号暂不加入。
- **安全机制**：全离线训练与压力测试，策略由克隆基准和 KL 惩罚约束漂移，并监控多样性指标防止坍缩。

**关键结果**：在 LUCID 平台 939 名用户、8784 个会话、5.99k 首歌曲的数据集上，严格冷启动按用户切分，世界模型对效价预测 R² 达 42.6%，唤醒度 37.9%，显著优于输入特征消融后的随机水平。DPO 策略在效价上相对 Copycat 提升 4.0%，唤醒度提升 3.7%，同时行为指标仅轻微下降，多样性指标（覆盖率、熵、ILD、Gini）保持健康，而贪心优化则完全坍缩。消融实验证实历史行为和反馈信号是世界模型预测能力的核心来源。

**最值得记住的一句话**：当在线实验被伦理禁止时，rollout 世界模型 + DPO 提供了以低风险方式优化多维（包括情感）推荐策略的完整方法论。
