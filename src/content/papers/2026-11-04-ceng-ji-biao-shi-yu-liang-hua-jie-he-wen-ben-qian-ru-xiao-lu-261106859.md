---
title: 'Balancing hierarchical representation and quantization: A performance trade-off
  in text embeddings'
title_zh: 层级表示与量化结合：文本嵌入效率与效果权衡
authors:
- Kai Ponel
- Marco Polignano
- Erasmo Purificato
- Aylin Julia Temizkan
- Marco Levantesi
- Giovanni Semeraro
- Ernesto William De Luca
affiliations:
- Ludwig-Maximilian-University Munich
- University of Bari Aldo Moro
- European Commission, Joint Research Centre (JRC)
- IBM Germany
- Otto von Guericke University Magdeburg
arxiv_id: '2611.06859'
url: https://arxiv.org/abs/2611.06859
pdf_url: https://arxiv.org/pdf/2611.06859
published: '2026-11-04'
collected: '2026-11-05'
category: Eval
direction: Embedding 压缩与量化基准评估
tags:
- text embeddings
- quantization
- Matryoshka
- MTEB
- efficiency
- benchmark
one_liner: 基准 38 个 MTEB 任务发现 int8 量化几乎不损效果，一次维度减半无显著差异，检索最敏感
practical_value: '- 向量召回/商品 embedding 存储优化：优先对已有 Matryoshka 或层级 embedding 做 int8 量化，存储减少
  4 倍且检索效果损失很小；binary 量化对检索伤害大，需避免直接用于召回。

  - 层级截断与两级检索：利用一次维度减半在 m≥16 无显著损失，可将高维精排、低维粗排或缓存层结合，但不要连续多次截断，否则效果显著下降。

  - 检索与排序分开评估：论文表明检索对压缩远比 pair classification/rerank 敏感，因此在推荐系统中对召回和重排模型设置不同压缩策略，召回端应更保守。

  - 8x 降维 + int8 可作为大规模推荐系统 embedding 缓存的默认配置，32 倍存储降低且维持 94.4% 效果，适合高 QPS 场景。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：层级文本嵌入（Matryoshka 式可变长度）与量化是两种已确立的效率手段，但两者正交组合的系统副作用缺乏证据。

方法：对 4 个 transformer embedding 模型在 MTEB 38 个任务上做全因子基准，1D/2D 层级截断（含 2x/4x/8x 等降维）乘 float32/int8/binary，共 168 配置，报告单条向量存储与端到端评估时间，统计用 Friedman+Nemenyi。

结果：int8 在 pair classification 与 re-ranking 上与 float32 统计不可区分，总体最多差 1.5 个百分点；binary 在所有任务类别显著变差；一次维度减半在 m≥16 时不可检测，连续两次减半可检测；8x 降维 + int8 存储降至 1/32，效果保持 94.4%；检索类别退化远快于其他。时间方面未发现量化加速评估，中间层采样则显著缩短时间。
