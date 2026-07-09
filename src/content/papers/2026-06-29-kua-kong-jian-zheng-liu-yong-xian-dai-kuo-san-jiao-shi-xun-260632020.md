---
title: 'Cross-Space Distillation: Teaching One-Step Students with Modern Diffusion
  Teachers'
title_zh: 跨空间蒸馏：用现代扩散教师训练单步学生模型
authors:
- Anh Nguyen
- Ngan Nguyen
- Duc Vu
- Trung Dao
- Viet Nguyen
- Quan Dao
- Kien Nguyen
- Chi Tran
- Phong Nguyen
- Khoi Nguyen
affiliations:
- Qualcomm AI Research
- University of Wisconsin–Madison
- Johns Hopkins University
- Rutgers University
arxiv_id: '2606.32020'
url: https://arxiv.org/abs/2606.32020
pdf_url: https://arxiv.org/pdf/2606.32020
published: '2026-06-29'
collected: '2026-07-09'
category: Training
direction: 扩散模型蒸馏 · 跨空间对齐
tags:
- Diffusion Distillation
- Cross-Space
- Bridge Module
- One-Step Generation
- Latent Space Alignment
- Knowledge Transfer
one_liner: 提出 Bridge 模块实现跨潜空间蒸馏，让高分辨率大教师模型蒸馏到不兼容的低分辨率学生模型
practical_value: '- 若业务中需要将不同隐空间的大模型（如高维语义 ID 生成教师）蒸馏到低维学生，可借鉴 Bridge 的设计：冻结学生解码器作为空间先验
  + 小型可学习投影器，避免改动学生主干。

  - 训练稳定技巧：使用潜在重建损失与注意力保真度目标对齐教师空间，可复用到多模态 embedding 对齐场景（如视觉-文本语义空间映射）。

  - 工程上，Bridge 模块参数少、推理时即插即用，适合在移动端或边缘部署场景中，用大模型离线蒸馏、小模型在线推理的架构。

  - 这篇工作集中在图像生成，对电商搜索推荐系统的直接迁移价值有限；但其“跨空间知识迁移”的思路可启发异构推荐模型（如双塔 vs 多塔）之间的知识蒸馏设计。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有单步扩散模型蒸馏大多要求教师和学生共享相同的隐空间与分辨率（Shared-Space 约束），导致 FLUX、SD 3.5 等现代大教师无法将知识迁移到 SD 1.5 等低分辨率小模型上，因为隐空间维度、VAE 参数化不兼容。作者将这一广泛存在但未被系统研究的问题形式化为跨空间蒸馏（Cross-Space Distillation）。

**方法**：提出 Bridge 模块（Bϕ），它是一个轻量级的隐空间接口。Bridge 将学生隐变量 zS 映射为教师兼容的隐变量 ẑT = Bϕ(zS)，而无需修改学生骨干。其设计核心为：（1）冻结的学生 VAE 解码器作为空间先验，将学生隐变量解码到像素级再投影回教师空间；（2）一个可学习的紧凑投影网络（约 5% 的学生参数），通过教师空间中的潜在重建损失和注意力保真度损失进行训练，保证对齐稳定。蒸馏过程完全在教师空间进行，学生通过网络输出经 Bridge 映射后与教师输出计算分布匹配损失。

**结果**：在多个现代教师（如 SD 3.5、FLUX）上，Bridge 显著提升紧凑的单步学生模型质量。例如，将 SD 1.5 从 HPSv3 5.4 提升到 9.4，同时保持单步推理低时延，并解锁了 1024×1024 分辨率输出的能力（原本仅支持 512×512）。重要的是，学生模型本体未变，完全兼容原有生态工具和管线。
