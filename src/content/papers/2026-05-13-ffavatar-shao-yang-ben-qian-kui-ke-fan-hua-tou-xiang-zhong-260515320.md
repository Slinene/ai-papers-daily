---
title: 'FFAvatar: Few-Shot, Feed-Forward, and Generalizable Avatar Reconstruction'
title_zh: FFAvatar：少样本前馈可泛化头像重建
authors:
- Thuan Hoang Nguyen
- Jiahao Luo
- Yinyu Nie
- Hao Li
- Gordon Guocheng Qian
- Jian Wang
affiliations:
- Snap Inc.
- University of California, Santa Cruz
- MBZUAI
arxiv_id: '2605.15320'
url: https://arxiv.org/abs/2605.15320
pdf_url: https://arxiv.org/pdf/2605.15320
published: '2026-05-13'
collected: '2026-05-18'
category: Multimodal
direction: 少样本前馈三维头像重建与实时动画
tags:
- 3D Gaussian Splatting
- Avatar Reconstruction
- Few-shot Learning
- Feed-forward Network
- FLAME
- Real-time Animation
one_liner: 从几张未标姿态的肖像秒级重建可动画3D高斯头像，无需逐主体优化，达到实时动画
practical_value: '- 多视图融合机制（Multi-View Query-Former）可借鉴到电商商品多角度图像生成3D展示，统一规范空间表示。

  - 三阶段训练课程：大规模预训练→高质量多视图微调→可选个性化，适用于需要兼顾泛化与高保真的生成模型。

  - 端到端从像素直接回归FLAME参数驱动动画，避免离线预处理，可用于实时Agent数字人面部控制。

  - 前馈网络+轻量个性化在单GPU上实现秒级重建与高帧率动画，为虚拟直播、客服Avatar等低延迟场景提供工程参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统头像重建依赖逐主体优化（耗时数小时）或昂贵预处理，难以规模化。FFAvatar提出通用前馈框架，从少样本无姿势图像中秒级重建高质量可动画3D高斯头像，彻底省去离线处理。

**方法关键点**：
- **多视图融合**：通过Multi-View Query-Former将多张源图像信息聚合为统一规范高斯表示，支持单视图或多视图输入。
- **端到端动画驱动**：直接从像素预测FLAME参数，无需离线提取，实现实时动画。
- **三阶段训练课程**：(i) 大规模预训练：使用含1M+身份的单目视频数据训练强泛化先验；(ii) 多视图微调：在256身份的高质量360°捕获数据集上提升几何保真度与极端视角感知；(iii) 可选个性化：对特定身份在500优化步内达到最高保真度。

**关键结果**：在NeRSemble基准上，PSNR比LAM高出5.5；无个性化重建仅需2秒，个性化10秒；单块A100支持49 FPS动画。
