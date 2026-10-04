---
title: 'From Rules to Neural Graphs: Scalable Structured Prediction for Patent Prior
  Art Search'
title_zh: 从规则到神经图：可扩展结构化预测用于专利现有技术检索
authors:
- Nikolai Zenovkin
- Sebastian Björkqvist
affiliations:
- IPRally Technologies Oy
arxiv_id: '2610.01553'
url: https://arxiv.org/abs/2610.01553
pdf_url: https://arxiv.org/pdf/2610.01553
published: '2026-10-01'
collected: '2026-10-04'
category: Other
direction: 信息检索 · 图结构化预测
tags:
- Patent Search
- Biaffine Attention
- Invention Graph
- Knowledge Distillation
- Long Document Retrieval
- Graph Transformer
one_liner: 用局部 biaffine attention 构建专利发明图，蒸馏规则解析器，实现长文档可扩展图检索
practical_value: '- 长商品描述/详情页常被截断，可借鉴局部 biaffine attention 构建商品属性/关系图，用图表示替代截断；短序列训练、长序列部署，适合线上低延迟。

  - 规则解析器（类目、属性、标签体系）脆弱且维护成本高，可仿照知识蒸馏：用已有规则系统生成百万级标注，训练轻量神经解析器，通常能超越规则模型且推理成本更低。

  - 对超长文档检索，图结构 + Graph Transformer 比直接 dense 向量在全文档上更有效，尤其查询与文档长度差异大时；商品详情页可构建轻量图做相关性匹配。

  - 滑动窗口限制 pair scoring 是简单有效的 O(n²)→O(n·w) 优化，对任何需长序列实体/关系抽取的模块都有参考，且权重共享使短序列训练直接部署到长序列，无需重训。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：专利检索需处理超长文档，常用神经检索截断输入，损失信息；图检索用发明图表示专利，但构建依赖脆弱的规则解析器。

**方法**：提出神经解析器，将依存解析中的 biaffine attention 用于直接从专利文本预测发明图。局部滑动窗口限制 pair 评分，复杂度从 O(n²) 降至 O(n·w)；局部与全局评分共享权重，因此短序列训练可部署到 4 万+ token 文档。从 100 万规则解析文档蒸馏，替代规则 teacher。

**结果**：推理成本降低 3 倍，下游 Graph Transformer 检索系统上，短查询引用召回 +0.5%，全文档 +1.1%。
