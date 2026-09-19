---
title: Grounded Product Understanding in Livestream Videos
title_zh: 直播视频中的产品定位理解
authors:
- Xinyu Zhang
- Junjie Chen
- Jiawei Ge
- Qianlong Li
- Libin Ma
- Baokun Pan
- Yahui Luo
affiliations:
- Kuaishou Technology
- Institute of AI for Industries, Chinese Academy of Sciences
arxiv_id: '2609.20508'
url: https://arxiv.org/abs/2609.20508
pdf_url: https://arxiv.org/pdf/2609.20508
published: '2026-09-17'
collected: '2026-09-19'
category: Multimodal
direction: 多模态视频产品理解与时刻定位
tags:
- Multimodal
- Video Understanding
- Product Retrieval
- Temporal Localization
- Benchmark
- Livestream E-commerce
one_liner: 提出GPUB基准和UniPro模型，联合评估产品检索与时刻定位，大幅提升直播视频产品理解性能
practical_value: '- 直播电商中产品信息分散在多个非连续片段，仅做产品检索或片段定位无法满足自动剪辑、摘要等需求。可借鉴GPUB的联合任务定义，在业务中构造“产品-片段”对齐数据，训练模型同时输出产品ID和对应时刻，直接用于产品讲解片段自动生成。

  - UniPro采用共享多模态编码器同时处理视频和产品目录，并强制学习产品对齐和时间结构化表示，相比分离式两阶段方案能更好地利用产品与时刻的对应关系。实际部署中可复用该架构，在召回或粗排阶段同时输出产品候选和关键片段，减少级联误差。

  - 面对31K规模产品目录，UniPro的候选集构建和负采样策略值得参考：可利用直播中出现的产品时序信息构造hard negative，提升模型区分相似产品的能力，尤其适用于时尚等非标品类。

  - 评估指标Pair mAP@.3和Joint R@1@.3同时衡量产品检索和时刻定位的联合精度，比单一指标更能反映真实业务效果，建议在类似多模态理解任务中采用。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：直播电商中产品证据分散在多个非连续时刻，视觉与语音信息互补，现有基准通常孤立评估产品检索和时刻定位，缺乏产品身份与时间证据的对应性评估，制约了下游产品剪辑、摘要等应用。

**方法关键点**：
- 构建GPUB基准：包含3,000个直播实例、质量受控的多时刻标注，以及31K+时尚产品目录；
- 定义三个任务：主任务GPrU联合识别目标产品并定位支持时刻，子任务为产品检索和产品时刻定位；
- 提出UniPro模型：通过共享多模态编码器学习产品对齐和时序结构化表示，同时处理视频与候选产品集。

**关键结果数字**：
- 现有最佳基线在GPrU上仅达到10.13% Pair mAP@.3；
- UniPro将Pair mAP@.3提升至21.53%，Joint R@1@.3达到37.23%，相对提升超过一倍。
