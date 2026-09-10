---
title: 'Graph Machine: Towards Better Pretraining via Edges'
title_zh: Graph Machine：边驱动的稀疏动态路由预训练
authors:
- Lintai Hou
affiliations:
- IterLabs
arxiv_id: '2609.02881'
url: https://arxiv.org/abs/2609.02881
pdf_url: https://arxiv.org/pdf/2609.02881
published: '2026-09-01'
collected: '2026-09-10'
category: Training
direction: 稀疏动态路由预训练架构
tags:
- Graph Machine
- Sparse Dynamic Routing
- Pretraining
- Efficiency
- Transformer
one_liner: 以可微指针边实现 O(n) 状态 + O(1) 稀疏动态路由，替换 Qwen3-0.6B 75% 层后检索 2-4 个 token 即保持或改善
  loss
practical_value: '- 电商推荐中的用户行为序列常达数千甚至更长，可借鉴 GM 的 O(n) 状态 + O(1) 动态稀疏访问思想：用可学习的边/指针替代固定窗口或全局
  attention，在序列建模中同时保留长程状态并控制计算与 KV cache 成本。

  - 对 Agent 或多轮对话场景，referral mechanism 可看作一种可微的记忆寻址：比固定 top-k 的 RAG 检索更灵活，可以尝试在召回或知识引用模块中引入类似
  pointer chasing 的更新，让模型自己学该引用哪些历史状态。

  - 工程上，GM 稀疏层每个 KV head 只取 2-4 个 token 即能保持 loss，意味着在线推理时可大幅减少 KV cache 读写和 attention
  计算；在推荐模型做长序列或全生命周期建模时，这可能直接降低延迟和显存。

  - 注意这是通用 LLM 预训练工作，迁移到电商推荐或搜索需在领域数据上验证混合比例（论文为 75% 稀疏层）、检索 token 数和边更新频率对 CTR/CVR
  等业务指标的影响。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有序列建模可按状态大小、访问大小和动态地址分类：RNN/SSM 状态 O(1)；vanilla Transformer 状态 O(n) 但访问 O(n)；滑窗 Transformer 虽然访问 O(1) 但稀疏静态，与当前 token 内容无关。Graph Machine (GM) 想实现第 4 类：O(n) 状态、O(1) 访问，但由新 token 提供约 Θ(log n) 动态地址 bits 来选择状态子集。

**方法关键点**：GM 用 edges（指针对象）维护状态引用，通过 referral mechanism 类似 pointer chasing 来可微地更新。替换 Qwen3-0.6B 中 75% 的 dense Transformer 层，从零预训练 15.7B tokens；每个稀疏层每个 KV head 仅从 4096 个 token 中动态检索 2 或 4 个。

**关键结果**：检索 2 个 token 时 loss 仅轻微退化；检索 4 个 token 时最佳模型 loss 略优于 baseline，说明极低访问比例能保持预训练质量。
