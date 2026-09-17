---
title: 'Rethinking Critic Learning in PPO: Understanding and Mitigating Value Flattening'
title_zh: 重新思考 PPO 中的 Critic 学习：理解并缓解价值平坦化
authors:
- Yizhuo Li
- Jianhao Yan
- Yun Luo
- Zhi Wang
- Futing Wang
- Rong-Xi Tan
- Kanghui Tian
- Ganqu Cui
- Ning Ding
- Peilin Zhao
affiliations:
- Shanghai Jiao Tong University
- Shanghai AI Laboratory
- Westlake University
- Nanjing University
- Tsinghua University
arxiv_id: '2609.18708'
url: https://arxiv.org/abs/2609.18708
pdf_url: https://arxiv.org/pdf/2609.18708
published: '2026-09-16'
collected: '2026-09-17'
category: Training
direction: PPO critic 稀疏监督优化
tags:
- PPO
- critic learning
- value flattening
- sparse supervision
- LLM RL
- reasoning
one_liner: 发现 PPO critic 的价值平坦化失效模式，提出仅对少数间隔状态施加 critic loss 的 SP3O，提升推理策略与训练稳定性
practical_value: '- 若用 PPO/RLAIF 优化多轮对话、Agent 或推荐策略且奖励常是 terminal（转化/完成/点击），可把 critic
  loss 从逐 token 改成只对 3-5 个间隔位置（如 30%/60%/90% 加尾部）监督；实现只是 loss mask 改动，通常不增加 rollouts，但能改善
  token 级 credit assignment。

  - 建立 critic 价值分辨率诊断：对中间状态采样多条 continuation 估计 MC value，对比 critic 预测的响应内变化幅度；若 critic
  变化远小于 MC，即存在 flattening，从而避免只看 response-level AUC 或 loss。

  - 对长序列训练，关注相邻状态表征/梯度冗余：密集监督会产生大量相似更新，稀疏锚点能提升 critic 表征 effective rank、降低 actor 更新震荡，可结合训练稳定性指标上线验证。

  - 如果业务里使用 PPO 并观察到训练不稳或 critic 无法区分过程好坏，不妨尝试 sparse critic supervision；论文还提示 tail
  anchor 对减少重复输出有额外收益，可在长文本生成任务中单独试验。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
在 LLM 推理 RL 中，PPO 依赖 critic 估计状态价值以构造 token 级 advantage。但作者发现 critic 存在系统性失效：MC continuations 估计的状态价值在同一个 response 内可剧烈变化，而 critic 预测几乎平坦，称为 Value Flattening。该现象在 FrozenLake 中随状态空间扩大更明显，直接影响长程任务的精细 credit assignment。

**方法关键点**
- 将 critic MSE 在 terminal-only reward 下分解为响应均值误差与响应内预测方差惩罚；因为所有 token 共享同一终端 reward，dense 监督隐式惩罚响应内价值变化，压制 critic 分辨率。
- 相邻 LLM 状态仅差一个 token，表征与梯度高度相关，距离越近的 token 梯度越相似，密集监督产生冗余更新。
- 提出 SP3O：只对每个 response 的少数几个 well-separated anchors（默认 0.3/0.6/0.9，长序列再加 0.95 tail）计算 value loss，actor/rollout 不变；critic 仍可预测所有状态值。

**关键实验结果**
- Qwen3-4B/8B-Base + DAPO-Math-17k：在数学推理 avg@32 上，4B SP3O 45.57 对 PPO 37.60、GRPO 39.26；8B SP3O 50.51 对 PPO 48.50、GRPO 47.91。
- OOD avg@4 上，4B SP3O 59.28 对 PPO 51.95；8B SP3O 66.37 对 PPO 64.38。
- 稀疏监督 K=3 最优，K=16/64 回落近 dense PPO；固定间隔锚优于随机；tail anchor 把重复率从 18.33% 降到 1.12%。

**最值得记住的一句话**
在 terminal-only reward 的 PPO 中，dense critic 监督会隐式惩罚响应内价值方差；只监督少数几个间隔状态反而能恢复 critic 的分辨率并提升策略训练。
