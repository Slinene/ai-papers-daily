---
title: Entropic Auto-Encoding via Implicit Free-Energy Minimization
title_zh: 熵自编码器：通过隐式自由能最小化避免后验坍塌
authors:
- Hazhir Aliahmadi
- Irina Babayan
- Greg van Anders
affiliations:
- Queen’s University
arxiv_id: '2605.16164'
url: https://arxiv.org/abs/2605.16164
pdf_url: https://arxiv.org/pdf/2605.16164
published: '2026-05-15'
collected: '2026-05-18'
category: GenRec
direction: 生成模型训练 · 抗后验坍塌
tags:
- posterior collapse
- entropic autoencoder
- free energy
- latent representation
- variational inference
- unsupervised learning
one_liner: 只用重建损失，通过编码器集成与熵隐式生成先验，解决VAE后验坍塌问题
practical_value: '- 在推荐系统的表示学习（如用户/物品潜变量）中，可用类似框架：**仅保留重建损失，放弃显式KL正则**，通过编码器集成与熵约束隐式形成结构化潜空间，避免后验坍塌导致表示退化。

  - 多模态隐空间（本工作的非高斯、多模态分布）**天然适合捕获用户行为的多意图性**，例如电商用户会话中隐含的类别/风格层级，可借鉴EAE的层次化解耦能力。

  - 自由能最小化集成训练方法（多个编码器协同）可迁移到**多智能体或分布式特征提取场景**，通过参数扰动扩展搜索范围，缓解单一编码器陷入无信息表示。

  - 工程实现上，该方法无需修改现有自编码器架构，**改动仅在于损失函数与编码器前向过程**，易于在PyTorch/TF中尝试，尤其适合处理后验坍塌严重的稀疏数据（如行为序列）。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：变分自编码器（VAE）因显式KL散度迫使后验向高斯先验对齐，频繁发生后验坍塌，导致潜变量被忽视，表示学习失效。现有解释归因于KL压力或优化难题，但根本在于显式先验的强硬约束。

**方法**：提出熵自编码器（EAE），彻底移除显式KL项，**仅保留重建损失作为唯一显式目标**。潜变量先验通过熵最小化隐式产生：维护一个编码器集成（free-energy ensemble），借助物理自由能原理，搜索过程偏向损失景观中高容量近优区域，并由解码器梯度引导至有信息表征。训练时编码器参数在集成中演化，无需额外正则项，自发形成结构化隐空间。

**结果**：在反应-扩散过程数据上，EAE成功恢复低维动力学叠加态；在MNIST上，隐空间自发呈现类别分组；在CelebA上，展现出“所有人类→个体特征”的层次化面部结构。生成的样本多样且数据一致，有效缓解后验坍塌，且无需显式先验选择。
