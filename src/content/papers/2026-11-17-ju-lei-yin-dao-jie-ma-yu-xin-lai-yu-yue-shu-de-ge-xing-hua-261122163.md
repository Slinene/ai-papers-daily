---
title: Cluster-Guided Decoding with Trust-Region Constraints for Personalized Recommendation
title_zh: 聚类引导解码与信赖域约束的个性化推荐
authors:
- Gezheng Wen
- Chao Shen
- Raviteja Anantha
- Tan Shen Cliff Chung
- Layne C. Price
affiliations:
- Amazon
arxiv_id: '2611.22163'
url: https://arxiv.org/abs/2611.22163
pdf_url: https://arxiv.org/pdf/2611.22163
published: '2026-11-17'
collected: '2026-11-18'
category: RecSys
direction: 聚类引导的低延迟推荐排序
tags:
- cluster-guided decoding
- trust-region constraints
- semantic clustering
- cold-start recommendation
- residual quantization
- sequential recommendation
one_liner: 用语义簇层级先验直接作用于 item 打分，在毫秒级内提升稀疏目录和冷启动推荐效果
practical_value: '- 在召回/粗排阶段引入 item 语义簇先验，并直接加到打分公式中，而不是只做候选预选：这样可以让簇结构真正影响排序，提升推荐的可控性和区域解释性。

  - 簇先验从簇质心组装，不依赖具体 item 的交互统计，适合电商冷启动用户和新商品：可以用聚类质心表示用户兴趣，避免新用户无历史时无法计算个性化分数。

  - 毫秒级推理使其可作为大规模目录的第一阶段检索：线上大规模商品库场景下，可以先做低延迟簇引导检索，再做精排，平衡效率与个性化。

  - 采用 residual quantization 构建语义簇层级的思想，可以作为替代 KMeans 的聚类方案，尤其在需要细粒度语义划分时，能学到更好的层级结构，便于后续做可解释推荐。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有推荐系统通常逐 item 独立打分，没有显式控制推荐结果来自于目录中的哪个语义区域。具备这种控制能力的模型往往在高维目录上推理过慢，无法用于在线大规模检索。

**方法关键点**：CG2R 学习一个语义簇层级结构，并将簇级先验直接加入 item 打分规则，使聚类结构真正塑造排序结果，而非仅用于候选预筛选。该先验由簇质心组装，不依赖 per-item 统计，因此对没有历史行为的冷启动用户仍然可用。此外，方法结合 trust-region 约束，在簇引导下稳定优化推荐排序。

**关键结果**：在三个 benchmark 数据集上，CG2R 在 Recall 和 nDCG 上优于经典协同过滤、神经序列模型和 LLM-based baseline；目录越稀疏，性能优势越大。推理耗时在毫秒级，具备作为低延迟第一阶段检索的潜力。
