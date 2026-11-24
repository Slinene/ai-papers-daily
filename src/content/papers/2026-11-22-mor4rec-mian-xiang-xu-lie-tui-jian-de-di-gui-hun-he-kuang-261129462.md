---
title: 'MoR4Rec: Mixture-of-Recursion for Sequential Recommendation'
title_zh: MoR4Rec：面向序列推荐的递归混合框架
authors:
- Tiwari Ankit Satyaprakash
- Adamya Shyam
- Vikas Kumar
- Bharti Rana
- Venkateswara Rao Kagita
affiliations:
- University of Delhi, India
- K.R. Mangalam University, India
- National Institute of Technology Warangal, India
arxiv_id: '2611.29462'
url: https://arxiv.org/abs/2611.29462
pdf_url: https://arxiv.org/pdf/2611.29462
published: '2026-11-22'
collected: '2026-11-24'
category: RecSys
direction: 序列推荐 · 自适应计算深度
tags:
- Sequential Recommendation
- Adaptive Computation
- Mixture-of-Recursion
- Dynamic Routing
- Key-Value Sharing
- Gated Attention
one_liner: 用递归混合实现 item 级自适应计算深度，在序列推荐中同时提升精度与计算效率
practical_value: '- 在线推荐系统通常为所有用户或物品固定 transformer 层数，可借鉴 item-wise 动态深度：让简单行为序列浅层计算，将算力倾斜给复杂长序列，降低
  RT 并提升吞吐，尤其适合电商大促期间弹性计算。

  - 动态路由训练稳定性可参考其 cascade + KV sharing 设计：不同递归深度之间复用 attention key/value，避免深层重复计算，适合在召回或粗排阶段先验证，因为
  latency 收益更明显。

  - gated attention 思想可迁移到多行为序列建模：对点击、加购、转化等不同行为类型用门控调节对兴趣表征的贡献，而不是简单拼接或求和，能更好捕捉行为异质性。

  - 评估自适应计算模型时，除了 Recall/NDCG，要同时报告实际计算量或推理时间，否则动态深度在工程上无法证明收益；该论文展示了 vanilla transformer
  基线下的效率对比，可作为评估范式。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：序列推荐常用 transformer 捕捉长程依赖，但所有交互 item 使用相同计算深度。真实用户行为中大量交互只是简单重复模式，少数需要高阶依赖建模，固定深度导致算力浪费与容量利用不充分。

**方法**：MoR4Rec 采用 Mixture-of-Recursion 范式，在共享 transformer backbone 上引入学习路由，为每个 item 动态选择递归深度：复杂交互分配更深的计算，简单模式用较浅层。同时提出 cascade 策略并在递归步间共享 key-value，降低重复注意力计算开销；进一步引入 gated attention 自适应调节序列上下文信息。

**结果**：在三个 benchmark 数据集上，MoR4Rec 相比最强 transformer baseline 平均提升 Recall@5 2.28%、NDCG@5 2.50%、MRR@5 2.0%，且 top-10、top-20 指标同样稳定。与 vanilla transformer 对比显示自适应递归处理带来明显的计算效率优势。
