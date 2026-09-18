---
title: Region-Level Policy Optimization for Fine-grained MLLM Perception
title_zh: 细粒度 MLLM 感知的区域级策略优化
authors:
- Yuheng Shi
- Xiaohuan Pei
- Minjing Dong
- Chang Xu
affiliations:
- University of Sydney
- City University of Hong Kong
arxiv_id: '2609.19745'
url: https://arxiv.org/abs/2609.19745
pdf_url: https://arxiv.org/pdf/2609.19745
published: '2026-09-16'
collected: '2026-09-18'
category: Multimodal
direction: 多模态视觉感知 · 稀疏 token 选择
tags:
- Region-level RL
- MLLM
- Fine-grained perception
- Visual token compression
- Sparse encoding
- Proposal network
one_liner: 用区域级强化学习训练轻量提案网络，以约 4 倍更少视觉 token 超越全分辨率 MLLM 的细粒度准确率
practical_value: '- **借鉴区域级 RL 训练前处理筛选器**：在商品图、广告图或多模态内容理解中，先用轻量网络从全局粗粒度视图定位关键区域（如商品主体、文字标签），再对候选区域做高分辨率编码，可大幅降低
  MLLM 的 token 成本；冻结大模型只更新提案网络，适合基座模型昂贵、不想全量微调的业务场景。

  - **用 remove/add 双目标做无监督奖励**：以“移除某区域导致答案似然下降”作为负面信号抑制噪声，“补回丢失区域提升似然”作为正信号恢复缺失证据。不需要标注框或
  reasoning trajectory，可直接迁移到推荐系统多模态召回/排序：用大模型对候选内容打分差异作为奖励，训练轻量重要性评估器筛掉无关图像区域或视频帧。

  - **稀疏编码放大证据区域而非均匀下采样**：将视觉 token 集中到选中区域并降低背景分辨率，可用同等算力提升信息密度。在电商视频理解、直播切片审核等场景，可先选高信息量帧/区域再输入生成式推荐模型，兼顾成本与细粒度表征。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：MLLM 处理细粒度视觉任务通常靠提高分辨率，但视觉 token 数量剧增导致编码和 prefill 成本膨胀。诊断实验发现，定位 RoI 和识别内容所需分辨率不同——定位可承受约 3-4 倍更强的 token 压缩，因此可以从粗视图定位、集中分辨率到关键证据。

**方法关键点**：提出 Vision-RL2，训练一个轻量级区域提案网络从粗粒度全局视图定位 RoI。将连贯区域视为 action，用冻结的 MLLM reader 评估移除该区域对答案似然的影响作为 reward；设计 subtractive 目标抑制分散注意力的 proposal，additive 目标恢复缺失证据；仅更新提案网络，无需区域标注、response sampling 或 reasoning trajectory。精炼后的提案进一步支持稀疏编码，放大证据 token 并排除背景。

**关键结果**：在 6 个细粒度基准和 4 个 MLLM backbone 上，Vision-RL2 在每个 token 预算下都优于 base model，用约 4 倍更少的视觉 token 超过 base 模型最大预算的准确率；相同 token 限制下超过此前 SOTA 方法，训练参数量少一个数量级。
