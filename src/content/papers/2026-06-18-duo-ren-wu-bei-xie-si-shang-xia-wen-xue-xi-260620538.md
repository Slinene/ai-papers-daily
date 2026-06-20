---
title: Multi-Task Bayesian In-Context Learning
title_zh: 多任务贝叶斯上下文学习
authors:
- Qingyang Zhu
- Eric Karl Oermann
- Kyunghyun Cho
affiliations:
- New York University
- NYU Langone Health
arxiv_id: '2606.20538'
url: https://arxiv.org/abs/2606.20538
pdf_url: https://arxiv.org/pdf/2606.20538
published: '2026-06-18'
collected: '2026-06-20'
category: Training
direction: 摊销贝叶斯推理 · 先验自适应上下文学习
tags:
- In-Context Learning
- Bayesian Inference
- Amortized Inference
- Uncertainty Quantification
- Distribution Shift
one_liner: 将先验信息表示为上下文数据集前缀，训练Transformer快速适应不同先验的贝叶斯预测推理
practical_value: '- 在推荐系统中，利用类似上下文学习机制快速适应新的用户群体或变化偏好：将少量历史交互作为上下文示例，模型动态调整预测分布，无需微调。

  - 为推荐模型提供轻量级的不确定性量化：预测分布可直接用于探索-利用决策，提升数据效率。

  - 将用户/物品元特征或领域知识构造为先验前缀，使模型在推理时即插即用适应新场景，缓解冷启动与分布偏移问题。

  - 工程上可作为元学习组件嵌入现有多任务推荐管道，只需增加少量上下文 token 开销，实现快速任务适应。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有摊销贝叶斯推理方法（如 PFN）依赖固定的训练先验，当测试任务来自未见过的新先验时预测性能急剧退化。实际应用中先验分布往往随时间或环境变化，急需能够动态适应不同先验的推断方法。

**方法关键点**：提出多任务上下文学习框架，将先验信息显式编码为 in-context 数据集的前缀（prior prefix）。用 Transformer 在大规模多任务序列上训练，每个序列包含来自同一先验的多个 prior task 和 target task 的数据点。模型由此学会从 prior prefix 中提取先验信息，并据此调整目标任务的预测分布，实现跨先验族的快速自适应。训练目标是最小化后验预测分布的变分界，支持高维潜在结构。

**关键结果**：在合成数据集、分布外先验以及高维随机效应模型上，该方法达到与 oracle 贝叶斯预测器一致的性能，且推理速度提升数个数量级。在真实世界时空温度预测任务上同样超越基线，展示了在分布偏移下的鲁棒性和计算效率优势。
