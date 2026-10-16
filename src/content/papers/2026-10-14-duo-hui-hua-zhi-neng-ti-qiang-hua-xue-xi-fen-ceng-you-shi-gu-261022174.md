---
title: 'Mosaic: Multi-Session Agentic Reinforcement Learning'
title_zh: 多会话智能体强化学习：分层优势估计与塑造
authors:
- Yilong Xu
- Minrui Xu
- Xinyu Zhou
- Xiang Long
- Haochen Tan
- Zhijiang Guo
affiliations:
- LARK, HKUST(GZ)
- Foundation Model Lab, Huawei
- City University of Hong Kong
- HKUST
arxiv_id: '2610.22174'
url: https://arxiv.org/abs/2610.22174
pdf_url: https://arxiv.org/pdf/2610.22174
published: '2026-10-14'
collected: '2026-10-16'
category: Agent
direction: Agent 强化学习 · 多会话轨迹优化
tags:
- Agentic RL
- GRPO
- Multi-Session
- Advantage Shaping
- Context Compaction
- Subagent
one_liner: 提出 Mosaic，用 session-aware 轨迹优势与 session 级边际信息增益塑造，在 BrowseComp 上超越广播基线且会话数更少
practical_value: '- 搜索/对话 Agent 常因 query 改写、上下文压缩、子 agent 并行搜索产生多会话轨迹，RL 训练时不要简单广播轨迹奖励；可借鉴
  session-aware advantage：按 outcome 分组对 session 数做居中排名，成功样本少 session 给更高优势，失败样本多 session
  降低负优势，既提升样本效率又控制推理成本。

  - 用 answer-likelihood 的边际信息增益做过程监督，无需额外 critic，仅需两次前向计算 log-prob；按 session 类型（普通、压缩、子代理）分别归一化，避免类型分布偏差，适合多组件
  Agent 架构。

  - 工程实现上，把每个 session 作为独立 training segment，聚合时保持 trajectory 级 token 权重一致，可兼容 Megatron
  等多 segment 训练；对多轮搜索/电商 Agent 的长轨迹训练有直接迁移价值。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 Agentic RL 方法普遍假设单会话轨迹，但实际 agent harness 中上下文压缩（context compaction）和子代理分叉（subagent forking）会自然产生多会话轨迹，训练与推理不匹配；简单广播轨迹优势到所有 session 无法区分各会话贡献，缺少对 session 分配的控制。  

**方法关键点**  
- 提出多会话 Agentic RL 设置，将轨迹表示为一组 session。
- 轨迹级 session-aware advantage estimation：在 GRPO 优势上乘一个由 session 数决定的调制因子 (1−ρu)，其中 u 是按 outcome 分组内的居中排名。成功轨迹用更多 session 优势更低，失败轨迹用更多 session 负优势更小（鼓励探索），且 outcome 信号保持主导；同质 outcome 组用加性 fallback 提供 session 相关变化。
- 会话级 advantage shaping：将每个 session 视为状态转移，计算 session 前后策略对 ground-truth answer 平均对数似然的边际信息增益（marginal IG）作为即时奖励，按 session 类型分别归一化后与轨迹级优势相加；排除最后一个 session 避免最终答案混淆。

**关键结果**  
在 BrowseComp 上以 Qwen3.5-4B 为基座，对比 GRPO、IGPO、Broadcasting 等 baseline。Mosaic 在 context compaction 场景准确率 38.86 vs Broadcasting 35.31（相对提升 10.1%），平均 session 数从 3.17 降至 2.35；在 subagent 场景准确率 32.46 vs 31.44，session 数从 4.43 降至 3.77。消融表明两个组件均有贡献，并观察到 session utility 和 allocation 的提升。

**最值得记住的一句话**  
多会话优化的核心不是用多少 session，而是从执行的 session 中获得多少有用进展。
