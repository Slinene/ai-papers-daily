---
title: 'Looking Farther with Confidence: Uncertainty-Guided Future Learning for Sequential
  Recommendation'
title_zh: 不确定性引导的未来学习增强序列推荐
authors:
- Ziqiang Cui
- Xing Tang
- Peiyang Liu
- Xiaokun Zhang
- Shiwei Li
- Xiuqiang He
- Chen Ma
affiliations:
- City University of Hong Kong
- Shenzhen Technology University
- Peking University
- Huazhong University of Science and Technology
arxiv_id: '2605.28493'
url: https://arxiv.org/abs/2605.28493
pdf_url: https://arxiv.org/pdf/2605.28493
published: '2026-05-27'
collected: '2026-05-28'
category: RecSys
direction: 序列推荐 · 未来监督 · 不确定性估计
tags:
- Sequential Recommendation
- Future Supervision
- Uncertainty Estimation
- Self-Supervised Learning
- Contrastive Learning
one_liner: 提出不确定感知框架，根据模型对当前预测的置信度动态调节多步未来监督权重，显著提升序列推荐性能
practical_value: '- **自适应未来监督权重**：用当前预测的熵计算实例级权重，对不确定样本降低未来监督强度，避免噪声注入。可直接复用到电商序列模型的训练中，尤其适合用户行为稀疏或点击噪声多的场景。

  - **零推理开销的辅助训练**：未来监督和对比学习仅作为训练期正则化，推理时完全移除，不增加线上延时。业务中可放心加入未来辅助任务，不影响部署效率。

  - **未来对比学习对齐全局趋势**：将未来K个物品的嵌入做平均池化作为“未来视野”正样本，与当前用户表示对齐，然后区分其他用户的未来视野。这种全局偏好对齐可强化用户长期兴趣的建模，适合长周期购买决策的商品推荐。

  - **模型无关的即插即用设计**：框架可集成到Transformer、LLM增强等不同骨干结构上，实验表明对SASRec、DuoRec、LLM-ESR均有稳定提升，适合在现有推荐系统中快速尝试。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：序列推荐常因数据稀疏而受限，现有自监督方法仅利用下一个物品作为监督，忽视远期交互中的丰富信息。少量工作（如FENRec）尝试加入未来监督，但对所有样本施加等权未来损失，在模型对当前预测不确定时会引入有害噪声，损害主任务性能。

**方法关键点**
- **不确定性引导的未来监督**：对每个训练样本，并行预测未来1~K步的物品（通过轻量投影头），同时计算主任务预测分布的香农熵，得到实例级权重 ω = exp(-H/τ)，将加权后的未来交叉熵损失作为辅助目标。高熵（不确定）时 ω 趋近0，迫使模型聚焦当下；低熵（确定）时 ω 趋近1，鼓励看得更远。
- **未来感知对比学习**：将未来K个物品的嵌入均值作为“未来视野”表示，通过单独的投影头将当前用户表示映射到对比空间，用InfoNCE损失拉近与自身未来视野的距离，推远批次内其他用户未来视野。
- **纯训练期模块**：所有辅助任务仅在训练时存在，推理时完全去除，计算开销为零。

**关键实验与结果**
- 数据集：Yelp（POI）、Amazon Sports、Beauty、Office（电商）。
- 基线：13种方法，含传统（SASRec、BERT4Rec）、LLM增强（LRD、LLM-ESR）、自监督（S³-Rec、CL4SRec、FENRec等）。
- UFRec在所有数据集全部指标上均显著最优，HR@20最高相对提升10.88%（Yelp），NDCG@20最高提升9.41%。
- 消融：去除不确定性调制（w/o UG）导致性能急剧下降，甚至比完全去掉未来监督更差，验证自适应加权机制的关键性；各组件均必要。
- 泛化性：在SASRec、LLM-ESR、DuoRec骨干上附加UFRec，HR@20相对提升7.5%~13.6%，框架模型无关。
- 超参数：K=2~4，τ=3~5，λ=0.05~0.2 通常较优；稀疏用户组上优势依旧明显。

**核心启示**：“模型不确定时，少看未来；模型确定时，多看未来”这一简单但有效的思想，为利用序列未来信息提供了安全且高效的正则化范式。
