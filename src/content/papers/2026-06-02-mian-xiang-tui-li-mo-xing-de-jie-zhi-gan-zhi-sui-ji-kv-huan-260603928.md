---
title: Value-Aware Stochastic KV Cache Eviction for Reasoning Models
title_zh: 面向推理模型的价值感知随机 KV 缓存淘汰方法
authors:
- Ting-Yun Chang
- Harvey Yiyun Fu
- Deqing Fu
- Chenghao Yang
- Jesse Thomason
- Robin Jia
affiliations:
- University of Southern California
- University of Chicago
arxiv_id: '2606.03928'
url: https://arxiv.org/abs/2606.03928
pdf_url: https://arxiv.org/pdf/2606.03928
published: '2026-06-02'
collected: '2026-06-03'
category: LLM
direction: LLM 高效推理 · KV 缓存淘汰
tags:
- KV cache
- eviction
- reasoning
- stochastic
- value-aware
- efficient inference
one_liner: 发现大值状态淘汰导致灾难性重复并利用随机性提升多样性，提出训练无关的 VaSE 方法，4 倍压缩下准确率优于 SOTA
practical_value: '- 在电商/Agent 系统中部署长链推理模型（如复杂商品推荐解释）时，可直接引入 VaSE 降低显存开销，同时避免精度下降。

  - 价值保护策略：任何 KV 缓存淘汰方案均可增加按 value 向量范数排序的前 k 个 token 保护步骤，防止高幅值 token 被误删导致生成重复循环。

  - 随机化淘汰：在淘汰决策中注入高斯噪声（如基于噪声后的重要性分数排序），可提升缓存多样性，适用于 Agent 多轮对话或推荐理由生成，减少输出退化。

  - 与 FlashAttention2 兼容，可实现静态显存分配，减少 OOM 风险，适合长期运行的在线推理服务。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：推理模型通过长链思维提升准确率，但长输出带来显存与计算瓶颈。现有 KV 缓存淘汰方法虽能压缩缓存，但常导致精度下降，甚至引发模型陷入重复推理循环。

**方法关键点**：
- 发现两个关键因素：① 极小部分 token 的 value 状态具有异常大的幅值，淘汰它们会引发灾难性重复；② 在淘汰决策中引入随机性可提高缓存多样性，改善精度。
- 提出 **Value‑aware Stochastic KV Cache Eviction (VaSE)**，一种训练无关的淘汰方案：保护大 value 幅值 token，并在淘汰分数上引入噪声以促进多样化决策。

**关键结果**：
- 在 6 个推理任务上，使用 Qwen3 模型和 4 倍 KV 缓存压缩，VaSE 在相同稀疏度下平均准确率高于保持全缓存的 SOTA 选择方法，且比最强淘汰方法高出超过 4%。
- 支持 FlashAttention2，可实现静态显存占用。
