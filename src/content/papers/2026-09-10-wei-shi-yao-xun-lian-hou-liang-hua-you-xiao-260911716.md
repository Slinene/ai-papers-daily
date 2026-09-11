---
title: Why Does Post-Training Quantization Work?
title_zh: 为什么训练后量化有效？
authors:
- Yuxiang Chen
- Michael Beyer
- Jun Zhu
- Jianfei Chen
affiliations:
- Tsinghua University
- Bosch AI Research
arxiv_id: '2609.11716'
url: https://arxiv.org/abs/2609.11716
pdf_url: https://arxiv.org/pdf/2609.11716
published: '2026-09-10'
collected: '2026-09-11'
category: LLM
direction: LLM 量化鲁棒性机制
tags:
- PTQ
- Quantization
- LLM
- Error Propagation
- Counteraction
- LM-head geometry
one_liner: 发现预训练模型量化鲁棒性源于层间误差抵消与 LM-head 几何对高排名 token 的优先保留，解释 PTQ 为何有效。
practical_value: '- 在电商搜索/推荐中部署 LLM 做 query 理解、候选生成或 Agent 决策时，4-bit weight-only 量化（如
  NVFP4 RTN）能基本保持 top-k 预测稳定（Ret@10/20≈85%），可直接采用低精度推理节省成本，不必担心高排名候选被破坏。

  - 量化误差在层间存在“抵消”效应，说明常规 PTQ 校准并非每层都需要精细调整；可以优先关注输出层和 LM-head 对准，而非逐层最小化隐藏状态误差。

  - 若业务依赖长尾 token（例如 niche 品类词、冷门 Semantic ID），需注意量化对低排名 token 的概率扰动更大，建议对长尾候选单独评估或保持关键生成路径高精度。

  - 对于需要高一致性的 Agent 多步推理，量化后 top-1 翻转率约 8-13%，仍有风险；在关键决策步骤可采用混合精度或保留 LM-head 及关键层为
  BF16。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：后训练量化（PTQ）把 LLM 权重存为低精度，每层误差理论上会随深度累积；但直接 NVFP4 round Qwen3-32B 只掉 0.43 个百分点精度，且随机初始化模型在相同权重重建误差下隐藏误差大 5.5 倍，说明预训练本身带来鲁棒性。本文问：为什么 PTQ 有效？

**方法关键点**：
- 在同一输入前缀下对比 BF16 与量化模型，逐层追踪隐藏状态差异 Δh。
- 推导平方误差递归，分解为 block-update error、输入-更新交互项 T_inter、residual-norm 对齐项 T_align。
- 发现预训练模型中层间误差呈负交互：新引入的 block-update error 倾向与继承误差方向相反，产生抵消（counteraction），显著减缓误差增长。
- 通过干预实验（removal 和 reversal）验证 counteraction 的因果作用。
- 进一步分解最终隐藏误差，发现主要是旋转而非长度变化；LM-head 高维几何对旋转有强衰减，且高排名 token 与 h_LM 夹角更小，导致其分数和概率更稳定。

**关键结果**：
- Qwen3-32B NVFP4 RTN 六基准平均精度降 0.43pp；预训练最终相对隐藏误差约 0.15。
- Counteraction 抵消 T_add 的 63.4%，加 T_align 共抵消 81.8%；随机初始化几乎无抵消。
- 干预移除/反转 counteraction 使相对隐藏误差增大 2.94x / 8.41x。
- 最终 LM-head 输入旋转约 12.5°，但词汇平均投影角变化仅 0.159°，衰减 78.6x。
- 高排名 token 分数和 log-prob 变化更小；Flip@1 约 8.3-12.7%，Ret@10/20 均约 85%。

**最值得记住**：预训练残差层会主动抵消量化误差，LM-head 几何进一步保护高置信预测。
