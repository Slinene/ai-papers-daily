---
title: 'Complete-SVD: A Functional Norm Approach to Low-Rank LLM Compression'
title_zh: Complete-SVD：一种基于函数范数的低秩 LLM 压缩方法
authors:
- Alper Kalle
- Theo Rudkiewicz
- Mohamed-Oumar Ouerfelli
- Mohamed Tamaazousti
affiliations:
- Université Paris-Saclay, CEA, List
- TAU team, LISN, Université Paris-Saclay, CNRS, Inria
arxiv_id: '2611.26059'
url: https://arxiv.org/abs/2611.26059
pdf_url: https://arxiv.org/pdf/2611.26059
published: '2026-11-19'
collected: '2026-11-21'
category: LLM
direction: LLM 低秩压缩 · 输出感知 SVD
tags:
- Low-Rank Compression
- LLM
- Post-Training
- SVD
- Output-Aware
- Kronecker-Factored
one_liner: 通过最小化 logits 的 L2 距离，将低秩压缩转化为加权 SVD，并用无偏随机探针估计输出侧因子
practical_value: '- 部署大模型做推荐/搜索时，低秩压缩比量化更易保留 dense 计算，Complete-SVD 的输出感知目标（最小化 logits
  L2 距离）比仅重建权重更贴近线上效果，尤其适合打分/生成式推荐模型。

  - 其 Kronecker 分解近似将目标变成加权 SVD，计算高效；输出侧因子用无偏随机探针估计，只做 K 次反向传播，与词表大小、序列长度无关，对商品 ID
  空间大、候选序列长的场景非常友好。

  - 如果压缩后部署用于指令遵循或 Agent 任务（如商品文案、query 改写），优先用 KL-SVD 变体，它在校准集困惑度和下游精度上更好；但跨域（换业务数据）时需重新校准或监控，因为跨语料困惑度可能上升。

  - 工程实现可复用：随机探针估计输出 Fisher 信息矩阵的方法，无需真实标签分布，适合线上没有完整日志时做压缩校准。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：低秩压缩 LLM 权重不仅要逼近原始矩阵，还要保持输入输出行为。现有 output-aware 方法在模型输出层衡量压缩误差，但仅加权观察到的 next token 或预测概率；这里提出均匀加权所有 logit 变化，最小化原始与压缩模型 logits 的 $L_2$ 距离。

**方法关键点**：围绕原始权重线性化网络，结合 Kronecker-factored 近似，把目标转化为加权 SVD，得到闭式解。输出侧因子难以精确计算，使用随机探针无偏估计，每个序列只需 $K$ 次反向传播，成本与词表大小和序列长度无关。此外，将 $L_2$ 距离替换为 KL 散度得到 KL-SVD，使用同一估计框架。

**关键结果**：在 WikiText-2 校准、均匀秩设置下，Complete-SVD 在所有 C4 和 PTB 困惑度指标上最低；在 0.7 压缩比及 LEMS 秩分配下同样最优。KL-SVD 在校准困惑度上多数设置更低、下游精度更高，但跨语料困惑度上升。IFEval 指令遵循精度全程优于最强的先验 output-aware 方法。
