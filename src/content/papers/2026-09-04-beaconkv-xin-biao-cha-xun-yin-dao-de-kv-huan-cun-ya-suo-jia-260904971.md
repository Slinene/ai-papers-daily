---
title: 'BeaconKV: Key-Value Cache Compression Guided by Beacon Queries for Efficient
  Large Reasoning Model Inference'
title_zh: BeaconKV：信标查询引导的 KV 缓存压缩加速大推理模型推理
authors:
- Janghyeon Kim
- Minsoo Kim
- Kyuhong Shim
- Jungwook Choi
affiliations:
- Hanyang University
- Sungkyunkwan University
arxiv_id: '2609.04971'
url: https://arxiv.org/abs/2609.04971
pdf_url: https://arxiv.org/pdf/2609.04971
published: '2026-09-04'
collected: '2026-09-07'
category: LLM
direction: LLM 推理加速 · KV cache 压缩
tags:
- KV cache
- LLM inference
- compression
- reasoning models
- training-free
one_liner: 发现长程推理中查询聚类可预测重访 KV，提出训练无关信标查询压缩 KV 缓存，内存降5.8倍且准确率几乎无损
practical_value: '- 在自研/部署 LRM（如 DeepSeek-R1、Qwen3）的推理服务中，KV cache 内存常成为瓶颈；BeaconKV
  训练无关，可直接插入现有推理框架（如 vLLM、SGLang），无需微调，适合电商/广告场景的复杂导购 Agent、自动策略生成等长 CoT 任务。

  - 借鉴“thought revisiting”洞察：模型长推理时会重访早期计划/关键信息，若在 Agent 记忆或上下文选择中使用简单的 recent-biased
  策略可能丢失重要远距离信息；建议对历史 query 做聚类，保留每个聚类的代表性 query，用于判断哪些 KV 应保留。

  - 工程实现上，可维护少量 beacon queries（每个聚类代表）而非完整 query 历史，预测后续 token 是否会重访，从而动态裁剪 KV cache；该方法已在四个开源
  LRM 上验证，内存减少最高5.8×、吞吐提升4.3×，可先在离线长推理任务上 A/B 测试效果。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LRMs 通过长 CoT 实现强推理，但 KV cache 随序列长度线性增长，严重内存瓶颈，经常超出 GPU 容量。现有 KV cache 压缩方法依赖 recent queries 估计未来 token 重要性，隐含假设近期查询是未来注意模式的可靠代理。作者发现该假设在长程推理中不成立：存在 Thought Revisiting Tokens (TRT) 会重新关注远距离上下文，如早期制定的任务求解计划。

**方法关键点**：系统分析发现 TRT 对应的 queries 在嵌入空间中聚成少量相似组。基于此提出 BeaconKV，训练无关，维护 beacon queries（每个全局 query 聚类的紧凑代表）来预测哪些 KV 对会被重访，无需存储整个 query 历史。Beacon queries 作为轻量级代理，在解码时动态决定保留哪些 KV 对。

**结果**：在四个开源 LRMs（如 DeepSeek-R1、Qwen3）和多个推理基准上，BeaconKV 一般优于现有压缩方法，内存减少最高 5.8×，几乎保持全缓存准确率，吞吐提升超过 4.3×。
