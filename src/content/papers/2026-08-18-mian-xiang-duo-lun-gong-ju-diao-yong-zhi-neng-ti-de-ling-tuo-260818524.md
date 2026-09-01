---
title: 'DART-SD: Diamond-topology Aware Retrieval and Tuning for Self-Distillation
  of Multi-Turn Tool-Calling Agents'
title_zh: 面向多轮工具调用智能体的菱形拓扑感知检索与自蒸馏训练框架
authors:
- Hangrui Xu
- Jiarui Wang
- Yang Yang
- Chuanbo Zhu
- Fangda Chen
- Ziqi Wu
- Jingming Cai
- Yan Song
affiliations:
- ByteDance
- University of Science and Technology of China
arxiv_id: '2608.18524'
url: https://arxiv.org/abs/2608.18524
pdf_url: https://arxiv.org/pdf/2608.18524
published: '2026-08-18'
collected: '2026-09-01'
category: Agent
direction: 多轮工具调用 Agent 的自蒸馏训练
tags:
- Agent
- Self-Distillation
- Tool-Calling
- Graph Topology
- Credit Assignment
- Localized Supervision
one_liner: 构建交互状态转移图并识别关键拓扑断点，仅对恢复步骤做局部监督，提升多轮工具调用效率与泛化。
practical_value: '业务值得借鉴的：

  - 将多轮工具调用轨迹建模为交互状态转移图（ISTG），用信息原子抽象归一化语义等价工具响应，可有效压缩状态空间并捕捉顺序无关子目标的菱形拓扑，适合电商/搜索
  Agent 中多路径比价、商品查询等场景。

  - 用成功可达区域投影定位第一个偏离点（CTB），只对失败后的恢复步骤做局部监督并 mask 有效前缀，避免全局 SFT/RL 对有效探索的误惩罚，可缓解 credit
  misassignment 和灾难性遗忘。

  - 采用渐进式自蒸馏：每轮从学生 rollout 中检测能力边界，用教师轨迹检索恢复参考，形成自步课程；工程上可低成本迭代，且能逐步缩短工具调用链（文中 3.55
  vs golden 4.02）。

  - 在具备 verifiable feedback 的自动构建环境（类似 FTRL）中先构造教师轨迹池与状态图，再迁移到真实业务前可用该框架做离线自蒸馏。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多轮工具调用是构建自主 Agent 的关键能力，但现有训练范式将执行过程压成线性轨迹。对于含顺序无关子目标的任务，最优解空间本质是组合爆炸的菱形拓扑，全局 SFT 或 GRPO 式 RL 会造成“拓扑坍缩”：要么强制模仿整条轨迹，要么把奖励均匀分摊到所有中间步骤，导致有效探索被错误惩罚、策略多样性下降。

**方法关键点**
- **交互状态转移图 ISTG**：把每个状态定义为累积信息原子集 + 无效操作多重集；语义等价响应归一到同一信息原子，无效/空响应不产生原子，从而自然形成可汇聚的菱形结构。
- **成功可达投影与 CTB**：将所有教师 rollout（成功/失败）嵌入图，用预算过滤出经验成功可达区域；学生状态按主/辅节点类型投影到教师锚点，首个“可投影→不可投影”的转移即为 Critical Topological Breakpoint。
- **CTB 引导的局部监督**：保留 CTB 前的学生有效前缀，从教师图中采样成功/失败轨迹作为特权上下文，生成恢复续写；损失 mask 只作用于 CTB 之后生成的 assistant 恢复步骤，保护前缀和最终答案。
- **渐进式自蒸馏**：每轮用当前学生生成多条轨迹，动态重定位 CTB，随着能力边界后移形成自步课程，无需手工课程设计。

**关键结果**
在 FTRL 训练，Qwen3-4B/8B 上平均得分分别达到 39.17/45.58，超过 SFT、FTRL-GRPO、ToolRL、MatchTIR 等基线；8B 模型在 FTRL Solve-F1 上从 base 23.48 提升到 45.66，并超过教师；成功轨迹平均工具调用数从 4.23 降到 3.55，短于 golden 4.02；CTB 位置从 0.348 推进到 1.452；通用能力（IFEval/AIME/MMLU）平均 49.89，也高于 base 43.92 和 SFT 44.18。

**最值得记住的一句话**
有效的 Agent 蒸馏应由交互状态拓扑而非刚性轨迹模仿驱动——找到第一个偏离点，只纠正恢复步骤，保护有效前缀。
