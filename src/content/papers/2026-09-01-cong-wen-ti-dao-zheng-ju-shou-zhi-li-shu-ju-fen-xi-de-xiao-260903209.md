---
title: MasterControl Seventeen Every Time
title_zh: 从问题到证据：受治理数据分析的小型分析代数
authors:
- MasterControl AI Lab
affiliations:
- MasterControl AI Lab
arxiv_id: '2609.03209'
url: https://arxiv.org/abs/2609.03209
pdf_url: https://arxiv.org/pdf/2609.03209
published: '2026-09-01'
collected: '2026-09-10'
category: LLM
direction: 受治理数据分析 · 确定性策略执行
tags:
- Governed Analytics
- Deterministic Policy Execution
- LLM Intent Parsing
- Tool Planning
- SQL Generation
- Replayability
one_liner: LLM只解释用户意图，由确定性策略执行预批准分析程序，110/110匹配答案与证据契约，而运行时规划0/330
practical_value: '- 在电商/广告的指标数据问答、AB实验分析等场景，可将「意图解析」与「工具选择/SQL生成」解耦：LLM只做意图分类和参数抽取，指标口径、SQL模板、执行程序由预注册目录确定性选择，避免每次生成口径漂移。

  - 返回结果同时返回 evidence（口径、时间区间、支持记录），方便审计、回放和线上事故排查；对推荐系统日报、监控告警类分析尤其有价值。

  - 用小型类型化操作集（关系操作+聚合+窗口+排名+相似度）表达业务分析需求，先为有限场景证明 scoped completeness，再逐步扩展，比直接开放端到端
  agent 更可控。

  - 对比结果提示：8B 级模型做运行时 SQL 生成和工具规划，在完整答案+证据契约上失败率很高；若在业务 Agent 中做数据查询，必须加强验证、模板约束或策略回退，不能只靠自由规划。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**
企业分析场景中，事实分析器不应每次回答都临时发明测量方法。难点不在生成数字，而在保持数字含义：人群、时间区间、指标定义、口径和支持记录。

**方法关键点**
- 定义一个小型类型化操作集：从有限关系和一阶满足构造关系操作，再显式加入聚合、比较、窗口、排名和版本化相似度，覆盖指定分析类并证明 scoped completeness。
- 架构上解耦：LLM 只负责把用户问题解释为受治理的意图；之后由确定性策略选择预写好的分析程序，程序返回结果和证据。
- 证明 replay：固定意图口径、策略、数据、内核状态、数值规则和输出契约时，同一问题可得相同结果与证据。

**关键结果**
- 440 次运行对比：三种 8B 开源模型在运行时自主决定查询方式、工具选择和 SQL 生成；Qwen3-8B 只解释意图，策略执行预批准程序。
- 330 次运行时规划中，没有任何一次最终程序在开发快照和四个 held-out 变体上匹配完整的答案与证据契约。
- 策略执行分析器在 110/110 次上匹配契约。
- 该结果是配置特定的实验结论，不代表运行时 agent 在其他设计下不能成功。
