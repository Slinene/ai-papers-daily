---
title: 'D3D: Decoupled Diffusion Drafting for Asynchronous Speculative Decoding'
title_zh: D3D：解耦扩散草案的异步投机解码
authors:
- Baoyou Chen
- Ruiqiao Mei
- Guancong Lin
- Tao Song
- Weihao Yuan
- Qun Liu
- Siyu Zhu
affiliations:
- Shanghai Innovation Institute
- Shanghai Academy of AI for Science
- Fudan University
- Nanjing University
- Huawei Technologies Co., Ltd.
arxiv_id: '2611.06425'
url: https://arxiv.org/abs/2611.06425
pdf_url: https://arxiv.org/pdf/2611.06425
published: '2026-11-03'
collected: '2026-11-06'
category: LLM
direction: LLM 推理加速 · 异步投机解码
tags:
- speculative decoding
- diffusion drafter
- asynchronous decoding
- layer pruning
- LLM inference
- Qwen3
one_liner: 提出解耦目标隐藏状态的扩散 drafter，实现异步投机解码，Qwen3-8B/32B 平均加速 5.00/5.71 倍
practical_value: '- 可将 D3D 的异步投机解码思想用于降低在线 LLM 服务延迟：在推荐 Agent 生成解释、对话或 query 时，用独立
  drafter 与目标模型并行，提高吞吐

  - 层剪枝策略可直接借鉴：根据每层对关键指标（如 acceptance length）的影响进行敏感性剪枝，而不是盲目减少 drafter 层数，以极低成本保留性能

  - 对需要高频调用 LLM 生成文案、搜索建议等场景，训练一个轻量 diffusion drafter 可带来数倍加速，且不影响目标模型输出分布

  - 解耦设计避免修改原始模型，适合生产环境快速接入；但需要额外训练 drafter 并管理其与目标模型的交互，适合高调用量、延迟敏感的业务'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在 LLM 推理中，speculative decoding 利用轻量 drafter 生成候选 token，目标模型并行验证。但现有 target-conditioned diffusion drafter 要求每个新块等待目标模型隐藏状态，导致 drafting 和 verification 串行，并行度受限。

**方法**：提出 D3D，一个独立的 diffusion drafter，解除对目标模型隐藏状态的依赖。D3D 结合 blockwise denoising 与辅助自回归监督，在没有目标隐藏状态的情况下仍能生成较长的可接受前缀（accepted prefix）。这种独立性使得 D3D 可以在目标模型验证当前块的同时，一次性打包生成后续多个候选块，实现异步 speculative decoding。为进一步降低打包 drafting 的开销，方法根据各层对 acceptance length 的影响逐步剪枝；在 Qwen3-8B 上移除 36 层中的 5 层后，三个 benchmark 上平均 acceptance length 仍保留 99% 以上。

**结果**：在 7 个 benchmark 上，以 Qwen3-8B 为目标模型，D3D 平均解码加速 5.00 倍；以 Qwen3-32B 为目标模型，平均加速 5.71 倍，均优于 DFlash 的 4.03 倍和 3.67 倍。在 GSM8K 上 Qwen3-32B 达到 7.48 倍加速。代码开源。
