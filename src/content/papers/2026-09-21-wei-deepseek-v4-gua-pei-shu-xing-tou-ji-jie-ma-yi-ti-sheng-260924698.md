---
title: Adapting Tree-Structured Speculative Decoding to DeepSeek-V4 for Efficient
  Inference
title_zh: 为 DeepSeek-V4 适配树形投机解码以提升推理效率
authors:
- Changxu Liu
- Zhaogeng Li
affiliations:
- Baige AI Team, Baidu Inc.
- Fudan University
arxiv_id: '2609.24698'
url: https://arxiv.org/abs/2609.24698
pdf_url: https://arxiv.org/pdf/2609.24698
published: '2026-09-21'
collected: '2026-09-22'
category: LLM
direction: LLM 推理优化 · 树形投机解码
tags:
- speculative decoding
- tree-structured speculation
- DeepSeek-V4
- compressed attention
- LLM inference
one_liner: 在 DeepSeek-V4 压缩注意力上实现树形投机解码，通过分支感知验证与状态刷新，吞吐最高提升约 18.5%
practical_value: '- 在开放域低可预测的生成任务（对话式推荐、query 改写、广告文案生成）上，树形投机比线性投机吞吐提升更明显，batch 4
  左右最优；线上可优先在这些场景开启。

  - 若线上模型使用 KV cache 压缩/稀疏注意力，上 tree speculative decoding 不能只加 mask，必须隔离每个分支的压缩状态（scratch
  pad + 接受后刷新），否则会污染持久缓存上下文。

  - 验证预算不是越大越好：研究中 D>6 后吞吐与接受长度脱钩，只涨质量不涨速度；工程上应根据 draft 能力和负载联合调 depth/width。

  - 树形验证与 DSpark 类 draft 提质方案正交，可分开迭代：draft 侧负责候选质量，verify 侧负责分支利用，收益可叠加。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：长上下文 LLM 中自回归解码重复执行 target model 是主要延迟来源。DeepSeek-V4 虽用 CSA/HCA 压缩注意力降低上下文存储和计算，但生成仍是自回归。线性投机只跟单条候选链，早期错误会浪费后续后缀；树形投机保留多条分支，在相同预算下可能提高接受长度。难点在于 DeepSeek-V4 的在线序列级压缩不是独立 per-token KV，分支从共享前缀分叉后会压成不同状态，破坏跨分支一致性。

**方法关键点**：
- 三阶段 speculative forward：draft extend（扩展 accepted prefix 成候选树）、draft decode（按树拓扑计算 draft 表示，复用 FlashMLA/tree attention）、target verify（分支感知因果验证 + accepted path selection）。
- 核心是状态管理：每个候选链的压缩 token、压缩 attention state、中间结果放 scratch pad，不直接写持久 page-based KV cache；接受后沿 accepted path 刷新 token history、KV、CSA/HCA 状态，拒绝分支丢弃。
- 优化细节：C4 和 C128 采用不同刷新节奏，device-side 元数据处理减少 host 开销，CUDA graph 覆盖按树配置有界，接受后若缓存已最新可跳过刷新。
- 集成进 SGLang，与 DSpark 等 draft-side 方案正交。

**关键实验**：DeepSeek-V4-Flash，8 GPU，验证预算 D=5–8，batch 1–64，数据集 GSM8K/MBPP/ShareGPT。同预算对比 top-k=1 线性 vs top-k=2 树。接受长度树全胜：D=5 约 +11%，D=6 +14.4%，D=7 +17.1%，D=8 +18.6% 相对增益；绝对 GSM8K 2.836→3.406 等。吞吐几乎全部配置改善，最高 +18.5%（ShareGPT, s3_k2_d6, bs=4）；但 D=5 接近打平，D≥6~7 后吞吐增益饱和而接受长度仍涨，二者脱钩。增益随 batch 呈倒 U，峰值在 bs≈4，最难预测的 ShareGPT 受益最大。

**最值得记住的一句话**：树形投机的净收益 ≈ 更宽树带来的额外接受 − 分支状态分歧带来的验证开销；后者在压缩注意力范式（如 CSA）下最大，因此当 draft 是瓶颈且验证侧够便宜时，树形投机才最划算。
