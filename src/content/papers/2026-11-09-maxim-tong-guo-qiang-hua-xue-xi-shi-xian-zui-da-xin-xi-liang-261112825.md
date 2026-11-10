---
title: 'MaxIM: Maximally Informative Incremental Summarization via Reinforcement Learning'
title_zh: MaxIM：通过强化学习实现最大信息量增量摘要
authors:
- Jihwan Jeong
- Guy Tennenholtz
- Yinlam Chow
- Chih-Wei Hsu
- Craig Boutilier
affiliations:
- Google Research
- Noetive
- Google DeepMind
arxiv_id: '2611.12825'
url: https://arxiv.org/abs/2611.12825
pdf_url: https://arxiv.org/pdf/2611.12825
published: '2026-11-09'
collected: '2026-11-10'
category: Agent
direction: LLM Agent 记忆压缩 · 信息论 reward shaping
tags:
- Incremental Summarization
- Reward Shaping
- Mutual Information
- RL
- LLM Memory
- POMDP
one_liner: 提出信息论 reward shaping 的 RL 框架 MaxIM，用 predictive sufficiency 和 recursive
  consistency 解决长程记忆压缩的信用分配与幻觉问题
practical_value: '- **长序列用户行为建模的稠密奖励设计**：直接优化终端转化奖励常因稀疏信用分配难以训练。可借鉴 MaxIM 引入 auxiliary
  dense reward：训练一个 critic 估算当前状态（摘要）对最终目标的预测 log-likelihood，并设计一致性正则（如与最近行为互信息）抑制状态生成中的幻觉，提升
  RL 训练稳定性。

  - **不对称 critic 架构抠生产部署**：训练时 critic 有权访问完整上下文或 oracle 目标（例如未来购买标签、用户真实意图），在线推理时
  actor 只使用有界记忆且零 critic 调用。可以用离线数据训练一个文本打分器（critic），对用户状态或记忆摘要提供逐 token 的 PMI 奖励，无需在线额外成本。

  - **离散文本摘要对接 frozen 黑盒 LLM**：用离散文本而非连续 embedding 压缩用户历史，可直接接入对话式推荐、客服 agent 等下游
  frozen 黑盒 LLM，无需重训下游模型或访问内部表示；在固定 token 预算下，通过信息论目标训练可实现更优的 Pareto 前沿。

  - **奖励权重余弦退火策略**：训练早期依赖 shaping 信号探索，中期衰减到 0 直接优化任务奖励，可减轻 critic 偏差。具体参考：shaping
  权重 λs 前半段置 1，45–60% 训练步数处开始衰减，后期 λs = 0。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：AI 智能体在流式环境（多轮对话、实时个性化）中无法保留无限上下文，长上下文还会引起“lost in the middle”。现有记忆机制如 MemGPT 启发式，或 MemAgent、Mem-α 等 RL 模型，依赖稀疏任务奖励，导致严重信用分配问题；而表面文本重建又忽略深层意图。需要一种有原则的方法，在固定 token 预算下主动将历史压缩为对下游任务最有用的摘要。

**方法关键点**：
- 将增量摘要建模为容量约束 POMDP，摘要 zt 作为 belief state 追踪潜在目标 Yt（对话中用户意图，阅读中待答问题）。推导值次优界：最小化序列信息损失 I(Yt;Ht|zt) 可最大化下游任务性能。
- 设计两个稠密信息论奖励：① **predictive sufficiency**：最大化 −H(Yt|zt)，用 variational 下界 E[log qϕ(Yt|zt)] 近似；② **recursive consistency**：最大化新摘要与局部上下文 (zt−1, at−1, ot) 的互信息，防止为了追求预测而编造与历史无关的内容。
- 训练统一 **asymmetric critic**：离线合成数据训练 critic qϕ，训练时可见 oracle 未来信息，推理时零 critic 调用。critic 以长度归一化 PMI 形式评分，减去无条件基线避免目标难度偏差。
- 策略用 KL-regularized PPO 更新，backward-discounted return-to-go，shaping 权重 cosine 退火：早期用 shaping 信号引导探索，后期衰减直接优化任务奖励。

**关键实验**：
- 两个基准：arXiv 科学阅读（K=500 token，20–25 块）和 WildChat 多轮对话（K=1024）。
- arXiv：MaxIM 的 Abstain-MCQ 准确率 66.39%，比 Task-Only RL 高 +11.95pp，比 MemAgent RL 高 +13.49pp；abstention 从 43.7% 降到 32.0%；Early-Section Stress Test 上 48.55% vs 32.23%（相对 +50.6%）。
- WildChat：MaxIM 是唯一在所有指标上正收益的方法，长对话（T≥10）上 Preference Retention +0.30，而 Task-Only RL 为 −0.37。事实一致性：contradiction 仅 4.27%，远低于 MemAgent 的 9.35% 和 Task-Only 的 7.04%。
- 消融：去掉 recursive consistency（Suff-Only）导致 arXiv 降 14.85pp，contradiction 升 51.8%；shaping 权重 mid-decay (45–60%) 最优，比不衰减高 +9.29pp。

**最值得记住的一句话**：用信息论 reward shaping 将长程稀疏奖励分解为稠密的预测充分性和递归一致性信号，能显著改善记忆压缩的信用分配和事实一致性，且推理时零额外开销。
