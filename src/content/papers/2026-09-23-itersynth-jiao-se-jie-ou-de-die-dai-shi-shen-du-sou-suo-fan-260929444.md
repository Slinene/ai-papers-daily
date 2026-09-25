---
title: 'IterSynth: Rethinking Deep Search Agents via Role-Decoupled Iterative Synthesis'
title_zh: IterSynth：角色解耦的迭代式深度搜索范式
authors:
- Xingyu Wu
- Yuchen Yan
- Zhengxi Lu
- Siqi Chen
- Xin ZHANG
- Aiting Liu
- Chao Deng
- Jie Liu
- Jin Ma
- Jian Shao
affiliations:
- 浙江大学
- 腾讯
arxiv_id: '2609.29444'
url: https://arxiv.org/abs/2609.29444
pdf_url: https://arxiv.org/pdf/2609.29444
published: '2026-09-23'
collected: '2026-09-25'
category: Agent
direction: 深度搜索 Agent 角色解耦与长程记忆优化
tags:
- Deep Search Agent
- Role Decoupling
- Long-Horizon RL
- Summarization
- Planner-Synthesizer
one_liner: 提出 IterSynth，将深度搜索拆为 Planner/Synthesizer 双角色共享策略并以 summary 为状态，通过角色解耦 RL
  将 8B 模型推至同级最强
practical_value: '- 在电商/搜索推荐等需要多步信息收集与决策的场景（如深度导购 Agent、商品调研、复杂 query 回答），可采用 Planner-Synthesizer
  双角色解耦：让一个角色专注于决定下一步查什么（query 规划），另一个角色负责把检索结果整合进紧凑的 summary，避免单一上下文无限增长。无需额外参数，只靠
  prompt 和 action 约束即可提升长程任务稳定性。

  - RL 训练中，把不同角色或不同功能模块的 advantage 分开归一化（role-specific group advantage），而不是混在一起，可以显著改善
  credit assignment，特别是多步交互中终端奖励稀疏的场景。工作里可替换成“规划器”和“执行器”等角色分组，分别计算基线。

  - 使用 evolving summary 作为唯一持久状态并每轮重构工作区，可以控制上下文长度，减少噪声积累；在电商推荐解释或对话式导购中，可用摘要维护用户画像/需求状态，逐步更新，而非保留全量历史。

  - 对已有闭源大模型，IterSynth 作为纯 prompting 工作流即可带来零样本提升（Claude 上 +5.5%, DeepSeek 上 +4.5%），可低成本快速验证：直接修改
  prompt 让模型交替规划与整合，无需训练。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**
现有 ReAct 式深度搜索 agent 存在两个核心问题：角色耦合——单一策略同时负责规划、证据使用和最终合成，容易导致过早终止、冗余搜索或浅层证据利用；上下文累积——不断增长的搜索历史引入噪声并淹没有用信息，实验显示 BrowseComp 上 59% 的 ReAct 轨迹在 64K 上下文中耗尽。因此需要同时解耦角色并管理上下文。

**方法关键点**
- **IterSynth 工作流**：一个共享参数的 LLM 交替扮演 Planner 和 Synthesizer。Planner 只看原始问题和当前全局 summary，决定是发起新 query 还是给出最终答案；Synthesizer 只接收检索结果，负责过滤噪声、提取事实并更新 summary。规划与整合分离，summary 成为持久搜索状态，且每轮上下文有界。
- **训练配方**：SFT 阶段用约 10K 高质量轨迹（由 Qwen3.5-397B 教师模型在真实搜索环境 rollout，平均 4.37 轮，展开为 87.4K per-turn 样本）教模型学会双角色格式。RL 阶段提出 RDPO：复合奖励 = 终端正确性 + α×角色特定 rubric 奖励（LLM judge 评分，rubric 从对比轨迹中归纳，每个角色 5 个维度），并按角色分组归一化 advantage，避免混合角色共享基线导致的 credit assignment 偏差。

**关键实验**
- IterSynth-8B 在五个长程 benchmark（BrowseComp、BrowseComp-ZH、GAIA、xBench-2505/2510）平均得分 50.7%，超过最强 ≤8B agent 4.2%；BrowseComp-ZH 达 55.4%，超最强小模型 15.2%。
- 在 30B 级 agent 中也有竞争力，参数仅 1/3 以下，超过 ReSum-30B、AgentFold-30B、OpenSeeker-30B。
- RDPO 有效性：SFT 44.1 → outcome-only GRPO 48.9 → RDPO 50.7；混合角色归一化变体仅 47.2。角色替换实验：Planner 换成未训练 base 下降 41.1%，Synthesizer 下降 17.4%。
- 纯 prompting 工作流：Claude-4.5-Opus 平均 66.1 vs ReAct 60.6，DeepSeek-V3.1 47.9 vs 43.4；BrowseComp-ZH 上比 ReAct 高 10.0%。

**最值得记住的一句话**
角色解耦 + 有界 summary 状态 + 角色分组优势估计，让 8B 模型在长程搜索中打平或超越更大 agent，且无需额外参数，对前沿模型 prompting 也有增益。
