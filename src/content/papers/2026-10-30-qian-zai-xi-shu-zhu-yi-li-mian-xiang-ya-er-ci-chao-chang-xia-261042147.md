---
title: 'Latent Sparse Attention: Towards Subquadratic Ultra-Long Context Attention'
title_zh: 潜在稀疏注意力：面向亚二次超长上下文注意力
authors:
- Ales Kubicek
- Andrea Caciolai
- Liangzu Peng
- Sukrit Sumant
- Benjamin Hoover
- Fraser Greenlee
- Ruairidh M. Battleday
- Radim Urban
- Torsten Hoefler
- James C. R. Whittington
arxiv_id: '2610.42147'
url: https://arxiv.org/abs/2610.42147
pdf_url: https://arxiv.org/pdf/2610.42147
published: '2026-10-30'
collected: '2026-11-02'
category: LLM
direction: 高效注意力 · 超长上下文
tags:
- Latent Sparse Attention
- Long Context
- Efficient Attention
- Hierarchical Clustering
- Distillation
- Agentic Workflows
one_liner: 提出潜在稀疏注意力 LSA，通过可学习层次聚类实现超长上下文亚二次注意力且保持精度
practical_value: '- 长上下文 Agent 会话/记忆管理可借鉴：电商导购、客服等 Agent 维护超长多轮历史时，用 learned latent
  space 对 keys 做层次聚类，query 只打分聚类中心，大幅降低 decode 阶段的 KV cache 访问与计算，适合在线低延迟场景。

  - 已有预训练模型不想重训的情况下，D-LSA 蒸馏提供低成本升级路径：仅在注意力层增加分层聚类索引，用原模型蒸馏对齐，可离线验证精度损失后逐步上线。

  - 若从零训练或大规模训练长上下文模型，N-LSA 原生训练同时降低训练与推理成本（128k tokens 单层训练 1.6x），对自建基础模型或微调有参考价值。

  - 局限与注意：方法依赖键空间聚类稳定性，电商推荐中商品/query 分布快速变化，需评估索引重建频率与召回误差；目前验证集中于语言模型，迁移到推荐特征需要额外实验。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：Agent 工作流转向长程任务，超长上下文（>1M tokens）下全注意力成本过高；已有稀疏注意力索引要么仍 O(n²) 要么在超长上下文失去精度。

方法关键点：LSA 在可学习潜在空间对 keys 做层次聚类，query 只对聚类层次打分而非逐 key 打分，降低 prefill、decode、训练复杂度。两个变体：Distilled-LSA (D-LSA) 通过蒸馏应用于预训练模型；Native-LSA (N-LSA) 直接以 next-token loss 原生训练。

关键结果：在 GLM-5.3-FLASH（相对其原始稀疏注意力）和 QWEN-3.8-27B（相对全注意力）10M tokens 下，D-LSA 单层 prefill 加速 22.7× / 72.4×，decode 加速 4.6× / 42.5×，各任务精度接近。N-LSA 达到全注意力精度，128k tokens 时每层训练加速 1.6×。
