---
title: 'Single-Teacher View Augmentation: Enhancing Knowledge Distillation with Student-Guided
  Perturbations'
title_zh: 单教师视角增强：利用学生引导扰动改进知识蒸馏
authors:
- Xuyi Yu
- Yaohua Liu
- Ziming Song
- Yinghai Zhao
- Huipeng Zhang
- Kuizhi Mei
arxiv_id: '2607.11557'
url: https://arxiv.org/abs/2607.11557
pdf_url: https://arxiv.org/pdf/2607.11557
published: '2026-07-13'
collected: '2026-07-14'
category: Training
direction: 知识蒸馏 · 视角增强
tags:
- Knowledge Distillation
- View Augmentation
- Student-Guided Perturbation
- Cyclic Shift
- Model Compression
one_liner: 用学生动态特征引导无参数循环移位生成多样视角，实现单阶段高效知识蒸馏
practical_value: '- 电商/广告推荐模型压缩场景（如CTR、排序模型）中，蒸馏轻量级在线模型时，可直接使用学生模型的动态特征生成多视角监督，提升泛化能力，无需维护多个教师或复杂的训练流程。

  - 无参数的循环移位扰动实现零额外参数开销，适合资源敏感型线上推理环境；单阶段训练避免预教师训练，简化工程链路。

  - 可借鉴该思路将学生特征作为条件，设计自适应噪声注入（如特征层随机移位、维度重排），生成多样化的虚拟教师视图，替代传统的固定教师输出。

  - 方法对模型结构无侵入性，可快速集成到现有的 logit/feature 蒸馏框架中，实验观察可直接迁移至电商领域的同等架构模型。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：传统知识蒸馏仅依赖单一教师的固定视角，监督信号缺乏多样性；多教师蒸馏计算与存储成本过高。现有单教师虚拟视角方法存在权衡：随机扰动高效但缺乏受控多样性，结构化增广需多阶段训练且参数线性增长。该权衡源于共同设计——使用教师静态强特征生成视图。

**方法**：提出 Shift-Augmented Knowledge Distillation (SAKD)，放弃教师静态特征，转而利用学生模型中动态演化的特征作为扰动生成条件。具体通过对学生特征进行无参数的循环移位（cyclic shift）产生自适应、多样化的视图，作为增强的监督信号。该方法实现单阶段训练，无需额外可学习参数或预训练过程。

**结果**：在 CIFAR-100 和 ImageNet 上，SAKD 显著优于随机扰动方法，且准确率与两阶段结构化方法持平，同时参数大幅减少，完全免除预训练需求。例如，在 ImageNet 上与 ResNet-34 为教师、ResNet-18 为学生时，SAKD 提升 Top-1 准确率约 1.2%，接近两阶段方法性能，但训练效率更高。
