---
title: Coding Agents with an Obstacle-Aware Harness for Safe Robot Manipulation
title_zh: 面向安全机器人操作的障碍感知编码智能体约束框架
authors:
- Bingxin Xu
- Yuzhang Shang
- Zhen Dong
- Emilio Ferrara
affiliations:
- USC
- UCF
- UCSB
arxiv_id: '2609.20822'
url: https://arxiv.org/abs/2609.20822
pdf_url: https://arxiv.org/pdf/2609.20822
published: '2026-09-17'
collected: '2026-09-20'
category: Agent
direction: 编码智能体的安全约束规划
tags:
- Coding Agents
- Robot Manipulation
- Safety
- Obstacle Avoidance
- LLM Planning
- Harness
one_liner: 提出 SafeHarness，通过障碍感知路径规划与接触执行显著提升编码智能体的任务成功率和避碰率
practical_value: '- 约束优先级显式化：在 prompt 里写“不要撞障碍物”不够，需把安全约束拆成结构化步骤。电商 Agent 中“不违规”“不超预算”等约束可借鉴：先规划、验证约束、必要时重新规划，再执行。

  - 阶段分解定位失败：将任务拆成 route phase 和 contact-rich moment，分别定位不满足约束的环节。推荐/广告 Agent 可对“选品→出价→文案”分段做约束检查，避免只在最终输出把关。

  - 用结构化中间表示消解歧义：将物体表示成 bounding boxes、路径写成 waypoints，减少 LLM 对场景的自由裁量。对应到业务可用结构化 schema（如候选
  query 列表 + 规则标签）让 Agent 做约束内选择。

  - 验证-重规划闭环：选择路径后先 verify，不可行就 replan，而非一步到位。适合用在需要多步决策的推荐 Agent 流程，比如先选候选集再过滤违规项，失败后回退重选。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
编码智能体（coding agents）能生成机器人控制程序而无需任务专用训练，但安全性未受关注。论文在“目标+不可触碰障碍物”的约束下评估，发现智能体大多只追求任务完成而碰撞障碍物：它能感知障碍物、指令中也已禁止触碰，但约束从未成为规划优先级。

**方法关键点**
将操作分解为路线阶段（route phase）与接触密集时刻（contact-rich moment），定位失败来源。SafeHarness 提供两个障碍感知 harness：
- *障碍感知路径规划*：将物体建模为 bounding boxes，候选路线表示为 waypoints 序列；智能体先规划、验证，必要时重规划，再执行。
- *障碍感知接触执行*：选择接触位置，使接触动作本身避开障碍物。

**关键结果**
SafeHarness 达到 71.9% 任务成功率和 87.5% 避碰率，较之前 SOTA 分别提升 6.5% 和 27.0%；相比无 harness 的同一智能体，分别是 2.3× 和 1.5×。
