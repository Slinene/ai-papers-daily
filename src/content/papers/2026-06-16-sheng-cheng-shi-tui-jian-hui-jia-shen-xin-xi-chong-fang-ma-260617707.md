---
title: Do Generative Recommenders Deepen the Information Cocoon? A Closed-Loop Simulation
  with LLM-powered User Simulators
title_zh: 生成式推荐会加深信息茧房吗？一项基于LLM用户模拟的闭环仿真研究
authors:
- Jiyuan Yang
- Gengxin Sun
- Mengqi Zhang
- Lingjie Wang
- Yuanzi Li
- Hongxi Cui
- Xin Xin
- Pengjie Ren
affiliations:
- Shandong University
- Renmin University of China
- Shandong Provincial Key Laboratory of Computing-Network Integration
- Qingdao Key Laboratory of Trustworthy Artificial Intelligence
arxiv_id: '2606.17707'
url: https://arxiv.org/abs/2606.17707
pdf_url: https://arxiv.org/pdf/2606.17707
published: '2026-06-16'
collected: '2026-06-17'
category: RecSys
direction: 生成式推荐信息茧房闭环模拟
tags:
- 信息茧房
- 生成式推荐
- 闭环仿真
- LLM用户模拟
- Semantic ID
- 代码空间塌缩
one_liner: 生成式推荐减缓类别级曝光塌缩但仍在代码空间形成结构性茧房，语义ID与更大模型有助于抵抗蚕食
practical_value: '- **用LLM用户模拟器做闭环评估**：在生成式推荐上线前，可参考RecLoop框架搭建“推荐-交互-重训”循环，用LLM agent模拟用户偏好演化，评估长期信息茧房风险，尤其适合需要对算法负向效应进行离线预测的电商/广告场景。

  - **监控代码空间的结构化茧房**：除了曝光指标，还应监控生成式模型离散码空间的层级熵与Top-κ集中度，重点观察粗粒度层的塌缩，一旦发现早期路由码高度集中，即使终端物品多样化，信息茧房已开始形成。

  - **tokenization策略的取舍**：实验表明Semantic ID比Collaborative ID产生的茧房更轻，因此在电商生成式推荐中优先采用语义量化而不是协同聚类，可以减少流行度偏差向代码空间的迁移。

  - **模型容量作为缓冲**：更大规模的生成模型（如OneRec 3B vs 0.5B）能保持更宽广的活跃码空间，对抗茧房塌缩，所以在算力允许时选择较大LLM
  backbone有助于长期信息多样化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：传统ID推荐在反馈循环中容易形成信息茧房（暴露范围收窄、用户间同质化加剧），但生成式推荐将物品表示为多级离散码序列并自回归生成，这一范式转移对茧房效应的影响未知。该工作旨在系统对比生成式推荐与传统序列推荐在闭环交互下的茧房动力学。

**方法**：
- 提出RecLoop框架：耦合推荐模块与LLM驱动的用户模拟器，构建“推荐 → 用户选择 → 数据更新 → 模型重训”的15轮闭环模拟。
- 用户模拟器：基于Qwen3-8B的LLM agent，包含动态用户画像、双记忆系统（长短期）、周期性反思机制，以保留历史偏好并演化兴趣。
- 推荐模型：2个生成式（TIGER、OneRec）和2个传统序列模型（SASRec、Mamba4Rec），在Amazon Office和Toys & Games数据集上对比。
- 评估指标：曝光级（类别熵、Jaccard同质度、覆盖率、Gini集中度）以及代码空间级（层熵、Top-κ码集中度）的结构性茧房度量。

**关键结果**：
- 生成式推荐普遍减缓曝光级茧房：类别熵下降更慢，用户间Jaccard相似度更低（Office上SASRec 0.223 vs OneRec 0.064），但Gini系数在所有模型上仍上升，即无法完全阻止头部物品集中。
- 代码空间内检测到结构性茧房：粗粒度码层塌缩显著，TIGER第0层码熵降低53.6%，而最细层仅降13.4%；OneRec的第0层码的Top-10概率质量升至86.6%，意味着大部分推荐仅路由通过少数粗语义簇。
- 语义ID vs 协同ID：协同ID导致更严重的代码前缀多样性下降，而语义ID能更好保持码空间广度。
- 模型尺度效应：更大的生成模型（如OneRec 3B）能显著减缓码空间塌缩，保留更多尾部分类访问能力。

**核心结论**：生成推荐并非免疫茧房，而是将塌缩压力从物品类别级转移至内部码空间的粗粒度层；选择合适的tokenization策略与足够大的模型容量可有效缓冲这一趋势。
