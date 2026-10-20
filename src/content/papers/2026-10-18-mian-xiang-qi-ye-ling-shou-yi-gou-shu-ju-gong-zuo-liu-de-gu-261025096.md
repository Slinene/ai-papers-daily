---
title: Toward Agentic Retrieval-Augmented Generation for Enterprise Retail Workflows
  over Heterogeneous Data Sources
title_zh: 面向企业零售异构数据工作流的Agentic RAG评估基准与框架
authors:
- Jeonghwan Choi
- Jibin Hwang
- Hayoon Park
- Hyeonjae Cheon
- Hwanjun Song
affiliations:
- KAIST
- Cluvion
- GS Retail
arxiv_id: '2610.25096'
url: https://arxiv.org/abs/2610.25096
pdf_url: https://arxiv.org/pdf/2610.25096
published: '2026-10-18'
collected: '2026-10-20'
category: RAG
direction: Agentic RAG · 多源异构零售问答评测
tags:
- Agentic RAG
- Retail QA
- Heterogeneous Data
- Multi-hop Reasoning
- Benchmark
- Schema Briefing
one_liner: 提出RetailBridge多源零售QA基准与RetailRAG框架，定位跨源链式为瓶颈
practical_value: '- 在电商 Text-to-SQL / 数据分析 Agent 中，先构建并注入 auto-schema briefing：包括列类型与示例值、类别枚举、跨表
  join 键、派生指标公式，可提升 planner 路由和 SQL 生成准确率。

  - 采用 source-routed plan chaining：对复杂查询一次性生成显式依赖链，支持 SQL→文本→SQL 的中间结果传递；简单查询走快速通道，控制
  API 调用成本。

  - 失败恢复用 diagnostic plan revision：只定位并局部修正失败步骤，保留已完成步骤，避免整体 replan；把失败类型划分为 schema
  mismatch、filter 过严等，可显著降低 token 消耗并提高成功率。

  - 构建内部评测集可借鉴 RetailBridge 的合成管线：用 persona 仿真生成订单/评论/客服交互数据，再用 entity-linked/answer-linked
  算子递归组合出多跳查询，按推理深度、跨源数和证据模态分层，便于诊断 agent 短板。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：企业零售真实查询常跨商品表、订单、客服文本等多源异构数据，现有 agentic RAG 基准多为单一同质语料，无法体现跨源链式推理难度，且企业数据不可得。

方法关键点：
- RetailBridge：基于 persona 驱动仿真生成异构零售库（5张表+3个文本源），再从单源原子QA经 entity-linked 和 answer-linked 算子递归组合，产出 1,680 条多跳多源查询，按推理深度、来源多样性、证据模态分层。
- RetailRAG：auto-schema briefing 预计算 schema 摘要、类别值约束、实体链接键、派生指标并注入 planner；source-routed plan chaining 一次性规划每步源和查询，将中间结果显式传递；diagnostic plan revision 对失败步骤做类型化诊断和局部重写，不整体重规划。

关键结果：
- RetailRAG 在 RetailBridge 上平均 LLM-judge 0.429，超过 HetaRAG 0.293，API calls 7.45 vs 25.21；消融显示 schema briefing 和 plan revision 贡献最大，注入 briefing 到各 baseline 都提升。
- 10 个 LLM 骨干中最好 Qwen3.6-Plus 0.511、GPT-5.4 0.508；Level-3 比 Level-1 普遍腰斩；Text-only 模态最弱；source routing F1 较高但 answer 正确率低，定位整合环节。

最值得记住的一句话：跨源编排和 schema 先验是当前企业零售 agent 的主要瓶颈，单纯增大模型规模不能解决。
