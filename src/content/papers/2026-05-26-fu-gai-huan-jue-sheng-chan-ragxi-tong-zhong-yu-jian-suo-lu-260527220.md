---
title: 'The Coverage Illusion: From Pre-retrieval Routing Failure to Post-retrieval
  Cascades in a Production RAG System'
title_zh: 覆盖幻觉：生产RAG系统中预检索路由失败与检索后级联
authors:
- Zafar Hussain
- Kristoffer Nielbo
affiliations:
- Aarhus University, Denmark
arxiv_id: '2605.27220'
url: https://arxiv.org/abs/2605.27220
pdf_url: https://arxiv.org/pdf/2605.27220
published: '2026-05-26'
collected: '2026-05-27'
category: RAG
direction: RAG查询增强与检索后级联优化
tags:
- Coverage Illusion
- Retrieval Cascade
- Query Routing
- HyDE
- Production RAG
- LLM Augmentation
one_liner: 合成查询高估LLM增强需求 72.2%真实查询仅靠混合检索即可，检索后级联无需训练提质量降延迟
practical_value: '- 电商/推荐系统RAG评估务必使用真实查询，合成查询会严重高估复杂增强（如HyDE）的必要性，造成算力浪费与高延迟

  - 实体密集型索引（如商品目录）中，最佳策略是 cheapest-first 检索后级联：先用 BM25+向量混合检索，无结果时再递进调用 LLM 增强，大幅降低推理成本

  - 预检索路由（基于查询文本预测是否需要增强）在以上场景几乎无效，因为增强需求取决于索引内容而非查询本身，has_sources 布尔检查比任何 ML 路由都简洁有效

  - LLM-as-judge 评估应以覆盖率为主要质量信号，而非回答本身，可据此设计延迟优化：检索落空才触发增强，避免昂贵模型滥用'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
现代 RAG 系统普遍对所有查询应用 LLM 增强（HyDE、查询扩展），尽管显著提升检索覆盖，但带来高推理成本和延迟。在真实生产流量中，这种开销是否必要？丹麦国家百科全书的生产案例显示，合成查询与真实查询对增强需求的判断存在巨大鸿沟，预检索路由无法弥合，亟需一种低成本、无训练的适配方案。

### 方法关键点
- **工作流对比**：五种检索工作流，包含 Tier 1（仅检索：Semantic、Semantic-CE、Hybrid）与 Tier 2（LLM 增强：QE-CE、HyDE），在 1,000 条真实查询和三种合成查询条件下评估。
- **覆盖幻觉量化**：合成查询显示 90% 以上需要 LLM 增强，而真实查询仅 27.8% 需要升级，因为 Hybrid（BM25 + 向量 + RRF）已覆盖 72.2%。
- **预检索路由实验**：尝试规则、分类、神经网络微调、回归四种范式，发现索引内容决定增强需求，查询文本无预测信号，最佳模型增强回避率仅 13.4%。
- **检索后级联设计**：工作流按成本排序（Hybrid → QE-CE → HyDE），每一步检查是否返回文档（has_sources），是则终止，否则升级。无需训练或额外基础设施。

### 关键结果
- 级联在真实查询上 CO 达 4.084，较 Always-HyDE 提升 +0.140，端到端延迟降低 31.8%，LLM 增强调用仅 27.8%。
- 在 Hybrid 已成功的查询中，HyDE 反而降低质量（21.2% 案例），级联避免了这种语义漂移。
- 级联增强回避率 72.2%，远超 ML 路由器的 13.4% 上限，且质量占优，实现帕累托改进。
- 覆盖幻觉根源：合成查询长而丰富，真实查询多为简短关键词，分布不匹配导致对增强需求的高估。

**核心洞察：在实体密集型 RAG 中，检索后级联以 O(1) 的 has_sources 判断替代复杂路由，实现质量、成本、延迟三重优化。**
