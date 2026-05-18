---
title: 'VGGT-Edit: Feed-forward Native 3D Scene Editing with Residual Field Prediction'
title_zh: VGGT-Edit：基于残差场预测的前馈式原生3D场景编辑
authors:
- Kaixin Zhu
- Yiwen Tang
- Yifan Yang
- Renrui Zhang
- Bohan Zeng
- Ziyu Guo
- Ruichuan An
- Zhou Liu
- Qizhi Chen
- Delin Qu
affiliations:
- Peking University
- Tencent
- The Chinese University of Hong Kong
- Shanghai AI Lab
- NTU
arxiv_id: '2605.15186'
url: https://arxiv.org/abs/2605.15186
pdf_url: https://arxiv.org/pdf/2605.15186
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 文本引导的前馈式3D场景编辑
tags:
- 3D Scene Editing
- Feed-forward
- Residual Field
- Text-conditioned
- Multi-view Consistency
- DeltaScene Dataset
one_liner: 提出深度同步文本注入与残差变换头，实现快速、多视角一致的文本驱动3D场景编辑。
practical_value: '- **3D编辑架构选择**：直接预测几何残差场而非2D-lifting，避免了纹理模糊和几何不一致，可借鉴到电商3D商品模型的快速修改中，保持多视角一致性。

  - **深度同步特征注入**：将文本语义特征按深度对齐到3D空间，确保指令跟随的稳定性，类似思路可用于多模态推荐中的跨模态对齐。

  - **数据集构造方法**：利用自动化管线结合3D一致性过滤生成高质量编辑对，为业务中构建3D编辑训练数据提供了一种高效范式。

  - **损失函数设计**：多目标损失联合约束几何精度和视角一致性，可迁移至其他3D生成或编辑任务的训练监督。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有前馈式3D重建模型无法响应动态编辑指令，而依赖2D-lifting的编辑方法因缺乏空间感知导致纹理模糊和几何不一致，限制了交互式应用。

**方法**：
1. **深度同步文本注入**：将文本条件特征与骨干网络的空间姿态（深度信息）对齐，稳定指令语义在3D空间的落地。
2. **残差变换头**：直接预测3D几何位移场，对场景进行可控变形，同时保持背景稳定。
3. **多目标损失**：联合几何精度损失与跨视角一致性约束，确保编辑结果的高保真。
4. **DeltaScene数据集**：通过自动化管线生成大规模编辑对，并利用3D一致性过滤保证真值质量。

**结果**：在实验上，VGGT-Edit相比2D-lifting基线，生成物体细节更锐利，多视角一致性显著增强，且推理速度接近即时。
