---
title: 'Cut Binary Cross Entropy: Efficient Large-Vocabulary Loss and Gradient Kernels
  for Sequential Recommendation'
title_zh: CutBCE：大词表序列推荐的高效 BCE 损失与梯度内核
authors:
- Yaoyiran Li
- Haowen Ning
- Mohamed Hammad
affiliations:
- Google Cloud
arxiv_id: '2610.05559'
url: https://arxiv.org/abs/2610.05559
pdf_url: https://arxiv.org/pdf/2610.05559
published: '2026-10-04'
collected: '2026-10-06'
category: Training
direction: 大词表 BCE 训练优化 · TPU Kernel
tags:
- CutBCE
- BCE loss
- TPU kernel
- Pallas
- Sequential Recommendation
- Large Vocabulary
one_liner: CutBCE 通过分块重算与稀疏修正避免 [B,N,V] logits 驻留 HBM，在 876k 词表上将训练显存降 65.7%、速度提 225.9%
practical_value: '- 训练多标签召回/序列模型时，用分块 BCE：把 BCE 写成 max(x,0)+log(1+e^{-|x|}) 减去 y*x，按
  vocab chunk 计算并立即释放，避免 [B,N,V] logits；PyTorch 里可实现为 chunked loss 或自定义 autograd.Function。

  - 反向不要存完整 logits：自定义 VJP/rematerialization 只保留 activations、embedding 和稀疏 target
  IDs，逐块重算 logits 和梯度；对电商百万级 catalog，这是时间换空间，在 TPU 上因减少 HBM 往返甚至更快。

  - 如果部署在 TPU/JAX，可以用 Pallas 把 embedding 梯度累积在 VMEM，降低 HBM 读写；动态查询 VMEM 预算并做序列 chunking，分布式训练用
  shard_map 显式控制 psum 和 vocab_offset。

  - 训练监控用 count-based 指标：前向直接统计 TP/FP/FN/TN 获得 accuracy/precision/recall/Fβ，不要为监控重建全量
  logits，保持低显存。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业级序列推荐要在百万级 item 目录上做多标签训练，标准 BCE 会在 HBM 中物化 [B,N,V] logits。以 Yambda-50M 的 V=876,939、本地 batch 16、序列长度 256 计算，单卡 32-bit logits 约 13.38 GiB，直接触发 OOM；已有 Cut Cross Entropy、Liger 等主要面向 softmax CE 且基于 CUDA，不等价于大规模多标签 BCE。

### 方法关键点
- 将 BCE 按类分解为 dense background loss max(x,0)+log(1+e^{-|x|}) 与 sparse target correction -y·x，逐 vocab block（默认 4096）计算并立即释放，激活峰值从 O(BNV) 降到 O(BN·block_v)。
- 自定义 VJP：前向只保留 A、E 和稀疏 [B,N,L] target IDs；反向在专用 Pallas TPU kernel 中逐块重算 logits 并累积梯度，logits 与梯度不驻留 HBM。
- kernel 侧利用 VMEM 累积 embedding 梯度，减少 HBM 往返；动态 VMEM budgeting、序列 chunking 与 shard_map 分布式通信优化。
- 训练监控用 count-based Cut Metrics 直接统计 TP/FP/FN/TN，避免重建全量 logits。

### 关键结果
单芯片 mini-benchmark 中，B=128,N=128,V=100k 时 Keras BCE OOM，CutBCE 在 TPU v6e 上 6.93ms 完成；V=200k 时相对 Keras BCE 加速 91.9%。在 8 芯片 TPU v6e 上训练 multi-label SASRec（Yambda-50M，876k items，预测 next 8 items）：B=64,N=256 时 CutBCE 将每芯片 HBM 从 22.37GiB 降至 7.67GiB（-65.7%），训练速度从 6.14 提升到 20.01 steps/s（+225.9%），Hit@8 为 0.183，对比标准 BCE 的 0.186 基本持平；B=128 或 N=512 下标准 BCE OOM，CutBCE 仍稳定。

值得记住：大规模多标签推荐训练不要物化 [B,N,V] logits，用分块重算 + 稀疏修正即可显著降显存、提速度。
