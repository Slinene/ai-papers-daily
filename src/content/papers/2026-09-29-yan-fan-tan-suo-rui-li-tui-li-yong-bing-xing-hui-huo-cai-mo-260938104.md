---
title: 'Explore Broadly, Reason Sharply: Push Small Models toward the Frontier via
  Sampling'
title_zh: 广泛探索、锐利推理：用并行回火采样将小模型推向前沿
authors:
- Panagiotis Theodoropoulos
- Nan Jiang
- Xintong Duan
- Ali Hasan
- Yuriy Nevmyvaka
- Evangelos A. Theodorou
- Wei Deng
affiliations:
- Georgia Institute of Technology
- University of Texas at El Paso
- Morgan Stanley
arxiv_id: '2609.38104'
url: https://arxiv.org/abs/2609.38104
pdf_url: https://arxiv.org/pdf/2609.38104
published: '2026-09-29'
collected: '2026-09-30'
category: Reasoning
direction: 推理采样 · parallel tempering
tags:
- power sharpening
- parallel tempering
- MCMC
- inference-time sampling
- LLM reasoning
one_liner: 用并行回火耦合多档功率锐化采样链，解决探索利用矛盾，让小模型无需训练逼近前沿推理
practical_value: '- 商品文案、搜索 query 改写、Agent 多步规划等开放式生成任务，可借鉴 PPT 的探索-利用分工：低 sharpening
  链生成多样候选，高 sharpening 链筛选稳定高质量答案，swap 让好路径快速上传，无需额外训练。

  - 如果线上已缓存 log-probs 和 KV cache，swap 只是交换状态指针，几乎没有额外模型调用；适合叠加到 vLLM/paged attention
  服务，峰值显存约增加 2.5-3.7 倍，按 replica 数可预估。

  - 实现可变长度生成重采样时要注意截断偏差：采用固定 horizon + post-EOS padding，否则短序列会被单方面接受，导致目标分布偏置，直接影响生成质量。

  - 不想上 RL post-training 但需要提升小模型推理能力时，可先试 PPT：不依赖 reward model，也避免 RL 的 jagged generalization；对数学、代码、科学推理等可验证任务尤其有效。ladder
  调参优先用 equi-accepting，避免相邻 swap 接受率出现瓶颈。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

单链 power-sharpened sampling 在推理时按 p0(x)^α 重采样完整序列，能放大模型已有推理路径，无需 reward model 或梯度更新，但面临探索-利用权衡：强 sharpening 会陷入局部合理但错误的轨迹，弱 sharpening 则分布过散。

方法关键点：
- 用 parallel tempering 把 K 条 replica 放到不同 sharpening power α1<...<αK 上；低 α 链充当高温 explorer，高 α 链充当 exploit 链，相邻链通过 Metropolis-Hastings swap 交换完整 completion。
- swap 接受率只依赖两条链的 cached base-model log-prob，几乎零额外模型调用。
- 修正先前 power samplers 的早期截断偏差：用固定 horizon + 后缀补 ⊥，使反向 proposal 始终可算，保证目标分布不变。
- ladder 设计采用 equi-accepting：调中间 α 使相邻 swap 接受率尽量相等，消除通信瓶颈；实际从几何 ladder 初始化再微调。
- 每 stage 先 block extension 到当前 horizon，再做局部后缀重采样，最后执行 ordered adjacent sweep 交换。

关键结果：
在 Qwen3-4B、Qwen3-8B、Qwen3.5-9B 上，覆盖 MATH500、GPQA、HumanEval、GSM8K、AIME 24&25、LiveCodeBench v5。PPT 在全部 15 个模型-基准组合中最佳或并列最佳，超过 Power Sampling、PowerSMC、GRPO 等 baseline；例如 Qwen3-8B 上 MATH500 从 83.9 提到 88.0，AIME 24&25 从 72.7 提到 78.3。Qwen3.5-9B 在 GPQA/AIME/LCB 达 85.9/93.3/84.9，与 GPT-5、Opus 4.5、GLM 4.7 等 frontier 模型可比。计算匹配控制证明增益来自 swap 而非额外计算；swap 时间开销约 0.1%，峰值显存高 2.47-3.73x。

最值得记住的一句话：用极低通信开销的 parallel tempering 串起多温度采样链，可以在不训练、不依赖 reward 的情况下，让小模型推理能力大幅逼近 frontier。
