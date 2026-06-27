---
title: Information-Aware KV Cache Compression for Long Reasoning
title_zh: 信息感知的 KV 缓存压缩用于长推理
authors:
- Jushi Kai
- Zhuiri Xiao
- Alexandra Birch
- Zhouhan Lin
affiliations:
- Shanghai Jiao Tong University
- University of Edinburgh
arxiv_id: '2606.26875'
url: https://arxiv.org/abs/2606.26875
pdf_url: https://arxiv.org/pdf/2606.26875
published: '2026-06-24'
collected: '2026-06-27'
category: Reasoning
direction: LLM 推理优化 · 熵感知 KV 压缩
tags:
- KV cache compression
- entropy
- attention
- long reasoning
- LLM
one_liner: 提出熵感知的 KV 缓存压缩框架 InfoKV，结合预测不确定性与注意力得分，提升长推理效率。
practical_value: '- **长对话/文档推理的部署加速**：在电商搜索推荐系统的多轮助手、售后长文档分析等场景，可直接用 InfoKV 压缩 KV
  缓存，减少显存占用与解码延迟，无需重新训练模型。

  - **Agent 长期记忆的高效管理**：Agent 在维护对话历史或用户行为序列时，利用预测不确定性筛选对远期推理关键的信息 token，既保留关键上下文又控制缓存大小，提升持续交互的响应速度。

  - **混合重要性评估范式**：将 token 级熵信号与传统的注意力权重结合，是一种低成本、即插即用的重要性评分增强方式，可迁移到其它需要上下文剪枝的 LLM
  应用中（如 RAG 中的长文档分块选择）。

  - **解码阶段动态压缩**：InfoKV 在解码阶段同样有效，适合流式生成时不断增长的 KV 缓存管理，可降低线上长时生成过程的尾部延迟。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 长推理场景下 KV 缓存内存与计算开销激增，现有压缩方法仅依赖注意力权重衡量 token 重要性，忽略了预测不确定性与信息量等互补信号，导致对远距离依赖的 token 保留不足。

**方法**：首先定义“前向影响”指标，量化被压缩 token 对后续生成的影响。分析发现：高注意力 token 主要影响近邻上下文，而高预测不确定性 token 对远距离上下文影响显著更强。基于此提出 InfoKV 框架：对每个 token 计算预测分布的熵作为不确定性度量，结合层间表示变化的范数得到信息论重要性得分，再与原始注意力分数加权融合，动态选择保留 token 进行 KV 缓存压缩。

**结果**：在 LongBench 等长上下文推理基准上，使用 Llama-3.1、Llama-3.2 和 DeepSeek-R1 模型，InfoKV 在不同压缩率下均优于仅使用注意力权重的压缩方法，尤其在长输入预填充和长解码阶段表现更突出。
