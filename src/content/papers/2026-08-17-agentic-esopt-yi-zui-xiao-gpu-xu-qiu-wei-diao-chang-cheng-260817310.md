---
title: 'Agentic ESOpt: Fine-Tuning Long-Horizon LLM Agents with Minimal GPU Requirements'
title_zh: Agentic ESOpt：以最小 GPU 需求微调长程 LLM Agent
authors:
- Zhi Zheng
- Rongsheng Chen
- Yunpeng Ba
- Zhenkun Wang
- Yee Whye Teh
- Wee Sun Lee
affiliations:
- National University of Singapore
- Southern University of Science and Technology
- University of Oxford
arxiv_id: '2608.17310'
url: https://arxiv.org/abs/2608.17310
pdf_url: https://arxiv.org/pdf/2608.17310
published: '2026-08-17'
collected: '2026-08-19'
category: Training
direction: Agent 微调 · Evolution Strategies
tags:
- Evolution Strategies
- Long-horizon Agents
- Fine-tuning
- Prompt-Parameter Co-evolution
- GPU Memory Efficiency
- GRPO
one_liner: 用进化策略替代强化学习微调长程 LLM Agent，仅需推理级显存并支持 prompt-参数协同演化
practical_value: '- 长程、稀疏奖励的 Agent 业务（多轮对话推荐、工具调用、自动化工作流）可考虑用 ES 全参数微调替代 GRPO/PPO：只需推理级
  GPU 内存，适合无法承载 RL 反向传播的大模型。

  - 实现 trick：只存噪声种子、in-place 加减扰动量；每批采样后用 z-score 归一化 reward 再加权更新；扰动半径 σ 用余弦衰减，train-time
  保留非零 σ_T 防止过拟合，test-time 衰减到 0。

  - prompt-space 优化（如 Trace2Skill、EoH）与参数优化共享同一批 rollout，交替更新 prompt 和参数，可迁移到自动 heuristic/策略设计或线上
  prompt-参数协同调优。

  - 根据模型能力调整 ES population：强 backbone 可能只需较小 G，能进一步降低采样成本；在 4B 上 G=8→16 提升巨大，但 9B
  上提升极小。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：长程 agentic 任务轨迹分支多、奖励稀疏。RL 需要存激活、优化器状态并回传，GPU 成本高；且 PPO/GRPO 把轨迹级奖励分配到每个 turn，信用分配随 horizon 恶化。ES 在参数空间直接做轨迹级归因，天然规避这些问题。

**方法关键点**：
- 全参数 ES 更新：从当前参数采样 G 个扰动，评估对应 agent 的任务回报，z-score 归一化后做加权更新 θ←θ+α/G∑R̂_iε_i；只需存噪声种子，内存同推理。
- 余弦衰减扰动半径 σ_t，train-time 保留非零 σ_T 平衡探索与平滑正则，test-time 衰减到 0 减少偏差。
- 黑盒反馈接口：同一批 rollout 可被 prompt-space 优化器复用，实现 prompt-parameter co-evolution，与 Trace2Skill/EoH 等组合。

**关键实验**：
- Sudoku H*=5/10/15：ESOpt 在 H*=15 达 53.13%，比最强 GRPO 40.63% 高 12.5 个点，PPO 为 0%；训练内存仅 8.41GB，GRPO 为 58.88GB。
- ReAct 工具使用 Math/DocVQA：ESOpt 平均比 base 高 13.7%，比 GRPO 高 8.3%，且 Pass@4 不下降。
- WebArena-Lite 27B：ESOpt 将 No Skill 从 29.47% 提升到 36.16%，与 Trace2Skill 组合从 33.94% 到 36.36%。
- test-time 自动启发式设计：36 个匹配比较中改善 28 个。

**最值得记住的一句话**：ES 的 trajectory-level 参数归因不随 horizon 累积方差，因此在长程稀疏奖励 Agent 训练中，它不是 RL 的廉价替代，而是更匹配的优化范式。
