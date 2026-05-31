---
title: 'DocRetriever: A Plug-and-Play Framework for Multimodal Document Retrieval
  with Comprehensive Benchmark'
title_zh: DocRetriever：即插即用的多模态文档检索框架与全面基准
authors:
- Ruofan Hu
- Menghui Zhu
- Jieming Zhu
- Bo Chen
- Shengyang Xu
- Minjie Hong
- Xiaoda Yang
- Sashuai Zhou
- Li Tang
- Tao Jin
affiliations:
- Zhejiang University
- Huawei Technologies Co., Ltd
arxiv_id: '2605.30027'
url: https://arxiv.org/abs/2605.30027
pdf_url: https://arxiv.org/pdf/2605.30027
published: '2026-05-28'
collected: '2026-05-31'
category: Other
direction: 多模态文档检索
tags:
- multimodal document retrieval
- layout-aware sparse embedding
- reranker
- few-shot learning
- benchmark
one_liner: 提出布局感知稀疏嵌入与推理增强重排序的即插即用框架，并构建多维度评估基准MultiDocR
practical_value: '- **布局感知稀疏嵌入**：无需OCR即可编码文档结构，适合电商商品详情页（图文混排）的检索，可迁移至商品描述与图片联合编码，保留排版信息提升匹配精度。

  - **推理增强少样本重排序器**：利用推理链演示和优化采样降低领域数据依赖，可用于推荐系统重排模块，在冷启动或跨域场景下快速适应，提升泛化能力。

  - **混合编码策略**：结合密集与稀疏表征，平衡效率与精度，可直接应用于Agent知识库的多模态文档检索，改善问答系统的证据召回质量。

  - **评估基准MultiDocR**：提供细粒度相关性和多维度评估设计，可借鉴其构建思路，为电商搜索或推荐场景设计更全面的相关性评估集。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态文档（含表格、图表、复杂排版）检索面临两大挑战：密集视觉嵌入忽略显式结构语义，监督重排序模型泛化能力受限于领域数据。此外，现有基准缺乏多维度评估与细粒度相关性标注。  
**方法**：提出DocRetriever，一个即插即用框架，包含三项核心设计：(1) 布局感知稀疏嵌入技术，在不依赖OCR的前提下混合编码视觉与布局信息；(2) 推理增强的通用重排序器，通过推理链演示和优化采样实现少样本下的高效泛化；(3) 新基准MultiDocR，覆盖多层级相关性判断和评估维度。  
**关键结果**：在多个文档检索基准上，DocRetriever均取得优于SOTA方法的性能，验证了布局感知稀疏嵌入和推理增强重排的有效性。
