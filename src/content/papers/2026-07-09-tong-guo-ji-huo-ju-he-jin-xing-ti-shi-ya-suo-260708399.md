---
title: Prompt Compression via Activation Aggregation
title_zh: 通过激活聚合进行提示压缩
authors:
- Thibaud Ardoin
- Semira Einsele
- Evis Bregu
- Gerhard Wunder
affiliations:
- Freie Universität Berlin
arxiv_id: '2607.08399'
url: https://arxiv.org/abs/2607.08399
pdf_url: https://arxiv.org/pdf/2607.08399
published: '2026-07-09'
collected: '2026-07-11'
category: LLM
direction: LLM 推理效率 · 激活压缩与重用
tags:
- prompt compression
- activation aggregation
- LLM inference
- efficiency
- cross-layer injection
one_liner: 将固定指令提示压缩为单个激活向量并注入 LLM 早期层，准确率下降小于 2%
practical_value: '- 在电商搜索、推荐场景中，常用固定指令模板（如意图分类、商品属性抽取）可预计算压缩向量，跳过重复的 token 处理，显著降低线上推理延迟与计算成本。

  - 多步 Agent 系统若共享同一系统提示，可将其压缩后注入各子任务，加速整体响应。

  - 压缩器训练离线完成，不影响在线推理，且 patch 维度可调，便于在精度与效率之间做工程权衡。

  - 方法依赖对目标 LLM 中间层激活的加权求和，需冻结模型并在特定任务上微调压缩器，适合指令固定、调用量大的场景。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：大模型推理中，重复的提示前缀（系统指令、few-shot 示例）每次请求都需重新编码，浪费计算。现有 KV cache 仅缓存已生成 tokens，无法省略前缀的前向计算。本文探索是否可将固定提示压缩为单个激活向量，直接注入模型以替换原 token 序列。

**方法**：提出三步框架：①从冻结 LLM 的中间层提取所有 token 的隐藏状态；②学习一个加权和，将其压缩为一个 “patch” 向量；③将该向量注入到同一 LLM 的早期层（替换原提示 token 的键值对）。压缩器通过训练最小化任务性能损失，可适应不同任务。

**关键结果**：在多种基准上，压缩向量仅带来不到 2% 的准确率下降，同时大幅减少每个查询的计算量。分析表明：中层表示可有效迁移到早期层，单个向量编码了可量化的语义信息，加权和是鲁棒的压缩表示。
