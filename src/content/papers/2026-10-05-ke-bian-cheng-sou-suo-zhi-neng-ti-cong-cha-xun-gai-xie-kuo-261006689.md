---
title: 'Programmatic Search Agents: Extending Agentic Search Beyond Query Reformulation'
title_zh: 可编程搜索智能体：从查询改写扩展到候选处理与证据呈现
authors:
- Jiaming Qian
- Huiyan Yang
- Mandi Liu
- Jie Liu
- Wenkai Shen
- Pengyang Zhou
- Jing Jin
- Jin Ma
- Dezhi Ye
- Chaochao Chen
affiliations:
- Zhejiang University
- Yuanbao Team, Tencent
- Peking University
arxiv_id: '2610.06689'
url: https://arxiv.org/abs/2610.06689
pdf_url: https://arxiv.org/pdf/2610.06689
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 搜索接口 · 程序化候选处理与证据呈现
tags:
- Agentic Search
- Programmatic Search
- Evidence Presentation
- Candidate Workspace
- LLM Agent
- Search Interface
one_liner: 提出 Programmatic Search Agent，以可执行程序单元组织搜索动作，统一候选工作区、原语组合与选择性证据呈现，提升成功率并显著降低
  token 消耗
practical_value: '- **把“保留候选”和“呈现证据”解耦**：在电商搜索/推荐 Agent 中，让检索/召回结果作为可寻址对象持久化在工作区，LLM
  只接收程序选择的精简 notes，不把完整候选全部塞进 prompt。可直接复用上一轮 product pool 做 filter/rerank/extract，减少重复召回和上下文膨胀。

  - **用可组合原语代替单一 search(query) 工具**：定义 retrieve/filter/rerank/extract/dedupe 及变量引用，让
  Agent 生成一个 cell 表达“过滤上一轮池子 → 条件补召 → 合并去重 → 重排 → 抽取证据”的依赖链；避免多轮 tool call，适合多跳商品属性/活动规则验证等场景。

  - **审计 evidence-delivery gap**：线上 RAG/搜索链路常出现“文档已经进候选但未透出给模型”。可离线回放轨迹，统计支持性证据是否进入
  extraction 候选却未返回；对完全遗漏做同页补全的消融，能量化呈现瓶颈并指导界面改造。

  - **交互预算下优先做程序化动作**：如果决策轮次或成本受限，PSA 在 30-50 decision 预算下比 query agent 成功率高 11-13pp
  且 final-step tokens 省 38-41%。在商品搜索助手里，可把多个确定性操作（去重、重排、按条件筛选）合并进一个可执行 cell，只在需要语义判断时回到
  LLM。'
score: 9
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
现有搜索智能体通常只改写 query，固定 search(query) 管道掌控候选保留、排序与证据返回，模型无法控制已检索内容如何被加工和呈现。轨迹分析显示，BrowseComp-Plus 上 42.7% 的支持性段落进入过 extraction 候选集却从未返回给 agent；同页 oracle 实验里，补全完全遗漏证据使任务成功率 +16.7pp，后续搜索决策减少 64.0%。瓶颈不仅是找不到，更可能是“找到了但没呈现”。

**方法关键点**
- 将搜索动作单元从 query 或 tool call 改为对候选集的局部可执行 program cell。
- persistent candidate workspace：候选集合作为可寻址对象持久化，可跨 cell 复用和重处理。
- flexible primitive composition：用 retrieve/filter/rerank/extract/dedupe 原语 + 变量、列表操作、有界条件/循环组合成数据流；runtime 在一个 cell 内解析数据依赖。
- selective evidence presentation：cell 最后选择返回哪些结果作为下一轮观察，保留内容与展示内容分离。
- 与 Tool-based Agent 共享原语和 workspace，但 Tool-based 的依赖阶段需要多轮，PSA 可在一个 cell 内表达依赖链。

**关键结果**
在 InfoSeek-Eval 与 BrowseComp-Plus 上，以 5 个 policy backbone 无任务特定训练评测。相对 Query-based Agent，PSA 的 macro-averaged 任务成功率分别 +4.00pp 和 +7.56pp；final-step tokens 平均减少 28.3% 和 33.9%；BrowseComp-Plus 支持文档 Recall +4.46pp。选择性反馈相比 full-view 返回文本减少 37.2%，成功率 +3.91pp，tokens -24.5%。在 30-50 decision 预算下，PSA 比 Query-based Agent 成功率高 11.72-13.28pp，final-step tokens 少 38.3-40.9%。

**最值得记住的一句话**
搜索智能体的控制权应从 query 改写扩展到候选处理和证据呈现；把“保留状态”与“展示证据”解耦，可同时提升成功率并显著降低 token 成本。
