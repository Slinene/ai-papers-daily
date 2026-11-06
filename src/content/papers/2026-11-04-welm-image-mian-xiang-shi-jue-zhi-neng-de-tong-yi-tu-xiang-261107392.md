---
title: 'WeLM-Image: A Unified Image Generation Model towards Visual Intelligence'
title_zh: WeLM-Image：面向视觉智能的统一图像生成模型
authors:
- Canmiao Fu
- Chen Li
- Guohui Zhang
- Hao Lu
- Hongyang Wei
- Huadong Wu
- Huaisong Zhang
- Hubery Yin
- Liyuan Cui
- Qixin Yan
affiliations:
- WeChat Vision, Tencent Inc.
arxiv_id: '2611.07392'
url: https://arxiv.org/abs/2611.07392
pdf_url: https://arxiv.org/pdf/2611.07392
published: '2026-11-04'
collected: '2026-11-06'
category: Multimodal
direction: 多模态生成模型 · MoE/MoT
tags:
- Multimodal
- MoE
- MoT
- Image Generation
- Distillation
- RLHF
one_liner: 统一多模态理解与图像生成/编辑，通过MoE+MoT稀疏架构与蒸馏实现单GPU高效部署
practical_value: '- **多任务解耦的MoE+MoT架构可借鉴到电商多目标模型**：共享注意力、独立任务参数的设计能降低CTR/CVR等多任务优化干扰；对生成式推荐中的item生成、文案生成、query生成，可以用类似稀疏激活结构控制在线成本与容量。

  - **训练时评估驱动的数据迭代**：用rubric/checklist自动评估并筛选高质量生成/编辑样本，该闭环可直接迁移到电商场景的文案生成、商品图合成等数据清洗，提升训练数据质量。

  - **噪声感知on-policy蒸馏**：先分开优化生成与编辑策略，再蒸馏整合，适合业务中多个专项Agent（如选品Agent、文案Agent）合并为统一模型，同时保持各自能力，降低部署复杂度。

  - **单GPU推理优化**：few-step蒸馏（8步无引导）配合稀疏激活，1024×1024生成仅4.98s，为推荐/Agent系统中多模态内容生成的在线化提供了可行的工程参考。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：文本到图像生成、指令编辑、多参考合成任务通常由分散模型承担，难以在微信等大规模应用的单GPU环境统一部署。WeLM-Image 目标是将多模态理解与生成能力整合进一个可高效推理的基础模型。

**方法关键点**：
- 将文本、参考图像、目标 latents 编码为交错序列，统一输入。
- 采用 Mixture-of-Transformers（MoT）骨干：共享注意力层，但理解与生成路径分别持有独立参数，减少优化干扰；每条路径再嵌入 MoE 模块，存储参数31.7B，每个目标 token 仅激活约5.4B生成参数。
- 数据引擎结合知识基础视觉词汇与大规模视觉聚类，双语注释与验证编辑监督，支持渐进训练至原生1.5K分辨率。
- 训练上，生成与编辑分别用 rubric 和 checklist 奖励优化，再通过噪声感知 on-policy 蒸馏合并策略。
- 使用 MeanFlow 进行 few-step 蒸馏得到 Turbo 版本，8步无引导生成。

**关键结果**：1536分辨率模型在 PRISM-Bench、Qwen-Image-Bench、UnicBench 三个开源评测集上综合排名第一；Turbo 版在单个 NVIDIA H20 GPU 上以 4.98s 生成 1024×1024 图像。
