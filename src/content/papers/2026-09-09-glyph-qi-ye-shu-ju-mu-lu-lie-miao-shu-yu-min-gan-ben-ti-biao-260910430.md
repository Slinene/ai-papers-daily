---
title: 'Glyph: A Multi-Strategy Agentic System for Column Description and Sensitivity-Ontology
  Tagging of Enterprise Data Catalogs'
title_zh: Glyph：企业数据目录列描述与敏感本体标注的多策略智能体系统
authors:
- Kostia Kudriavtsev
- Parvez Rafi
- Sha Sundaram
affiliations:
- Apple
arxiv_id: '2609.10430'
url: https://arxiv.org/abs/2609.10430
pdf_url: https://arxiv.org/pdf/2609.10430
published: '2026-09-09'
collected: '2026-09-10'
category: MultiAgent
direction: 多智能体数据目录标注与敏感分类
tags:
- Agent
- RAG
- Fine-tuning
- Data Catalog
- Sensitivity Classification
- Contrastive Learning
one_liner: 用协作式 LLM Agent 将列描述生成与 275 类敏感标签分类落地为可审计的生产系统
practical_value: '- **代码而非数据值作为生成依据**：Descriptor 通过 active RAG 从 GitHub 检索产生列的上游 pipeline
  源码，再生成描述。做电商/推荐特征库、指标口径或广告字段文档时，可以让 Agent 以业务代码/ETL 逻辑为 grounding，避免只看数据值产生幻觉。

  - **多策略并行 + RRF 融合**：Tagger 同时跑描述打标、业务正则、基于向量库的 metadata tagger，再用 Reciprocal Rank
  Fusion 合并排序。对大 taxonomy（如 275 类）的商品/内容/广告分类或多标签治理，可复用「语义、规则、精确元数据三路并行 + RRF」的架构，稳定且可解释。

  - **小模型对比微调收益显著**：用 in-batch contrastive objective 微调 6 层 MiniLM，NDCG@10 从 0.55
  提升到 0.92。在标签体系较大、域内文本较短的特征/类目标注任务中，轻量 encoder 微调 + 向量检索是低成本高回报方案。

  - **每个标签保留 provenance 与降级路径**：系统记录每个 tag 来自哪条策略，并在代码不可取、服务失败时优雅降级。生产 Agent/LLM 系统做治理或推荐元数据标注时，应设计来源审计和
  fallback，满足合规与可运维要求。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：企业数据湖表增长远快于人工治理，列描述缺失、敏感标签未分配会破坏数据发现、权限控制与合规。

**方法关键点**：Glyph 将列描述生成与列类型标注建模为两个协作 LLM Agent，以 stateful graph 编排。Descriptor 通过 reasoning-acting tool loop 按需从企业 GitHub 检索产生列的上游 pipeline 源码，实现 active RAG，使描述基于代码而非数据值。Tagger 面向 275 叶节点的 Data Classification Ontology，并行执行三个策略：description tagger、基于业务 line-of-business 的 regex tagger、以及由微调 contrastive encoder 支撑的 metadata tagger；三路排序结果用 Reciprocal Rank Fusion 融合。微调对象是 6 层 MiniLM，采用 in-batch contrastive objective。

**关键结果**：同标签检索在 held-out 集上 NDCG@10 从 0.55 提升到 0.92，MAP@100 从 0.19 提升到 0.90。端到端多标签分类以 recall-weighted F2 评估，消融实验隔离了各策略与 RRF 融合的贡献。工程上强调 value-free 与 code-grounded 设计、逐标签 provenance 以及 graceful degradation，使多 Agent 数据目录标注可审计、可上线运营。
