---
title: 'Tasklets: A Unit-Test Benchmark for Language Model Architectures'
title_zh: Tasklets：语言模型序列混合层的单元测试基准
authors:
- Zayd Muhammad Kawakibi Zuhri
- Munachiso Samuel Nwadike
- Kentaro Inui
- Alham Fikri Aji
affiliations:
- Mila
- MBZUAI
- RIKEN AIP
- Tohoku University
arxiv_id: '2611.27607'
url: https://arxiv.org/abs/2611.27607
pdf_url: https://arxiv.org/pdf/2611.27607
published: '2026-11-20'
collected: '2026-11-23'
category: Eval
direction: 语言模型架构单元测试与选型
tags:
- benchmark
- sequence-mixing
- architecture
- synthetic tasks
- LLM evaluation
one_liner: 提出统一的小型合成任务基准，评估 LLM 序列混合层的基础计算能力并对比 20+ 架构
practical_value: '- 在引入 Mamba、RetNet、Gated DeltaNet 等新 LLM 骨干到推荐/广告模型前，可先跑 Tasklets
  这类单元测试快速评估序列建模基础能力（recall、state tracking），避免直接上业务大模型试错。

  - 长序列用户行为建模是电商/广告核心，该基准覆盖的 recall、copy、counting 等能力与用户历史建模直接相关，序列层选型时可作为低成本过滤层。

  - 统一任务定义与评估代码，团队内部可沉淀自己的“架构能力清单”来横向对比不同候选层，减少重复实验。

  - 任务偏合成、规模小，无法直接证明线上效果，需结合真实推荐任务微调验证，业务可借鉴点有限。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 中 sequence-mixing 层（如 attention、SSM、线性注意力）的计算能力差异多用合成任务评估，但各研究任务选择、形式与评估不一致，难以横向比较。

**方法关键点**：Tasklets 收集并统一了一批小型合成任务，按能力分组为 Recall、Copy、Memorization、Counting、Stack、Formal languages、State tracking 等，提供共享设置和评估代码。在控制实验条件下训练小模型，对比 20+ 种层类型（PaTH Attention、Transformer、Gated DeltaProduct、DeltaNet、Comba、Samba、RetNet、Mamba 系列、RWKV、HGRN 等）。

**关键结果**：不同架构在基础计算能力上表现差异明显，Softmax attention 类及 PaTH Attention 整体靠前，若干 SSM/线性注意力在部分任务上存在短板；测试成本低，可复现，适用于新架构快速筛选。
