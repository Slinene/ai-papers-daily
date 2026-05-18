---
title: 'MIND: Decoupling Model-Induced Label Noise via Latent Manifold Disentanglement'
title_zh: MIND：通过潜在流形解耦分离模型诱导的标签噪声
authors:
- Dayong Ren
affiliations:
- State Key Laboratory of Novel Software Technology, Nanjing University
arxiv_id: '2605.16081'
url: https://arxiv.org/abs/2605.16081
pdf_url: https://arxiv.org/pdf/2605.16081
published: '2026-05-15'
collected: '2026-05-18'
category: Training
direction: 标签噪声鲁棒学习 · 潜在流形解耦
tags:
- label noise
- manifold disentanglement
- pseudo-label
- foundation model distillation
- noise transition matrix
one_liner: 将模型诱导的系统性标签噪声解耦为子空间依赖成分，用动态聚类估计噪声以校正伪标注。
practical_value: '- 在电商商品自动分类/属性标注中，使用伪标签训练时，可借鉴LDE模块动态聚类识别系统性错误模式，提升伪标签质量。

  - 作为基础模型蒸馏的鲁棒框架，在生成式推荐（如用VLM生成商品描述）中校正幻觉噪声，避免错误级联。

  - 为Agent反馈信号去噪提供思路：通过将噪声与数据流形解耦，识别智能体交互中重复出现的偏差模式，提高强化训练稳定性。

  - 采用分层噪声鲁棒性评估协议，设计更贴近真实分布外噪声的结构压力测试，评估实际部署中的模型韧性。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：自动标注范式依赖预训练基础模型生成伪标签，但引入“模型诱导的标签噪声”——并非随机扰动，而是与数据局部流形紧密耦合的系统性错误。现有全局转移矩阵方法欠拟合此类结构模式，而实例特异性矩阵又难以求解。

**方法**：提出MIND框架，通过潜在流形解耦将高维噪声流形分解为可处理的子空间依赖成分。核心模块Latent Decoupling Estimator (LDE)将样本动态投影到潜在结构簇，每个簇内错误模式一致，从而无需干净锚点即可识别和校正噪声。

**结果**：在CIFAR-100合成噪声和S3DIS/ScanNet真实3D分割数据上，MIND显著超越SOTA；并能有效校正Vision-Language Models（如OpenSeg）的零样本幻觉错误，验证其作为基础模型鲁棒蒸馏框架的潜力。
