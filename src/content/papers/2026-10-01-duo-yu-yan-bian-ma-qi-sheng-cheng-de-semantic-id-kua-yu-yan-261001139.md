---
title: Do Multilingual Encoders Produce Language-Consistent Semantic IDs?
title_zh: 多语言编码器生成的 Semantic ID 跨语言一致性检验
authors:
- Abhinav Bohra
- Anuj Bohra
affiliations:
- Amazon
- Rutgers University
arxiv_id: '2610.01139'
url: https://arxiv.org/abs/2610.01139
pdf_url: https://arxiv.org/pdf/2610.01139
published: '2026-10-01'
collected: '2026-10-02'
category: GenRec
direction: 生成式推荐 · Semantic ID 跨语言一致性
tags:
- Semantic ID
- Multilingual
- RQ-VAE
- Generative Retrieval
- Cross-lingual
- Quantization
one_liner: 用 ESCI 翻译对照证明：多语言编码器与平衡码本不能保证同一商品跨语言 SID 前缀一致，需显式对齐目标。
practical_value: '- 部署多语言生成式推荐时，不要假设多语言 encoder 的 SID 天然跨语言一致；若用 exact prefix 做召回/索引，需为同一商品的不同语言文本增加显式对齐约束或后处理映射。

  - RQ-VAE 第一层易坍缩到单码，工程实现要加输入 centering、per-step dead-code recycling，并监控每层有效码数 Keff；E5
  原始空间共享 offset 强，直接量化会失效。

  - 拟合码本时语言平衡不必然带来更好 cross-lingual agreement；实验中英文 only 拟合反而保留更多翻译前缀。若目标是英文为主索引，可保守采用英文主导拟合
  + 跨语言一致性损失。

  - 评估 quantizer 扰动敏感度时，isotropic control 会高估语言方向选择性，应构造 product-directed control（沿真实产品
  embedding 方向移动相同距离）才能得到可靠结论。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：多语言商品目录里同一产品在不同语言下的标题、描述是独立编写或翻译的，语义 ID（SID）是从文本 embedding 量化得到的离散标识。若同一商品的英文、西语、日语文本得到不同 SID 前缀，生成式检索的 exact prefix lookup 会让跨语言商品互不可达；而很多系统假设多语言 encoder 天然解决这一问题，论文检验该假设是否成立。

**方法**：从 Amazon ESCI 抽 20K 商品，用 NLLB 翻译成西语/日语，英文规则复述作为同语言对照；主 encoder 为 multilingual-E5-large，并用 LaBSE 做独立检查。RQ-VAE 采用 3 层、每层 256 码本，Euclidean assignment + cosine reconstruction loss。三种量化拟合混合：纯英语、80/10/10 英语主导、三种语言等比例；设置 distance-matched isotropic 与 product-directed 两种扰动控制。指标包括 paired cosine distance、语言 probe、Jaccard@10、prefix consistency、有效容量 Keff 与 full SID mismatch。

**关键结果**：E5 中西语/日语翻译与英文原文的 cosine distance 为 0.081/0.113，英文复述仅 0.011，语言 probe 高达 99.9%。80/10/10 拟合下，西语翻译保留英文首个 SID 码的比例只有 28.3%，日语仅 7.7%，英文复述为 89.0%；日语 full SID 一致性几乎为 0。Product-directed control 显示翻译与等距离产品方向扰动 mismatch 接近，quantizer 没有选择性放大语言方向。平衡混合使各语言有效容量更均匀（49/42/42 vs 76/30/16），但 prefix@1 西语从 28.3% 降到 6.6%、日语从 7.7% 降到 4.8%；英文 only 拟合反而保留 67.6% 西语、64.3% 日语首码。LaBSE 没有 E5 的容量失衡。

**最值得记住的一句话**：多语言暴露与平衡码本使用本身不产生跨语言一致的 SID，系统需要在量化或训练目标中显式对齐同一商品的 parallel renderings。
