---
title: 'RegionFed: Federated Learning for Personalized Query Understanding in Heterogeneous
  Retail Environments'
title_zh: RegionFed：异构零售环境下查询理解的联邦个性化学习
authors:
- Quoc H. Nguyen
- Ali Lafzi
- Abhijeet Phatak
- Siddharth Pratap Singh
- Rohit Upadhyay
- Yogananda Domlur Seetharama
- Chittaranjan Tripathy
affiliations:
- Walmart Global Tech
arxiv_id: '2609.05403'
url: https://arxiv.org/abs/2609.05403
pdf_url: https://arxiv.org/pdf/2609.05403
published: '2026-09-04'
collected: '2026-09-08'
category: Training
direction: 联邦学习个性化训练 · 梯度级路由
tags:
- Federated Learning
- Personalization
- Query Understanding
- Transformer
- Differential Privacy
- Retail Search
one_liner: 提出梯度级联邦个性化框架 RegionFed，用区域与全局梯度冲突路由个性化策略，在 transformer 上避免参数级方法崩溃
practical_value: '- 在电商搜索的多地域/多人群 Query 理解模型（如意图分类、实体识别、拼写纠错）需要联邦学习或去中心化训练时，优先采用梯度级个性化，而非在
  T5/RoBERTa 等 transformer 上做参数级个性化；后者因 tied embeddings 和 LayerNorm 交互可能崩溃，RegionFed
  的梯度冲突路由可规避。

  - 将区域梯度与全局梯度的 ℓ2 冲突作为诊断信号，动态决定每个区域是否需要独立模型/适配器，避免对所有区域盲目做个性化，可节省 GPU 与维护成本；该信号也可作为后续
  A/B 测试的分流依据。

  - RegionFed 对模型结构零侵入，适合在不改线上模型代码的前提下快速验证个性化收益；如果业务已用 T5/RoBERTa 等成熟 backbone，可复用该思路做跨流量段个性化，无需引入新架构。

  - 隐私敏感场景下，其 ε≈0.60 差分隐私与 O(1/√T) 收敛保障可作为合规方案参考，但需注意论文在公开数据集上验证，迁移到亿级真实流量前应评估通信与客户端规模。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：零售搜索系统跨地域存在显著差异——query 模式、词汇、商品偏好不同，导致数据异构。联邦学习能保护隐私，但标准 FL 的全局模型会牺牲区域性能；已有个性化 FL 方法在参数层面操作，在 T5 等现代 transformer 上因 tied embeddings 与 LayerNorm 相互作用而崩溃（准确率低于 10%）。

**方法关键点**：RegionFed 完全在梯度层面操作，避免参数级个性化在 transformer 上的失效。核心信号是区域梯度与全局梯度的 ℓ2 冲突，统一用于：诊断异构性、为每个区域路由到最便宜且足够的个性化策略、自适应控制个性化强度。模型被视为可微黑盒，部署到 T5-Small、T5-3B、RoBERTa、CNN 时零代码改动。

**关键结果数字**：在 Amazon ESCI、Amazon Reviews、LEAF-FEMNIST 三个公开数据集和四种架构上，RegionFed-Meta 达到 92.27%，接近集中式上界（Centralized + Regional Weighting：92.04%，Δ=0.23pp，1σ 以内），同时提供 ε≈0.60 差分隐私和 O(1/√T) 收敛保证。
