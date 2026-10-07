---
title: 'TRACE: Rollout-Guided Quantization-Aware Training for FP4 Reinforcement Learning
  of MoE Language Models'
title_zh: Rollout 引导的 MoE LLM 强化学习 FP4 量化感知训练框架
authors:
- Xin Wang
- Hao Yu
- Zhengyang Zhuge
- Bochao Mao
- Zheng Li
- Junda Feng
- Yuyan Luo
- Yi Zhang
- Yizhong Cao
- Mi Zhang
affiliations:
- Alibaba Token Hub, Alibaba Group
- Ohio State University
arxiv_id: '2610.07767'
url: https://arxiv.org/abs/2610.07767
pdf_url: https://arxiv.org/pdf/2610.07767
published: '2026-10-05'
collected: '2026-10-07'
category: Training
direction: 低精度 rollout 加速 MoE LLM 强化学习训练
tags:
- FP4
- Quantization-Aware Training
- MoE
- Reinforcement Learning
- KV Cache
- Efficient Training
one_liner: 提出 TRACE，通过 rollout 侧量化结果引导训练侧 FP4 舍入，实现 FP4 rollout 与 BF16 性能相当并最高加速 5.4
  倍
practical_value: '- 在 RL 调 LLM 推荐/搜索 Agent 或生成式 ranker 时，rollout 阶段是主要算力瓶颈，可尝试 FP4
  权重/激活 + FP4 KV cache 联合做 rollout；TRACE 表明可与 BF16 rollout 获得相近的最终策略质量。

  - 避免直接用离线 PTQ 量化 BF16 训练好的策略：把 rollout 侧实际量化噪声（舍入结果、scale）作为监督信号引入训练侧 QAT，能显著改善最终
  FP4 策略性能，比事后量化更可靠。

  - 工程上可借鉴 selective quantization-info caching：只缓存深层 mantissa/scale，降低多 GPU 或分布式 rollout
  worker 间的存储与通信开销，对 MoE 或超大 LLM 生成服务有直接参考。

  - 低精度 rollout 最高 5.4 倍加速意味着相同算力下可大幅增加采样轨迹数量，适合需要大量探索的 query 推荐、对话式推荐 Agent 等 RL
  训练场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
LLM 强化学习后训练在 rollout 阶段产生大量长轨迹，计算与内存开销高，低精度 rollout 是有效的加速思路。但现有 FP4 RL 方法分别优化训练和 rollout 路径的量化精度，没有直接缩小两者执行差异，容易造成 train-rollout 不一致，影响策略质量。

**方法关键点**
TRACE 面向 MoE LLM 的 FP4 RL 训练设计：采用 rollout-guided quantization-aware training，利用 rollout 侧量化输出（舍入结果、scale 等）引导训练侧 FP4 舍入决策，直接对齐两条量化路径；同时提出 efficient quantization-information caching，选择性保留更深层的 mantissa 和 scale 信息，减少 rollout guidance 带来的存储与通信开销。支持 FP4 权重/激活与 FP4 KV cache 联合 rollout。

**关键结果**
在 4 个大规模 MoE LLM、覆盖 reasoning/coding/long-horizon RL 任务上，TRACE 的 FP4 rollout 与 BF16 rollout 的 RL 性能相当，rollout 加速最高 5.4 倍；最终 FP4 策略性能优于对 BF16 训练策略做事后 FP4 量化。
