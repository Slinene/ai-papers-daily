---
title: 'Quantization-Aware Healing: A Practical Recipe for Recovering Compressed,
  4-Bit LLMs'
title_zh: 量化感知修复：恢复压缩4位大模型的实用方法
authors:
- Bakbergen Ryskulov
- Iker García-Ferrero
- David Montero
- David Jansen
- Ali Hashemi
- Jezabel R. Garcia
- Antonio Tiene
- Román Orús
affiliations:
- Multiverse Computing
arxiv_id: '2608.20953'
url: https://arxiv.org/abs/2608.20953
pdf_url: https://arxiv.org/pdf/2608.20953
published: '2026-08-21'
collected: '2026-08-24'
category: Training
direction: LLM 压缩量化与蒸馏修复
tags:
- Quantization-Aware Healing
- QAT
- 4-bit quantization
- MXFP4
- distillation
- LLM compression
one_liner: 提出 Quantization-Aware Healing (QAH)，从原始未压缩模型直接蒸馏到4-bit量化学生，比 QAT 更快更稳，并开源
  Hypernova-60B
practical_value: '- **部署压缩大模型时，直接采用 QAH 蒸馏代替传统 QAT 恢复流程**：在结构压缩+量化后，从原始未压缩模型蒸馏到量化学生，而非从
  bfloat16 压缩中间模型蒸馏或 QAT 重训，可显著加速收敛（约7倍）并避免峰值后崩溃，减少手动早停的调参成本。

  - **适用于电商/Agent 中需要低成本 LLM 推理的场景**：例如用压缩量化后的 LLM 做 query 推荐、对话生成或商品文案，QAH 能保持与更大模型相近的质量，同时降低
  4 倍权重内存和一半参数量，适合线上部署。

  - **注意分布式训练后端对质量的影响**：工程实现时需固定并验证后端（如 PyTorch FSDP、DeepSpeed 等），该论文报告了后端差异导致的可复现性差距，建议在训练压缩模型时对比后端并固定配置。

  - **如果追求快速低成本恢复压缩模型，可以优先尝试蒸馏而非硬标签 QAT**：QAH 对超参不敏感，不需要多周搜索，适合业务中快速迭代模型压缩版本。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：大模型部署需同时采用结构化压缩和4-bit量化，但两者叠加会严重损害推理、数学、代码和长上下文能力，需在部署前进行恢复训练。默认 QAT 在压缩管线上收敛慢且训练峰值后性能崩塌。

**方法关键点**：提出 Quantization-Aware Healing (QAH)，核心观察是结构压缩后的 bfloat16 模型从未单独训练过，只是蒸馏得到的近似，因此 QAH 直接让4-bit量化学生从原始未压缩教师模型蒸馏，绕过 bfloat16 中间状态。在 GPT-OSS 120B→60B→MXFP4 管线上实施，并报告了分布式训练后端对质量的影响。

**关键结果**：QAH 学生在9个基准中有7个匹配或超过其 bfloat16 源模型，权重内存约为4倍降低，参数量减半。与匹配的 QAT 基线相比，达到可比峰值约快7倍，且无需手工早停即可保持稳定。模型开源为 Hypernova-60B。
