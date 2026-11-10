---
title: 'Scaling Taxonomy-Free Image Labeling with Generative AI: A Multimodal'
title_zh: 生成式 AI 规模化无分类体系图像标注：多模态搜索应用
authors:
- Zhenjie Zhang
- Sainan Chen
- Kshiteesh Hegde
- Mengze
- Li
- Pouya Rezazadeh Kalehbasti
- Munachim Ezema
- Karina Sobhani
affiliations:
- Pinterest, Inc.
arxiv_id: '2611.12725'
url: https://arxiv.org/abs/2611.12725
pdf_url: https://arxiv.org/pdf/2611.12725
published: '2026-11-09'
collected: '2026-11-10'
category: QueryRec
direction: 生成式图像标注 · 聚类规模化
tags:
- Image Labeling
- Multimodal Search
- VLM
- Clustering
- Query Suggestion
one_liner: 用图像聚类共享 VLM 标签，将生成式图像描述和搜索建议成本降至 0.05% 并提升 CTR 与互动
practical_value: '- 用聚类共享 VLM 标注：对图像 embedding 聚类后只对代表图做 VLM 生成标签，簇内共享，可把商品图描述/属性补全成本降到千分级，适合电商大规模
  SKU 图库。

  - 分层 K-means 工程实现：先粗分片再细聚类，将复杂度从 O(N²) 降到线性，可用单机 GPU 处理十亿级图像；避免分布式 GPU 集群成本。

  - Embedding 必须匹配 insight 类型：用视觉感知强的 Unified Visual Embedding，不要用混入 engagement 优化的
  embedding；针对颜色等具体属性建议单独训练专用 embedding。

  - 在线 lookup 用单层网络编码 centroid（~1M 规模）或 ANN index 查簇，再读 KV store；可作为低延迟生成式标签 serving
  的模板。

  - A/B 结论：聚类共享 VLM 标签的 query 建议相关性显著优于 text-based GPT baseline（pivot CTR +69.5%），值得在搜索建议、推荐理由等场景尝试。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
Pinterest Hybrid Search 需要为图片提供 descriptors 和 pivots 两类 query suggestions。传统 taxonomy-based 标注固定、昂贵、覆盖不足；直接调用 VLM 生成标签虽然质量高，但十亿级图片推理成本过高、延迟不满足在线服务。因而需要一种低成本、低延迟、可规模化的无 taxonomy 图像标注方案。

## 方法关键点
- GLOC（Generative Labeling On Clusters）：先对图像 embedding 做大规模聚类，每个簇选代表图，仅对代表图用 VLM 生成 descriptors/pivots，簇内成员共享标签，在线时查簇 ID 再取 KV store 标签。
- 分层 K-means：先粗分成可放入单机 GPU 的分区，再在分区内做细粒度聚类；复杂度由经典 K-means 的 O(N²T/C) 降为线性 O(NST/C)，其中 S 为分区大小，保持常数。
- Embedding 选择：使用 Pinterest 的 Unified Visual Embedding，强调细粒度视觉感知相似性；不采用加入 engagement 优化的 embedding，针对颜色等特定 insight 可换用专用 embedding。
- 聚类密度：平均 cluster size 约 2000，平衡质量与成本。
- 在线服务：约 100 万 centroid 时用单层 NN 编码 centroid 做 membership inference；更大规模用 ANN index；查到簇 ID 后从 KV store 读取标签。

## 关键结果
- 标签生成成本降到原来的 0.05%。
- 离线人工评估：pivots 平均 3.5/4 分；descriptors 平均 2.51/3 分，irrelevant 率仅 4%。
- 在线 A/B：pivot CTR 相对 text-based GPT baseline 提升 69.5%，pivot feed engagement 相对 baseline 提升 100%，相对无 pivot 控制组提升 146%；descriptor feed engagement 相对控制组提升 79%。

最值得记住的一句话：用聚类共享 VLM 标签，让生成式图像 query 建议在十亿级图像库上既便宜又快，还比纯文本 GPT 更相关。
