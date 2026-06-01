---
title: Inference-Free Multimodal Learned Sparse Retrieval for Production-Scale Visual
  Document Search
title_zh: 面向生产级视觉文档搜索的免推断多模态稀疏检索
authors:
- Gyu-Hwung Cho
- Youngjune Lee
- Kiyoon Jeong
- Siyoung Lee
- Sanggyu Han
- Hervé Dejean
- Stéphane Clinchant
- Seung-won Hwang
affiliations:
- NAVER Corp.
- Seoul National University
- Naver Labs Europe
arxiv_id: '2605.30917'
url: https://arxiv.org/abs/2605.30917
pdf_url: https://arxiv.org/pdf/2605.30917
published: '2026-05-29'
collected: '2026-06-01'
category: RecSys
direction: 多模态稀疏检索 · 视觉文档搜索
tags:
- sparse retrieval
- visual document retrieval
- SPLADE
- caption-gated supervision
- lexical grounding
- inference-free
one_liner: 提出 caption-gated token supervision 解决视觉稀疏检索的词汇接地问题，使 V-SPLADE 在无神经查询编码下直接索引图文
practical_value: '- **训练技巧可复用**：caption-gated token supervision 利用 VLM 生成的 caption
  来强化视觉稀疏表示中关键词汇维度的激活，这一思路可直接迁移到电商商品图片搜索，用商品描述或属性文案作为 caption 监督训练视觉-词汇对齐。

  - **架构选择务实**：采用 ModernVBERT 骨干 + SPLADE 风格的 LM head 投影 + Li-LSR 令牌查找，查询侧完全免去神经网络编码，部署时仅需倒排索引，这个设计组合适合工业界追求低延迟、高吞吐的检索场景。

  - **互补性融合策略**：稀疏表征与密集检索（如 ColModernVBERT）或 OCR BM25 进行相对分数融合（RSF）后，平均 NDCG@5 可从
  60.1 提升至 64.5，电商搜索中可将视觉稀疏检索作为辅助信号低成本融入已有 pipeline。

  - **工程实现启示**：用训练时 gating 规避推理时的依赖，且文档编码速度比 OCR 和 caption 生成快 20 倍以上，适合大规模语料冷启动，对需要同时索引图文和产品的电商搜索系统有直接参考价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：大规模视觉文档检索（如 arXiv 论文、企业 PDF）缺少一种可直接索引图像、查询时无需神经编码的高效词汇检索器。现有方案要么依赖 VLM 密集检索（需查询编码），要么基于 OCR/caption 的 BM25（文本提取耗时）。多模态学习稀疏检索（MMLSR）天然适合该场景，但因视觉页面缺乏明确词汇锚点，存在“词汇接地”问题——即模型难以将像素中的文字信息准确映射到词汇表维度，导致稀疏表示质量差。

**方法关键点**
- **V-SPLADE 架构**：基于 SPLADE 的稀疏检索框架，使用 ModernVBERT（~250M）视觉语言骨干，对页面图像经 LM head 得到词汇空间稀疏向量（max pooling + ReLU + log1p）；查询侧采用 Li-LSR 风格的令牌查找表（softplus 激活），完全免除神经网络编码，仅需倒排索引。
- **Caption-gated token supervision**：训练时利用 VLM 离线生成的描述作为词汇监督。图像和 caption 分别编码到同一稀疏空间，计算两者的元素积门控系数，经温度缩放后作为损失权重，增强图像侧中与 caption 一致的词汇维度，弥补视觉输入的词汇缺失。
- **训练目标**：由图像-查询排名损失、caption-查询排名损失、caption-gated 交叉熵损失和 FLOPS 稀疏正则化共同组成，caption 分支仅训练时使用。

**关键实验与结果**
- 在 6 个视觉文档基准（ViDoRe v1/v2/v3、VisRAG、VisDoc OOD、IRPAPERS）上，V-SPLADE 质量版平均 NDCG@5 达 60.1，比同规模密集基线 BiModernVBERT（46.3）提升 13.8pp，比 OCR-BM25（54.4）和 caption-BM25（53.8）分别高 5.7、6.3pp。
- 在 1870 万页大规模语料上，R@5 达到 0.228，是同等密集检索器（0.090）的 2.5 倍；查询子集分析显示，在包含数字或大写字母的词汇密集型查询上增益更大（最高 0.363 vs 0.135）。
- 效率方面：文档编码吞吐 20.19 页/秒，是 caption 生成或 OCR 的 20 倍以上；两阶段稀疏检索在 20 线程 CPU 上可达 0.45 ms/查询，不需 GPU 查询编码。
- 融合实验表明 V-SPLADE 可与密集检索互补，通过分数融合将密集模型 R@5 提升 1.6–2.4pp。

**最值得记住的结论**：caption-gated token supervision 仅用于训练，却能显著修复视觉稀疏检索的词汇接地缺陷，使模型在推理时完全摆脱对文本提取和查询神经编码的依赖，性能超越同规模密集基线，并具备天然的可融合性和规模鲁棒性。
