---
title: 'Mage-Flow: An Efficient Native-Resolution Foundation Model for Image Generation
  and Editing'
title_zh: Mage-Flow：高效原生分辨率图像生成与编辑基础模型
authors:
- Xinjie Zhang
- Peng Zhang
- Shicheng Zheng
- Jinghao Guo
- Zhaoyang Jia
- Yifei Shen
- Xun Guo
- Yuxuan Luo
- Jiahao Li
- Wenxuan Xie
affiliations:
- Microsoft
arxiv_id: '2607.19064'
url: https://arxiv.org/abs/2607.19064
pdf_url: https://arxiv.org/pdf/2607.19064
published: '2026-07-20'
collected: '2026-07-24'
category: Multimodal
direction: 高效多模态生成 · 原生分辨率扩散 Transformer
tags:
- efficient-generation
- rectified-flow
- latent-tokenizer
- image-editing
- model-distillation
- diffusion-transformer
one_liner: 通过 tokenizer-骨干-系统协同设计，以 4B 规模实现高效高分辨率图像生成与编辑
practical_value: '- **高效 tokenizer 设计**：Mage-VAE 一步扩散式编解码与 anchor-latent 正则化，在保持重建质量的同时将
  tokenization 成本降低一个数量级。该思路可迁移至电商生成式推荐中的 item image/text 压缩，减少序列长度与训练开销。

  - **原生分辨率训练加速**：采用 native-resolution packing 与 CUDA kernel fusion，支持任意分辨率训练，端到端吞吐提升约
  2.5 倍。推荐系统中的多模态召回/排序模型可借鉴此系统优化方法，在 GPU 集群上高效训练多尺度内容。

  - **低延迟推理蒸馏**：通过对抗感知蒸馏与 rectified flow 匹配，实现 4 步 Turbo 模型，大幅降低推理延迟（1024 生成 0.59s，编辑
  1.02s）。可用于推荐系统中的图像生成模块（如广告创意生成、商品图编辑）实现实时交互。

  - **系统协同设计思想**：tokenizer、backbone、训练策略联合优化，而非独立改进各模块。构建推荐模型时，可借鉴统一考虑特征编码、模型架构与训练效率，达到性能与成本的更优平衡。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前大模型在图像生成与编辑上虽性能强劲，但训练、微调、部署成本过高，难以满足高效、低延迟的交互式应用需求。

**方法**：提出 Mage-Flow 高效 4B 规模生成栈，包含两大协同设计组件：
1. **Mage-VAE**：轻量高保真 latent tokenizer，采用一步扩散式编解码与 anchor-latent 正则化，在保持主流 VAE 重建质量的同时，tokenization 成本降低一个数量级以上。
2. **Native-Resolution 多模态扩散 Transformer**：基于 rectified flow 匹配训练，结合原生分辨率打包与 CUDA kernel fusion，支持灵活分辨率训练，端到端吞吐提升约 2.5 倍。
在此基础上构建完整模型家族：Base、RL 对齐、Turbo 变体。Diffusion-NFT 增强提示跟随、文本渲染、美学质量与编辑保真度；通过对抗感知蒸馏得到 4 步 Turbo 模型，实现极低延迟推理。

**结果**：紧凑规模下，生成与编辑性能达到有竞争力水平。Turbo 变体真正使高分辨率交互实用：在单张 A100 上，1024² 生成仅需 0.59s，编辑仅需 1.02s，且内存占用低。证明了 tokenizer-骨干-系统协同设计可在 4B 内实现强大高效的高分辨率生成与编辑。
