---
title: 'RoboRSI: Stable, efficient, and reusable robot self-evolution in complex real-world
  environments'
title_zh: RoboRSI：复杂真实环境中稳定高效可复用的机器人自我进化
authors:
- Zimo Wen
- Yijin Chen
- Yuxuan Cao
- Wendi Chen
- Yanwen Zou
- Wenye Yu
- Fuhang Kuang
- Han Xue
- Jun Lv
- Chuan Wen
arxiv_id: '2610.12424'
url: https://arxiv.org/abs/2610.12424
pdf_url: https://arxiv.org/pdf/2610.12424
published: '2026-10-08'
collected: '2026-10-10'
category: MultiAgent
direction: 多智能体机器人技能自进化
tags:
- self-improvement
- multi-agent
- code-as-policy
- skill learning
- hierarchical decomposition
one_liner: 通过Top-Down Skill Refinement将任务分解为分层技能，多智能体协作实现机器人技能自我进化与复用
practical_value: '- 任务分层与责任归属：将复杂 Agent 工作流分解为 compound/atomic/base 技能，并明确定义输入-输出契约，每个失败可定位到具体技能分支，避免全局重写。电商
  Agent 中可将“选品策略”“生成文案”“出价”等拆为独立技能，定位问题更精准。

  - 验证后发布（Reviewer gate）：新技能或修复必须经过执行证据验证才能进入可复用库，防止低质量更新污染系统。推荐系统中策略更新可比照设置回归验证关卡。

  - 稳定序列固化为 compound skill：频繁出现的成功技能序列可封装为高级技能，减少后续规划 token 和推理时间。例如广告投放中“查询库存→生成标题→选目标人群”可固化为复合技能，降低
  LLM 调用成本。

  - 人在环（objectives and corrections）：用户只提供目标和纠正，不参与细节，多智能体自主规划、执行、诊断。电商 Agent 可让运营设定目标（如提升
  GMV）和纠正，系统自主迭代。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：通用机器人应通过经验自我提升，但现有代码生成 agent 的修复难以归因到具体能力，导致不稳定、低效、难以复用。

**方法**：提出 RoboRSI，基于 Top-Down Skill Refinement (TSR)。TSR 将任务分解为 compound、atomic、base 三层技能，每个技能有明确输入-输出契约和职责范围；执行结果被归因到具体技能分支，修订仅限该分支。系统包含 Manager、Planner、Engineer、Reviewer 四个角色：Manager 接收目标与纠正，Planner 规划，Engineer 执行与诊断，Reviewer 验证并发布新技能。稳定技能序列可固化为 compound skill 复用。人类通过目标和纠正引导。

**结果**：在移动机械臂上，RoboRSI 经过 104 轮开发出多物体家庭清理能力；在模拟环境 LIBERO、LIBERO-PRO、LIBERO-Plus、RoboTwin 上取得最高成功率，超出最强基线 2.7 到 11.0 个百分点；真实环境中，开启 code 后成功率达到 29.0%（对比 21.5%），token 使用减少 29.4%，VLM 调用减少 27.2%，wall time 减少 17.0%。
