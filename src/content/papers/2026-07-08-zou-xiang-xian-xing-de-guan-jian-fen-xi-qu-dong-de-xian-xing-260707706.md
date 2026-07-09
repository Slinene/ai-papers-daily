---
title: 'The Key to Going Linear: Analysis-Driven Transformer Linearization'
title_zh: 走向线性的关键：分析驱动的 Transformer 线性化
authors:
- Anna Kuzina
- Paul N. Whatmough
- Babak Ehteshami Bejnordi
affiliations:
- Qualcomm AI Research
arxiv_id: '2607.07706'
url: https://arxiv.org/abs/2607.07706
pdf_url: https://arxiv.org/pdf/2607.07706
published: '2026-07-08'
collected: '2026-07-09'
category: LLM
direction: LLM 后处理线性化 · 冻结骨干注意力近似
tags:
- linear attention
- post hoc linearization
- softmax approximation
- sink tokens
- fixed-budget cache
- transformer inference
one_liner: 证明 key-dependent rank-1 正交投影是 softmax 的关键，提出 sink tokens、短卷积、固定预算缓存路由等干预，实现冻结骨干线性化，在
  32B 规模超越前方法
practical_value: '- 若业务使用 LLM 做长上下文推理（如 Agent 长记忆、长文档理解），可采用冻结骨干 + 训练轻量线性注意力替换的方式，大幅降低
  KV 缓存和计算量，保持模型质量。

  - 提出的 sink tokens、短卷积、固定预算缓存路由是低成本的结构干预，可直接嵌入现有注意力层，尤其适合需要实时响应的推荐或搜索系统。

  - 分析揭示 key-dependent rank-1 投影是 softmax 的核心操作，为设计定制化的高效注意力模块提供了理论依据，避免盲目试错。

  - 该方法无需全参数微调，只需训练少量新增参数，适合模型频繁更新或需保持原始性能稳定的场景。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：Transformer 长上下文推理受限于自注意力的二次复杂度，已有后处理线性化方法混合多种干预，难以确定哪种状态更新最能近似 softmax。本文严格冻结预训练骨干，仅训练注意力替换部分，以分离线性化效果。

**方法**：作者推导一阶近似，证明 softmax 本质是在 key 上做 rank-1 正交投影，这解释了为何 delta 风格网络（如 Mamba）优于简单门控累积。发现近似误差来源后，引入三项结构干预：1) **sink tokens** 吸收冗余信息以稳定状态；2) **短卷积** 捕获局部上下文；3) **固定预算缓存路由** 动态选择最有用的 KV 对。整个线性化过程在原模型参数不变下完成，新增模块训练成本低。

**结果**：在 LLaMA 和 Qwen 上扩展到 32B 参数，MMLU 分数超越所有后处理基线，长文本检索性能与复杂的自适应缓存框架持平，验证了冻结骨干线性化的可行性。
