---
title: Towards Full Pipeline FP8 Reinforcement Learning for LLMs
title_zh: 面向LLM的全流程FP8强化学习训练稳定性优化
authors:
- Fanchao Chen
- Ziheng Jiang
- Ziyun Wei
- Zheng Zhong
- Du Li
- Chi Zhang
- Haibin Lin
- Shivaram Venkataraman
affiliations:
- University of Wisconsin–Madison
- ByteDance Seed
arxiv_id: '2609.22870'
url: https://arxiv.org/abs/2609.22870
pdf_url: https://arxiv.org/pdf/2609.22870
published: '2026-09-18'
collected: '2026-09-23'
category: Training
direction: FP8强化学习训练稳定性优化
tags:
- FP8
- RL
- LLM
- Quantization
- GRPO
- Training Stability
one_liner: 揭示FP8全流程RL中量化噪声扭曲importance ratio导致训练崩溃，提出Calibrated Clipping动态校准剪切界
practical_value: '- 若在电商搜索/推荐Agent或生成式推荐中用FP8做RL微调，除train-inference mismatch外，需重点监控entropy
  surge和输出乱码，这是重要性比被量化噪声扭曲的早期信号。

  - Calibrated Clipping可迁移：在低精度训练时，动态对齐FP8与BF16分布的低位分位数并重新平衡上界，能防止negative-advantage
  tokens梯度被错误零化，适合GRPO/DAPO等常见RL算法。

  - 对生成式推荐或Agent策略优化，FP8全流程加速价值大，但直接套用预训练FP8配置有风险；建议在RL阶段引入基于分位数的动态clipping机制，并监控importance
  ratio分布。

  - 若业务中同时使用多种FP8 scaling granularity，该方法在不同粒度上均有效，可作为通用稳定性补丁。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：RL已成为提升LLM推理与Agent能力的关键手段，FP8量化能显著加速训练，但全流程FP8 RL仍存在训练不稳定问题。现有工作多关注train-inference mismatch，本文发现即使修正该问题，训练中仍会出现熵激增和输出乱码。

**方法关键点**：问题根源在于复合FP8量化噪声会扭曲importance ratio，使负优势token被推离trust region，导致其梯度被错误置零，病理输出无法被惩罚并逐步累积。为此提出Calibrated Clipping，通过匹配低精度FP8与高精度BF16分布的低位clipping分位数，并相应重新平衡上界，动态校准FP8裁剪边界。

**关键结果**：在GRPO与DAPO算法、8B到32B模型规模、多种FP8 scaling粒度上验证，方法成功消除熵激增，恢复至与BF16基线相当的性能。
