---
title: 'RenderRank: Learning to Rerank Text with Compressed Visual Tokens'
title_zh: RenderRank：用压缩视觉 Token 学习文本重排序
authors:
- Seongtae Hong
- Youngjoon Jang
- Jungseob Lee
- Hyeonseok Moon
- Heuiseok Lim
affiliations:
- Korea University
- Sookmyung Women's University
arxiv_id: '2609.35069'
url: https://arxiv.org/abs/2609.35069
pdf_url: https://arxiv.org/pdf/2609.35069
published: '2026-09-27'
collected: '2026-09-29'
category: RecSys
direction: 文档重排序 · 视觉 token 压缩
tags:
- Visual Token Compression
- Document Reranking
- Cross-Modal Distillation
- Long-Document
- Inference Efficiency
- LoRA
one_liner: 将文档渲染成图像并以压缩视觉 token 表示，在重排序中减少 16.5–35.5% 输入 token 且保持或提升 NDCG@10。
practical_value: '- 对电商搜索/广告里的长文本（商品详情、用户评论、广告落地页）可离线渲染成图像并用 VLM 视觉编码器产出压缩 token 缓存；在线
  rerank 只输入 query token + 文档视觉 token，候选集越大、文档越长，单候选打分成本节省越明显。

  - 两阶段训练可直接复用：先用已有文本 reranker 做教师，在 score 级别做 MSE 蒸馏，让压缩/视觉表示对齐文本分数；再用 query-local
  InfoNCE 对比同一 query 下正负文档。不需要 token 级对齐，且冻结视觉编码器、只对语言 decoder 做 LoRA，训练成本低。

  - 渲染参数（font size、行距、DPI、图像宽度）是成本/质量旋钮：10pt→14pt 的 NDCG 只提升约 0.8 个百分点，但 token 增加约
  57%、吞吐下降约 33%；业务上可先做 QA/摘要小实验选性价比点，论文的 12pt + 行距 1.0 是较稳默认值。

  - 工程上必须把文档视觉编码离线化并缓存：论文中不带缓存时吞吐从 76.83 PPS 掉到 37.31 PPS。若业务已有商品图/多模态特征，可考虑直接复用视觉
  embedding，进一步省掉渲染与编码成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
RAG/搜索重排序需要对每个候选文档单独打分，输入长度直接影响算力与吞吐。文本 token 序列通常较长，而把文档渲染成图片、用 VLM 视觉编码器产生视觉 token，可以压缩表示长度。问题在于视觉压缩是否保留 relevance 信息，以及如何训练 reranker 适应视觉输入。

**方法关键点**
- 渲染配置：Roboto Regular，12pt，行距 1.0，96 DPI，固定宽 896px，高最多 896px 且按 32px 调整；长文档多页渲染并保持顺序。
- 初始化自 Qwen3-VL-Reranker-2B，冻结视觉编码器与 visual feature merger，只对语言 decoder 做 LoRA；第一阶段合并后按 ReLoRA 原则重初始化 adapter。
- 两阶段训练：Cross-Modal Relevance Distillation 用 Qwen3-Reranker-4B 作为文本教师，对 1.57M 训练数据采 1 正 3 负，共 6.28M query-doc 对，用 MSE 让视觉输入分数逼近文本输入分数；Query-Local Relevance Discrimination 在 RLHN-100K 上用 query-local InfoNCE 对比正负文档。

**关键结果**
- BEIR 11 个数据集平均 NDCG@10 55.96，超过所有 <4B 文本 baseline 和部分更大模型；平均输入 token 290.07，比文本 reranker 少 16.5–35.5%；吞吐 76.83 PPS。
- 长文档 4 个数据集平均 NDCG@10 88.27，输入 token 约为文本 baseline 一半，吞吐平均 4.51 PPS，是最快 baseline 的 1.70 倍；在 2K/4K/8K 最大长度限制下均优于 baselines。
- 消融：去掉第二阶段 NDCG 从 55.96 降至 54.86，去掉两阶段降至 50.20；不带视觉缓存时吞吐从 76.83 降至 37.31。

**最值得记住的一句话**
把文档文本渲染成图像并用视觉 token 压缩，配合「分数蒸馏 + query-local 对比」两阶段训练，可以在不牺牲 rerank 效果的前提下大幅降低逐候选打分成本，尤其利于长文档和候选集大的场景。
