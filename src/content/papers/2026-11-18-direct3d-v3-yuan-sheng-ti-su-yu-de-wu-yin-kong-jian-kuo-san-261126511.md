---
title: 'Direct3D-V3: Latent-Free Diffusion Transformers in the Native Voxel Domain'
title_zh: Direct3D-V3：原生体素域的无隐空间扩散Transformer
authors:
- Shuang Wu
- Jiachen Qian
- Youtian Lin
- Feihu Zhang
- Philip Torr
- Yao Yao
- Xun Cao
affiliations:
- Nanjing University
- DreamTech
- The University of Hong Kong
- University of Oxford
arxiv_id: '2611.26511'
url: https://arxiv.org/abs/2611.26511
pdf_url: https://arxiv.org/pdf/2611.26511
published: '2026-11-18'
collected: '2026-11-21'
category: Multimodal
direction: 3D生成 · 原生体素扩散Transformer
tags:
- Diffusion Transformer
- 3D Generation
- Latent-Free
- SDF Voxel
- Implicit Manifold Regularization
- Camera Prediction
one_liner: 去除VAE直接在原生SDF体素上训练扩散Transformer，通过隐式流形正则和相机预测提升细节与一致性
practical_value: '- 架构选择：若业务中两阶段压缩-生成流程（如先聚成Semantic ID再生成推荐列表）存在重建瓶颈，可尝试去除中间压缩，直接在原生高维空间（如item
  token序列）训练扩散/生成式模型，用适合稀疏高维输入的损失替代重建损失，保留细节信息。

  - 辅助任务对齐：通过预测条件信号的潜在属性（如本文预测相机参数）作为辅助任务，可提升生成结果与输入条件的一致性。在query/推荐生成中，可增加预测用户意图类别、商品属性等辅助头，强化条件建模。

  - 隐式正则：对生成的结构化输出（如商品序列、图结构）加入邻域一致性/流形正则，可在不引入复杂后处理的情况下提升输出质量；采用Marching Cubes类可微转换让生成结果直接受下游任务监督，也是值得借鉴的端到端训练思路。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有原生3D生成大多基于latent diffusion，依赖VAE将几何压缩到隐空间，存在两个内在局限：VAE重建会移除细粒度几何细节；两阶段流程存在目标不一致（VAE为重建训练，扩散模型为分布匹配训练）。

**方法关键点**：Direct3D-V3提出latent-free扩散Transformer框架，完全丢弃VAE，在原生体素域直接建模原始SDF体素网格。为保障几何可靠性，引入邻域体素的隐式流形正则，抑制非水密表面；通过Marching Cubes将预测SDF转为网格，用渲染法线损失直接监督模型。同时，预测条件图像的相机参数作为辅助任务，鼓励DiT学习从图像观测到3D形状的映射。

**关键结果**：该设计消除了重建瓶颈，使训练直接在原生体素域进行，生成的网格局部细节显著更丰富；预测相机与原生SDF输出使模型可扩展到生成式重建，扩散过程与法线引导细化交错，在保留未见区域生成先验的同时提升与观测视角的对齐质量。
