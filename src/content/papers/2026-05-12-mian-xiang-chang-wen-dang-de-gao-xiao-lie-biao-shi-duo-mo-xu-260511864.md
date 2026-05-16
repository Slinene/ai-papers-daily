---
title: Very Efficient Listwise Multimodal Reranking for Long Documents
title_zh: 面向长文档的高效列表式多模态重排序
authors:
- Yiqun Sun
- Pengfei Wei
- Lawrence B. Hsieh
affiliations:
- Magellan Technology Research Institute (MTRI)
arxiv_id: '2605.11864'
url: https://arxiv.org/abs/2605.11864
pdf_url: https://arxiv.org/pdf/2605.11864
published: '2026-05-12'
collected: '2026-05-16'
category: Multimodal
tags:
- Listwise Reranking
- Multimodal Retrieval
- VLMs
- Document Retrieval
- Token Pruning
- Soft Ranking
one_liner: 提出 ZipRerank，通过两阶段训练和查询感知视觉 token 剪枝与单步 logit 评分，将重排序延迟降低一个数量级
score: 8
source: arxiv-cs.MM
depth: full_pdf
---

## 动机
多模态检索增强生成（M-RAG）和视觉问答等场景需要在长文档中精准重排序。现有基于 VLM 的列表式重排器（如 MM-R5）虽然精度高，但面临两大瓶颈：长视觉 token 序列导致 prefill 代价巨大，以及自回归解码引入高延迟。这使得重排序在实际系统中的部署受限，亟需一种同时兼顾效率和效果的设计。

## 方法关键点
- **两阶段训练策略**：第一阶段在文本重排序数据（RankZephyr）上，将文本渲染为图像进行列表式预训练，使用语言建模损失和 RankNet 损失；第二阶段在多模态 VQA 数据（MMDocIR）上微调，引入强大 VLM 教师（如 GPT‑5‑mini）生成的软排序标签，并采用基于几何衰减的软排序损失，容忍教师排序中的噪声。
- **高效推理机制**：
  - **查询感知视觉 token 剪枝**：在 LLM 处理前缀后提取查询 token 隐藏状态，计算每个图像 token 与查询的余弦相似度，保留 top‑ρ 比例最相关的 token（典型值 0.5），将输入长度大幅缩短，同时复用前缀 KV cache。
  - **单步 logit 评分**：每个候选页面关联一个唯一标识 token（A, B, ...），LLM 仅做一次前向传播，提取这些标识的 logit，按降序排列即得重排序结果，完全消除自回归解码。
- **训练与推理协同**：模型在训练阶段学习按标识 logit 大小排序，推理时直接使用该能力，无需生成任何 token。

## 关键实验
在长文档多模态检索基准 MMDocIR 上，以 DSE 和 ColQwen 为第一阶段检索器，检索 top‑20 候选页面，与 MM‑R5、UniME、LamRA、GPT‑5 等对比。
- ZipRerank 在不同 k 值下均提升第一阶段基线，Recall@3 达到 84.8/84.5（DSE）和 84.9/84.4（ColQwen），略优于 MM‑R5 的 79.1/79.0 和 83.0/82.1。
- 推理延迟仅 0.36 秒（LLM 部分），比 MM‑R5 的 3.82 秒快约 10 倍，比 GPT‑5‑mini 快约 58 倍。
- 在 ViDoRe 英文子集上也获得最佳列表式 NDCG@5，印证泛化性。
- 消融实验证实两阶段训练、软排序损失和单步解码各自带来显著收益，去除第一阶段预训练会使 Recall@1 下降近 2 个点。

## 核心发现
通过深度联合优化训练与推理，ZipRerank 证明了在长文档多模态重排序中，无需自回归生成即可达到顶尖精度，且延迟压缩至十分之一，为延迟敏感的真实系统提供了可行方案。
