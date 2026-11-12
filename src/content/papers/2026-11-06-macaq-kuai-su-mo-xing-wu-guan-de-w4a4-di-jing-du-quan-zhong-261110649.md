---
title: 'MACaQ: Fast, Model Agnostic Calibrated Quantization for Low-Precision Weights
  and Activations'
title_zh: MACaQ：快速模型无关的 W4A4 低精度权重激活标定量化
authors:
- Lorenz K. Muller
- Philippe Bich
- Chiara Boretti
- Hyun-Min Chang
- Jiawei Zhuang
- Lukas Cavigelli
affiliations:
- Computing Systems Lab, Huawei Technologies, Switzerland
arxiv_id: '2611.10649'
url: https://arxiv.org/abs/2611.10649
pdf_url: https://arxiv.org/pdf/2611.10649
published: '2026-11-06'
collected: '2026-11-12'
category: LLM
direction: LLM 低精度量化 · W4A4
tags:
- quantization
- MXFP4
- W4A4
- Hadamard
- LLM inference
- post-training quantization
one_liner: MACaQ 用逐层块 Hadamard 变换与 Hessian 感知 Flip-Refinement 实现快速 W4A4 量化，推理开销仅 2.3%
practical_value: '- 在 GPU 内存受限的推荐/Agent 系统中部署 LLM 时，可直接采用 MACaQ 的逐层块 Hadamard 在线变换方案：每层激活做
  per-channel scale + block-Hadamard，并把逆变换吸进权重，推理端到端开销仅 2.3%，且不依赖跨层传播，支持流式量化和单层驻留内存。

  - 需要快速量化多个 LLM 版本或做 A/B 实验时，MACaQ 的量化时间优势明显：Llama-3-8B 上以 11 倍少于 DuQuant++/MR-GPTQ
  的时间达到同等 perplexity，适合对大量领域微调模型做快速低精度部署。

  - Flip-Refinement 是一个轻量可复用的模块：用 Hessian 感知的坐标下降，在逐层 FP4 码本里贪心翻转相邻代表值，可以在不改动主量化流程的前提下叠加到已有
  PTQ 管线，进一步压低 perplexity。

  - MACaQ 的 layer-local 设计与模型架构无关，不仅适用于 LLM，也可迁移到商品图像/视频生成等 diffusion 或多模态模型；对 122B
  模型仅需 32.5GB GPU RAM、64 分钟完成量化，适合中小团队资源受限环境。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：权重-激活量化可降低神经网络推理的显存和计算成本，但近期方法往往需要昂贵的优化，以及跨层传播 basis transform 等架构特定改动，部署复杂。

**方法**：MACaQ 是 MXFP4 W4A4 post-training quantization 方法，把每个 linear layer 独立处理。在线对每层激活施加 per-channel scale 和 block-Hadamard transform，同时把对应逆变换吸收到权重中；由于变换在线保留，不产生跨层依赖，实现流式量化，任意时刻只需一层驻留显存。为进一步超越 round-to-nearest，提出 Flip-Refinement：Hessian-aware 坐标下降，贪心地把单个 FP4 code 移动到相邻可表示值。

**结果**：在 vLLM 的 Qwen3-32B 上，相比纯 MXFP4 仅增加 2.3% 端到端推理开销；perplexity 低于 DuQuant++ 和 MR-GPTQ，并且在 Llama-3-8B 上达到同等最优 perplexity 时，量化时间只需前者的 1/11。无需架构特定修改即可用于 image diffusion 模型；122B 参数模型可在 64 分钟内完成量化，仅需 32.5GB GPU RAM。
