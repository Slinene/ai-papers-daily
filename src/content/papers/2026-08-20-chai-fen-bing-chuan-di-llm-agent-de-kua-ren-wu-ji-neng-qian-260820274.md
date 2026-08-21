---
title: 'Break It Down, Pass It On: Cross-Task Skill Transfer in LLM Agents'
title_zh: 拆分并传递：LLM Agent 的跨任务技能迁移
authors:
- Yiyang Feng
- Biddut Sarker Bijoy
- Niranjan Balasubramanian
- Jiawei Zhou
affiliations:
- Stony Brook University
arxiv_id: '2608.20274'
url: https://arxiv.org/abs/2608.20274
pdf_url: https://arxiv.org/pdf/2608.20274
published: '2026-08-20'
collected: '2026-08-21'
category: Agent
direction: Agent 技能归纳与跨任务迁移
tags:
- LLM Agents
- Skill Transfer
- Memory
- Subtask Decomposition
- Text Skills
- Code Skills
one_liner: 系统比较技能归纳层级与格式，发现子任务级文本技能迁移最可靠，并给出无需执行的技能效用评分
practical_value: '- 在构建 Agent 技能库/长期记忆时，优先按**子任务粒度**归纳技能，而不是整个任务轨迹。任务级技能容易过拟合源任务，插入后续任务上下文反而会拉低基线；子任务级技能在多个
  benchmark 上稳定带来提升。

  - 技能表示优先用**文本工作流笔记**而非代码函数。文本技能跨域迁移更稳，代码技能存在加载失败、参数化不干净、上下文干扰等问题；如必须用代码，要严格控制可加载性和参数抽象。

  - 可以用论文中的轻量诊断 score 在**任务执行前评估技能库质量**：对每条技能计算 specificity×abstractness，筛掉低分技能或调整归纳方式。该分数只依赖技能描述和任务描述，无需实际跑任务，适合上线前的技能库治理。

  - 在电商/Agent 场景可复用思路：把用户操作流程（登录、查购物车、下单、移愿望单等）拆成可共享子技能，并在 Agent memory 中按子任务检索；避免把整条用户
  session 总结成一条“大技能”塞进 prompt。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM agent 从已完成任务中归纳技能并复用，是经验增长的关键路径。但实践中技能迁移不可靠：从整条任务轨迹归纳出的技能往往过拟合源任务，在后续任务中成为无关或错位上下文，甚至让 agent 表现低于无记忆基线。已有工作要么只评估任务级技能，要么只在单一领域、少数模型上验证子任务级技能，缺乏对“何时技能能可靠跨任务迁移”的系统分析。

**方法关键点**
- 在两个维度上进行受控对比：**技能归纳层级**（task-level 对整个轨迹归纳一条技能 vs subtask-level 对每个子轨迹归纳一条技能）和**技能格式**（text 工作流笔记 vs code Python 函数），交叉共 6 个条件。
- 任务级 agent 是平坦 ReAct 循环；子任务级 agent 由 planner、executor、summarizer 循环分解任务，运行子轨迹后压缩成 summary。
- 技能记忆使用 all-MiniLM-L6-v2 做 description 检索；代码技能额外加载到命名空间。
- 提出**技能效用分数**：specificity 衡量技能与真实任务的匹配度，abstractness 衡量技能相关性在任务间的均匀度，效用为两者乘积；该分数只需技能描述和任务描述，无需执行任何任务。

**关键实验与结果**
在 AppWorld、OfficeBench、KramaBench 三个长程 benchmark 上，覆盖 11 个开源/商业模型。子任务级+Text 平均提升 1.9 点成功率，子任务级+Code 提升 0.5 点；任务级+Text 反而下降 1.2 点，任务级+Code 下降 4.1 点。文本技能在两种归纳层级下均优于代码技能。技能效用分数与任务成功率单调相关，且子任务级、文本技能的效用分数更高；transfer density 也显示子任务级技能被更密集地跨任务复用。

**最值得记住的一句话**
技能迁移的关键是“拆分粒度”：按子任务归纳的文本技能更抽象、更可复用，任务级技能过拟合源任务；specificity×abstractness 能在任务运行前诊断技能库质量。
