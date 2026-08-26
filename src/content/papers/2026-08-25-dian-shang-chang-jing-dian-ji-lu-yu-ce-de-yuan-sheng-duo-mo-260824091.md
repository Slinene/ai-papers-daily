---
title: Native Multimodal Representation Learning for Click-Through Rate Prediction
  in E-Commerce Scenarios
title_zh: 电商场景点击率预测的原生多模态表示学习
authors:
- Chao Yi
- Feifan Yang
- Jiawei Feng
- Sishuo Chen
- Zhangming Chan
- Xiang-Rong Sheng
- Han Zhu
affiliations:
- Taobao & Tmall Group of Alibaba
- University of Science and Technology of China
arxiv_id: '2608.24091'
url: https://arxiv.org/abs/2608.24091
pdf_url: https://arxiv.org/pdf/2608.24091
published: '2026-08-25'
collected: '2026-08-26'
category: RecSys
direction: 多模态表示与 CTR 预测对齐
tags:
- Multimodal
- CTR Prediction
- E2EM
- Mine-Then-Train
- Semantic ID
one_liner: 提出 Mine-Then-Train：从 CTR 数据挖掘可解释三元组微调多模态编码器，在线 CTR 提升 1.5%
practical_value: '- 不要盲目对强预训练多模态编码器与 ID CTR 模型做端到端联合训练：梯度不一致且成本高；先在数据层过滤噪声、挖掘干净监督更有效。

  - 用 annotation model 捕捉 CTR 增量信号：SID Decode Codebook 零初始化 + 残差结构，能保留预训练语义不退化，同时学习点击偏好。

  - 三元组筛选可复用：SCL 相似度差距小但 annotation score margin 大的样本，对应语义相似但用户偏好排序不同的 hard cases，适合微调
  encoder。

  - 多模态表示集成到 CTR 模型有两条路径：similarity-based（SimTier/SA-TA）和 direct fusion；NMRL 改进可即插即用，无需改动其他模块。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商推荐普遍采用两阶段多模态范式：先用业务数据预训练多模态编码器（如 SCL），再冻结提取表示给 CTR 模型。但预训练任务与 CTR 目标、数据分布不一致，限制了表示效果。直觉方案是端到端联合训练（E2EM）编码器与 CTR 模型，让编码器自动学习下游知识。然而在淘宝展示广告系统中，对已强预训练的 SCL 编码器做 E2EM 不仅没有增益，反而 GAUC 下降。分析发现，CTR 行为只有部分可归因于多模态语义，混合了价格比较、误点击、位置偏差、兴趣疲劳等非语义因素，导致监督模糊；co-training 无法显式解耦信号，梯度一致性差；且端到端训练 GPU 内存最高增至 25 倍，成本不可接受。

**方法关键点**
- 提出 Mine-Then-Train：先训练多模态 annotation model，在 CTR 数据上学习点击相关性分数；采用残差结构：冻结 SCL 编码器，通过 RK-Means 聚类得到 SID，SID Decode Codebook 零初始化残差模块，保留 SCL 语义同时学习 CTR 增量信息。
- 基于 annotation model 输出，结合 SCL 相似度构造三元组：要求 SCL 相似度差距小（𝜏𝑠<0.05）但 annotation score margin 大（𝜏𝑎>0.15），筛选语义相似但用户偏好排序不同的样本；共挖掘 30M 高质量三元组。
- 用 triplet margin loss 加 SCL loss 微调 SCL 编码器，得到 Native Multimodal Representation (NMR)。

**关键实验**
数据集为淘宝展示广告，84M 用户、88M 商品、1.9B 样本；基线是已集成 SCL 表示的 CTR 模型。E2EM 所有变体均低于 MUSE 基线 GAUC 0.6154，最低 0.6124；梯度分析显示 E2EM 批内相似度 0.016、批间 0.006，远低于 SCL 的 0.144/0.849。NMRL 离线相对提升 GAUC +0.22%、AUC +0.11%；在线 A/B 测试 CTR +1.5%、RPM +0.5%。

**最值得记住的一句话**：在已有强多模态编码器的工业推荐系统中，端到端联合训练不是最优解；先挖掘多模态可解释的干净监督再微调编码器，才能避免 CTR 标签中非语义因素破坏共享表示。
