---
title: 'MG-Thinker: Bi-Axial Self-Reflection for Multi-Image Reasoning Grounding'
title_zh: MG-Thinker：多图像推理定位的双轴自反思框架
authors:
- Heyu Huang
- Chi Chen
- Zonghao Guo
- Yuhua Li
- Maosong Sun
- Ruixuan Li
affiliations:
- Huazhong University of Science and Technology
- Tsinghua University
arxiv_id: '2609.37374'
url: https://arxiv.org/abs/2609.37374
pdf_url: https://arxiv.org/pdf/2609.37374
published: '2026-09-29'
collected: '2026-10-04'
category: Multimodal
direction: 多模态推理定位 · RL 后训练
tags:
- Multimodal
- Reinforcement Learning
- Grounding
- Multi-Image
- Chain-of-Thought
- Post-training
one_liner: 提出MG-Thinker后训练RL框架，通过层次化推理与双轴优势分解提升多图像推理定位性能
practical_value: '- **BiA-DAPO 优势分解可借鉴到多任务/多场景推荐 RL 训练**：将 rollout 优势沿组内信号轴和组间能力轴分解，能缓解不同任务难度、不同用户群体样本分布异质带来的优势估计偏差，适合电商推荐中不同品类、不同活跃度用户的差异化建模。

  - **任务自适应 CoT 可迁移到 Agent 规划与复杂查询理解**：根据任务难度动态调整思维链粒度——简单 query 直接生成、复杂 query 多步推理，能节省
  token 并提升推理效率，可用于搜索广告中的 query 改写或商品推荐理由生成。

  - **候选池稳定组级统计的方法值得工程实现借鉴**：在 RL 训练中维护候选池以获得稳定的组级统计量，可迁移到推荐模型的在线学习或 A/B 测试分桶中，减少小样本波动对策略更新的影响。

  - **层次化推理范式可复用于多模态商品理解**：从粗到细定位（先全局场景后局部细节）的思路，适合电商中多角度商品图、视频帧的细粒度视觉定位任务，如自动识别商品瑕疵或关键属性区域。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有 RL 方法在多模态推理上取得进展，但用于多图像推理定位（MRG）时，忽略了该任务的两大特性：粗到细的层次推理模式，以及任务-样本难度的异质分布。这导致模型在真实多图像场景下难以稳定收敛到像素级精确输出。

**方法关键点**：
- 提出 MG-Thinker 后训练 RL 框架，构建 25K MRG 数据集，标注任务自适应 Chain-of-Thought（CoT），引导模型先收集多视角证据再下结论。
- 设计 Bi-Axial DAPO（BiA-DAPO），将 rollout 优势沿两个轴分解：组内信号轴捕捉同一任务组内样本的相对优劣，组间能力轴刻画不同任务组之间的难度差异；两个机制均基于定义的候选池计算稳定组级统计。
- 框架支持层次化推理：先从粗粒度全局理解到细粒度局部定位。

**关键结果**：MG-Thinker 在多图像推理定位任务上取得 SOTA，并在多图像理解和多种多模态基准上展现出一致的泛化提升。
