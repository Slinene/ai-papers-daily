---
title: 'WARP: Weight-Space Analysis for Recovering Training Data Portfolios'
title_zh: WARP：从权重空间恢复训练数据组合
authors:
- Tzu-Heng Huang
- Aditya Goyal
- John Cooper
- Frederic Sala
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2607.01686'
url: https://arxiv.org/abs/2607.01686
pdf_url: https://arxiv.org/pdf/2607.01686
published: '2026-07-01'
collected: '2026-07-05'
category: Other
direction: 权重空间几何分析 · 数据配比推断
tags:
- Model Weights
- Data Mixture
- Domain Proportions
- Model Merging
- Weight Space
one_liner: 仅凭模型权重即可恢复微调时的领域混合比例，无需训练数据或训练轨迹
practical_value: '- **推断微调推荐模型的数据配方**：拿到一个第三方发布的推荐模型（如商品表示模型），可以用 WARP 反推其微调时所用数据集的领域构成（如服饰、电子、家居比例），判断是否偏离我方场景。

  - **检测数据泄露与分布漂移**：将线上模型与基础模型做权重插值，观察权重空间几何足迹，可快速发现模型是否在敏感数据上做过微调，辅助合规审计。

  - **指导增量训练的数据采样**：当需要继续微调开源推荐模型时，先恢复其原始训练数据的领域配比，据此调整自己的数据采样策略，避免灾难性遗忘或能力坍缩。

  - **简易实现：只需基础模型和微调模型权重**：不用访问原始训练数据或中间检查点，仅通过模型融合生成伪检查点，再用几何特征（如权重差向量的角度、长度）和线性映射即可推断，工程成本低。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：基金会模型（如 BERT、GPT-2）常微调后公开发布，但训练数据配方（如不同领域采样权重）几乎从不公开，造成“访问不对称”——研究者只能拿到模型，不知其训练分布。已有成员推理只能检测单样本级别，无法还原全局数据构成。

**方法**：WARP 仅利用公开发布的基模型和微调模型权重，通过**模型融合内插**生成一系列伪检查点，模拟缺失的训练轨迹，在权重空间中暴露训练数据的几何足迹。从这些模拟足迹中提取几何特征（如权重变化向量间的角度、长度），再通过无需参数的 Softmax 读出器或用合成混合训练的 MLP 投影器，将几何特征映射为领域混合比例。整个过程无需原始训练数据或真实中间检查点。

**结果**：在受控实验中，对 5 领域 BERT 和 GPT-2，WARP 恢复领域混合的**平均 MAE 低至 0.046 和 0.104**，显著优于成员推理基线，甚至优于能访问真实训练轨迹的变体。这表明权重空间中的几何信号足够捕捉训练数据组成信息。
