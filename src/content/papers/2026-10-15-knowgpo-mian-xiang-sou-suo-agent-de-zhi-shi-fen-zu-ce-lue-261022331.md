---
title: 'KnowGPO: Knowledge-Grouped Policy Optimization for Search Agents'
title_zh: KnowGPO：面向搜索 Agent 的知识分组策略优化
authors:
- Siqi Chen
- Zhengxi Lu
- Yuchen Yan
- Xingyu Wu
- Qipeng Chen
- Xin Zhang
- Aiting Liu
- Chao Deng
- Jie Liu
- Jin Ma
affiliations:
- Zhejiang University
- Tencent
arxiv_id: '2610.22331'
url: https://arxiv.org/abs/2610.22331
pdf_url: https://arxiv.org/pdf/2610.22331
published: '2026-10-15'
collected: '2026-10-16'
category: Training
direction: 搜索 Agent 强化学习 · 过程奖励
tags:
- Process Reward
- Search Agent
- Credit Assignment
- GRPO
- Knowledge State
- RLHF
one_liner: 把搜索轨迹按已满足的原子知识条件分组，用增量知识增益做过程奖励，8B agent 超过多数 32B 开源系统
practical_value: '- 电商导购/客服 Agent 可把多轮对话状态抽象为“已确认的原子约束集合”，例如已确认类目、预算、尺码、场景；每轮新增确认约束作为
  incremental gain，按“当前已确认约束集合”分组做组内对比，避免按 query 文本相似度硬聚类。论文显示这种语义分组有效对比步数 ESR 达 97.8%，远高于
  observation 相似度的 51.8%。

  - 若有转化/成交/收藏等结局 label，可离线把成功会话反向拆成必须确认的知识条件，再用这些条件给失败或中间轨迹构造过程奖励。两阶段构造 pipeline：先生成
  placeholder 条件，再用答案和成功轨迹做实体接地，能降低对单条成功轨迹的依赖。

  - 过程奖励只需 incremental knowledge gain，不需要 critic 或 learned reward model；verifier 用
  LLM 异步执行，可隐藏训练墙钟开销。对预算有限的团队，这比学 reward model 更容易落地。

  - 混合 outcome reward 与 process reward 时不要过度偏向 process：论文最佳 ω=0.3，过大会偏离最终转化目标。业务中可优先在
  0.2–0.4 内调参，避免多轮 agent 只优化局部信息收集。'
score: 9
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
Deep search agents 是多跳、长程、多轮检索决策，只有最终 outcome reward 很难区分每一步搜索动作是有用、冗余还是有害。现有过程监督方法要么依赖表面状态复用，如 GiGPO 按 observation 相似度对齐轨迹；要么依赖模型自身答案概率，如 IGPO 用内部置信度做密集奖励。但在异构检索结果、长噪声上下文中，表面状态复用率低，模型置信度也不可靠。需要一种环境中立、可验证的进展信号。

## 方法关键点
- 对每个 query，把推导答案所需信息分解为原子知识条件集合 K(Q)。用两阶段构建：Stage 1 只从 query 生成带占位符的 reasoning skeleton；Stage 2 用正确答案 y* 和一条成功参考轨迹把实体占位符接地，保证 atomicity、completeness 和 grounding consistency。
- 每步用 LLM verifier 判断新观察是否验证了某个知识条件，单调累积成 knowledge state s_{i,t}。
- 将相同前序 knowledge state 的 step 分成一组 G(̃s)；用 incremental knowledge gain r_{i,t}=||s_{i,t}||_1−||s_{i,t−1}||_1 作为 step reward，组内归一化得到 step advantage。
- 最终优势 A=(1−ω)A_E+ωA_S，用 PPO-clipped 目标加 KL 约束训练。无需 observation matching、critic 或模型自身概率。

## 关键实验
基座 Qwen3-8B，上下文扩展到 128K。在 Xbench-2505/2510、BrowseComp-ZH、GAIA 上，KnowGPO 比 GRPO 高 2.0–5.9 个百分点，比最近的过程监督基线 GiGPO/IGPO 平均高 3.8–4.2 个百分点。8B agent 在 BrowseComp-ZH 达 38.8%，超过同尺寸 WebExplorer-8B 6.8 个百分点，也超过 WebSailor-32B、DeepDive-32B，仅比 DeepMiner-32B-RL 低 1.3 个百分点。消融显示 ω=0.3 最优；incremental gain 和 knowledge-state grouping 都必要；incremental gain 优于 discounted future return。分组质量上，knowledge anchor 的 ESR 为 97.8%，远高于 observation 的 51.8% 和 action 的 79.4%。训练成本方面，异步 verifier 可隐藏墙钟开销，额外 bookkeeping 不到总预算的 0.08%。

**最值得记住：在长程搜索中，用“已满足的原子知识条件”表示状态，并用增量知识增益做组内过程奖励，比匹配表面观察或对模型置信度建模更稳定、更可落地。**
