---
title: Learning to Reason with Predictive Gains for Generative Recommendation
title_zh: 基于预测增益学习推理的生成式推荐
authors:
- Zhuoyang Li
- Teng Shi
- Jiakai Tang
- Weijie Yu
- Guofu Xie
- Xiao Zhang
- Lei Kou
- Yang Yu
- Lei Shen
- Xin Chen
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- School of Artificial Intelligence and Data Science, University of International
  Business and Economics
- Alibaba International Digital Commercial Group
arxiv_id: '2611.21441'
url: https://arxiv.org/abs/2611.21441
pdf_url: https://arxiv.org/pdf/2611.21441
published: '2026-11-16'
collected: '2026-11-17'
category: GenRec
direction: 生成式推荐 · Semantic ID · Reasoning RL
tags:
- Generative Recommendation
- Semantic ID
- Reasoning
- GRPO
- Predictive Gain
- Process Reward
one_liner: 用句子级预测增益作为过程奖励优化生成式推荐中的显式推理，提升 SID 预测并理论对齐排序目标
practical_value: '- **用目标 SID log-likelihood 增量作为过程奖励**：在 LLM 生成用户兴趣推理时，可以逐句计算预测目标商品
  SID 的 log-likelihood 变化，把变化量作为句子级 reward 赋给 GRPO/PPO 的优势函数，替代稀疏的最终匹配 reward。电商推荐中可复用：先用历史行为+候选商品构造
  CoT，再计算每句话对目标商品概率的贡献，直接优化推理质量。

  - **自定义 causal attention 一次前向计算多个前缀得分**：需要评估多个条件前缀下的目标商品概率时，可以把多个 target SID 副本按不同前缀拼接，用自定义
  mask 让每个副本只看到对应前缀，从而一次 forward 拿到所有前缀 log-likelihood，避免重复计算共享历史。适合在需要频繁计算 CoT 中间步骤对最终预测影响的场景落地，能显著降低
  RL 训练成本。

  - **PGRU 的 bump weighting 处理“无效推理”**：对累计 PG 接近 0 的轨迹做加权 SFT，增强推理被模型利用的程度。电商场景中经常出现
  LLM 生成的推理看似合理但没改变预测结果，可借鉴这种自适应加权，只对近零增益样本补强 reasoning-conditioned prediction，避免对已有增益的样本过度干预。

  - **PG 与排序目标有理论对齐**：论文证明最大化期望 PG 能收紧 Top-K ranking regret 上界，这给“过程奖励不一定非要基于最终推荐结果”提供了理论支撑，业务中可放心用预测增益信号替代部分手工规则
  reward。'
score: 10
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
现有 reasoning-enhanced generative recommendation 通常先 SFT 激活 CoT 推理，再用 GRPO 优化推理，但 reward 主要靠最终 SID 匹配等规则信号。这带来两个问题：一是推理内部各步骤对预测的贡献未被度量，模型可能生成了看似合理但对目标商品预测没有帮助甚至有害的推理；二是组内不同推理轨迹常获得相同 reward，导致大量零优势组，GRPO 更新效率低。论文实证发现规则方法训练中正负预测贡献的推理句比例接近，且相当比例 rollout 组优势全为 0。

## 方法关键点
- **Predictive Gain (PG) 奖励**：把推理按句号等标点切分成句子级步骤，对每个步骤 j 计算目标 SID 在“历史+前 j 句推理”条件下的 log-likelihood ℓ_j，定义该句的 PG 为 ℓ_j − ℓ_{j−1}。这直接量化每句话对预测目标商品的增量贡献。
- **PGRO**：用句子级 PG 作为 reward，组内 z-normalization 后得到优势，对推理 token 做 GRPO 式策略优化。无需解码推荐结果，也不需要手工规则。
- **高效 PG 计算**：设计自定义 causal attention mask，把 N+1 个目标 SID 副本拼接到完整推理序列后，每个副本只 attend 到对应推理前缀，一次前向即可算出所有 ℓ_j，减少重复计算共享前缀。
- **PGRU**：对累计 PG 接近 0 的轨迹（可能是推理未被充分利用）用平滑 bump 函数加权，做 reasoning-conditioned SFT，增强模型利用推理的能力。
- **理论对齐**：证明最大化期望 PG 能收紧 Top-K ranking regret 的上界，说明 PG 优化与推荐排序目标一致。

## 关键实验与结果
在 Amazon Industrial、Movies 和 Yelp 三个基准上，对比传统序列推荐、生成式推荐（TIGER、LC-Rec 等）和显式推理基线（OneRec-Think、SIDReasoner、Evo-Rec、SAPO）。GainReason 在 Industrial 上 NDCG@5 达到 0.0985，相对最强基线 OneRec-Think 提升 7.7%；在 Movies 和 Yelp 上 NDCG@5 分别达到 0.0435 和 0.0204，相对最强基线提升约 2.7% 和 6.1%。消融显示 PGRO 和 PGRU 均有贡献，训练开销仅比 OneRec-Think 增加约 1%。

## 最值得记住的一句话
不要只问“最终推荐对不对”，要问“每一步推理让目标商品更可能了吗”——用预测增益作为过程奖励，才能让 LLM 的推理真正为排序目标服务。
