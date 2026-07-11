---
title: 'DocMaster: A Hierarchical Structure-Aware System for Document Analysis'
title_zh: DocMaster：层次结构感知的文档分析系统
authors:
- Ziqi Chen
- Yingli Zhou
- Fangyuan Zhang
- Quanqing Xu
- Chuanhui Yang
- Yixiang Fang
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- The Chinese University of Hong Kong
- OceanBase, AntGroup
arxiv_id: '2607.08539'
url: https://arxiv.org/abs/2607.08539
pdf_url: https://arxiv.org/pdf/2607.08539
published: '2026-07-09'
collected: '2026-07-11'
category: RAG
direction: 结构感知文档索引与多模态分析
tags:
- hierarchical document
- structure-aware indexing
- document filtering
- question answering
- RAG
one_liner: 保留文档层次结构，构建结构感知语义索引，提升复杂文档过滤与问答性能
practical_value: '- 电商商品搜索中，可借鉴文档树解析商品详情页，保留标题、属性、图片的层次结构，构建多粒度索引，提高长尾查询的召回精度。

  - 多视图语义索引策略可应用于商品评论和描述的分离索引，支持自然语言条件过滤（如“有赠品的商品”），增强可解释性过滤能力。

  - 先过滤后问答的 workflow 可迁移至智能客服：先基于层次化结构筛选相关商品/政策文档，再做精准回答，降低 token 消耗并提高准确率。

  - 树形结构语义索引的设计思路可复用到商品类目体系，结合 LLM 进行类目感知的个性化推荐，保持层次约束。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有 LLM 文档分析系统将文档拍平为纯文本块，丢失了章节、表格、图表、公式等层次结构，导致下游文档过滤和问答性能下降。特别在科研、金融等需要从大量文档中先筛选再深度分析的场景，结构信息缺失严重影响了结果准确性。

**方法**：提出 DocMaster，一个层次结构感知的文档分析系统。核心设计包括：
1. **文档解析**：将 PDF 解析为保留原始布局的层次化文档树，每个节点对应章节、表格、图表、公式等结构单元。
2. **结构感知语义索引**：基于文档树构建两种索引——树形索引（维护节点间层级关系）和多视图语义索引（为不同结构类型分别建立向量库），支持跨粒度语义匹配。
3. **过滤与问答管线**：用户用自然语言条件过滤文档集合，系统利用索引快速定位相关子树，随后在过滤结果上执行检索增强生成（RAG）问答。

**关键结果**：系统通过交互式 Web 界面演示了完整流程：上传文档集、构建索引、自然语言过滤、上下文问答。相比扁平化基线，保留结构显著提升了文档检索的精确率和问答的事实一致性。代码和 demo 已开源，提供了可直接部署的文档分析解决方案。
