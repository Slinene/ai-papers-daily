---
title: 'MaskAlign: Token-Subset Representation Alignment for Efficient Diffusion Training'
title_zh: 'MaskAlign: 用于高效扩散训练的 Token 子集表示对齐'
authors:
- Lianyu Pang
- Tianlin Pan
- Cheng Da
- Changqian Yu
- Huan Yang
- Kun Gai
- Song Guo
- Wenhan Luo
affiliations:
- The Hong Kong University of Science and Technology
- Kuaishou Technology
- University of Chinese Academy of Sciences
arxiv_id: '2606.08788'
url: https://arxiv.org/abs/2606.08788
pdf_url: https://arxiv.org/pdf/2606.08788
published: '2026-06-06'
collected: '2026-06-14'
category: Training
direction: 高效扩散模型训练 · Token 子集对齐
tags:
- Diffusion Models
- Representation Alignment
- Training Efficiency
- Masking
- Token Subset
one_liner: 提出随机 Token 子集对齐与预掩码混合，大幅加速扩散 Transformer 训练并提升生成质量。
practical_value: '- 主要是学术贡献，面向电商/推荐/AI 业务可借鉴点有限，但以下思路可参考：

  - 训练跨模态对齐模型（如商品图文匹配）时，可尝试随机屏蔽部分 token 进行子集对齐，并引入轻量 token mixing 模块，增强对不完整输入的鲁棒性。

  - 梯度分析定位重要 token 的方法可迁移用于诊断推荐模型的特征对齐过程，识别哪些用户行为 Token 更关键。

  - 随机子集采样减少了对齐所需计算量，可作为训练加速 trick 在资源受限时使用。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有扩散模型训练中，通过对齐扩散特征与预训练视觉编码器的干净图像表示可以加速收敛，但噪声输入在不同时间步包含的可信信息差异很大，而参考特征始终来自干净图像。这种不对齐会导致全 token 对齐目标过度依赖完整 token 集，且观察到的对齐梯度范数大的 token 具有空间偏好，表明对齐不均匀。

**方法**：提出 **MaskAlign**，在训练时随机采样子集 token 进行表示对齐，迫使模型在不同迭代中学习适应 token 子集的扰动，减少对全集的依赖。为缓解直接丢弃 token 带来的信息损失，引入一个轻量级 **pre-mask token mixing block**，在对齐前在 token 间进行信息交互。

**关键结果**：在 ImageNet 256×256 上，使用 SiT-XL/2 模型，MaskAlign 达到 8.3 FID 所需的迭代次数比基线快约 77 倍，达到 5.9 FID 快约 30 倍；相比 REG，每步训练时间减少 11.6%，并在 400K/1M 迭代下将 FID 从 3.4/2.7 降至 2.8/2.4。
