---
title: 'Flash-dLLM: IO-Aware KV Caching and Parallel Decoding for Fast, Memory-Efficient
  Diffusion LLMs'
title_zh: Flash-dLLM：IO感知KV缓存与并行解码加速扩散LLM
authors:
- Quan Nguyen-Tri
- Mukul Ranjan
- Zhiqiang Shen
affiliations:
- VILA Lab, MBZUAI
arxiv_id: '2609.26796'
url: https://arxiv.org/abs/2609.26796
pdf_url: https://arxiv.org/pdf/2609.26796
published: '2026-09-21'
collected: '2026-09-23'
category: LLM
direction: 扩散LLM推理加速·KV cache
tags:
- Diffusion LLM
- KV Cache
- Parallel Decoding
- Inference Acceleration
- IO-Aware
one_liner: 训练无关Flash-dLLM以IO感知融合KV cache和自草稿-验证解码，显著加速扩散LLM推理并省内存
practical_value: '- 在 LLM 推理服务（如广告文案/搜索词生成）中，KV cache 的 HBM 读写常成为瓶颈；可借鉴 Flash-dLLM
  的 IO-aware 融合 kernel，把多个注意力/cache 操作合并执行，减少冗余显存搬运，提升 batch/long-context 吞吐。

  - 自草稿-验证（self draft-and-verify）不引入额外 drafter 模型，适合资源受限的 Agent/推荐系统：让主模型复用 KV cache
  同时生成候选并按验证结果接受，降低延迟且不增加显存。

  - 其并行解码与 KV-cache 驱动候选验证思路可迁移到批量生成场景，例如离线批量生成商品标题、query 改写或 push 文案；考虑非自回归或半自回归解码来扩大
  batch size、缩短首 token 延迟。

  - 面对 RAG 长文档或用户长序列，KV cache 显存与 I/O 受限时，可参考其对缓存复用和显存效率的优化策略，设计更紧凑的 cache 分层或融合模式。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：扩散 LLM（dLLM）以非自回归方式生成文本，但缺少有效 KV cache 和并行解码，推理效率低；现有方法将 cache 与并行解码分开研究，忽略二者结合时的 I/O 瓶颈。

方法：Flash-dLLM 是训练无关的推理加速框架。首先指出 GPU 显存 I/O 是启用 KV cache 的 dLLM 推理主要瓶颈，提出 IO-aware 融合 KV-cache kernel，减少冗余显存搬运。基于优化后的缓存，设计 KV-cache 驱动的 draft-and-verify 解码：由 dLLM 自身同时充当 drafter 和 verifier，无需辅助模型，用缓存复用支撑候选生成与验证。统一设计在不损失生成质量的前提下提升解码速度，并支持更长序列和更大 batch。

结果：在数学推理 GSM8K 与代码生成 HumanEval 上，Flash-dLLM 超过现有最强基线 Elastic-Cache，分别获得 5.1× 和 11.0× 加速，同时保持生成质量、提升显存效率。
