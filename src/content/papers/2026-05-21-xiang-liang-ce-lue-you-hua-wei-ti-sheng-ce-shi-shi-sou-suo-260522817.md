---
title: 'Vector Policy Optimization: Training for Diversity Improves Test-Time Search'
title_zh: 向量策略优化：为提升测试时搜索而训练多样性
authors:
- Ryan Bahlous-Boldi
- Isha Puri
- Idan Shenfeld
- Akarsh Kumar
- Mehul Damani
- Sebastian Risi
- Omar Khattab
- Zhang-Wei Hong
- Pulkit Agrawal
affiliations:
- MIT
- Improbable AI Lab
- MIT-IBM Computing Research Lab
- Sakana AI
arxiv_id: '2605.22817'
url: https://arxiv.org/abs/2605.22817
pdf_url: https://arxiv.org/pdf/2605.22817
published: '2026-05-21'
collected: '2026-05-22'
category: Training
direction: RL 后训练多样性优化 · 测试时搜索
tags:
- VPO
- GRPO
- reward diversity
- test-time search
- multi-objective RL
- multi-answer generation
one_liner: 用向量奖励和随机标量化替代固定标量奖励，训练语言模型输出覆盖帕累托前沿的多样候选集，使测试时搜索收益随预算持续扩大。
practical_value: '- **多目标推荐/排序**：在电商推荐中，CTR、GMV、多样性常需平衡。借鉴 VPO 的向量奖励设计：将各指标作为独立维度，训练时随机采样权重标量化，鼓励模型生成覆盖不同
  trade-off 的候选集，供下游重排或搜索选择。

  - **Agent 工具调用与多步推理**：Agent 任务天然可拆解为子奖励（格式正确、工具名准确、参数填充质量等）。使用 VPO 可避免策略过早收敛到单一模式，保留探索能力，提升
  test-time 搜索（如 beam search、进化算法）的解空间质量。

  - **生成式推荐中的多样候选生成**：需生成多个推荐理由或商品序列时，直接在一条 autoregressive chain 中输出多个答案（multi‑answer
  chain），配合 VPO 的 set‑level 奖励，能获得内在差异化的候选，减少后续 rerank 的冗余。

  - **训练效率与多样性平衡**：若担心 VPO 牺牲单次生成精度，可在上线时结合 pass@1 和 pass@k 评估；也可仅在搜索型场景（如多轮交互式 Agent）使用
  VPO 微调，而单次推理保留 GRPO 版本，实现按场景切换。'
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
现代 LLM 后训练（如 GRPO）追求固定标量奖励下的最优，导致策略输出熵急剧下降，生成的候选解严重同质化。当模型被纳入 test‑time search（best‑of‑k、进化搜索）时，这种多样性丧失使搜索无法从更多样本中获益。该工作认为：RL 后训练应专注射出多种高质量、不同偏好的解，而将利用留给下游搜索；利用许多任务奖励天然具有向量结构（如代码生成按测试用例、问答按各跳正确性）的机会，可训练策略覆盖帕累托前沿。

**方法关键点**  
- **向量奖励建模**：保留奖励的 d 维分量，不做加权求和。为每个 rollout 采样随机标量化权重 w∼Dir(1) 均匀覆盖 simplex，以期望 max_{y∈S} wᵀr(x,y) 作为集合级奖励。
- **多答案链**：单次 autoregressive 生成 m 个候选（用分隔符连接），后生成答案可参阅前文，实现 in‑context 探索；比独立采样更有覆盖意识。
- **与 GRPO 结合**：用上述集合奖励替代 GRPO 中的标量奖励，计算组内优势后统一更新所有 token。代码只需更换 advantage 估计器。
- **其他对比实现**：Multi‑RLVR（多答案但固定标量）、Random‑w GRPO（单答案但随机权重）、Max‑at‑K、MaxRL、目标条件策略等，用于剥离成分贡献。

**关键实验**  
- 四个领域：人工迷宫（4D 导航）、MuSiQue（多跳问答，5D）、EUREQA（5 跳推理，5D 二元）、ToolRL（工具调用，4D 连续）。
- 核心指标：best@k（按训练标量评价）和 reward‑space diversity（候选间 L1 距离）。
- 主要数字：Maze 上 VPO best@30 0.593 vs GRPO 0.432；MuSiQue 上 VPO best@30 0.832 vs GRPO 0.728，且 VPO 的多样性 0.587 远高于 GRPO 的 0.054。趋势上，GRPO 随 k 增大迅速饱和，VPO 持续上升。
- 扩展性：在 LiveCodeBench 上，VPO 的 best@k 全面优于 GRPO；把两者接入 OpenEvolve 进化搜索，VPO 解出了 GRPO 在 best@30 为 0 的 32 道难题中的一部分，GRPO 停滞。

**最值得记住的一句话**  
“RL post‑training should focus exclusively on producing diverse, competent solutions, leaving exploitation to search.”
