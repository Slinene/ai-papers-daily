---
title: Completeness and Cost of Retrieval Structures for Multi-Tool Requests in LLM
  Agents
title_zh: LLM Agent 多工具请求的检索结构完备性与成本
authors:
- Shuyang Zhang
affiliations:
- 香港理工大学
arxiv_id: '2610.41905'
url: https://arxiv.org/abs/2610.41905
pdf_url: https://arxiv.org/pdf/2610.41905
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agent 工具检索结构对比与完备性评估
tags:
- tool retrieval
- multi-tool completeness
- LLM agents
- retrieval structures
- cost analysis
one_liner: 比较六类工具检索结构，发现多工具完整检索需标注数据或30+次LLM调用，零训练/单次调用结构近乎失效
practical_value: '- 评估 Agent 多步骤任务时，把 completeness@k 作为主指标，不要只看 recall@k；按所需工具/技能数量分层，否则单目标请求会掩盖多目标真实水平。

  - 若工具池固定且有少量标注数据（75-90 条），优先训练 set-level retriever（如 COLT），查询期零 LLM 成本、完备率更高；若工具池频繁更新，用
  LLM 层级导航兜底，但需预留 30+ 次调用和分钟级延迟预算。

  - 失败归因决定修复方向：缺失项大量落在 top 17-50 时，可增大 K 或接 set-aware reranker；层级导航漏 prerequisite，则在导航后沿
  producer-consumer 依赖补全已找到工具的上游/下游。

  - 工具/技能描述尽量结构化声明 input/output schema，否则依赖图无法建边；没有 schema 时 LLM 补边不一定提升召回，可能反而引入噪声。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
Agent 需要调用多个工具才能完成请求时，只要 retriever 漏掉一个必需工具就会失败；但现有 tool retrieval 基准大多被单工具查询主导，聚合分数掩盖多工具场景的真实表现。

**方法关键点**  
- 比较 6 类结构：flat（BM25/bge/e5）、LLM query decomposition、LLM-navigated hierarchy（AnyTool）、server-then-tool（MCP-Zero）、dependency graph（Graph-of-Skills）、trained set-level（COLT/HYSET）。
- 指标：completeness@k（top-k 内必需工具集完整覆盖的比例）、recall@k、检索期 LLM calls/tokens/latency；失败归因区分 target / unrecognized prerequisite / rank depth。
- 数据：AppWorld 345 queries（有专家依赖标签，必需 API 2-12 个）；MCP-Bench 103 tasks/257 tools；先用 ToolRet 7,961 queries 做分层动机分析。

**关键实验与数字**  
- ToolRet 上 completeness@10 在单目标查询为 .58-.67，在 4+ 目标查询掉到 .08-.17；bge 在单目标最优，但在多目标被 COLT stage1 和 decomposition 反超。
- AppWorld k=16：无训练且最多 1 次 LLM 调用的 flat/分解/MCP-Zero/依赖图，完备率最高仅 .096。COLT 在 90 条训练查询下达到 .328，AnyTool 达到 .301（统计无显著差），但 AnyTool 需中位 31 次 LLM 调用、约 10 万 tokens、约 300 秒。
- MCP-Bench k=16：COLT .583 领先所有对比；AnyTool .398。COLT 的缺失工具 58% 排在 17-50 名，可加大预算或接 reranker；AnyTool 主要漏掉已找到 API 的 prerequisite。
- 下游检查：COLT top16 完整时官方 AppWorld agent 成功 21/21；不完整时仅 2/39，而 gold tool set 在同批不完整任务可成功 26/39。

**最值得记住的一句话**  
多工具请求的完整检索不能靠零训练/一次 LLM 调用的结构获得；要么用 75-90 条 in-domain 标注数据换 COLT，要么用每次查询 30+ 次 LLM 调用换 AnyTool。
