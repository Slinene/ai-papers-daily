---
title: Real-Time Hard Negative Sampling via LLM-based Clustering for Large-Scale Two-Tower
  Retrieval
title_zh: 基于 LLM 聚类的实时硬负采样双塔召回
authors:
- Ivan Ji
- Liuyi Hu
- Harrison
- Zhao
- Lei Huang
- Qunshu Zhang
- Max
- Fan
- Aameek Singh
affiliations:
- Meta
arxiv_id: '2607.00448'
url: https://arxiv.org/abs/2607.00448
pdf_url: https://arxiv.org/pdf/2607.00448
published: '2026-07-01'
collected: '2026-07-02'
category: RecSys
direction: 双塔召回 · 硬负采样 · LLM 聚类
tags:
- hard negative sampling
- LLM
- clustering
- two-tower
- retrieval
- popularity bias
one_liner: 提出一种在线聚类的硬负采样框架，利用 LLM 生成 item 语义簇并实时抽取簇内 hard negative，显著提升召回并缓解流行度偏差
practical_value: '- **用 LLM 离线生成 item 语义簇替代规则类别**：电商/视频场景可构建多模态内容理解模型，产出 300 级粗粒度簇（簇内
  item ≥ 10k），作为硬负采样的先验，比人工品类树更适应内容语义和用户兴趣迁移。

  - **实时 OOB 池 + 哈希分桶采样**：将 item 池按 cluster_id 分段维护，更新与采样均 O(1)，训练 QPS 损失仅 -1.4%，可直接嵌入现有双塔训练流，不需异步构建
  ANN 索引。

  - **簇内采样缓解反馈循环与流行度偏差**：从与正样本同簇的 item 中抽取负样本，迫使模型学习细粒度区分能力，工业实验中 Top100 热门 item 曝光占比从
  50% 降至 32%，长尾曝光桶（≥1k impressions）增加 50%，对去偏效果明显。

  - **评估避免 k-core 过滤与采样指标**：使用全量全局排序评估 HR@50/100，更反映冷启动与稀疏场景的真实效果，业务落地评估时可参考此严格设定。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商/社交推荐的双塔召回常采用 in-batch 或随机 OOB 负采样，产生大量容易区分的简单负样本，导致模型训练不充分、流行度偏差加剧与反馈循环固化。硬负采样（如 DNS、ANCE）计算开销大，难以在数十亿级工业数据上实时运行。需要一种高效、可实时生成有挑战性负样本的方法。

**方法关键点**：
1. **LLM 驱动的语义聚类**：基于预训练大模型构建多模态 content embedding（文本、图像、视频），通过微调产出约 300 个语义簇，每簇含 ≥10k item，作为硬负采样的先验标签。
2. **Cluster GOOBS 实时采样框架**：维护一个 item 池，按 cluster_id 分段的哈希表存储 item 特征。训练时，对每个正样本的同簇 item 进行随机采样作为硬负样本，采样与更新均为 O(1)，不依赖全局 ANN 索引。
3. **训练流程**：仍使用 in-batch 负样本 + LogQ 校正，并加入簇内 OOB 硬负样本，损失仅增加少量计算。预加载历史 item 池保证启动即用，训练过程中持续更新。

**关键结果**：
- 公开数据集（MovieLens-1M、Amazon 多个子集）上，Cluster GOOBS 的 HR@50 相对 In-batch 基线提升 +7.2%～+55.6%，尤其在稀疏的 Amazon-Electronics 上增幅最大，且均优于 ANCE（+28.6% vs ANCE）等硬负采样方法。
- 工业 A/B 测试：CTR 提升 **+53%**，训练 QPS 仅下降 **-1.4%**，零推理开销。
- 流行度偏差显著缓解：曝光 ≥1k 的 item 桶数增加 **50%**，Top100 热门 item 的曝光贡献从 50% 降低至 **32%**。

**一句话精华**：用 LLM 产出的语义粗簇做实时桶内硬负采样，以极低工程成本同时实现召回大幅提升和去偏。
