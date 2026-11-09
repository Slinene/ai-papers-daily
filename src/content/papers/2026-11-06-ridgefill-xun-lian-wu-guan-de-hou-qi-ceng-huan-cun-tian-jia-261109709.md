---
title: 'RidgeFill: Training-Free Late-Layer Cache Fill for Faster Prefill'
title_zh: RidgeFill：训练无关的后期层缓存填充加速预填充
authors:
- Dylan Johnston
- Robert P. Smith
affiliations:
- Independent researcher
arxiv_id: '2611.09709'
url: https://arxiv.org/abs/2611.09709
pdf_url: https://arxiv.org/pdf/2611.09709
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: 训练无关 LLM 推理加速 · KV cache 填充
tags:
- LLM inference
- KV cache
- prefill acceleration
- training-free
- ridge regression
- long context
one_liner: 通过岭回归预测上层输入并填充 KV cache，长 prompt prefill 加速 1.25-1.60 倍且免训练
practical_value: '- 在线 Agent/RAG 服务（如会话历史、商品知识库、广告素材长文档）常受长 prompt 首 token 延迟困扰；RidgeFill
  的免训练 cache 填充适合快速接入现有 vLLM/llama.cpp 服务，仅需一次离线校准拟合 ridge map，无需训练资源。

  - 工程上保留尾部数千 token 和所有 decode step 使用 full model，是质量与速度的折中；若业务对长程检索/针任务敏感（如电商搜索精确召回），需用
  needle retrieval 和远端依赖 token loss 评估，而不是只看平均 loss。

  - 不同模型误差来源不同：Llama-3.1-8B 主要在 key 的 scale，Qwen3.5-9B 在 value 和 recurrent state；落地前应做
  splice test 定位瓶颈，避免盲目套用。

  - 强 RAG 且 query 依赖长文档定位时需谨慎：Qwen3.8-Flash-Next 在 vLLM 上 1.5-1.6x 加速，RULER 针任务 99.8
  vs 100.0，可能有微小损失；可先在非关键路径或离线批处理使用。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：长 prompt prefill 是首 token 延迟的主要瓶颈，例如 120K tokens 在 Qwen3.8-27B 上 A100 需 128 秒。现有 YOCO/DeepSeek-V4.1-Flash 在训练中学习 late-layer cache 填充，但无法用于已训练模型。

**方法关键点**：RidgeFill 对现有模型免训练改造：lower layers 跑到 split 层，用 per-layer ridge regression 从 split 层状态预测各上层输入，上层据此写 KV cache；回归用一次校准文本闭式拟合，不改变原有投影，保留尾部数千 token 且所有 decoding step 运行 full model，无 token 丢弃。测量发现平均 loss 会掩盖误差，需用 needle retrieval、远端 token loss、splice test 定位误差来源：Llama-3.1-8B 误差主要来自 key 的 scale，Qwen3.5-9B 来自 value 和 recurrent state。

**关键结果**：Qwen3.8-27B llama.cpp + A100，TTFT 在 16K-120K tokens 加速 1.25-1.31x，RULER 下降 1.2-1.4 点，LongBench v2 下降 1.4，95% 区间含零；Qwen3.8-Flash-Next vLLM 在 9K-32K 加速 1.50-1.60x，RULER needle tasks 99.8 vs 100.0，novel token perplexity 高 2.65%。在 8-9B 参考模型上，fitted map 的 filled-region RULER 点数比 identity fill 高约 49 分，long-document loss 与 SwiftKV checkpoint 差距在 0.03 nats 内。
