---
title: 'Chaos in the Text: Revealing the Modality Preference in Mixed-Modality Retrievers'
title_zh: 混合模态检索中的模态偏好与 Trident 去偏训练
authors:
- Yubo Sun
- Chunyi Peng
- Yukun Yan
- Zhenghao Liu
- Zhipeng Xu
- Sen Mei
- Linlin Xin
- Zheni Zeng
- Maosong Sun
affiliations:
- University of the Chinese Academy of Sciences
- Northeastern University
- Tsinghua University
- Nanjing University
arxiv_id: '2610.11816'
url: https://arxiv.org/abs/2610.11816
pdf_url: https://arxiv.org/pdf/2610.11816
published: '2026-10-08'
collected: '2026-10-11'
category: Multimodal
direction: 多模态检索 · 模态偏好纠偏
tags:
- modality preference
- dense retrieval
- contrastive learning
- multimodal RAG
- InfoNCE
- text-image fusion
one_liner: 发现文本高分偏置导致无关文本压制相关图像，提出多正视角 Trident 联合优化相关性判别与视角平衡，提升混合模态检索鲁棒性
practical_value: '- 电商/广告多模态商品库常混有文本和图片，可用「文本/图像/融合视图」构造等权正样本，采用 Multi-Positive View
  InfoNCE 抑制文本高分偏置，避免无关文本商品挤掉相关图片商品。

  - 上线前应做模态组成消融：当图片文档被语义对应文本逐步替换时若出现 V 型曲线，说明模型对混合模态敏感；需重点增加文本对抗负例或平衡文本相似度尺度。

  - 对图片文档补充语义等同的文本视图，并把 fused text-image 作为协同正样本训练，能同时提升混合模态与单模态平均检索，适合复用到多模态 RAG/搜索召回或精排。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：多模态语料常同时包含文本、图像和图文融合文档，但现有 dense retriever 在不同模态组成下性能不稳定，尤其文本干扰项会导致相关图像被错误压制。

方法：分析发现「模态偏好」——文本表示获得系统性更高的相似度分数，无关文本比等量无关图像造成更严重退化，称为 Chaos in the Text。为此提出 Trident：为每个文档构造 text、image、fused text-image 三种等权正视角，采用 Multi-Positive View InfoNCE 同时优化相关性判别与正视角平衡，缓解文本偏置。

结果：在视觉文档与自然图像基准上，基于 CLIP 与 VLM 的架构均获得混合模态检索提升，对模态组成和文本干扰的敏感度降低，单模态平均检索性能也提高。
