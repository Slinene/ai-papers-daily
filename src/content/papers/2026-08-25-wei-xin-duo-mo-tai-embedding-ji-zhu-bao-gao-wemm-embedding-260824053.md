---
title: 'WeMM-Embedding: WeChat Multi-Modal Embedding Technical Report'
title_zh: 微信多模态 Embedding 技术报告：WeMM-Embedding 家族
authors:
- Junjie Zhou
- Ke Mei
- Lei Li
- Tianyi Wang
- Fengyun Rao
- Jing Lyu
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2608.24053'
url: https://arxiv.org/abs/2608.24053
pdf_url: https://arxiv.org/pdf/2608.24053
published: '2026-08-25'
collected: '2026-08-26'
category: Multimodal
direction: 多模态表征学习 · 通用 Embedding
tags:
- Multimodal Embedding
- MLLM
- Matryoshka Representation Learning
- Contrastive Learning
- Semantic ID
- Recommendation
one_liner: 2B/4B/9B 通用多模态 embedding 家族，两阶段训练与蒸馏在 MMEB-v2 达 80.6 SOTA，并大规模落地微信推荐搜索
practical_value: '- 通用多模态 item embedding 直接复用：商品/视频/图文内容统一走 `<embedding>` 末 token
  出向量，可在召回、排序特征、用户序列建模、跨域理解中复用；视频场景可一次前向同时拿到“视频帧-only”和“视频+ASR文本”两种表示，适配不同召回通道。

  - 多任务 pair 统一格式优于分开训练：把搜索 query、商品详情、内容描述、分类标签、点击/转化分级相关统一成 `(instruction, source,
  target, hard_negatives, relevance)`，用 task-consistent batch 和 duplicate-aware masking，能显著提升
  in-batch negatives 质量；该技巧可直接迁移到电商搜索/推荐 embedding 训练。

  - 用 Semantic ID 做数据平衡和难负例挖掘：对 pair 表示做 RQ-KMeans 得到三层语义 ID，按频次降采样高频语义、保留长尾，配合 MLLM
  质量过滤和检索难负例，特别适合缓解电商长尾商品和新品冷启动；MRL 输出 256/512 维可降低向量索引成本，同时保留 97% 以上性能。

  - 蒸馏策略可压缩学生模型：2B/4B 用 9B teacher 的 batch 内双向相似度分布做 KL 蒸馏，不像 one-hot 对比损失那么硬，能高效传递细粒度关系；在广告/推荐小模型迭代时可用此方法把大模型能力压到线上可部署尺寸。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
多模态内容在微信生态（视频号、公众号、朋友圈、电商）中高度混合，推荐与搜索需要统一表征来做跨域召回、排序和内容理解。现有 MLLM-based embedding 支持任意交错输入，但规模数据与细粒度相关性监督仍不足；因此需要高性价比的通用多模态 embedding 家族。

## 方法关键点
- 基于 Qwen3.5 原生多模态 backbone，覆盖 2B/4B/9B；支持文本、图片、视频、视觉文档和 interleaved 输入。
- 输入末尾追加 `<embedding>` token，用 last-token hidden state 做 L2 归一化；同一序列可插入多个 embedding token，一次前向同时抽视频帧和视频+ASR 表征。
- 统一 pair-based 格式 `(instruction, query, target, hard negatives, graded relevance)`，把弱监督图文对、检索、分类、QA、分级相关等任务融合到一个多任务对训练。
- Stage 1 大规模多模态对齐：数亿 pairs；InfoNCE + 分级相关的 score-gap-weighted CoSENT 损失；task-consistent batching 提供更有效的 in-batch negatives；duplicate-aware masking 防止重复目标成为伪负例。
- Stage 2 curated fine-tuning：约 1/10 数据规模，Semantic-ID 引导重采样（RQ-KMeans 三层语义 ID）、MLLM 质量过滤、难负例挖掘；加入 reranker supervision 和 embedding distillation；9B 用多 specialist 模型合并替代更大 teacher。
- MRL：支持 64-2048 维截断输出，一次前向可出多维度向量。

## 关键实验结果
- MMEB-v2：2B 综合 77.9，已超过 Qwen3-VL-Embedding-8B 的 77.8；9B 达 80.6，登顶官方榜单。
- MMEB-v3：9B V3-All 59.5，明显领先 8B 基线 53.5。
- 12 个跨模态检索任务：2B 平均 79.8，优于 Gemini Embedding 2 的 79.5；9B 提升到 81.7。
- 微信内部 26 任务基准：2B 平均 72.0，较 Qwen3-VL-Embedding-2B 的 60.9 提升明显；14 个在线 A/B 均正向并上线推荐与搜索系统。
- MRL 分析：256 维保留 97% 以上 2048 维性能，适合低时延/低成本索引。

## 最值得记住的一句话
大规模对齐后的 curated 数据、难负例与 embedding 蒸馏，比单纯扩大规模更能提升通用多模态 embedding 的细粒度相关性；256/512 维 MRL 已足够承接多数推荐检索场景。
