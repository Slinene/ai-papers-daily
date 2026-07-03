---
title: 'From SRA to Self-Flow: Data Augmentation or Self-Supervision?'
title_zh: 从SRA到Self-Flow：数据增强还是自监督？
authors:
- Dengyang Jiang
- Mengmeng Wang
- Harry Yang
- Jingdong Wang
affiliations:
- The Hong Kong University of Science and Technology
- Zhejiang University of Technology
- Baidu Inc.
arxiv_id: '2607.02508'
url: https://arxiv.org/abs/2607.02508
pdf_url: https://arxiv.org/pdf/2607.02508
published: '2026-07-01'
collected: '2026-07-03'
category: Training
direction: 扩散模型训练中数据增强机制解析
tags:
- Data Augmentation
- Self-Supervision
- Diffusion Transformer
- Representation Alignment
- Attention Separation
- Training Acceleration
one_liner: 证明Self-Flow的改进主要来自双重时间步的数据增强，而非跨噪声token的自监督交互
practical_value: '- **扩散模型训练加速**：在推荐系统（如生成式推荐、用户行为序列生成）中训练扩散Transformer时，可直接采用Attention
  Separation作为一种简单有效的训练技巧，通过阻断不同噪声步token间的注意力，将一个样本拆成多个有效训练部分，扩大数据规模，加快收敛。

  - **省去外部编码器依赖**：该方法基于自表示对齐，无需额外的预训练编码器（如DINOv2），适合电商场景下多模态数据快速迭代，降低推理成本。

  - **训练鲁棒性提升**：实验表明，去除噪声间交互甚至优于允许交互，说明在搜索/推荐场景中，对不同噪声水平的序列片段独立建模可能更利于学习干净表示，可尝试在用户长期行为建模中引入类似分片增强。

  - **可与现有框架嫁接**：Attention Separation不改变模型结构，仅修改注意力掩码，可即插即用于各种DiT基推荐模型（如DreamRec），低风险提升训练效率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：Self-Flow通过让扩散Transformer中不同噪声级别的token相互注意来提升生成质量，但其改进机制究竟是数据增强还是自监督交互尚不清楚。本文旨在解耦这两种因素，重新理解从SRA到Self-Flow的性能增益来源。
**方法关键点**：提出Attention Separation，即在保持双重时间步输入的前提下，屏蔽不同噪声级别token之间的注意力交互。这样既保留了与Self-Flow相同的双重噪声输入，又阻止了“清洁token帮助推断噪声token”的机制。令人惊讶的是，去除这种交互后性能不降反升，从而证明Self-Flow的增益主要来自双重时间步本身的数据增强——每个图像被拆分成多个有效训练部分。进一步，将自表示对齐与双重时间步、注意力分离增强相结合，形成新的训练策略。
**关键结果**：在ImageNet上验证，Attention Separation优于原有Self-Flow，且与自表示对齐结合后，收敛速度和质量均提升，有力支持了数据增强假说。
