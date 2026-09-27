---
title: 'RAPID: Robot Agentic Programming from Demonstrations'
title_zh: RAPID：从视觉演示自动生成机器人程序
authors:
- Yuyao Liu
- Jiayuan Mao
- David Hsu
- Leslie Pack Kaelbling
- Tomás Lozano-Pérez
affiliations:
- Massachusetts Institute of Technology
- National University of Singapore
- University of Pennsylvania
- NVIDIA
arxiv_id: '2609.30249'
url: https://arxiv.org/abs/2609.30249
pdf_url: https://arxiv.org/pdf/2609.30249
published: '2026-09-24'
collected: '2026-09-27'
category: Agent
direction: 机器人 Agentic 编程与代码生成
tags:
- Agentic Programming
- Code Generation
- Robot Manipulation
- Object-Centric
- Trajectory Optimization
- Demonstration
one_liner: 利用编码 Agent 从单个视觉演示自动推断任务规范、动作原语与环境，迭代生成可泛化的机器人程序
practical_value: '- **Agentic loop 的要素拆解可复用**：将代码生成闭环拆成「可测试任务规范 + 动作原语 + 交互执行环境」，从单个演示自动推断。在推荐/搜索场景可类比：用
  LLM 从用户操作日志或行为样例中提炼可测试的策略约束（如点击率目标、多样性要求），再迭代生成和验证 query 或推荐策略。

  - **对象中心关系表示提升泛化**：用关系约束而非绝对坐标/ID 描述对象交互，使程序跨姿态、形状、材质泛化。可借鉴到生成式推荐或广告中：少用固定 item
  ID，改为对象属性、共现/替代/互补等关系特征，帮助冷启动与跨场景复用。

  - **高层意图与低层执行解耦**：动作原语定义为轨迹优化程序，只规定对象级运动效果，下层求解器处理具体路径。对应业务中把策略意图（如“提升 GMV”“增大曝光多样性”）编译为可执行算子，由底层排序/出价引擎实现，避免每次重新生成全量逻辑。

  - 主要是具身智能与机器人编程贡献，但验证-修正闭环和从演示自动推断规范的思路可借鉴到 Agent 工作流设计。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：编码 Agent 在软件编程中表现突出，但用于机器人系统需要同时解决可执行性、可验证性和泛化性。从单个视觉人类演示自动生成机器人程序仍具挑战，因为需要从低层运动轨迹中提炼可复用的高层策略。

**方法关键点**：RAPID 从演示中自动推断三个核心要素：可测试任务规范、动作原语和交互执行环境。代码生成采用迭代 Agentic 循环，反复执行、验证、修正。为提升泛化，程序使用**对象中心关系表示**，关注演示策略的底层结构而非具体运动：动作原语表达为轨迹优化程序，实现对象级运动效果；关系约束在运行时捕获场景几何，将原语组合成完整策略。这样生成的程序不绑定演示时的物体姿态、形状或材质。

**关键结果**：在仿真中评估了八个接触丰富的非抓取操作任务以及 LIBERO-Pro 基准中的通用抓取任务；在真实 Franka 机械臂上部署并评估所有八个非抓取任务。实验显示对物体姿态、形状、材质和环境的强泛化性能。
