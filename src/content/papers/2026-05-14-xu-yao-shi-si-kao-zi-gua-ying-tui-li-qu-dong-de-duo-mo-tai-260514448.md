---
title: 'Think When Needed: Adaptive Reasoning-Driven Multimodal Embeddings with a
  Dual-LoRA Architecture'
title_zh: 需要时思考：自适应推理驱动的多模态嵌入与双LoRA架构
authors:
- Longxiang Zhang
- Weilong Dai
- Guanghao Zhang
- Hao Jiang
- Pipei Huang
arxiv_id: '2605.14448'
url: https://arxiv.org/abs/2605.14448
pdf_url: https://arxiv.org/pdf/2605.14448
published: '2026-05-14'
collected: '2026-05-16'
category: Multimodal
tags:
- Multimodal
- Embeddings
- LoRA
- Reasoning
- CoT
- Retrieval
one_liner: 提出自适应推理框架，通过双LoRA和路由门动态决定是否生成思维链，实现高效且更优的多模态检索嵌入
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机
多模态大模型（MLLMs）用于生成式检索嵌入时，常引入思维链（CoT）推理提升质量，但现有方法存在两个问题：推理器与嵌入器分离导致参数量翻倍，且对所有输入无差别生成 CoT，简单样本可能被冗余推理误导。

## 方法关键点
- **统一双LoRA架构**：在冻结的共享骨干上分别附加推理和嵌入适配器，接口处梯度解耦，避免联合优化冲突，参数量接近单一模型。
- **自适应推理（Adaptive Think）**：自监督路由门根据输入动态决定是否生成 CoT，跳过不必要推理，减少推理开销并提升检索质量。
- **嵌入引导的强化学习**：以检索性能为奖励信号优化 CoT 生成，超越监督微调。

## 关键结果
在 MMEB-V2 的 78 个任务上达到最强嵌入质量，额外参数仅占骨干的 3-5%，相比全生成模式推理 token 数减少最高 50%。
