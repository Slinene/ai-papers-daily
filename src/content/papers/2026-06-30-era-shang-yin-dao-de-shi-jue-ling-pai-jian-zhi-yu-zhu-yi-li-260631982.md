---
title: 'ERA: Entropy-Guided Visual Token Pruning with Rectified Attention for Efficient
  MLLMs'
title_zh: ERA：熵引导的视觉令牌剪枝与注意力矫正框架
authors:
- Yuhao Wang
- Mu Qiao
- Haiwen Diao
- Yunzhi Zhuge
- Pingping Zhang
- Xindong Zhang
- Lei Zhang
- Huchuan Lu
arxiv_id: '2606.31982'
url: https://arxiv.org/abs/2606.31982
pdf_url: https://arxiv.org/pdf/2606.31982
published: '2026-06-30'
collected: '2026-07-01'
category: Multimodal
direction: 多模态大模型推理加速
tags:
- visual token pruning
- attention rectification
- entropy-guided
- training-free
- MLLM inference
one_liner: 提出训练免视觉令牌剪枝框架ERA，通过熵引导和注意力矫正解决logit崩塌，实现高效MLLMs
practical_value: '- **训练免剪枝方法**：可直接应用于商品图文理解等现有多模态模型，快速降低视觉令牌数量，减少推理延迟，无需重新训练。

  - **熵引导锚点选择**：利用视觉多样性和注意力头显著性保留商品图像关键区域（如主体细节），防止重要视觉信息丢失。

  - **偏置回收与注意力矫正**：在广告图片或视频帧压缩后，通过回收剪枝令牌信息并注入logit偏置，维持注意力分布一致，避免输出漂移。

  - **即插即用组件**：DEP、BTR、LAR可模块化嵌入推理流程，适合实时推荐、多模态Agent等对延迟敏感的场景。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：多模态大语言模型（MLLMs）因视觉令牌序列过长导致推理成本高昂，现有训练免令牌减少方法会扭曲注意力分布，引发“注意力logit崩塌”。  
**方法**：提出ERA框架，包含三个关键组件：  
- **双视图熵剪枝（DEP）**：联合建模视觉多样性与注意力头显著性，选取代表性锚点令牌。  
- **偏置感知令牌回收（BTR）**：将剪枝的令牌信息聚合到对应锚点，并估计簇级logit偏置。  
- **logit保留注意力矫正（LAR）**：将估计的偏置注入注意力logit，修正令牌减少导致的注意力崩溃。  
**结果**：在多种MLLMs上，单图、多图及视频场景下，即使高压剪率（如保留少量令牌）也能保持鲁棒性能，实现推理加速与视觉证据保留的统一。
