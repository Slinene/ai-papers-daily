---
title: 'MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent
  Systems'
title_zh: MANTA：多智能体通信拓扑的自适应演化框架
authors:
- Mao-xun Huang
- Jerry Wang
- Yi-Cheng Lai
- Zhengxin Zhang
- Claire Cardie
- Hen-Hsen Huang
affiliations:
- Cornell University
- University of Illinois Urbana-Champaign
- Academia Sinica
arxiv_id: '2607.28527'
url: https://arxiv.org/abs/2607.28527
pdf_url: https://arxiv.org/pdf/2607.28527
published: '2026-07-30'
collected: '2026-07-31'
category: MultiAgent
direction: 多智能体协作拓扑在线自适应
tags:
- multi-agent systems
- topology adaptation
- self-improvement
- inference-time repair
- LLM agents
- orchestration
one_liner: 提出推理时拓扑自进化框架，根据任务和过程信号动态调整多智能体协作结构，在五个基准上平均得分74.0，超越最强基线5.8个百分点
practical_value: '- **动态协作拓扑用于多agent推荐/搜索系统**：在电商搜索或推荐中，多agent系统可分别负责意图解析、召回、精排、风控、冷启动等职责。借鉴MANTA，根据任务复杂度（如查询是否为长尾、是否含歧义）动态调整agent间的通信模式（星型、链式、辩论型），当检测到协作异常（如召回不足、过早收敛、多agent重复修改状态）时自动插入验证agent或重连通信边，提升最终推荐质量。

  - **过程信号驱动拓扑修复，避免固定工作流**：不需要预定义死板的工作流，而是通过trace auditing实时捕获过程异常（如工具调用失败级联、证据丢失、决策置信度不足），触发≤3个操作的拓扑变异（增加验证者、重组为链式、改写可见性），这些修复可被工程化实现为检查点与策略函数，适合嵌入现有的Agent框架。

  - **跨任务拓扑经验积累（long-term playbook）**：每次运行的拓扑决策、维修操作和效果可提炼为通用原则，指导新任务初始化，实现类记忆的迁移。在电商场景下，可将历史活动（双11vs平销）的协作经验复用以提升新任务效率，无需新成本搜索。

  - **低token开销的智能协调**：MANTA仅用约12%的推理计算做协调，却获得显著收益。这对线上服务延迟敏感的系统有益，可避免所有agent全量交流，按需触发验证或辩论，控制成本和响应时间。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**  
当前LLM多智能体系统的通信拓扑（如谁与谁对话、信息如何路由、校验顺序）在设计时固定，无法在执行中根据任务难度或中间过程异常自我调整。现有自改进方法只能调整个体输出、提示或追溯，忽略协作结构本身的在线优化。受生物系统持续适应环境启发，论文将拓扑视为推理时可自我改进的对象，提出从过程异常中决定是否重组、如何重组。

**方法关键点**  
- **拓扑表示**：agent具有结构角色（协调者、工作者、验证者、辩论者）和阶段角色（工人/批评者），按交互模式（星型、链式、辩论、投票）组成组，支持嵌套分组，通信可见性由策略控制。  
- **编排循环**：① 拓扑规划器根据任务与长期记忆设计初步拓扑；② 执行一轮合作；③ 痕迹审计器扫描过程信号（如工具失败级联、过早共识、重复状态修改、证据丢失等），依据可修复标志评级决定是否允许修复；④ 控制器允许一次≤3个拓扑变异操作（增删边、改变组模式、扩展agent为子树、调整可见性）并执行最后一轮。  
- **双视野记忆**：短期剧本记录当前运行所有轮次的拓扑与审计结果；长期剧本从多运行中提炼拓扑选择原则，由技能反思器周期性重写，仅用过程标签（是否清洁共识）而不接触基准答案。  
- **训练无关**：所有模型权重固定，无离线搜索，仅靠推理时审计-修复-记忆实现持续进化。

**关键结果**  
在BrowseComp、StableToolBench、PlanCraft、WorkBench、MATH五个基准上，MANTA均使用Gemma 4，平均得分74.0，超过最强基线（ADAS的68.2）5.8个百分点，同时消耗各多agent系统中最少的推理token。消融表明任务条件化的初始拓扑规划贡献最大（←57.5 vs 71.7），拓扑修复进一步提分，跨领域长期经验可正向迁移（平均+3.3点）。案例显示修复可解决分支过载、缺少验证、早熟共识、重复动作等具体问题。

**核心洞察**  
拓扑演化并非简单加agent或边；有时只需重连通信、调整执行次序或插入纯校验agent即可修复结构缺陷——该思想对复杂推理系统的设计具有启发意义。
