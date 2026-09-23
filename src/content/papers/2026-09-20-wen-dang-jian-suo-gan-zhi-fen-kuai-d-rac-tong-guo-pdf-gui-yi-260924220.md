---
title: 'Document Retrieval-Aware Chunking (D-RAC): Universal Retrieval-Aware Ingestion
  of Enterprise Documents via PDF Normalization and Multimodal Markdown Conversion'
title_zh: 文档检索感知分块 D-RAC：通过 PDF 归一化与多模态 Markdown 转换实现通用企业文档摄入
authors:
- Uday Allu
- Abhivanth Sivaprakash
- Pratik Singh
- Aman Manocha
affiliations:
- AI Research Team, Yellow.ai
arxiv_id: '2609.24220'
url: https://arxiv.org/abs/2609.24220
pdf_url: https://arxiv.org/pdf/2609.24220
published: '2026-09-20'
collected: '2026-09-23'
category: RAG
direction: 企业文档 RAG 摄入与分块
tags:
- RAG
- Chunking
- Multimodal LLM
- PDF Normalization
- Markdown Conversion
- Enterprise Knowledge
one_liner: D-RAC 将任意文档先归一为 PDF，再用多模态 LLM 转检索优化 Markdown 后按 ID 规划分块，显著降本
practical_value: '- 对电商/广告团队构建产品文档、招商政策、客服知识库等 RAG 时，可先统一归一化为 PDF，再用单个多模态 LLM 转 Markdown，避免为
  DOCX/PPTX/XLSX/扫描件分别开发解析器。

  - 将表格改写为自包含 prose、保留标题层级，能显著提升商品规格表、价格政策等表格密集文档的 chunk 检索召回。

  - 分块规划只在 ID 层级做、不重写文本，既降低 token 成本又避免幻觉，适合离线大批量摄入文档并保持可复现、可审计。

  - 报告中 token 减少 95.7%、分块成本降低 77.8%~85.6%、时间降低 75%、线性扩展到 500+ 页，可直接作为内部 RAG 摄入预算与架构选择的参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：企业 RAG 需摄入 PDF、Word、PPT、扫描件等异构格式，规则抽取和 OCR 会破坏阅读顺序、表格结构与标题层级；完全 agentic chunking 在原始文本上做语义分块则成本高、有幻觉风险。

**方法关键点**：D-RAC 利用几乎所有文档格式都有确定性 PDF 渲染的特点，先把任意输入归一化为 PDF；单个多模态 LLM pass 将渲染页面转为检索优化 Markdown，表格被重写为自包含 prose、保留标题层级；随后沿用 W-RAC：确定性解析为 ID 可寻址单元，仅对标识做轻量 LLM chunk planning，不重新生成文本。

**关键结果**：在 236 文档、795 页的 RAG-Multi-Corpus 五领域 PDF 子集上，72 分钟零错误完成转换与分块，产出 1,748 个检索就绪 chunks。相比 frontier LLM 的 agentic chunking，分块阶段输出 token 减少 95.7%，分块成本降低 77.8%（GPT-4.1 定价）到 85.6%（Gemini 2.5 Pro 定价），时间降低 75%；并线性扩展到 500+ 页文档。
