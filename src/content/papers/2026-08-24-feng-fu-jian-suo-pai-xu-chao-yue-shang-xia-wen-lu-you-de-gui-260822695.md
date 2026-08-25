---
title: 'Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing'
title_zh: 丰富-检索-排序：超越上下文路由的规模化能力发现
authors:
- Nazib Sorathiya
- Daniel Zhang
- Bardiya Akhbari
affiliations:
- Amazon AGI
arxiv_id: '2608.22695'
url: https://arxiv.org/abs/2608.22695
pdf_url: https://arxiv.org/pdf/2608.22695
published: '2026-08-24'
collected: '2026-08-25'
category: Agent
direction: Agent 能力发现 · 检索-重排
tags:
- Agent
- Tool Retrieval
- Retrieve-Rerank
- LLM Routing
- BM25
- Scaling
one_liner: 将 Agent 能力发现重构为离线丰富+在线检索-重排，在 7,278 个工具上以约一半成本领先 Search&Pick 6.5pp，并比全量上下文便宜
  70 倍
practical_value: '- 如果业务里要用 LLM 从上千个 API/agent/tool 中选调用，不要让它读全量 registry：改为 BM25+dense
  召回 top-15，再单次 LLM listwise rerank。这样成本与 registry 规模解耦；Nova Micro 扫描显示单阶段全量路由在 N≈500
  后崩，可作为架构切换的经验阈值。

  - 离线把稀疏的 item/tool 元数据改写成结构化 profile（summary、action-led description、keywords、正/负
  usage examples）一次完成，供检索和 reranker 共用。干净公开数据上 enrichment 无收益（甚至 -4.4pp），但元数据只剩 name
  时 Match@1 +25.6pp、Recall@15 0.134→0.467；先评估自家商品/工具 metadata 稀疏度再决定是否上。

  - 做错误归因：约70%的大规模 miss 在 retrieval，换更强 reranker 只 +3pp。优先提升一阶段召回（hybrid、更好 dense
  encoder、字段加权）而不是继续优化 reranker prompt。

  - 打分信号可设计成可插拔加权：LLM 0.50 + BM25 0.05 + Quality 0.30 + Intent 0.15，字段缺失自动 renormalize；在有
  trust/type 元数据时 Quality+Intent 额外 +4.5pp。这种统一配置可以跨 tools/agents/skills 复用，避免每种能力单独调参。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Agent 生态正快速膨胀到数千个 MATS 组件，但主流发现方式仍是 in-context routing：LLM 读 registry 名字/描述，选一个、调用、失败重试。它的准确率和成本都随 registry 规模恶化，每次误调都消耗 token/延迟甚至触发不可信 endpoint。因此把能力发现重铸为对注册表的检索问题。

**方法**
- 离线 Enrich：注册时用 LLM 把稀疏元数据改写成五字段 profile（summary、action-led description、keywords、正/负使用示例），生产版再加 trust score 和 self-reported type tags；只做一次，供检索和 reranker 共用。
- 在线 Retrieve-Rank：先 BM25/dense/hybrid 召回 top-k（15/25），再用一次 LLM 对候选做 listwise 重排；打分权重 LLM 0.50、BM25 0.05、Quality 0.30、Intent 0.15，缺字段时重新归一化。公共数据只用 LLM+BM25（10:1）。
- 同一 configuration 跨 Tools/Agents/Skills，不按类型调参。

**关键结果**
- Tools-ToolRet（7,961 查询、7,278 工具）：Ours+Titan Match@1 0.397，比 Search&Pick 0.332 高 6.5pp，token 约一半；成本每千查询 $0.066，比 Full-Ctx $4.48 便宜约 70 倍。
- 规模扫描：Full-Ctx Match@1 从 N=10 的 0.85 跌到 N=7,278 的 0.12；pipeline 从 0.81 到 0.39，交叉约 N=500。Reranker 条件准确率稳定在 0.70–0.87，约 70% 的失败来自 retrieval 阶段。
- Enrichment 在已写好的公开数据上中性到负收益；在 name-only 稀疏化压力测试中 Match@1 +25.6pp、Recall@15 0.134→0.467。
- 生产部署于内部 multi-agent platform，单 index 覆盖全部 MATS 类型；Quality+Intent 信号带来 +4.5pp。

**最值得记**：大规模能力/工具选择的瓶颈在召回而不是重排，先做好第一阶段检索，固定 top-k reranker，避免 LLM 读全量 registry。
