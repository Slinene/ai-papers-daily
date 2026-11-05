---
title: 'Dory1.0-4B: A Looped Normalized-GPT'
title_zh: Dory1.0-4B：循环归一化 GPT 实现弹性深度推理
authors:
- Maxim Fishman
- Simeng Sun
- Shantanu Acharya
- Faisal Ladhak
- Brian Chmiel
- Santiago Akle Serano
- Ron Banner
- Boris Ginsburg
- Krishna C. Puvvada
affiliations:
- Nemotron Labs
arxiv_id: '2611.03998'
url: https://arxiv.org/abs/2611.03998
pdf_url: https://arxiv.org/pdf/2611.03998
published: '2026-11-01'
collected: '2026-11-05'
category: LLM
direction: 循环 Transformer · 测试时计算扩展
tags:
- looped LLM
- latent recurrent
- test-time compute
- nGPT
- KV cache
- RLVR
one_liner: 4B 循环 latent 模型，同一 checkpoint 可变循环次数，用隐空间计算替代长 token 提升 agentic/长上下文效率。
practical_value: '- 在搜索/推荐 Agent 服务中，可将「更长 CoT 输出」替换为 shared recurrent block 的隐空间循环：用
  4 loops 生成 token 数比 1 loop 少 1.3-2.5×，同时保持或提升成功率；适合线上低延迟、低 KV cache 成本场景。

  - KV cache 只保留 last loop，让循环模型显存占用与普通非循环模型相同，便于在长上下文 rerank、搜索摘要、会话式推荐等生成任务中引入循环计算而不显著增加部署成本。

  - 难度感知 loop curriculum 可以直接借鉴：把请求/会话难度特征或 reward 信号作为路由条件，按 query 难度动态决定 loop 深度或
  CoT 长度，避免所有流量统一最大计算预算。

  - 训练侧 NVFP4 低精度预训练 + 多量化 checkpoint（BF16/MXFP8/NVFP4/GGUF）提供弹性部署选项，适合电商大促等算力波动场景。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：测试时计算扩展主要消耗在 token 空间，生成更长推理轨迹会同时推高延迟、KV-cache 与 serving 成本；循环（latent-recurrent）模型提供了一条互补的扩展轴——重复共享层、在隐空间增加每 token 计算而无需增加参数。

**方法关键点**：Dory1.0-4B 基于 normalized Transformer（nGPT），交替使用 sliding-window 与 full-attention 层，结构拆为 input block、shared recurrent block、output block；推理时 recurrent block 可执行不同次数，单一 checkpoint 支持弹性深度。预训练共 6T tokens，前 4.5T 使用 NVFP4，后续扩展上下文到 256K；后训练采用 SFT + RLVR，并用 difficulty-aware loop curriculum 把更难 prompt 路由到更深循环。KV cache 只缓存上一个 loop，保持显存与非循环模型一致。

**关键结果**：增加 loop 数稳定提升准确率，coding、agentic、long-context 收益最大；2 个及以上 loop 时，在 12 个 benchmark 平均上超过 Qwen3.5-9B、Gemma 4 12B、Gemma 4 26B-A4B；4 loops 在 agentic benchmark 上生成 token 比 1 loop 少 1.3-2.5×，而额外算力花在 latent space。
