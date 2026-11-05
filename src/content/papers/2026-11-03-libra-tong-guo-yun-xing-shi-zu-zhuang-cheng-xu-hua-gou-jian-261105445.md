---
title: 'LIBRA: Programmatic Induction of Executable Tool Libraries'
title_zh: LIBRA：通过运行时组装程序化构建可执行工具库
authors:
- Zekai Li
- Zhenke Liu
- Yonghao Li
- Junhan Liu
- Xulong Xiao
- Jiapeng Zhang
affiliations:
- Brown University
- University of Southern California
arxiv_id: '2611.05445'
url: https://arxiv.org/abs/2611.05445
pdf_url: https://arxiv.org/pdf/2611.05445
published: '2026-11-03'
collected: '2026-11-05'
category: Agent
direction: Agent 工具检索 · 可执行库构建
tags:
- Tool Retrieval
- LLM Agents
- Multi-Tool Workflow
- Sandbox Validation
- Dense Retriever
- Tool Composition
one_liner: 将扁平工具目录变为经沙盒验证的可执行工具库，提升多工具任务 Recall 7.9 个百分点
practical_value: '- 对内部工具/API 平台，可以离线用 LLM 生成每个工具的候选调用、输出/状态变化和成功条件，再在沙盒中真实执行筛选，自动构建工具依赖库；不要完全依赖人工标注依赖关系，真实执行是低成本过滤幻觉的关键。

  - 多步工具任务（如商品创建需先认证、查类目、转图片格式）检索时，先召回目标工具，再从库中扩展它的前置工具或改写查询加入前置信息，可显著提升 Recall/NDCG，避免
  agent 在后续迭代里补漏。

  - 该库既能提升一次性 dense retrieval，也能作为 ReAct/agentic retrieval 的底座：把工具图/关系先验注入每一轮候选集，减少多轮检索误差累积，适合电商
  Agent 工具编排场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM agent 从大型工具目录检索时，大多数检索器按请求相似度独立排序每个工具。多工具任务中，用户往往只描述目标结果，缺少前置步骤（认证、ID 查询、状态初始化、格式转换），导致只召回目标匹配工具，遗漏工作流所需前置工具。

方法关键点：LIBRA 将扁平工具目录转化为可执行工具库。LLM 为每个工具生成契约，包括候选调用、可重用输出和状态变化、成功条件；LIBRA 在沙盒中测试这些组合，只保留运行时支持的关系。该过程在用户查询前离线完成，无需依赖标注、工具使用轨迹或任务特定训练，支持一次性检索和 agentic 检索。

结果：在 AppWorld、BFCL、SciToolEval 上，相比相同 dense retriever，one-shot Recall 和 NDCG 平均分别提高 7.9 和 3.7 个百分点；在 ToolReAGt 中，十轮检索迭代后分别提升 4.5 和 2.9 个百分点。
