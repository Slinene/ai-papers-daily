---
title: 'SAS: Simple Attention Sparsification via End-to-End Optimization of Context
  Ranking'
title_zh: 简单注意力稀疏化：端到端优化上下文排序
authors:
- Zhiwei Li
- Lei Zhu
- Hao Gu
- Xiang Hu
- Yan Wang
- Haitao Mi
- Sirui Han
- Leo Liang
- Zhijiang Guo
affiliations:
- Tencent HY LLM Frontier
- Hong Kong University of Science and Technology (Guangzhou)
- Hong Kong University of Science and Technology
arxiv_id: '2609.13141'
url: https://arxiv.org/abs/2609.13141
pdf_url: https://arxiv.org/pdf/2609.13141
published: '2026-09-10'
collected: '2026-09-14'
category: Training
direction: LLM 注意力稀疏化 · 端到端排序
tags:
- attention sparsification
- long context
- FlashAttention
- Triton kernel
- LM loss
- Top-K selector
one_liner: 用连续 selector 分数以 log 形式注入 attention softmax，端到端优化上下文排序，紧预算下大幅超过可训练稀疏注意力基线
practical_value: '- 需为长上下文/Agent 记忆做注意力稀疏化时，不要蒸馏 dense attention：把可训练 selector 的连续分数以
  log 形式塞进 attention softmax，用最终 LM loss 端到端更新，排序会更对齐固定预算下的下游效果；推理阶段仍可硬 Top-K。

  - 在流式/历史 context 场景（如用户长期行为序列、会话历史）保留 current block 并用 normalized softmax gate 校准历史窗口，可避免新
  block 被旧 context 淹没，适合电商推荐/广告文案生成里的长 prompt 组织。

  - 训练阶段保留连续 selector score 而非 hard selection，让模型学相对优先级；上线做硬稀疏时可显著提升紧预算下的性能，降低推理 KV
  cache/attention 成本。

  - 开源的 Triton/FlashAttention 融合 kernel 可作为长上下文稀疏训练底座，直接复用到商品描述、用户会话等长文本微调。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有可训练注意力稀疏化方法通常用轻量 selector 打分 + hard Top-K，梯度被截断，只能蒸馏 dense attention 分布；但 dense attention 排序未必对齐固定预算下对最终预测的影响，会浪费有限预算。

方法关键点：SAS 采用 gated sparse attention，将 selector 的连续分数以 log 形式注入 attention softmax，使 LM loss 能通过标准反向传播直接更新 selector；用 normalized softmax gate 校准历史 context 与始终保留的 current block；训练时保留连续 selector 分数，学习相对优先级而非仅 hard selection。为支持长序列训练，实现 Triton kernel 融合 FlashAttention 风格计算。

关键结果：在 reasoning、long-context understanding、agentic tasks 上，SAS 在不同 attention budget 下均优于可训练稀疏注意力基线，紧预算下提升尤其明显，说明其上下文排序对下游任务更有效。
