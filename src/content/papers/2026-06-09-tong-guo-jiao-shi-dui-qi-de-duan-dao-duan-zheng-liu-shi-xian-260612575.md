---
title: High-Fidelity Two-Step Image Generation via Teacher-Aligned End-to-End Distillation
title_zh: 通过教师对齐的端到端蒸馏实现高保真两步图像生成
authors:
- Dongyang Liu
- Ruoyi Du
- David Liu
- Dengyang Jiang
- Liangchen Li
- Qilong Wu
- Zhen Li
- Steven C. H. Hoi
- Hongsheng Li
- Peng Gao
affiliations:
- Z-Image Team, Alibaba Group
- The Chinese University of Hong Kong
arxiv_id: '2606.12575'
url: https://arxiv.org/abs/2606.12575
pdf_url: https://arxiv.org/pdf/2606.12575
published: '2026-06-09'
collected: '2026-06-14'
category: Other
direction: 图像生成 · 扩散模型蒸馏
tags:
- Diffusion Distillation
- Adversarial Learning
- Image Generation
- Few-Step Generation
- Model Compression
one_liner: 用教师对齐对抗学习、分步解耦参数化和端到端迭代正则化，将8步扩散模型蒸馏至2步，显著缩小质量差距
practical_value: '- 教师对齐对抗学习思路可迁移到推荐系统知识蒸馏：用教师模型输出作为 GAN 的“真实”样本，比外部数据更易拟合，可缓解模式坍塌，适用于召回
  / 排序模型的轻量化训练。

  - 分步解耦参数化可借鉴到多阶段 Agent 推理链：对不同步骤分配独立参数，针对性优化各阶段容量，适合多步推理、级联推荐等场景。

  - 端到端迭代正则化让中间步骤接收最终质量梯度，同时保留中间监督，可用于多阶段推荐模型训练，使粗排 / 召回同时对齐最终精度且保持中间结果可用。

  - 极限压缩（2 步）下的质量保持策略对实时推荐场景有启发：例如将重排序模型蒸馏为轻量两阶段模型时，可通过类似技巧压缩推理开销，维持效果。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：扩散模型虽图像生成质量高，但推理步数多（40~100 步），严重影响部署效率。少步蒸馏（如 4~8 步）已趋于成熟，但进一步压缩至 2 步时，任务难度与模型容量限制导致质量大幅下降，亟需针对性设计。

**方法**：提出 Z-Image Turbo++，从 8 步教师模型蒸馏至 2 步，包含三项关键设计：（1）**分布对齐对抗学习**：用教师生成的图像替代真实图像作为 GAN 判别器的正样本，提供更易达成且信息丰富的对抗目标；（2）**分步解耦参数化**：为两步去噪分配独立参数，匹配不同步骤的差异容量需求；（3）**端到端训练与迭代正则化**：第一步可直接从最终图像质量损失获取梯度，同时引入显式第一步中间损失，保证中间输出仍具有意义。

**结果**：定性与定量评估表明，该方法大幅缩小了 2 步与 8 步生成的品质差距，验证了精准蒸馏策略在少步生成中平衡质量与效率的潜力。
