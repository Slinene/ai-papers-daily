---
title: First Passage Attention
title_zh: 首达注意力机制（First Passage Attention）
authors:
- Yuxuan Liu
affiliations:
- University of Bergen
arxiv_id: '2610.22714'
url: https://arxiv.org/abs/2610.22714
pdf_url: https://arxiv.org/pdf/2610.22714
published: '2026-10-14'
collected: '2026-10-21'
category: LLM
direction: 注意力机制 · 选择性上下文擦除
tags:
- attention
- forget gate
- KV cache
- long context
- passkey retrieval
- selective erasure
one_liner: 用路径极值替代累加衰减，实现选择性上下文擦除并压缩 KV cache 到 25% 仍保持长程检索
practical_value: '- 长序列用户行为建模：FPA 的“路径极值”允许选择性擦除中间事件（如误触、临时会话）而保留早期长期偏好，适合电商用户序列编码。

  - 多轮 Agent/对话上下文管理：可借鉴其栈式存活 key 机制，在 RAG 长对话中自动丢弃已撤销指令或中间推理，降低噪声并压缩 KV cache。

  - 工程优化：FPA 在约 25% KV cache 压缩下保持 8 倍训练长度 passkey 检索，可直接用于长上下文推理降本，对搜索推荐 LLM 服务有实用价值。

  - 可尝试将 FPA 头部作为用户序列编码器，替代 additive forget gate，提高对层级事件（加入/删除购物车、订单状态变更）的敏感度。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有带遗忘门的 softmax attention 沿 key-query 路径累加衰减，单调累积导致无法选择性擦除中间上下文同时保留早期重要 token（如栈式嵌套结构）。

**方法关键点**：FPA 改用路径极值，将 key 的 logit 按中间跨度内学习标量场低于该 key 水平的最深下降比例惩罚；当标量场与水平遵循共享学习游走时，存活 key 自然形成栈。FPA 包含 FoX 为特例。

**关键结果**：合成实验中单层 FPA 收敛到目标集合，softmax/FoX 全部 seed 失败；110M 语言模型上 FPA 困惑度与 FoX 持平，且在 8 倍训练长度实现完美 passkey 检索，KV cache 压缩至约 25% 仍保持。
