---
title: 'MAGE-RAG: Multigranular Adaptive Graph Evidence for Agentic Multimodal RAG
  in Long-Document QA'
title_zh: 多粒度自适应图证据的智能体多模态RAG
authors:
- Yilong Zuo
- Xunkai Li
- Jing Yuan
- Qiangqiang Dai
- Hongchao Qin
- Ronghua Li
affiliations:
- Beijing Institute of Technology
arxiv_id: '2606.15906'
url: https://arxiv.org/abs/2606.15906
pdf_url: https://arxiv.org/pdf/2606.15906
published: '2026-06-14'
collected: '2026-06-17'
category: RAG
direction: 多模态长文档RAG · 图证据与智能体控制
tags:
- Multimodal RAG
- Graph Retrieval
- Agent
- Long-Document QA
- Evidence Budget
- LVLM
one_liner: 基于证据图与在线预算控制的多粒度多模态RAG，在长文档QA中动态平衡证据覆盖与噪声
practical_value: '- **多粒度证据图构建**：将文档拆解为页面与元素节点，编码布局、阅读顺序、章节层级等结构关系，可迁移到商品详情页的复杂多模态信息检索，例如将商品主图、详情图、参数表、评论链接为图，提升问答或推荐理由生成时的证据定位

  - **在线证据控制器与预算机制**：按预算迭代激活、搜索、剪枝证据，避免固定Top-k导致的噪声或遗漏。电商场景中可将此法用于动态组装推荐解释/导购上下文的证据片段，在有限令牌内提升说服力

  - **多模态证据渲染为结构化输入**：将文字、表格、图片等证据统一格式化后馈入大视觉语言模型，启发电商推理时可把商品图文、参数、问答截图等异构信息规范渲染，增强模型理解一致性

  - **证据覆盖与噪声的显式权衡**：通过预算-性能曲线分析最佳工作点，推荐系统面对长商品详情、长用户评论时，可借此思路为LLM推理设定预算、平衡信息量与推理成本'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：长文档多模态QA需在PDF中定位稀疏的多模态证据（文本、表格、图像、布局），现有RAG固定Top-k检索要么丢失视觉与布局信息，要么引入大量噪声，静态权衡覆盖与成本。

**方法**：提出MAGE-RAG，离线构建证据图，节点包括页面与元素（文本块、表格、图片等），边编码包含、阅读顺序、布局邻接、章节层级和语义邻居关系。在线查询时，一个Agent化的证据控制器在显式预算（如令牌数、节点数）约束下迭代执行激活、打开、搜索、剪枝操作，动态生成证据子图，最后将该子图渲染为结构化的多模态输入送入大视觉语言模型（LVLM）进行答案生成。

**结果**：在LongDocURL上总体准确率52.75，MMLongBench-Doc上准确率53.26、F1 51.19。细粒度分析、预算-性能曲线和消融实验验证了查询时证据子图构建能显著平衡分散证据的覆盖与上下文噪声控制。
