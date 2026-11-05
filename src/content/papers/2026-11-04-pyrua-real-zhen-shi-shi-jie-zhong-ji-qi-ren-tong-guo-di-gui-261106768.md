---
title: 'PyRUA-REAL: Robot Exploration and Adaptive Learning through RSI in the Real
  World'
title_zh: PyRUA-REAL：真实世界中机器人通过递归自我改进进行探索与自适应学习
authors:
- Qiang Wang
- Jianxin Bi
- Shulong Jiang
- Ruiyang Si
- Wenbo Huang
- Kaiqi Chen
- Jiaxin Li
- Liyun Li
- Xuanyi Li
- Daquan Zhou
affiliations:
- Peking University
- EngineAI
- National University of Singapore
arxiv_id: '2611.06768'
url: https://arxiv.org/abs/2611.06768
pdf_url: https://arxiv.org/pdf/2611.06768
published: '2026-11-04'
collected: '2026-11-05'
category: Agent
direction: Embodied Agent 递归自我改进与技能复用
tags:
- Embodied RSI
- Coding Agents
- Code as Policies
- Robot Learning
- Memory
- Skill Reuse
one_liner: 提出 PyRUA-REAL 框架，使 coding agent 将物理交互经验转为持久记忆与可复用技能，实现真实机器人递归自我改进
practical_value: '- 把交互经验沉淀为可复用技能：在推荐/搜索 Agent 中，将成功任务（如 query 改写、召回策略）固化为可调用函数或 Skill
  库，推理时优先检索复用，避免每次从零生成；对应论文的 persistent memory 与 reusable executable skills。

  - 用执行反馈驱动策略迭代：引入线上真实反馈（点击、转化、报错）作为 refinement 信号，构建“执行-观察-修改”闭环；论文验证了不同执行反馈对代码优化有显著影响，业务中可设计细粒度反馈格式提升
  Agent 自适应能力。

  - 任务规范与历史技能联合输入：将任务描述与已有 skill 库一起提供给 Agent，提升新任务上的迁移鲁棒性，类似 few-shot + skill library；对冷启动或跨品类推荐有借鉴意义。

  - 离线部署固化程序，降低在线决策成本：对高频固定任务，把 Agent 探索得到的策略导出为可独立运行的程序，不依赖在线 agent 决策，减少推理延迟和成本；论文评估了无
  agent 部署的效率与能力。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：LLM coding agents 能将任务指令转为可执行机器人程序，但如何将物理交互经验持久化并带来持续能力提升，仍不明确。

方法：提出 PyRUA-REAL 框架，coding agent 在真实环境中探索、执行代码并收集反馈；交互经验被保留为持久记忆与可复用可执行技能，用于指导下一次探索与改进。经验研究围绕物理操作展开，分析多个关键因素：agents 之间的协作方式、不同执行反馈（如错误信息、视觉观察）对代码优化的作用、任务规范与历史技能如何影响鲁棒性与任务迁移。此外，框架支持将探索得到的程序离线部署，无需在线 agent 参与决策，评估其效率与能力。

结果：在 8 个真实世界任务上平均成功率 91.1%；在 RoboDojo 基准的 42 个任务上平均成功率 84.4%。
