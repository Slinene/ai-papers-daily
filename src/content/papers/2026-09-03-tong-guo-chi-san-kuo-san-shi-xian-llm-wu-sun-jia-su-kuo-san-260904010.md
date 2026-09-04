---
title: Unlocking Lossless Speedups in LLMs via Discrete Diffusion
title_zh: 通过离散扩散实现 LLM 无损加速：扩散增强自回归模型
authors:
- Subham Sekhar Sahoo
- Lingjie Chen
- Khiem Pham
- Jonathan Geuter
- Chaitanya Dwivedi
- Varad Pimpalkhute
- Yash Akhauri
- Alexander Moreno
- Mikhail Yurochkin
- Zhenting Wang
affiliations:
- Institute of Foundation Models
- University of Illinois Urbana-Champaign
- Cornell Tech
- Harvard University
- Cerebras Systems
arxiv_id: '2609.04010'
url: https://arxiv.org/abs/2609.04010
pdf_url: https://arxiv.org/pdf/2609.04010
published: '2026-09-03'
collected: '2026-09-04'
category: LLM
direction: 扩散增强 LLM 无损并行解码加速
tags:
- Discrete Diffusion
- Speculative Decoding
- LLM Inference Acceleration
- LoRA
- Diffusion Distillation
- Parallel Decoding
one_liner: 用 LoRA 扩散权重并行 draft + AR rejection 实现无损加速，8B Uno 在吞吐与质量上超过主流 d-LLM 与 speculative
  方法
practical_value: '- 可无损加速现有 LLM serving：为线上 AR 模型（如 Qwen/DeepSeek）添加 rank-128 LoRA
  diffusion adapter，训练只需几 B tokens（公开数据即可），不碰原始权重；与 EAGLE/DFlash 相比共享 KV cache 省显存，高并发
  batch 下仍有 1.5× 以上吞吐，适合电商搜索/广告 agent 高并发调用。

  - 借鉴 gated LoRA + block-causal attention 训练法：单次前向同时算 teacher/student logits，训练 context
  length 约 2×L，不随 block size 增大；L_TV loss 比 DCD 更直接地优化 speculative 接受长度，实际可优先选 α=0,
  β=1 或 L_TV 主导。

  - 评估指标要区分 system throughput vs per-request throughput：batch=1 容易高估加速，业务中 agentic
  多请求并发和 RL rollout 更应看重最大 batch 吞吐；可采用固定 1K input/8K output 的标准化吞吐测试。

  - RL 训练加速：在 SFT 后冻结 diffusion adapter，RL 阶段只更新 AR 权重即可保留约 94% TPF，rollout 加速 40%；推荐/搜索模型若做大规模
  RL 微调，可复用此方案缩短训练时间。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：LLM 的 next-token prediction 造成逐 token 串行解码，latency 高且 memory-bound；现有 speculative decoding 需单独 draft 模型，diffusion LLM 又常牺牲质量，且 batch 大时加速消失，难以满足 agentic 高并发场景。

方法关键点：
- 在同一 causal Transformer 中保留 AR 权重 θ_AR 作为质量与验证分布；新增 diffusion 权重 θ_Δ，以 rank-128 LoRA（α=256）形式附着于每层。
- Diffusion Distillation 阶段冻结 AR 权重，只训 LoRA；对 clean/noisy 序列拼接后做 block-causal attention + gated LoRA，单次前向同时得到 teacher logits（只用 AR）和 student logits（AR+LoRA）。损失为 α L_DCD + β L_TV，L_TV 最小化 diffusion 与 AR 的块级 TV，提升 speculative 接受长度；训练用 block size curriculum。
- Ψ-Spec 采样：diffusion 路径并行 draft 一个 block，AR 路径做 rejection sampling；Linear sampler 优化系统吞吐，Tree sampler 优化 batch=1 请求吞吐；第一个 token 恒被接受，TPF∈[1,(B+1)/2]。
- 可从零训练，也可直接增强开源 AR 模型；diffusion 权重即使在不同数据分布上训练也能保证 lossless。

关键实验：
- 从零训练的 8B Uno 在 agentic tool use/coding/long-context reasoning 超过 26B DiffusionGemma 与闭源 Mercury 2；如 τ2 Telecom 90.1 vs 71，SWE-bench 68.4 vs DiffusionGemma 18.7；系统吞吐 5255 tok/s，显著高于 baselines。
- 在 Qwen3-8B 上增强：比 EAGLE-3/DFlash 更快，最大 batch 下 1.6×、batch=1 下 2.5× 加速，额外参数仅 0.35B，且共享 KV cache。
- RL rollout 阶段冻结 diffusion adapter 仍保留约 94% TPF，端到端 RL 最高 40% 训练加速。

最值得记住的一句话：把 AR 参数与轻量扩散 LoRA 解耦，用 diffusion 并行 draft + AR rejection，能在不牺牲目标分布的前提下获得跨 batch 的 lossless 加速。
