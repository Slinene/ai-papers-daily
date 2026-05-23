---
title: 'RiT: Vanilla Diffusion Transformers Suffice in Representation Space'
title_zh: RiT：普通扩散Transformer在表示空间即可胜任
authors:
- Le Zhang
- Ning Mang
- Aishwarya Agrawal
affiliations:
- Mila – Québec AI Institute
- Université de Montréal
- Utrecht University
- Canada CIFAR AI Chair
arxiv_id: '2605.21981'
url: https://arxiv.org/abs/2605.21981
pdf_url: https://arxiv.org/pdf/2605.21981
published: '2026-05-20'
collected: '2026-05-23'
category: Multimodal
direction: 生成模型 · 表示空间训练
tags:
- diffusion models
- flow matching
- representation space
- DINOv2
- image generation
- DiT
one_liner: 利用DINOv2特征的优良统计特性，仅用普通DiT加x-prediction实现高效极速图像生成
practical_value: '- **用语义表示替代像素空间做生成式推荐**：预训练语义嵌入（如 DINOv2）的内在维度与像素相似，但有效秩更高、协方差条件更好，使扩散模型训练更稳定、采样更快。在推荐场景中，可将用户行为序列或物品的语义
  embedding 作为扩散目标，替代原始 ID 或 VAE latents，降低建模难度。

  - **维度感知噪声调度**：不同特征维度可能包含不同层次的信息，RiT 对不同维度施加不同的噪声水平，避免各向同性噪声破坏低维结构。在生成序列或行为嵌入时，可对主要变化维度与噪声维度区别对待，提升生成质量。

  - **联合 [CLS]-patch 建模**：在序列生成中，类似地引入一个全局 token（如 user state）参与扩散过程，并与局部 patch（行为
  sub-sequence）联合建模，可能比独立生成各步行为更连贯。

  - **快速采样的工程优势**：无需蒸馏或一致性训练，RiT 仅用 5~10 个 Heun 步骤即可达到高画质。这为在线推荐中实时生成候选集（如 top-N 物品）提供了可能，大幅降低推理延迟。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：流匹配中的 x-prediction 在像素空间已能利用低维流形结构，但预训练表示空间是否更有利于学习？作者对比像素、SD-VAE 和 DINOv2 特征的几何性质，发现 DINOv2 与像素的内在维度几乎相同 (d≈33)，但其有效秩高 7.3 倍、协方差条件数优 35 倍、超标度峰度低 11.5 倍、流形插值误差低 1.7 倍。这些统计优势使回归问题良态，无需专用预测头或黎曼传输。

**方法**：提出 RiT，在冻结的 DINOv2 特征上直接用普通 DiT 进行 x-prediction 训练，仅引入两个关键设计：1) 维度感知噪声调度——对不同特征维度施加不同噪声水平，保护低维流形；2) 联合 [CLS]-patch 建模——同时预测全局 [CLS] 令牌和图像 patch 令牌，充分利用 DINOv2 的训练目标。

**结果**：在 ImageNet 256×256 上，RiT 无引导 FID 达 1.45，有引导 FID 1.14，参数 6.76 亿，比 DiT-XL 少 19%。采样效率极高：使用 Heun 求解器，5 步 FID 即达 2.0，10 步 1.25，无需蒸馏或一致性训练。
