---
title: 'KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache
  Quantization'
title_zh: KV4-RL：INT4 KV Cache 量化加速 RLVR 异步 Rollout
authors:
- Sihwan Park
- Sung-Yub Kim
- Doohyuk Jang
- Eunho Yang
affiliations:
- KAIST
- NAVER Cloud
- AITRICS
arxiv_id: '2610.14448'
url: https://arxiv.org/abs/2610.14448
pdf_url: https://arxiv.org/pdf/2610.14448
published: '2026-10-09'
collected: '2026-10-15'
category: Training
direction: RLVR 训练加速 · KV cache 量化
tags:
- KV cache quantization
- RLVR
- Asynchronous Rollouts
- GRPO
- INT4-INT8
- Training Efficiency
one_liner: 提出 KV4-RL，通过校准无关 INT4 KV 量化与选择性 INT8 保护 attention sinks 和近期上下文，在保持训练质量的同时大幅加速
  RLVR 异步 rollout
practical_value: '- 在使用 GRPO/RLVR 微调电商/搜索领域的推理型 LLM（如 query 改写、生成式推荐）时，可直接引入 KV cache
  量化加速 rollout：长尾生成导致 KV 工作负载集中，KV 量化比权重量化或 weight-activation 量化收益更大。

  - 选择性 INT8 保护策略可迁移到其他量化训练场景：对 attention sinks 和最近若干个 token 保持高精度，能有效缩小采样分布偏移（sampler
  mismatch），避免训练退化，同时保留大部分 INT4 加速。

  - 校准无关的 INT4 KV 量化无需校准数据集，适合 RLVR 异步 rollout 中动态变化的 prompt 和生成长度，工程实现门槛低，可与 token-level
  truncated importance sampling（TIS）结合进一步稳定训练。

  - 若业务中有大规模 LLM 自博弈或在线采样（如用 LLM 生成推荐理由、广告文案），可考虑对 KV cache 采用 INT4 量化，尤其当并发解码使 KV
  成为主要瓶颈时，能显著降低推理成本而不明显损失最终模型质量。'
score: 7
source: huggingface-daily
depth: abstract
---

### 动机
异步 rollout 通过减少长尾生成中的利用率不足来提升 RLVR 效率，但持续并发使 context 处理集中在更少的 decode step，每步 KV 工作负载增加。现有量化方案（weight-only、weight-activation）在这种工作负载下加速有限，而 INT4 KV 量化虽然加速明显，但直接用于 rollout 会损害学习，即使配合 token-level truncated importance sampling（TIS）也不够。

### 方法关键点
- 刻画异步 rollout 下的 KV 集中现象，发现 KV cache 量化在匹配工作负载比较中显著优于其他量化方式。
- 提出 KV4-RL：采用无需校准的 INT4 KV 量化，同时对 attention sinks 和近期上下文进行选择性 INT8 保护。
- 保护有界数量的位置，既减小 sampler mismatch，又保留 INT4 的大部分加速。

### 关键结果
在 Qwen3-8B-Base GRPO 训练 400 迭代中，KV4-RL 相较 BF16 rollout 累计 rollout 加速 1.80 倍，累计完整迭代加速 1.27 倍，最后 50 迭代 rollout 加速达 1.97 倍。在 BF16 评估器下，最终六个基准的平均准确率与 BF16-rollout 训练相差不超过 0.5 个百分点，对 Qwen3-4B-Base 和 Qwen3-8B-Base 均成立。
