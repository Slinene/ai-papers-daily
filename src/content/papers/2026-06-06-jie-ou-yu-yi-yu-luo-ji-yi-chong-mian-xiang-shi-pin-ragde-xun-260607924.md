---
title: 'Decoupling Semantics and Logic: A Training-Free Coarse-to-Fine Pipeline for
  Video Retrieval-Augmented Generation'
title_zh: 解耦语义与逻辑：一种面向视频RAG的免训练由粗到精流水线
authors:
- Jiaxin Dai
- Zehang Wei
- Jiamin Yan
- Xiang Xiang
affiliations:
- Huazhong University of Science and Technology
arxiv_id: '2606.07924'
url: https://arxiv.org/abs/2606.07924
pdf_url: https://arxiv.org/pdf/2606.07924
published: '2026-06-06'
collected: '2026-06-15'
category: RAG
direction: 视频RAG · 免训练粗精检索与生成
tags:
- Video RAG
- Training-Free
- Coarse-to-Fine
- Multimodal
- Persona Adherence
- LLM Agent
one_liner: 提出免训练两阶段Video RAG方案：粗召回用纯视觉/文本摘要避免噪声模态，细粒度推理过滤用LLM实现逻辑对齐与persona遵守
practical_value: '面向电商/Agent/生成式推荐从业者，可借鉴的工程化落地点：

  - **两阶段解耦范式**：将检索拆分为语义召回与逻辑重排序，召回时主动隔离ASR/OCR等噪声模态（仅用视觉摘要和全局文本），保持向量空间纯净，避免低质量信号污染；在推理阶段再引入全模态，适合多模态内容理解时对抗噪声。

  - **LLM作为自适应过滤Agent**：用商业LLM实现迭代推理式重排序，显式检查候选项与用户persona的逻辑一致性，可迁移到对话式推荐或query改写中，用于剪枝语义相似但意图不符的候选item/query。

  - **Prompt Sculpting强约束生成**：通过prompt工程迫使生成器输出结构化JSON并带精确来源引用，保证可追溯性；在电商场景中可用于从多源视频/直播/评论中生成规范化的商品摘要或问答，降低幻觉。

  - **全免训练方案**：不依赖标注数据进行微调，适合快速业务验证和资源受限环境，可直接复用现有视觉/文本编码器和LLM。'
score: 8
source: arxiv-cs.MM
depth: abstract
---

**动机**：视频RAG面临跨语言长视频理解、严格persona遵守和零幻觉时间定位的挑战。现有方法在多模态噪声（OCR、ASR等）下易产生语义漂移，且难以在检索阶段兼顾逻辑一致性。

**方法**：提出一种免训练的级联流水线，解耦语义与逻辑。第一阶段高召回语义预取：仅使用高保真视觉摘要（如关键帧）和全局文本描述进行密集检索，显式隔离OCR/ASR等噪声模态，维护纯净向量空间，保证召回率。第二阶段A.I.R.（Adaptive, Iterative, Reasoning-based）过滤Agent：由商用LLM驱动，重新引入全模态上下文，执行细粒度认知重排序，强制候选项与用户persona的逻辑对齐，有效剪除语义相似但逻辑无关的结果。最后，Prompt Sculpting机制约束生成器将蒸馏子集合成为严格JSON格式，并附带精确块级引用。

**结果**：在MAGMaR RAG track上取得优异精度，验证了资源友好型方案在信息检索和persona条件生成上的有效性。
