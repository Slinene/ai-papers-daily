---
title: 'HF-SID: High-Fidelity Semantic IDs for Generative Retrieval in Location-Based
  Services'
title_zh: HF-SID：面向位置服务生成式检索的高保真语义 ID
authors:
- Haowen Lin
- Jing Li
- Zhibin Hao
- Fangye Wang
- Lihui Su
- Song Yang
- Xiaojiang Zhou
- Pengjie Wang
affiliations:
- AMAP, Alibaba Group
- University of Science and Technology of China
- Tsinghua University
arxiv_id: '2608.30479'
url: https://arxiv.org/abs/2608.30479
pdf_url: https://arxiv.org/pdf/2608.30479
published: '2026-08-31'
collected: '2026-09-01'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Semantic ID
- Generative Retrieval
- LLM
- POI
- Numerical Encoding
- Contrastive Learning
one_liner: 通过 3D 坐标编码、数值专用编码器与末层结构对比学习，在不增加 SID 长度下大幅提升 LBS 生成式检索的地理与业务指标
practical_value: '- 生成式推荐里别只调 RQ-VAE/codebook：item 表示在量化前若丢失连续数值、层级、地理等信息，量化后无法弥补。优先审视
  embedding 是否保住了关键属性。

  - 对价格/评分/销量等异构数值，可以用单个 [NUM] token + 数值编码器 + Type Embedding，避免数字被 BPE 切碎、跨属性尺度混淆；这个
  trick 可迁移到电商生成式召回。

  - 结构对比学习只作用在最后一层残差，能分离同一粗类下的细分类目/共址 item，且不破坏前两层地理/语义前缀；对「同一商圈/同一店铺下的不同商品」场景有直接参考。

  - 线上 A/B 显示保真度主要提升 CVR 而非 CTR，说明 SID 影响的是候选资格/品类准确性而非曝光点击；评估生成式检索应更看重转化类指标。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

生成式检索把 POI 压缩为 Semantic ID，SID 是 LLM 感知 item 的唯一通道，量化前丢失的信息解码时不可恢复。LBS 对细粒度属性高度敏感，但现有 SID 方法普遍在坐标被 tokenizer 切成数字碎片后、数值属性被当普通文本后，才做地理/结构补偿，无法恢复连续数值与层级结构。

HF-SID 在量化前重建三类保真：坐标从经纬度转为 3D Cartesian，消除硬网格边界与经线跳变；每个数值（含坐标）用 sign + 带进位平滑的整数位 + sin/cos 小数位表示成单个 [NUM] token，由冻结的 Numerical Encoder 映射为连续嵌入，并用 Type Embedding 为 rating、价格、访问量等属性建立各自子空间。Geo-CPT 训练 pairwise distance 与 nearest-pair 推理，Num-CPT 训练跨属性比较；最后用 3 层 RQ-VAE 生成 3-token SID，并仅在第二层残差上做 Structure-based Contrastive Learning，让同粗标签但不同细标签的共址 POI 分离，不干扰前两层地理前缀。

在 AMap-L 上，Avg.Dist 从 6.07 km 降到 0.25 km（−95.9%），Hit@200 达 81.24%，比最强 baseline 高 3.66 点；AMap-S Hit@200 48.98%，比 6-token GenPOI 高 6.78 点。线上 A/B 平均 PV_CVR +6.74%、UV_CVR +6.03%，远高于 CTR 提升。消融显示地理保真贡献最大，结构保真次之，数值保真最小。

最值得记住：SID 质量由量化前的表示保真决定，编码阶段的连续性与子空间隔离比事后 codebook 设计更重要。
