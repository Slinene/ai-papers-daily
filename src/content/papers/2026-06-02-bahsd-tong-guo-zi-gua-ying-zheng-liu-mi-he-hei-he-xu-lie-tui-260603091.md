---
title: 'BAHSD: Bridging the Long-tail Gap via Adaptive Distillation in Black-box Sequential
  Recommendation'
title_zh: BAHSD：通过自适应蒸馏弥合黑盒序列推荐中的长尾差距
authors:
- Xi Zhou
- Famin Wu
- Mingming Li
- Hongyue Zhang
- Jiao Dai
- Jizhong Han
- Tao Guo
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- School of Cyber Security, University of Chinese Academy of Sciences
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2606.03091'
url: https://arxiv.org/abs/2606.03091
pdf_url: https://arxiv.org/pdf/2606.03091
published: '2026-06-02'
collected: '2026-06-03'
category: RecSys
direction: 黑盒蒸馏 · 序列推荐长尾优化
tags:
- Black-box Distillation
- Sequential Recommendation
- Long-tail
- Knowledge Distillation
- Model Extraction
one_liner: 提出自适应蒸馏框架 BAHSD，用多尺度一致性探测与层次化目标缓解黑盒序列推荐中长尾信号异质性问题，尾部用户提升超 80%
practical_value: '- 若业务需从黑盒推荐 API 蒸馏学生模型，可借鉴自适应信号处理：用多尺度一致性隐式量化 teacher 预测的可靠性，再分治高低置信度样本。

  - 对头部用户易出现的偏好固化问题，采用动态温度 KL 散度平滑 teacher 分布，避免学生过度拟合局部模式，可迁移到召回/排序模型的蒸馏训练。

  - 对尾部用户交互稀疏、信号嘈杂的场景，引入排序一致性损失和 InfoNCE 对比学习，可提升学生模型的泛化性与噪声鲁棒性，适合电商长尾商品/冷启用户建模。

  - 该框架为即插即用方案，可在不改变基座模型结构的情况下以多层损失注入，工程实现成本较低，适合快速验证。'
score: 8
source: arxiv-cs.IR
depth: abstract
---

**动机**：序列推荐系统常以黑盒 API 部署，模型提取面临长尾分布导致的信号异质性——头部序列 teacher 偏好固化，学生学偏局部模式；尾部稀疏序列 teacher 预测扁平噪声大。现有统一蒸馏忽略该差异，导致尾部过拟合噪声、知识迁移差。

**方法**：提出 BAHSD，包含两个核心设计：(1) 多尺度一致性探测机制，通过在不同 dropout/扰动下 teacher 预测的一致性程度隐式量化每个样本的监督信号可靠性；(2) 自适应层次目标，对高可靠性信号采用动态温度 KL 散度减轻偏好固化，对低可靠性信号采用排序一致性损失与 InfoNCE 对比学习进行噪声鲁棒增强。

**结果**：在多个数据集上，BAHSD 一致优于基线，相对 teacher 最高提 4.98%，尾部用户指标提升超 80%，验证了其高效黑盒知识迁移能力。
