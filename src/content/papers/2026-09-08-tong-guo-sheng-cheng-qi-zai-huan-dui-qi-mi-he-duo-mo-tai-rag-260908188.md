---
title: Bridging the Semantic-Utility Gap in Multimodal RAG via Generator-in-the-Loop
  Alignment
title_zh: 通过生成器在环对齐弥合多模态 RAG 中的语义-效用差距
authors:
- Zhan-Lun Chang
- Dong-Jun Han
- Seyyedali Hosseinalipour
- Mung Chiang
- Christopher G. Brinton
arxiv_id: '2609.08188'
url: https://arxiv.org/abs/2609.08188
pdf_url: https://arxiv.org/pdf/2609.08188
published: '2026-09-08'
collected: '2026-09-09'
category: RAG
direction: 多模态 RAG · 检索对齐
tags:
- Multimodal RAG
- Generator-in-the-loop
- Preference Alignment
- Cross-encoder Reranker
- LoRA
- VLM
one_liner: 两阶段生成器在环框架，用 VLM 生成假设文本并基于答案反馈微调 reranker，弥合多模态 RAG 语义相似与生成效用差距
practical_value: '- 检索/排序目标再对齐：现有向量召回和相关性模型常优化语义相似度，但业务目标可能是点击、转化或生成质量。可用生成器/模型反馈自动构造偏好对，比如候选商品描述是否能辅助生成正确推荐理由或回答，无需人工标注，降低标注成本。

  - 跨模态 query 桥接：电商中图片搜索、图文推荐可先让 VLM 根据图像和用户 query 生成“假设文本”（如商品属性、风格描述），再用该文本做 dense
  retrieval，缓解模态 gap，提升召回精度。

  - 低成本 reranker 微调：用 LoRA 微调 cross-encoder reranker，并支持 triplet/DPO/SFT 多种损失，方便在现有排序服务上快速实验。同时可周期性重新挖掘偏好对，随着
  reranker 提升迭代优化。

  - 生成器在环评估：可以直接将下游生成任务的表现（如推荐理由吸引力、答案正确性）作为排序信号，而不是只看排序指标 NDCG；在线实验时监控最终业务指标，更贴近业务价值。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多模态 VLM+RAG 中，标准检索和 reranker 优化语义相似度而非答案效用，导致检索到的文档看似相关但无助于生成正确答案，存在 preference gap；人工标注文档级相关性成本高。

**方法关键点**：提出两阶段生成器在环对齐。阶段1：冻住的 VLM 根据图像-query 生成假设文本，用作 dense text search 的检索 query，桥接图像到文本模态差距。阶段2：用冻住的 VLM 挖掘答案监督偏好对——候选文档作为上下文时 VLM 能生成正确答案则为正样本，否则负样本——然后用 LoRA 微调 cross-encoder reranker；偏好信号可搭配 triplet loss、pairwise DPO 或 SFT；支持周期性重新挖掘偏好对以跟上 reranker 改进。

**关键结果**：在 VQA-X 和 A-OKVQA 上，用 Qwen3.5-2B 和 Qwen3-VL-4B-Instruct 实验，框架在多种对齐损失和 pool size 设置下均优于 rank-order、random 和 REPLUG-style likelihood 基线，说明答案级生成器反馈是有效的偏好对齐监督信号。
