---
title: 'TokenGate: Adapting LLMs for Fast and Memory-Efficient Prefill with Learned
  Token Pruning'
title_zh: TokenGate：可学习 token 剪枝加速 LLM 预填充且精度不降
authors:
- Liana Patel
- Rishabh Ranjan
- Ion Stoica
- Matei Zaharia
- Carlos Guestrin
affiliations:
- Stanford University
- UC Berkeley
arxiv_id: '2610.26754'
url: https://arxiv.org/abs/2610.26754
pdf_url: https://arxiv.org/pdf/2610.26754
published: '2026-10-18'
collected: '2026-10-21'
category: LLM
direction: LLM 长上下文预填充加速 · 可学习 token 剪枝
tags:
- Token Pruning
- Prefill Efficiency
- KV Cache
- Long Context
- MoE
- LoRA
one_liner: 提出可插入组件 TokenGate，通过类 MoE 的 token-gated attention 端到端训练 token 剪枝，大幅加速长上下文预填充且精度不降
practical_value: '- 在电商/Agent 场景中，长文档（商品详情、用户评论、搜索广告上下文、RAG 检索文档）的预填充是延迟和内存瓶颈；可借鉴
  TokenGate 在模型中间层引入可学习 token 剪枝，相比 FastKV 等启发式方法，端到端训练能显著提升速度且精度无损，且可与 LoRA 一起微调，训练开销仅约
  1.3x/step，总体甚至更少。

  - token-gated attention 是关键 trick：把不可微的 top-K 剪枝通过类似 MoE 的门控值乘到 attention logits
  上，让 scoring network 获得梯度，同时让模型骨干自适应剪枝后的稀疏注意力；该思路可迁移到任何需要在 Transformer 中间层做软筛选的任务，如多文档
  RAG 中对检索片段做软裁剪。

  - 训练时使用 dual budget sampling（全量 + 对数均匀采样的剪枝预算各一半损失），使单个模型泛化到不同 token 预算，无需为每个压缩比重新训练；这对线上需要动态调整
  TTFT 和内存的推荐 / Agent 系统非常实用，可以一次训练，推理时按需调整 K。

  - 工程实现上，将 per-key gate bias 融合进 FlashAttention 内核、剪枝后 forward 用 CUDA graph 固定 padding、KV
  cache 选择性裁剪等做法可直接复用到自研推理引擎，降低集成成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Transformer 处理长上下文（代码库、长文档、个性化用户数据）时，所有层处理所有 token，导致 prefill 注意力计算 O(N²)、KV cache O(N)，成为 LLM 服务的核心瓶颈。人类专家阅读会略读关键信息，但模型全量读取。现有训练无关 token pruning 方法（如 FastKV、SlimInfer）基于启发式评分，加速有限且精度易损失；架构修改方案则需从头预训练，难以适配已有模型。

## 方法关键点
- **TokenGate 组件**：在指定层 L 插入 gate module，包含 scoring network（一个小 MLP 对 normalized post-attention residual 打分，RMSNorm 归一化）和 top-K selector；低于 L 层标准 forward，gate 层选出 top-K 个 prunable tokens（非 prunable tokens 如问题、答案强制保留），高于 L 层只处理保留 tokens。
- **token-gated attention**：将 gate 值（softmax 后重要性分数）乘以 attention logits 重新加权，解决 top-K 不可微问题，让 scoring network 通过 attention 获得梯度，类似 MoE 门控思想。引入 head-wise scaling（可学习增益）和 temperature scaling（长度泛化）两个改进。
- **训练**：使用标准 next-token prediction loss，无需辅助损失；LoRA 微调 backbone + gate 参数；训练时 dual budget sampling：全量上下文和 log-uniform 采样的剪枝预算各占一半损失，共享底层 forward 计算图，训练开销低。
- **推理优化**：定制 FlashAttention kernel 支持 per-key bias，剪枝后 forward 用 CUDA graph，KV cache 可选择性裁剪。

## 关键实验
在 Qwen3-1.7B 上，覆盖代码补全（RepoBench-P）、多跳 QA（2WikiMultihopQA）、摘要（MultiNews）、医学抽取（BioDEX）、大海捞针（NIAH）等任务。相对 fine-tuned full-context baseline，TokenGate 实现 TTFT 加速 1.4–11.3x，峰值内存降低 1.5–3.4x，精度无下降；相比最佳训练无关 baseline（FastKV 等），TTFT 最高 6.4x 加速，内存最高 2x 降低。在 hybrid attention 模型 Qwen3.5-2B 上，NIAH 32K 任务 Layer 3 处 3.8x TTFT 降低且精度不失，优于 FastKV 2.1x。训练效率方面，每步慢 1.3x 但收敛步数减少，总体训练时间与标准 LoRA 微调相当或更低。

最值得记住的一句话：通过类似 MoE 的门控值注入 attention logits，把不可微 top-K token pruning 变成可端到端训练的组件，在不损失精度下大幅加速长上下文预填充。
