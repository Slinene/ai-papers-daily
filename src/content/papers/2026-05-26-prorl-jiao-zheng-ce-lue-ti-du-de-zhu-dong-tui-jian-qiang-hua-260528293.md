---
title: 'ProRL: Effective Reinforcement Learning for Proactive Recommendation via Rectified
  Policy Gradient Estimation'
title_zh: ProRL：矫正策略梯度的主动推荐强化学习
authors:
- Hongru Hou
- Tiehua Mei
- Denghui Geng
- Jinhui Huang
- Ao Xu
- Hengrui Chen
- Jiaqing Liang
- Deqing Yang
affiliations:
- Fudan University
arxiv_id: '2605.28293'
url: https://arxiv.org/abs/2605.28293
pdf_url: https://arxiv.org/pdf/2605.28293
published: '2026-05-26'
collected: '2026-05-28'
category: RecSys
direction: 主动推荐 · 强化学习策略梯度矫正
tags:
- Proactive Recommendation
- Policy Gradient
- Reinforcement Learning
- Reward Centering
- Advantage Estimation
- PRS
one_liner: 识别并解决主动推荐中策略梯度的长度捷径与高方差问题，提出步级奖励中心化和位置特定优势估计
practical_value: '- 在序列决策任务中若步级奖励存在正均值，会诱导策略偏向延长序列。可直接套用“步级奖励中心化”：用在线统计估计全局步级奖励均值，每一步奖励减去该均值，使路径延长零期望增益，消除长度捷径。

  - 利用奖励分解为步级增量这一结构，无需额外 critic 模型即可计算位置特定优势：取同输入多个 rollouts 的 reward-to-go，在每个位置做组内平均作为基线，构造低方差优势估计。该
  trick 可直接用于对话推荐、路径规划等 RL 训练，训练稳定且无额外网络。

  - 多目标 RL 中，不同奖励成分的尺度差异大，采用“中心化 + 标准差缩放”的归一化策略，平衡各目标梯度量级，可借鉴到电商推荐中同时优化点击、转化、引导效果等复合指标。

  - 整个框架基于轻量 Transformer + 语义 ID 实现，部署成本低，适合工业界在类主动推荐（如新品引导、兴趣探索）场景中替代 LLM 规划，兼顾效果与在线效率。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**  
主动推荐系统（PRS）通过中间推荐路径将用户偏好逐步引导至目标商品，需兼顾路径可行性（每步高接受度）与引导有效性（最终接受目标）。已有方法或受限于模仿历史数据（监督式），或局部最优（启发式），或成本过高（LLM）。将 PRS 形式化为 RL 问题天然，但标准策略梯度遭遇两大缺陷：(1) 步级奖励有正均值，奖励与路径长度耦合，产生“长度捷径”，策略退化到生成极长路径而忽略质量；(2) 全程奖励权重加给每一步，忽略奖励分解结构，导致高梯度方差。

**方法关键点**  
- 用用户模拟器（如 SASRec）估计接受概率，定义路径奖励为 IoI、IoR、CTR 的加权和，任务化为自回归路径生成。  
- **步级奖励中心化（Stepwise Reward Centering）**：将每个步级奖励减去全局均值，确保延长路径的期望收益为零，消除长度捷径，迫使模型探索路径质量。多目标时进一步缩放各分量，平衡梯度。  
- **位置特定优势估计（Position-Specific Advantage Estimation）**：利用奖励分解为步级增量，对每一步计算 reward-to-go，并以同输入多条采样路径在该位置的均值作为基线，构造低方差优势估计，无需 critic 网络。  
- 实际采用语义 ID 表示物品，用自回归 Transformer 生成 tokens，所有同物品 tokens 共享物品级优势。

**关键实验与结果**  
在 MovieLens-1M、Steam、Amazon-Book 数据集上，ProRL 在所有指标（CTR、Coherence、IoI、IoR）上显著优于现有 SOTA（包括 IRN、IPG、ITMPRec、LLM-IPP、T-PRA）。交叉评估（用不同推荐模型作评估器）验证策略泛化性。消融实验证明去除步级奖励中心化会导致 CTR 虚高但引导效果骤降；去除位置特定优势则方差大、长度不稳定。对比多种梯度估计器（REINFORCE、reward-to-go、GRPO、A2C），ProRL 方差最低（仅为 REINFORCE 的 ~5%），引导效果最优。此外，RL 阶段主要将预训练模型已隐含的高质量路径从低概率尾部分布中“纠正”出来，而非凭空创造新能力。
