---
title: 'When Does Latent Reasoning Help? MeRa: Metric-Space Bias for Spatial Prediction'
title_zh: 潜在推理何时有效？MeRa：用度量空间偏差提升空间预测
authors:
- Zhenyu Yu
- Shuigeng Zhou
affiliations:
- Fudan University
arxiv_id: '2606.03727'
url: https://arxiv.org/abs/2606.03727
pdf_url: https://arxiv.org/pdf/2606.03727
published: '2026-06-02'
collected: '2026-06-04'
category: RecSys
direction: 序列推荐 · 隐式推理约束
tags:
- Spatial Prediction
- POI Recommendation
- Latent Reasoning
- Metric Space
- MeRa
one_liner: 证明隐式推理在空间预测中需度量空间偏差约束，否则有害；提出即插即用MeRa模块，实现显著提升
practical_value: '- 在序列推荐中引入迭代推理模块时，必须对齐任务先验结构（如空间距离），否则可能退化；电商推荐中，若用户轨迹有地理或时空模式，应加入类似的度量偏差。

  - MeRa的轻量级即插即用设计可直接嵌入现有推荐系统的 encoder 与预测头之间，仅需 pairwise 距离信息，为快速增强模型推理能力提供工程范本。

  - 度量空间偏差保证了迭代推理的收敛性和表达性，可推广至任何具有距离或相似度度量的推荐场景（如用户-物品图、商品 embedding 空间），利用语义距离构建类似约束。

  - CLEVR 实验表明欧氏距离偏差在非地理场景也有效，可在商品序列建模中尝试对 item embedding 施加距离偏差，提升多步预测。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：隐式推理（latent reasoning）在序列推荐中通过迭代更新表示提升预测，但在空间预测（如 POI 推荐）中不加约束会损害性能。本工作探索何时推理有帮助，发现是否引入度量空间偏差是关键。

**方法**：提出 MeRa（Metric-space Reasoning），一个轻量级、骨干无关的模块，插入序列编码器与预测头之间。它从 pairwise 距离学习度量空间偏差，在迭代推理中约束表示更新，确保收敛到唯一不动点，且 N 步推理严格比 N-1 步更具表达能力。

**结果**：在 GETNext 骨干上，不带偏差的推理 NDCG@10 比带偏差低 4.5%。MeRa 在三个空间预测基准上均获最优 NDCG@10，优于 GeoMamba 和 HMST。CLEVR 上的控制实验（欧氏距离）验证了结论的泛化性，表明度量空间约束对一般几何结构有效。
