---
title: 'HEXIS: Compiling Skills into Extended Finite State Machines'
title_zh: 将 Agent 技能编译为扩展有限状态机以提升执行合规性
authors:
- Minghao LI
affiliations:
- WorldBuilder013
arxiv_id: '2609.30123'
url: https://arxiv.org/abs/2609.30123
pdf_url: https://arxiv.org/pdf/2609.30123
published: '2026-09-24'
collected: '2026-09-25'
category: Agent
direction: Agent 技能编译与工作流执行优化
tags:
- EFSM
- Agent Skills
- Workflow Compilation
- Trace Alignment
- SkillOpt
- LLM Agents
one_liner: 把技能文档编译为扩展有限状态机，分离知识提示与显式控制流，跨 4 个基准平均提升 16.1 个百分点
practical_value: '- 可将电商/客服/审核/投放等领域的 SOP 或技能文档编译为状态机：状态内放局部 prompt 和工具调用，控制流交给 guard
  规则与 runtime，模型不再从长上下文里反复推断下一步，能显著减少步骤遗漏。

  - 用变量保存前序结果（商品列表、校验结果、已选类目等），guard 直接基于变量判断分支/循环/终止；模型只负责状态内推理和生成，控制决策边界由程序显式执行，适合流程固化。

  - 做增量更新时采用 trace replay 回归：每次根据新轨迹修改状态机，必须重放新旧全部轨迹且通过静态检查才接受，防止新增分支破坏已跑通任务，类似推荐系统里的回归测试。

  - 只需用一个强模型编译状态机，即可跨多个执行模型复用，无需按目标模型重新编译；若同时优化技能文本，可以先跑 SkillOpt 再编译，能进一步提分并降低 tokens。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
Agent 技能文档通常把领域知识、指令和控制要求混在自然语言里。常见做法是把整份文档塞进上下文，让模型在每一步自己推断下一步该做什么。但长任务中模型容易忽略明确要求，例如检测到失败后只报告而不执行修订；即使文档写清楚了，控制要求也没有被强制。这个问题在 SOP 类任务中特别突出，因为一两次步骤偏离就会导致整条流程失败。

## 方法关键点
HEXIS 把技能语义拆成两部分：**状态内知识**和**显式控制流**，将技能编译成扩展有限状态机（EFSM）。

- **状态表示**：每个状态绑定一个操作（模型调用、工具调用、判定或终止），携带局部指令 prompt、read/write 变量、工具参数模板和资源引用。模型只负责当前状态内的推理和生成。
- **控制流**：状态之间的转换由 guard 条件显式决定，guard 基于变量值计算；无条件边放最后，循环带计数器上限；终止状态记录 outcome category。
- **初始编译**：从技能文档提取 clause、必需操作、顺序要求、禁止行为和终止条件，生成机器草稿；再进行格式、类型、guard 语法、图结构、变量依赖等静态检查，失败则用错误信息重试。
- **轨迹增量更新**：提取开发轨迹中的可观测事件，按操作类型、工具名和调用阶段对齐到现有状态；未匹配事件生成新状态；通过修改变量绑定和转换补上缺失依赖。更新候选只有通过静态检查以及新轨迹和所有历史轨迹的 replay 后才被接受，否则保留原机器。

## 关键实验
在 SpreadsheetBench、LiveMath、DABench、LongSeal 四个基准、四个执行模型上评估。

- 相比 Skill + ReAct，HEXIS 在 16 个设置中 15 个提升，11 个最佳或并列；平均成功率提升 16.1 个百分点。
- LiveMath 上四个执行器提升 31.4–38 个百分点，明显超过 AWM、ReasoningBank、SkillOpt 和 AFlow。
- Qwen3.8-27B 使用 HEXIS 后，执行 token 降低 38.4–88.9%。
- SpreadsheetBench 上先做 SkillOpt 文本优化再编译，成功率达到 84.2%，同时 token 从 257k 降到 69k。

## 最值得记住的一句话
把技能文档中的**知识**留在状态提示里、把**控制关系**编译成显式 guard 和变量绑定，通过轨迹 replay 保证增量更新不回退，是提升 agent 长流程合规性的有效路径。
