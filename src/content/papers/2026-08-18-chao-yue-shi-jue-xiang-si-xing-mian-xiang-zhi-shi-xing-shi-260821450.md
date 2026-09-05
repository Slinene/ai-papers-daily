---
title: 'Beyond Visual Similarity: Entity-Aligned Retrieval for Knowledge-Based Visual
  Question Answering'
title_zh: 超越视觉相似性：面向知识型视觉问答的实体对齐检索
authors:
- Hangrui Xu
- Zhengxian Wu
- Yunyao Yu
- Zhuohong Chen
- Rui Cong
- Xiangwen Deng
- Zhifang Liu
- Peng Jiao
- Haoqian Wang
affiliations:
- Shenzhen International Graduate School, Tsinghua University
- University of Arizona
arxiv_id: '2608.21450'
url: https://arxiv.org/abs/2608.21450
pdf_url: https://arxiv.org/pdf/2608.21450
published: '2026-08-18'
collected: '2026-09-05'
category: RAG
direction: 多模态 RAG · 实体对齐嵌入检索
tags:
- MLLM
- Entity-Aligned Retrieval
- Semantic Distillation
- KB-VQA
- Hard Negative Sampling
one_liner: 提出 KBMR，首个基于 MLLM 的 KB-VQA 嵌入检索器，用实体一致性连续蒸馏实现实体级语义对齐，Recall@1 最高提升 14.7%
practical_value: '- 商品视觉检索可用 MLLM 自回归嵌入替代 CLIP 双编码器，显著区分“视觉相似但实体不同”的商品（如不同品牌同款鞋），降低误召回，适合电商以图搜图/相似商品推荐。

  - 连续实体一致性权重 + 软蒸馏可直接迁移到商品类目/SPU 级对比学习：用判别器生成软标签替代 hard negative 二元标签，缓解用户行为（点击、购买）中的弱监督噪声，改善
  hard negative 采样质量。

  - 在导购 Agent 或商品知识问答中，外部知识检索（商品详情、属性、类目树）可采用实体对齐的 MLLM retriever，对长尾、视觉多变商品的知识命中更稳定，提升最终回答/推荐准确率。

  - 工程实现上，大规模弱监督检索语料（如商家上传图文）可通过类似 semantic discriminator 产出连续一致性权重，再蒸馏到轻量检索模型，兼顾效果与推理成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Knowledge-Based VQA 依赖外部知识检索，但主流 CLIP 双编码器仅优化表面视觉相似，难以应对同概念大视觉差异或视觉相似但实体不同的情况。

**方法**：提出 KBMR，首个基于 MLLM 的嵌入检索器，利用 MLLM 自回归能力将图像映射到保留概念身份的语义空间。针对 Wikipedia 级检索中的噪声监督，引入 MLLM 语义判别器生成连续 entity-consistency 权重，并设计 continuous semantic distillation 目标，实现有效 hard negative sampling 和软监督，突破二元标签限制。

**结果**：KBMR 在多基准上显著超越 CLIP 基线，检索 Recall@1 最高提升 14.7%，端到端 VQA 准确率提升 9.4%，代码已开源。
