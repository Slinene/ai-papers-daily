---
title: 'NeoMME: A Single-Tower Multimodal-Native Multilingual Foundation Encoder for
  Efficient Fine-Tuning and Inference'
title_zh: NeoMME：单塔多模态多语言基础编码器，用于高效微调与推理
authors:
- Aurélien Lac
- Tony Wu
affiliations:
- H Company
arxiv_id: '2609.01657'
url: https://arxiv.org/abs/2609.01657
pdf_url: https://arxiv.org/pdf/2609.01657
published: '2026-08-30'
collected: '2026-09-05'
category: Multimodal
direction: 多模态原生单塔编码器与视觉文档检索
tags:
- Multimodal Encoder
- Single-Tower
- Vision-Document Retrieval
- Late Interaction
- Quantization
- Multilingual
one_liner: 提出单塔多模态多语言编码器，用掩码离散扩散预训练，视觉文档检索精度高且吞吐翻倍
practical_value: '- 在电商商品图文检索/视觉搜索中，可以尝试用单塔多模态编码器（图像 patchify + 2层MLP 与文本 token 一起输入
  bidirectional Transformer）替代双塔或 VLM 编码器，降低推理延迟和参数规模；NeoMME-260M 在同尺寸下吞吐约为 ColModernVBERT
  2x，适合对实时性有要求的召回/粗排。

  - 联合训练 dense 和 late-interaction heads，并在索引侧使用层级 token pooling + 非对称量化，可将多模态文档 embedding
  压缩 255x 且保留 >95% nDCG@10；该思路可直接迁移到海量商品/广告素材库的向量存储成本优化。

  - 多语言原生训练 + 16K 上下文，适合跨境业务中多语言商品标题/详情页与查询的匹配，无需为每种语言单独建塔；也支持编码两张 4K 图，能处理长图文详情页。

  - 如果业务已用 ColPali/Qwen-VL 做视觉文档 RAG，可评估用该开源编码器作为更轻量的检索底座，减少 VLM 在非生成式检索任务上的额外开销。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有多模态模型多基于生成式 VLM，视觉文档检索器（如 ColPali）沿用这些 VLM 架构，带来参数和计算开销，而检索任务本身不需要生成能力。

方法关键点：NeoMME 提供 260M 和 800M 参数版本，采用单一双向 Transformer 同时处理多语言文本和原始图像 patch，图像经 patchify 和 2 层 MLP 投影，无需独立的预训练视觉塔或因果解码器。预训练从零开始使用 masked discrete-diffusion 文本目标，以可见图像 patch 为条件；支持 16,384 token 上下文，可编码两张 4K UHD 图像。下游微调时联合训练 dense 和 late-interaction heads。

关键结果：在 ViDoRe v3 基准上，NeoMME-Retriever 260M 以 0.523 nDCG@10 超过所有低于 800M 的模型，800M 达到 0.556。在 L40S 上匹配 2048×2048 输入时，260M 吞吐约为 ColModernVBERT 的 2 倍。层级 token pooling 和非对称量化将 late-interaction 文档嵌入压缩 255 倍，并保留超过 95% 基线 nDCG@10。
