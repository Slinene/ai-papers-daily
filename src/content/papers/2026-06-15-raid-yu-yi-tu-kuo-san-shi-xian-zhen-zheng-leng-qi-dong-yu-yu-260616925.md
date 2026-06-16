---
title: 'RAID: Semantic Graph Diffusion for True Cold-Start and Cross-Lingual Forecasting'
title_zh: RAID：语义图扩散实现真正冷启动与跨语言预测
authors:
- Arunkumar V
- Manoranjan Gandhudi
- Gangadharan G. R.
- Arun Prakash
- S. Senthilkumar
affiliations:
- University College of Engineering, Anna University Tiruchirappalli
- Central University of Karnataka
- National Institute of Technology Tiruchirappalli
- Jawaharlal Nehru University
arxiv_id: '2606.16925'
url: https://arxiv.org/abs/2606.16925
pdf_url: https://arxiv.org/pdf/2606.16925
published: '2026-06-15'
collected: '2026-06-16'
category: RecSys
direction: 语义图扩散 · 冷启动预测
tags:
- cold-start
- semantic graph
- diffusion model
- multilingual
- retrieval-augmented
- time-series forecasting
one_liner: 利用元数据语义检索与图扩散，在无历史数据的真冷启动场景下实现时间序列预测并显著降低延迟
practical_value: '- **物品冷启动预测**：用商品的文本描述（标题、描述等）生成语义嵌入，检索相似商品的历史时间序列，聚合邻居序列得到基础预测，可解决新品销量/需求预测无历史数据的问题。

  - **不确定性量化**：门控扩散模块在基础预测上建模残差分布，输出预测区间而非点估计，适合库存管理、促销决策中的风险控制。

  - **低延迟非自回归解码**：非自回归生成方式使推理延迟降低一个数量级，对在线推荐、实时定价等时效性要求高的场景尤其重要。

  - **多语言共享语义空间**：利用冻结的多语言嵌入模型，单一英文训练模型可直接预测其他语言描述的商品，降低跨国业务的多语言维护成本。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有时间序列基础模型（如 Chronos、TimesFM）依赖历史窗口，在全新物品无任何观测值的真正冷启动场景下失效，且自回归推理延迟高。

**方法关键点**：
- **元数据驱动的语义检索**：将物品文本元数据用冻结的多语言嵌入模型映射到共享语义空间，构建归纳式检索图，使模型泛化到未见过的新物品。
- **图条件扩散**：先通过聚合语义邻居的历史序列形成基础预测，再用门控扩散模块细化，建模残差不确定性并输出预测区间。
- **非自回归解码**：一次性生成整个预测序列，大幅降低推理延迟。

**关键结果**：在严格真冷启动协议下，RAID 在预测准确率（如 MASE、RMSE）和预测区间覆盖率上均优于 TimesFM、Chronos 等基础模型及竞争基线；推理延迟降低一个数量级；零样本跨语言迁移实验验证了多语言泛化能力。
