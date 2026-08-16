---
title: 'SCULPT: Subtractive Composition for 3D Part Generation'
title_zh: SCULPT：3D 部件生成的减法组合框架
authors:
- Sikuang Li
- Chen Yang
- Jiemin Fang
- Jiazhong Cen
- Yuhe Wei
- Jichen Pang
- Wei Shen
- Qi Tian
affiliations:
- Shanghai Jiao Tong University
- Huawei
arxiv_id: '2608.13541'
url: https://arxiv.org/abs/2608.13541
pdf_url: https://arxiv.org/pdf/2608.13541
published: '2026-08-13'
collected: '2026-08-16'
category: Multimodal
direction: 3D 生成 · 部件分解与组合
tags:
- 3D Generation
- Part-aware
- Diffusion Models
- Structured Latent
- Subtractive Composition
one_liner: 提出 SCULPT，在结构化 3D 隐空间内通过联合分割预测器迭代提取部件，实现部件级生成与整体重建的协同优化
practical_value: '- 借鉴“联合预测 + 耦合去噪”思路：在商品属性/标题/描述等多粒度生成任务中，避免先整体后拆分或先部件后拼接，而是让部分与整体在生成过程中互相条件化，减少不一致。

  - 借鉴“稀疏支持重叠而非强制划分”：在结构化表示（如商品品类树、标签体系）中，允许节点/标签表示存在重叠，避免硬聚类带来的边界噪声；类似 RAG 中的 chunk
  也可以重叠。

  - 借鉴“迭代减法 + 自适应停止条件”：在生成多模块内容（如 banner 多区块文案、推荐理由多段生成）时，从完整草稿开始逐步剥离生成子模块，并设置安全上限，让模块数量自适应输入。

  - 注意：本文是 3D 生成领域，业务直接迁移有限，主要价值在于生成式框架的设计思想。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有部件级 3D 生成方法分两类：分割式（先生成完整形状再分割）固定了物体后才确定部件边界；加性方法从预定义布局、盒子或 token 合成部件再组装，导致共享边界出现间隙、穿透和材质不连续。SCULPT 提出减法组合，在生成循环内直接产生部件与剩余物体的耦合关系。

**方法关键点**：给定结构化 3D 隐空间中的完整物体，SCULPT 迭代应用联合分割预测器，每次生成一个提取部件和更新后的剩余物体。预测器执行耦合去噪，同时以图像和当前 3D 状态为条件，使提取部件与剩余物体一起生成而非事后调和。处理时使用两者原生稀疏 3D 支持的并集，允许邻接支持重叠而不是强制体素不相交划分。迭代终止条件为剩余支持为空或达到固定安全上限，因此部件数量能自适应每个物体。

**关键结果**：在 PartObjaverse 基准上达到 SOTA 几何质量，同时零件组装后保持强完整物体重建。在四个数据集图像、一个文生图输入和一个真实照片上展示了细粒度纹理部件分解，超出基准能力。
