---
title: 'BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks'
title_zh: BitSparse：ReLU 前馈网络的紧凑激活存储
authors:
- Max Zhu
- Bohang Sun
- Pietro Lio
- Jialin Yu
affiliations:
- University of Cambridge
- University of Oxford
arxiv_id: '2610.22256'
url: https://arxiv.org/abs/2610.22256
pdf_url: https://arxiv.org/pdf/2610.22256
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 训练显存优化 · 稀疏激活无损压缩
tags:
- LLM Training
- Activation Compression
- Sparse ReLU
- VRAM
- Triton
- Lossless Compression
one_liner: 提出 GPU 端无损稀疏激活压缩格式 BitSparse，在 Modded-NanoGPT 和 Nemotron-H 上降低每 token VRAM
  31%/30%，开销不超过 1%
practical_value: '- 若广告/推荐训练模型使用 ReLU/ReLU² 激活且前馈层存在大量稀疏零激活，可用 BitSparse 无损压缩激活缓存，降低训练
  VRAM，支撑更大 batch 或更长序列，不牺牲精度。

  - 压缩/解压以 Triton kernel 融合进 autograd function，开销 <1%，可作为自定义 activation checkpointing
  的轻量替代或补充，适合在大模型训练框架中集成。

  - 支持 BF16 和 FP8 激活，与混合精度训练兼容；业务上若已使用 FP8，可直接复用该压缩思路。

  - 预分配 buffer 避免 variable size tensor 分配时的 host synchronization，这个工程技巧对推荐模型中动态序列长度样本的训练同样有价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM 训练中激活缓存占用大量显存，现有方案如 activation checkpointing 以重计算换内存，lossy compression 改变存储值。近年来稀疏 ReLU/ReLU² 激活重新流行，提供了第三条路径：无损压缩稀疏激活缓存本身。

方法：BitSparse 是 GPU 端无损压缩格式，专为稀疏激活设计。压缩与重建在自定义 Triton kernel 中完成，并融合进 autograd function，前向存储压缩后的激活，反向时精确恢复，保证梯度计算不受影响。支持 BF16 和 FP8 激活，可选 sign-bit packing 进一步提升压缩率，接近理论极限。此外设计预分配 buffer 系统，避免训练中可变大小张量分配导致的主机同步。

结果：在 Modded-NanoGPT 和 Nemotron-H 上，BitSparse 将每 token VRAM 分别降低 31% 和 30%，在实用序列长度下额外计算开销不超过 1%。
