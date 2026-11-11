---
title: Controlled Knowledge Engineering for Taxonomy Induction with Tool-Grounded
  LLM Agents and Runtime-Adaptive Policies
title_zh: 工具接地LLM智能体与运行时自适应策略的分类体系归纳
authors:
- Jonas Limniatis
- Bennet Schaarmann
- Georg Reuber
- Robert Stahlbock
affiliations:
- Lufthansa Technik
- Lufthansa Industry Solutions
- University of Hamburg Business School
- Nordakademie University of Applied Sciences
- FOM University of Applied Sciences
arxiv_id: '2611.13966'
url: https://arxiv.org/abs/2611.13966
pdf_url: https://arxiv.org/pdf/2611.13966
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: LLM Agent 工具接地与动态策略构建分类体系
tags:
- Taxonomy Induction
- Tool-Grounded LLM Agents
- Runtime-Adaptive Policies
- Knowledge Engineering
- LLM Agents
one_liner: TIGA 用可执行分类编辑工具、交互记忆和运行时自适应策略，将分类体系归纳转为受控迭代决策，提升召回与 F1
practical_value: '- 在电商类目体系构建或清洗时，可将 taxonomy 维护封装为可执行工具（添加/移动/删除节点、环路与孤立节点校验），把 LLM
  自由生成转为对受限动作空间的决策，减少幻觉实体和非法层级。

  - 维护 interaction memory 记录每次工具调用、理由与结果，作为后续步骤上下文；这比单纯把整棵 taxonomy 塞进 prompt 更稳定，有助于提升多步构建的完整性与
  F1。

  - 引入运行时自适应策略适合业务分类标准不固定、需要边做边调整的类目梳理场景；但 token/API 成本显著上升，建议仅用于离线生成或人工审核的半自动流程。

  - Global reviewer 的效果依赖数据集和 revision budget，不要盲目加全局评审；在预算充足、质量优先的离线任务中再启用。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：Taxonomy 在语义搜索、推荐、商品目录组织和 RAG 中起关键作用，但从固定候选实体自动构建不仅需要文本通顺，还要求层级完整、结构有效、语义一致。LLM 自由生成易漏实体、产生幻觉层级或组织原则不一致。

**方法**：TIGA 将 taxonomy induction 形式化为显式状态与受限动作空间上的迭代决策。核心组件包括：
- 可执行的 taxonomy 编辑工具，限定合法操作（添加/移动/删除节点、结构校验等）；
- interaction memory，记录工具调用、理由和结果；
- runtime-adaptive organizational policy，agent 在推理中根据中间结果动态修订构建原则；
- 可选 global reviewer，对照候选集和当前策略评估已建 taxonomy。

**结果**：在四个基准 taxonomy 和两种 LLM backbone 上，TIGA 在多数配置下取得最强结构质量，尤其 recall 和 F1 表现突出，但并未在每项 precision 指标上占优，部分场景 run-to-run 差异更大。收益伴随显著更高的 token 消耗、API 调用量和推理时间。消融显示策略和交互记忆组件持续带来提升，而全局评审的效果依赖数据集和可用 revision budget。
