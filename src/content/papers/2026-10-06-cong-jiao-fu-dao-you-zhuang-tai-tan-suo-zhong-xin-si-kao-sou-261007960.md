---
title: 'From Delivery to Stateful Exploration: Rethinking the Index for Agentic Search'
title_zh: 从交付到有状态探索：重新思考 Agentic 搜索的索引
authors:
- Deogyong Kim
- Sunghwan Kim
- Sangam Lee
- Wonjae Lee
- Dongha Lee
affiliations:
- Yonsei University
arxiv_id: '2610.07960'
url: https://arxiv.org/abs/2610.07960
pdf_url: https://arxiv.org/pdf/2610.07960
published: '2026-10-06'
collected: '2026-10-07'
category: Agent
direction: Agentic Search 索引原生交互接口
tags:
- Agentic Search
- Inverted Index
- Evidence Discovery
- Context Management
- LLM Agent
one_liner: 提出 INDEXACT 索引原生接口，将候选集细化与源文本检查分离，用可复用状态与统计反馈提升多跳搜索证据发现并降低上下文占用
practical_value: '- 在电商/广告 Agent 搜索中，可借鉴“候选集引用 + 统计反馈”解耦：工具返回 SetRef 和候选集大小/条件命中数，而不是直接返回商品或文档列表，减少模型上下文浪费，尤其适用于多轮筛选和长程导购场景。

  - 状态化集合操作（FILTER/INTERSECT/UNION/DIFFERENCE）可复用中间候选集，避免重复检索；电商商品库筛选（类目、品牌、价格区间）天然适合基于倒排索引的布尔/位置条件，工程上可直接基于
  Lucene 构建，成本较低且可扩展。

  - 精确统计（COUNT_DOCS）优于二进制空/非空：实验显示二进制反馈准确率从 74.0 降至 62.0，精确计数让 Agent 判断条件是否过窄/过宽，辅助其决定继续过滤还是读取证据，可应用于导购
  Agent 的条件探索。

  - 细粒度读取（AROUND/DOCUMENT/RANGE）按需返回局部上下文，避免自动注入无关文本；Agent 可用 AROUND 定位关键词周边内容验证证据，减少非证据
  token 占比，提升长上下文稳定性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：搜索 Agent 通过查询-读取-决策迭代探索外部语料，但常见接口每次返回匹配段落，即使只需候选集大小做下一步决策，导致大量非证据文本占用上下文。初步分析显示，在 BrowseComp-Plus 上，非证据文档文本占最终上下文的 52%-74%，且相当部分出现在首次发现证据之前。这促使设计新接口，分离候选集细化与文本检查。

**方法关键点**：
- INDEXACT 将候选文档组织为可复用的 SetRef 状态，初始 CORPUS；FILTER 支持布尔（AND/OR/NOT）与位置（PHRASE/NEAR）条件；INTERSECT/UNION/DIFFERENCE 组合状态；RANK/TOPK 只改变检查顺序；所有操作返回状态引用和候选数，不返回匹配文本。
- 统计反馈：COUNT/COUNT_DOCS 提供候选集大小和条件命中数，Agent 可评估条件是否过窄或命中范围，无需读取文本。
- 细粒度读取：READ 支持 AROUND（锚定关键词周围）、DOCUMENT、RANGE，按需获取证据文本；状态可保留，Agent 可回到早期候选集探索不同分支。
- 实现：后端 Apache Lucene 倒排索引，Java 服务，Pi harness，结构化工具调用。

**关键实验**：
- 在 BrowseComp-Plus 上，INDEXACT 准确率 73.5%、证据覆盖 60.7%、平均实时上下文 13,960 tokens，均优于 RARG（69.4/57.2/27,896）等 baseline；相比 PI-SERINI 上下文更少但覆盖更高。
- 多跳 QA：HotpotQA 71.8、MuSiQue 46.2、2Wiki 69.2、Bamboogle 71.2 均最高，说明可泛化到 Wikipedia 语料。
- 消融：Auto Preview 70.0、Binary Feedback 62.0、去除状态复用 66.0、去除集合操作 62.0、去除位置操作 70.0，证明候选集状态和精确统计反馈关键。
- 语料从 100K 扩展到 800K 文档，INDEXACT 准确率保持 70-74%，上下文和成本稳定，优于 DCI。

**最值得记住的一句话**：Agent 搜索应“返回引用和统计，而不是源文本”，让模型在需要时按需读取证据，能同时降低上下文占用和提升证据发现质量。
