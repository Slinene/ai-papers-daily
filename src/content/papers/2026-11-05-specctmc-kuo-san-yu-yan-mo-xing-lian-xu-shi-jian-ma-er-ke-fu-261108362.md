---
title: 'SpecCTMC: Exact Speculative Simulation of Diffusion Language Model Continuous-Time
  Markov Chains'
title_zh: SpecCTMC：扩散语言模型连续时间马尔可夫链的精确推测模拟
authors:
- Siva Rajesh Kasa
- Yasong Dai
- Sumit Negi
- Hongdong Li
arxiv_id: '2611.08362'
url: https://arxiv.org/abs/2611.08362
pdf_url: https://arxiv.org/pdf/2611.08362
published: '2026-11-05'
collected: '2026-11-08'
category: LLM
direction: 扩散语言模型精确推测采样加速
tags:
- diffusion language model
- speculative sampling
- CTMC
- parallel decoding
- inference acceleration
- training-free
one_liner: 训练无关的推测采样器，无需草稿模型即可减少顺序模型评估并精确保持 CTMC 分布
practical_value: '- 在电商场景中需要大量生成商品标题、广告文案、搜索词改写时，可借鉴 SpecCTMC 思路减少 LLM 推理的串行模型调用次数，提升吞吐，且无需训练草稿模型或引入额外参数。

  - 精确保持采样分布的特性适合对质量与合规敏感的业务（如广告法合规文案、品牌信息），避免近似解码带来的语义漂移和分布偏移。

  - 中间状态的并行评估可与现有 KV cache 复用机制结合，在 Agent 多步生成或实时对话场景中降低单步迭代延迟。

  - 相比传统 speculative decoding，该方法不需要 draft model，工程实现更轻量，可直接嵌入现有 diffusion LM 推理流水线。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：Masked diffusion language models 支持并行文本生成，但独立采样多个 token 会破坏依赖关系并改变输出分布；精确的连续时间采样需要逐 token 顺序模型评估，形成串行瓶颈。

**方法关键点**：SpecCTMC 是一种训练无关的推测采样器。它利用先前计算得到的模型预测提出连续的 token 更新，并行评估这些中间状态，再执行精确的接受-修正过程。无需单独的草稿模型。作者证明了 SpecCTMC 能保持底层连续时间马尔可夫链的事件时间、生成顺序和 token 值的联合分布，因此既不引入时间离散化误差，也不引入并行解码带来的额外因子化误差。

**关键结果**：在 LLaDA-8B-Instruct 和 Dream-v0-Instruct-7B 上，跨五个基准测试，SpecCTMC 相比直接连续时间采样将顺序模型评估次数减少 1.73–4.38 倍，同时保持参考采样分布不变。代码已开源。
