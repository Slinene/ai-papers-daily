---
title: 'Tessera: Structure-Completed Evidence Units for Web Retrieval-Augmented Generation'
title_zh: Tessera：面向 Web RAG 的结构补全证据单元
authors:
- Peichun Hua
- He Sun
- Zirui Zhuang
- Qi Qi
- Yiming Qiu
- Shinan Liu
- Yunming Xiao
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- The University of Hong Kong
- Beijing University of Posts and Telecommunications
arxiv_id: '2610.37080'
url: https://arxiv.org/abs/2610.37080
pdf_url: https://arxiv.org/pdf/2610.37080
published: '2026-10-27'
collected: '2026-10-29'
category: RAG
direction: RAG 结构化证据交付优化
tags:
- RAG
- Evidence Units
- HTML Structure
- Agentic Search
- Budget-Neutral
one_liner: 训练无关的证据交付层，将检索页面重建为结构完整的证据单元，文本/截图/Agentic RAG 提升 5-6 点准确率
practical_value: '- 电商详情页/商品参数表在 RAG 中常因提取或固定 chunk 丢失表头、价格、规格等结构化证据。可借鉴 Tessera 在
  query-time 从原始 HTML 重建“标题路径+表头+行”的证据单元，用 cross-encoder 选相关行打包进一个 token 槽，保留 top
  检索结果中的 prose。

  - Agent 多跳搜索（如选品、竞品分析）可在每次 search 工具返回中加入该层：替换最后一个 doc 为结构补全的单元块，不仅提升准确率，还让 agent
  少搜索、上下文更短（FRAMES +5.2，搜索次数 2.41→2.19）。

  - 对多模态/截图索引同样有效：用 top tiles 定位页面，再从 HTML 构建单元替换最后一个 tile，比单纯增加 tile 数量更省 token 且更准；适合在截图索引上叠加，无需重建索引。

  - 工程实现：单元构建可离线缓存 per page，query 时只需解析少量 anchor pages 和 cross-encoder 打分，新增成本低（15ms
  CPU/页 + 0.2 GPU-s/query）；可作为现有 RAG pipeline 的即插即用层，不改变 index/retriever/reader。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
Web RAG 通常将页面切成固定 chunk 或截图 tile，并把同一对象同时用于索引、排序、阅读。对英文 Wikipedia 全量证据追踪发现，text 与 screenshot pipeline 都在丢失结构化证据：9.7% 的问题证据已存在存储 chunk 中却未进入 top-3；7.6% 的证据从未完整进入索引，其中 81% 是表格单元格、表头或 caption。更强抽取、上下文扩展、更大 reader 预算都无法自然恢复。

**方法关键点**
- **训练无关的查询时交付层**：从 ranked list 收集 anchor pages 的 HTML，保留 top k-1 项，用最后一个 slot 替换成结构补全的证据单元块，token 预算不变。
- **单元构建**：按 DOM 顺序生成段落、列表项、figure caption 和表格行；每行携带页面标题、章节路径、表格标题和列 header。针对合并单元格构建 faithful grid（span expansion、title/header/group rows、key-value、嵌套表继承）。
- **选择与打包**：lexical prefilter（N=100）后用 cross-encoder（复用 BGE-reranker-v2-m3）对 (query, completed unit) 打分，按分组共享 context/headers 进行预算中性打包。

**关键结果**
- NQ/NQ-Tables/SimpleQA 共 7,851 问题上，Tessera 对 hybrid text pipeline +5.0 点，PixelRAG text +6.2，PixelRAG screenshot +5.6；跨检索器增益 4.9-5.5，跨 reader 保持。
- 对比 14 种 baseline，matched budget 下最优；3K tokens + Tessera 超过 12K tokens chunks，1 tile + unit block 2K 超过 14 tiles 12K。
- Agentic search：FRAMES +5.22，搜索次数减少，上下文更短；消融显示结构补全是关键（bare units +1.8 vs completed +4.6）。

**最值得记住的一句话**
检索到页面后不要直接读 chunk，从页面 HTML 重建结构完整的小证据单元并塞进不变预算，可稳定提升 5-6 点准确率。
