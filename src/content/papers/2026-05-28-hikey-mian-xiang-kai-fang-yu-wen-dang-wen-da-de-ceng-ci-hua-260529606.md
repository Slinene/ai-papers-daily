---
title: 'HiKEY: Hierarchical Multimodal Retrieval for Open-Domain Document Question
  Answering'
title_zh: HiKEY：面向开放域文档问答的层次化多模态检索框架
authors:
- Joongmin Shin
- Gyuho Shim
- Jeongbae Park
- Jaehyung Seo
- Heuiseok Lim
affiliations:
- Korea University
- Konkuk University
arxiv_id: '2605.29606'
url: https://arxiv.org/abs/2605.29606
pdf_url: https://arxiv.org/pdf/2605.29606
published: '2026-05-28'
collected: '2026-05-31'
category: RAG
direction: 层次化多模态检索 · RAG
tags:
- hierarchical retrieval
- multimodal RAG
- document QA
- coarse-to-fine
- evidence subgraph
one_liner: 提出层次化树状多模态检索框架，将文档结构作为第一检索信号，通过从粗到细策略大幅提升检索召回和问答性能。
practical_value: '- 在处理电商的海量产品文档、说明书或政策文件时，可将文档的层次结构（章节、段落、表格、图表）显式建模为树状图，作为检索信号，缓解简单分块带来的证据碎片化问题。

  - 从粗到细的检索策略可应用于大规模商品库的搜索：先通过高层级索引（如类目或文档标题）快速定位候选集，再精细匹配多模态证据，大幅降低检索延迟和无效内容。

  - 多模态融合思路可借鉴到商品详情页理解：将文本描述、表格参数、示意图等映射到统一语义空间，做细粒度排序，提升复杂问题的回答准确率。

  - 混合结构-语义打包策略可用于优化 Agent 从多模态文档中提取上下文的 token 效率，在维护逻辑完整性的同时控制成本，尤其适合长文档对话场景。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：工业级开放域文档问答（ODQA）中，基于 RAG 的方法面临两大瓶颈——文档定位失败和多模态证据分散，传统扁平块或页面级图像难以精准捕获文档层级结构与表格、图表等多元信息，导致检索召回率低、生成质量受限。

**方法**：HiKEY 提出层次化树状多模态检索框架，核心创新包括：(1) 文档层次解析（DHP）将多页文档重构为逻辑异构图，显式编码标题-段落-多模态元素的父子关系；(2) 层次化粗到细策略，利用全局索引快速剪枝候选空间，再通过多模态融合排序精细定位最相关章节；(3) 混合结构-语义打包策略构建 token 高效的证据子图，维持证据链的完整性和紧凑性。

**结果**：在 ODQA 基准上，HiKEY 显著优于页面级和块级基线，检索召回率最高提升 12.9%，端到端问答性能最高提升 6.8%，验证了文档层次作为第一类检索信号的有效性。
