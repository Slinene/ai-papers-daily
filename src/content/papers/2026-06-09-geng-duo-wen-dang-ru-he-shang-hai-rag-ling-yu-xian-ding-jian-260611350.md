---
title: 'When More Documents Hurt RAG: Mitigating Vector Search Dilution with Domain-Scoped,
  Model-Agnostic Retrieval'
title_zh: 更多文档如何伤害 RAG：领域限定检索缓解向量搜索稀释
authors:
- Nabaraj Subedi
- Ahmed Abdelaty
- Shivanand Venkanna Sheshappanavar
affiliations:
- University of Wyoming
arxiv_id: '2606.11350'
url: https://arxiv.org/abs/2606.11350
pdf_url: https://arxiv.org/pdf/2606.11350
published: '2026-06-09'
collected: '2026-06-12'
category: RAG
direction: RAG 检索增强生成 · 向量搜索稀释与领域限定检索
tags:
- RAG
- vector search dilution
- domain scoping
- multi-agent
- retrieval
- faithfulness
one_liner: 发现大规模异质文档库中的向量搜索稀释问题，提出基于元数据的领域限定检索显著提升精度，指出多智体编排存在精度-忠实性悖论。
practical_value: '- **利用业务元数据做检索范围限定**：当知识库规模大、类别多（如商品文档、售后手册、政策库混合），可借鉴文档类型、类目等现有元数据在查询时过滤索引，能避开密集检索的区分力下降，提升召回精度。工程上轻量级，直接复用已有的字段，不用重新标注。

  - **路由模块实用设计**：先正则快速匹配，失败再调用 LLM 零样本分类；进一步可训练一个轻量分类器（如 BGE-M3 + 线性层）替代 LLM 路由，在准确性（+28pt）和成本上更优。对于电商搜索或
  Agent 工具选择，这种容错路由策略可直接复用。

  - **多智体编排小心“忠实度陷阱”**：在商业 API 模型上多工具调用可能导致生成忠实度急剧下降（如 Claude 0.25→0.01），优先使用单次检索+单次生成的架构，仅当领域间强隔离且使用开源模型（如
  Qwen、DeepSeek）时才考虑多轮调度，否则得不偿失。

  - **评测体系需同时关注检索与生成**：单看检索精度（P@10）提升可能掩盖生成忠实度退化，需同时监控 RAGAS faithfulness。对于电商问答、产品推荐文案生成等场景，这一点可避免上线后隐式错误。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：标准 RAG 在扩展到大规模、异质文档集合时，密集检索的判别力会下降，即使使用混合检索也不例外。作者在部署的 Wyoming 交通部知识库中发现，从 54 份文档扩展到 1,128 份（88,907 个 chunk）后，准确率从 75% 跌至 40% 以下。他们称此为“向量搜索稀释”（vector search dilution），即语义相关但上下文无关的 chunk 淹没了 top-k 结果。

**方法关键点**：
- **领域限定检索（Domain Scoping）**：利用文档图中已有的组织元数据（如 document_series、article_category）在查询时限制检索范围，使搜索空间减少 85–98%，显著提升 p@10。
- **路由策略**：混合路由（HYBRID-ROUTED）先用正则表达式快速匹配，失败时回退到 LLM 零样本分类；进一步可训练 BGE-M3 线性探测器路由（R2-ROUTED），提升路由准确率 28.4 个百分点。
- **多智体编排及悖论**：MASDR-RAG 由一个推理 agent 携带 K 个领域限定检索工具，允许多轮工具调用。但发现存在“精度–忠实性悖论”：检索精度提高却导致生成忠实度下降（如 Gemini 上从 0.61 → 0.35），根源是跨来源合成的碎片化上下文干扰。

**关键实验与结果**：
- 在 WYDOT 200 条专家验证查询上，领域限定检索（Scoped）将 P@10 从 0.77 提升到 0.86（p<0.05），但 MASDR-RAG 的 RAGAS 忠实度从 0.61 降至 0.35（p<0.01）。HYBRID-ROUTED 保持忠实度 0.62。
- 开源复现（Qwen-7B, Llama-8B）保留架构排序，忠实度悖论只在商业生成器中发生（Claude, GPT），开源模型无此退化，表明悖论是配置依赖的。
- 在 6 个跨域语料库（含 HotpotQA、MultiHop-RAG）上，领域限定在可识别子域的语料库上生效；多智体编排仅在真正多跳查询时有收益。
- 效率上，HYBRID-ROUTED 比 ReAct 少 5.9× token 消耗和 2.2× 延迟。

**值得记住的一句话**：对于大规模企业 RAG，核心决策是利用现有元数据做检索范围限定，单次合成更安全，多智体编排只在特定条件下才值得引入。
