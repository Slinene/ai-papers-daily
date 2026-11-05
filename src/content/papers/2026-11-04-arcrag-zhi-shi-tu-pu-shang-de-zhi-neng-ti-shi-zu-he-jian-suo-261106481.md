---
title: 'ArcRAG: Agentic Compositional Retrieval over Knowledge Graphs'
title_zh: ArcRAG：知识图谱上的智能体式组合检索
authors:
- Jyotin Goel
- Abhinav Arun
- Tejas Prakash Agarwal
- Bhaskarjit Sarmah
- Stefano Pasquali
affiliations:
- Domyn
arxiv_id: '2611.06481'
url: https://arxiv.org/abs/2611.06481
pdf_url: https://arxiv.org/pdf/2611.06481
published: '2026-11-04'
collected: '2026-11-05'
category: RAG
direction: Agentic GraphRAG · 跨建图检索可移植
tags:
- GraphRAG
- Agentic Retrieval
- Knowledge Graph
- Cypher
- Cross-Construction Portability
- Multi-hop QA
one_liner: 提出 ArcRAG，在推理时归纳查询局部图接口并规划执行 Cypher，实现跨建图方式的组合检索可移植性
practical_value: '- 检索时动态归纳 query-local 图接口：电商/广告知识图谱常由异构源构建（商品表、详情、评论、搜索日志），不必维护全局本体或离线实体关系
  canonicalization。可借鉴 Explorer 在问题实体锚点附近发现关系描述符、别名和属性键，再用这些局部信息生成查询。

  - 可执行图查询 + witness 路径作为证据：当推荐/搜索需要解释“为什么推这个商品/广告”“是否满足优惠条件”时，让 agent 生成并执行 Cypher/traversal，返回路径与来源
  chunk/row，answer 只基于 witness，便于合规与溯源。

  - 预算分配经验：Explorer 贡献最大且跨图稳健；Planner 在 typed schema 图上低 retry 时更有效，在 open-vocabulary
  噪声图上小预算时几乎无收益。业务可据此调整 agent 阶段：非受控文本关系优先多轮探索，少做复杂规划。

  - 工程上按 schema-agnostic 设计检索端：schema 全部通过 introspection 读取，prompts/hyperparams 对多种图构造不变，能显著降低多源建图切换时的适配成本。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：多跳问题需要组合多个证据，而单段落 top-k 检索对关系不可见；GraphRAG 用路径提供可追溯性，但现有检索策略通常与其建图 pipeline 强耦合，换一种图构建方式就失效。ArcRAG 研究跨构建可移植性：同一检索流程，不做图特定 schema、关系名或重调，能否在 typed schema-guided 图与 open-vocabulary OpenIE 图上都有效。

方法关键点：
- 探索/利用分离：Explorer 在推理时对问题实体锚点做只读 Cypher 探索，产出 query-local 图接口（关系描述符、属性键、可达路径及别名变体），避免离线 canonicalization。
- Planner 基于该接口规划多跳子计划，每轮强制一个 open neighborhood scan 兜底；Generator 将子计划编译为 Cypher 并执行，不可接受结果则在固定 traversal shape 下 refine predicates/bindings，retries 预算内修复。
- 外层 retrieve-answer loop 支持多 pass：答案证据不足时生成 follow-up question 重新探索，witness 跨 pass 累积。
- 仅通过 introspection 读取图 schema，prompts/hyperparams 对两种图构造一致，仅 provenance 决定证据来自 chunk 还是 edge rows。

关键实验：对 MuSiQue、HotpotQA、TriviaQA 分别用 FinReflectKG typed 图和 HippoRAG OpenIE 图构建两组图。与 Direct-Cypher 及组件消融对比；typed 图上 ArcRAG EM/F1 为 MuSiQue 44.0/53.0、HotpotQA 74.5/80.8、TriviaQA F1 87.9；OpenIE 上为 38.0/45.0、65.5/72.2、71.6。Explorer 在所有 retry/pass 预算下提升 15-39 点(typed)和 12-32 点(OpenIE)；Planner 收益取决于图类型。跨构造保持竞争力，但绝对精度仍受构造影响。

最值得记住的一句话：检索不必与建图共同设计；query-time interface 归纳能让 construction-agnostic 检索跨图有效，但 construction 仍决定精度上限。
