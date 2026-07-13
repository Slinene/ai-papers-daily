---
title: Robustifying Vision-Language Models via Test-Time Prompt Adaptation
title_zh: 通过测试时提示自适应增强视觉-语言模型鲁棒性
authors:
- Xingyu Zhu
- Huanshen Wu
- Shuo Wang
- Beier Zhu
- Jiannan Ge
- Jiaheng Zhang
- Long Chen
affiliations:
- National University of Singapore
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2607.09450'
url: https://arxiv.org/abs/2607.09450
pdf_url: https://arxiv.org/pdf/2607.09450
published: '2026-07-10'
collected: '2026-07-13'
category: Multimodal
direction: 测试时自适应 · 多模态对齐 · 对抗鲁棒性
tags:
- Test-Time Adaptation
- Vision-Language Models
- Adversarial Robustness
- Optimal Transport
- Prompt Tuning
- Distribution Alignment
one_liner: 提出分布级最优传输对齐与动态缓存的测试时提示适应方法，大幅提升VLM对抗鲁棒性且无损清洁性能
practical_value: '- 测试时适应思想可迁移至搜索推荐系统的在线学习：当数据分布因季节、事件或对抗攻击发生偏移，借鉴RITA的分布级对齐而非样本级校正，提升模型鲁棒性。

  - 多模态推荐中视觉与文本特征对齐是关键瓶颈：最优传输（Optimal Transport）的分布匹配方法可直接用于对齐商品图像与标题（或用户评论）的特征空间，缓解语义错位。

  - 动态缓存（dynamic cache）累积可靠测试样本的思路适合电商推荐的高频流式更新：设计信任度阈值，仅将高质量预测样本加入缓存，逐步优化提示或轻量适配器，实现低延迟在线进化。

  - 增强视图（augmented views）保留语义完整性的观察可启发搜索推荐中的“多视图”特征利用：例如同一商品的不同角度、背景，通过分布视角聚合来抵抗图像噪声或恶意对抗样本。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：CLIP等视觉语言模型面对对抗扰动时性能急剧下降，现有测试时适应方法依赖样本级置信度启发式，无法区分自信的对抗误判与语义一致的预测，忽视了数据的整体分布结构。作者观察到，对抗扰动虽破坏整体表征，但增强视图的分布往往保留语义完整性，由此提出从样本级估计转向分布级对齐。

**方法关键点**：提出RITA（Robust Test-Time Prompt Adaptation）框架，核心包括两部分。① 使用最优传输将增强视图的视觉特征分布与文本类原型分布对齐，通过最小化Wasserstein距离校正跨模态语义错位并抑制对抗离群点。② 引入动态缓存，在测试流中渐进积累可靠线索，用于在线细化文本提示，从而持续提升鲁棒性。

**关键结果**：在多个对抗基准上，RITA显著提升对抗鲁棒性（例如对抗攻击下准确率大幅回升），同时保持甚至轻微提升清洁数据准确率，优于现有测试时适应方法。
