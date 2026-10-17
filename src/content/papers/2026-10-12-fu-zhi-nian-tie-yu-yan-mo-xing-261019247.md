---
title: Copy-Paste Language Models
title_zh: 复制粘贴语言模型
authors:
- Nathan Godey
- Yoav Artzi
affiliations:
- Cornell University
arxiv_id: '2610.19247'
url: https://arxiv.org/abs/2610.19247
pdf_url: https://arxiv.org/pdf/2610.19247
published: '2026-10-12'
collected: '2026-10-17'
category: LLM
direction: LLM 预训练 · 上下文复制机制
tags:
- Copy Mechanism
- Pretraining
- Long Context
- RAG
- Gradient Bottleneck
one_liner: 在 LM 头旁增加轻量 Copy-Paste 头显式建模上下文复制，提升训练效率与下游表现
practical_value: '- 商品名/品牌词/SKU/Query 需要精确复现：在微调或继续预训练时，可在 LM head 旁加一个 pointer/copy
  分支，从输入序列直接复制 token，降低改写错误与幻觉。

  - RAG / 长上下文用户行为建模：模型常需从知识库或历史序列中复现实体，CPLM 思路可帮助提升长程复制准确率；可对现有 LLM 做轻量适配，不必重训 backbone。

  - Agent 工具调用：API 名、参数、ID 等必须逐字复制，copy head 能增强此类能力；建议在工具选择评测中对比标准 LM head 与 copy
  分支。

  - 实际成本：增加头参数极少，推理可结合 KV cache 实现高效复制计算，适合对延迟敏感的生产环境。'
score: 6
source: huggingface-daily
depth: abstract
---

### 动机
预训练语料中约 60% token 已在 4k 上下文前文出现，复制是语言模型的基础操作。但标准 LM head 是低秩线性投影，既限制表达分布，又截断回传梯度，导致 vanilla Transformer 在大词表复制任务上失败。

### 方法关键点
提出 CPLM：在常规 LM head 旁增加轻量 Copy-Paste head，显式建模从上下文复制 token 的路径。模型可同时使用生成分布和复制分布，预测时融合；训练几乎无额外开销。

### 关键结果
在 135M–1.7B 多尺度/多骨干预训练中，CPLM 一致提升训练效率和下游性能，且在长上下文与检索设置中表现更好；作者将收益归因于 Copy-Paste 头提供了替代梯度路径，部分绕过 LM head 的梯度瓶颈。
