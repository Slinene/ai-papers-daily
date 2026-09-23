---
title: 'MAGIC: Mixed-Granularity Agent Graphs via Incremental Construction with Dense-Reward
  Reinforcement Learning'
title_zh: MAGIC：通过增量构建与稠密奖励强化学习生成混合粒度智能体图
authors:
- Kairui Yang
- Ziheng Yi
- Xunkai Li
- Minghao An
- Zhanke Liu
- Zekai Chen
- Rong-Hua Li
arxiv_id: '2609.26667'
url: https://arxiv.org/abs/2609.26667
pdf_url: https://arxiv.org/pdf/2609.26667
published: '2026-09-22'
collected: '2026-09-23'
category: MultiAgent
direction: 多智能体任务自适应拓扑生成
tags:
- Multi-Agent Systems
- Reinforcement Learning
- Graph Generation
- Mixed-Granularity
- Potential-Based Reward Shaping
one_liner: 提出混合粒度多智能体组织图生成，局部选择单智能体或可复用组，以稠密奖励 RL 直接优化构建策略，在 8 个基准上全面领先
practical_value: '- 业务多智能体 pipeline（如电商搜索/推荐 Agent、广告文案生成、客服）常固定拓扑；MAGIC 的做法是把角色库做成
  single/group 可选，局部决定子任务是否需要小组协作，能显著降低 token 成本并保持精度。可直接借鉴：将高频子任务封装为可复用 group 模板，简单子任务保留
  atomic agent。

  - 训练构建策略时可放弃先搜索再 SFT，直接用 on-policy RL + potential-based reward shaping；用固定 probe
  集评估部分图效用，给中间 ADD 决策稠密信号，在任务反馈稀疏、API 预算有限时更划算。

  - potential 由 probe utility + structural complexity + role repetition 三部分构成，总回报保持不变（potential-based
  shaping），最终任务分数被重分配到中间步骤，适合离线日志/仿真环境训练组织策略。

  - 工程上注意训练与推理成本分离：推理只执行最终组织；训练 probe 评估可缓存复用。这对线上 LLM Agent 编排有直接参考价值。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
LLM 多智能体系统的效果和成本取决于协作拓扑。现有方法要么全原子 agent、要么全 group，固定粒度无法适配同一任务内不同子任务的复杂度差异。例如 API 更新任务中，调查变更和测试兼容性适合小组协作，而一两行补丁可能只需单个 Programmer。因此需要混合粒度组织空间，支持局部选择单 agent 或可复用 group。

## 方法关键点
- **混合粒度组织空间**：库角色 r 可被实例化为 atomic agent 或固定内部 DAG 的 group，两者暴露相同外层接口；组织图由顶层单元和依赖边构成。
- **增量构建策略**：从空图开始，每步选择角色、粒度、前驱连接，显式 STOP 结束；策略用 GRU + 注意力编码当前图和任务，三个头输出分层动作。
- **稠密奖励**：用固定 probe 集评估部分图的边际效用，加上结构复杂度和角色重复惩罚，构造 potential-based shaping；总回报仍保持终端任务分数。
- **优化方式**：on-policy policy gradient，每 query 采样 2 条轨迹，位置对齐 advantage 标准化，KL/熵正则，参照冻结初始策略；不依赖搜索-SFT 成功轨迹语料。

## 关键实验
在 MMLU-Pro、StrategyQA、AQuA、GSM8K、HumanEval、LiveCodeBench-v6、TAT-QA、TabFact 共 8 个基准上对比 17 个基线，MAGIC 全部排名第一。主要提升：MMLU-Pro 从 73.60% 到 83.20%，LCB-v6 pass@1 从 26.86% 到 36.57%。消融显示混合粒度 + 稠密奖励在 MMLU-Pro 达 77.00 acc、TAT-QA 达 83.51 F1，均高于 All-Atomic、All-Group 和 Final-reward-only，且 token 消耗更低。匹配 API 预算下 Dense-reward RL 优于 Search-then-SFT：CNY 10 时 MMLU-Pro 78.00 vs 70.00。推理效率上，MAGIC 在四个代表基准上处于 Pareto 前沿，其中三个数据集 token 使用最低。

**最值得记住**：混合粒度局部选择让同一组织内把需协作的子任务用 group、简单子任务用单 agent，可同时提升效果并压低执行 token；potential-based shaping 给中间构建步骤反馈，不改变终端任务目标。
