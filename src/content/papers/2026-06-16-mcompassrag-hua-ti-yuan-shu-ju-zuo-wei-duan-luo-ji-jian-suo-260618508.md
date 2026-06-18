---
title: 'MCompassRAG: Topic Metadata as a Semantic Compass for Paragraph-Level Retrieval'
title_zh: MCompassRAG：话题元数据作为段落级检索的语义指南针
authors:
- Amirhossein Abaskohi
- Raymond Li
- Gaetano Cimino
- Peter West
- Giuseppe Carenini
- Issam H. Laradji
affiliations:
- University of British Columbia
- University of Salerno
- ServiceNow Research
arxiv_id: '2606.18508'
url: https://arxiv.org/abs/2606.18508
pdf_url: https://arxiv.org/pdf/2606.18508
published: '2026-06-16'
collected: '2026-06-18'
category: RAG
direction: RAG 检索优化 · 话题元数据引导
tags:
- RAG
- Retrieval
- Topic Metadata
- Distillation
- Efficiency
- Paragraph-level
one_liner: 用话题元数据增强段落嵌入并通过LLM蒸馏训练轻量检索器，实现高效、精确的话题感知检索
practical_value: '- **电商搜索/推荐场景的文档切分优化**：商品描述、评论往往混合多主题，直接使用粗粒度段落会引入语义噪声。可借鉴用商品类目、属性等元数据增强段落embedding，让检索结果更精准。

  - **低延迟检索器蒸馏**：用LLM作为教师蒸馏一个轻量双编码器，推理时无需调用LLM，显著降低线上检索延迟和成本，适合高并发实时推荐系统。

  - **话题感知的Agent检索**：在多跳推理或Agent工作流中，当需要从大规模非结构化文档中提取证据时，可引入话题元数据引导检索，减少无关片段干扰，提升事实准确性。

  - **工程实现简单**：只需在现有dense retriever基础上注入话题embedding，无需改动索引结构，易于迁移到商品库、帮助中心文档等场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：RAG系统的检索质量高度依赖文档切分粒度。细粒度chunk精确但搜索空间膨胀、延迟高；粗粒度chunk效率高但语义混合严重，稠密相似度不可靠。这一权衡在深度研究任务中尤为突出，需要同时保证速度和精度。

**方法**：提出MCompassRAG，将话题元数据作为语义指南针。首先用现成工具提取段落级话题标签，然后将话题标签与原文拼接，通过一个双编码器模型（基于Qwen2-1.5B）联合编码，使chunk嵌入包含明确话题信号。为了在推理时不依赖LLM，采用知识蒸馏：用LLM（Llama-3.1-70B）打分作为软标签，训练一个轻量级重排序器，实现话题感知的检索。整个流程无需额外LLM调用，仅增加少量计算。

**关键结果**：在6个复杂检索基准（包括多跳问答、法律/科学文档检索）上，信息效率（IE，综合准确率与耗时）平均提升8.24%，且端到端延迟比最强的高效RAG基线低5倍以上。消融实验证实，话题元数据和蒸馏训练对增益贡献最大。
