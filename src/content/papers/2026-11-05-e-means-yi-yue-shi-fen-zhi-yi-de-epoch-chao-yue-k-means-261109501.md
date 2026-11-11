---
title: 'e-means: outperforming k-means (in one-tenth the epochs)'
title_zh: e-means：以约十分之一的 epoch 超越 k-means
authors:
- Swann Bessa
- Pierre-Emmanuel Mazaré
- Gergely Szilvasy
- Hugo Touvron
- David Picard
- Matthijs Douze
- Hervé Jégou
affiliations:
- FAIR at Meta
- École Nationale des Ponts et Chaussées
arxiv_id: '2611.09501'
url: https://arxiv.org/abs/2611.09501
pdf_url: https://arxiv.org/pdf/2611.09501
published: '2026-11-05'
collected: '2026-11-11'
category: Other
direction: 大规模 embedding 聚类优化
tags:
- k-means
- EMA
- clustering
- GPU
- vector quantization
- embeddings
one_liner: 提出 mini-batch 指数滑动平均的 k-means 优化算法 e-means，以 1.4-2.6 个 epoch 达到 Lloyd 25-epoch
  损失，取得 10-45 倍 GPU 加速
practical_value: '- 在电商/推荐里构建 embedding 索引（IVF、PQ、语义 ID 聚类）时，可用 e-means 替代标准 Lloyd
  k-means：其 decay rate 与 batch size 有公式化 scaling law，无需逐业务扫超参，1.4-2.6 个 epoch 即可达到
  25-epoch Lloyd 损失，训练时间大幅下降。

  - 对超大规模商品/用户 embedding（10B 级）建库时，e-means + IVF 可继续加速；论文给出按 n 和 k 直接设定参数的规则，适合大规模
  ANN 索引或类目划分场景。

  - mini-batch EMA 更新可迁移到在线聚类/流式 embedding 场景，如商品类目增量更新、用户兴趣聚类；用衰减率控制旧中心权重，提升稳定性并加快收敛。

  - 需要更低聚类损失以提升量化索引召回/精度时，e-means 常优于 k-means++，可作为 Faiss 之外的高质量初始化或训练方案落地。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Lloyd k-means 在大规模 embedding（检索、量化、数据治理）上收敛慢，需要多个 epoch；现有 GPU k-means 实现仍不够高效。

**方法关键点**：引入 mini-batch 指数滑动平均（EMA）优化簇中心，借用现代深度学习训练机制；同时建立 decay rate 与 batch size 随 dataset size n、cluster 数 k 变化的 scaling law，使参数无需超参搜索即可确定。

**关键结果数字**：在多种 embedding 数据集上，e-means 在 1.4-2.6 个 epoch 内达到 Lloyd k-means 25 epoch 的损失，相对 SOTA k-means GPU 实现有 10-45 倍墙钟加速；在 DINO10B（10B 个 1024 维 DINO embedding）上，仅 2.5 epoch 划分出 16M clusters，损失低于 Lloyd 25 epoch，且经常超过 k-means++。
