---
title: 'Transforming Integer Grids to Spatial Intuition: Perception, Not Planning,
  Governs ARC-AGI-3'
title_zh: 将整数网格转化为空间直觉：感知而非规划主导 ARC-AGI-3
authors:
- Harsidak Singh Banwait
affiliations:
- Independent Researcher
arxiv_id: '2611.06793'
url: https://arxiv.org/abs/2611.06793
pdf_url: https://arxiv.org/pdf/2611.06793
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Agent 空间感知引擎
tags:
- ARC-AGI
- spatial perception
- code-as-action
- agent architecture
- sample efficiency
- visual reasoning
one_liner: SARBLOH用零参数O(HW)空间感知引擎配合代码动作，ARC-AGI-3评分从3/28升至25/28，token降89.4%。
practical_value: '- 在将页面/商品网格、布局或搜索广告位状态喂给 Agent 时，不要直接序列化原始矩阵/像素：先用轻量 O(HW) 感知器提取对象、边界、邻接关系，保留空间拓扑，能显著降低
  LLM token 并减少“重新发现基本结构”的浪费。

  - 借鉴“measured vs guessed”分层：把系统已知的确定性特征与需要验证的 affordance 假设分开，Agent 只对不确定假设做主动 probe，避免在已经证明的不变量上反复探索；可用于交互式推荐策略和会话
  Agent 的探索控制。

  - 动作空间上移：面向电商 Agent，尽量让 LLM 输出高层可执行代码/API/DSL（如批量规则、检索条件）而非逐项点击/滑动；这种 code-as-action
  能提高单次决策成功率，也可与推荐策略编排结合。

  - 35ms 零参数感知 + 结构化简报是很好的实时压缩范式：低延迟、无训练，适合线上推荐/广告场景中作为 LLM 的前置特征编码层，先空间结构化再推理，避免高成本
  planning。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：ARC-AGI-3 用 Relative Human Action Efficiency 惩罚探索浪费。前沿模型直接读整数网格会因序列化破坏空间拓扑，出现感知误导，把大量动作浪费在重新发现基本边界和对称上。工作假设是：限制交互推理的瓶颈是空间感知，而不是规划能力。

**方法关键点**：SARBLOH 用零参数 O(HW) 感知引擎，每帧 35ms 转为对象清单、双向时序跟踪、几何简报和标注画布。几何简报按 Measured–Guessed 规则分离已证明不变量和 affordance 假设。动作端采用 code-as-action：LLM 输出算法假设，而不是低层移动。实验区分 briefing off 和 briefing on。

**关键结果**：8 个结构演示上，grounded perception 把 rubric 得分从 3/28 提升到 25/28（8.3 倍），token 消耗减少 89.4%。23 个留出游戏上，几何不变量 100% 泛化，单帧 affordance 猜测仅 6–50%，说明主动验证探针仍必要。公开集 Run A 解决 143/183 关，8.2 小时，单遍效率 59.4%；Run B 提升到 63.5%。官方 9 小时单卡评测中，隐藏 Kaggle 得分 16.53，是首个 Milestone winner 的 13.7 倍。
