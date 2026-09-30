---
title: 'PrismQuant: Optimal Null-Space Rotations for Grouped Quantizers'
title_zh: PrismQuant：分组量化器的最优零空间旋转对齐
authors:
- Yanlong Chen
- Yining Chen
- Song Zhang
- Amirhossein Habibian
- Yawei Li
affiliations:
- Nanyang Technological University
- Nanjing University of Posts and Telecommunications
- Nanjing University
- Qualcomm AI Research
arxiv_id: '2609.32429'
url: https://arxiv.org/abs/2609.32429
pdf_url: https://arxiv.org/pdf/2609.32429
published: '2026-09-25'
collected: '2026-09-30'
category: LLM
direction: LLM 量化 · 零空间旋转对齐
tags:
- LLM Quantization
- Rotation
- Grouped Asymmetric INT4
- Null-Space Alignment
- W4A4KV4
- Householder
one_liner: 把激活主特征空间对齐到分组非对称 INT4 的组内常量子空间，实现 W4A4KV4 下 SOTA 且近乎无损
practical_value: '- 部署 LLM 在线推理（Agent / LLM ranker / 生成式推荐）时，W4A4KV4 是可用压缩点；不要只做 Hadamard
  式“把能量摊平”，而应把 activation 的主成分旋转到 per-group 常量方向，让已有 fp16 zero-point 吸收大能量，减少组内 range。这个思路可直接复用到你的
  activation quantizer。

  - 分组大小 g 不仅决定 scale 分辨率，还决定可供对齐的零空间维度（d/g 个零 slot）。在相同 activation bit 预算下，优先用更细
  group（g=128）而不是在更粗 group 里加额外 affine 方向；实测 g=128 单方向优于 g=256 三方向。对 KV cache / item
  embedding 表量化同样有借鉴意义。

  - 如果业务模型是 MoE（多领域 / 多场景 Expert 推荐或 MoE LLM），每个 expert 单独估计 activation 二阶矩并给独立 R4，router
  保持 bf16 且 R1 fold 进 router 输入以保持路由不变；冷 expert 用 pooled covariance shrinkage，能恢复大部分
  Hadamard 损失。

  - 工程实现上，旋转可折叠进相邻权重，避免在线 dense rotation；对不可折叠的 down-projection 输入，用 rank-k compact
  WY 修正 + block Hadamard，Tensor Core 两 kernel 实现，增加约 2.4% decode latency，但 prefill
  1.51× / decode 1.22× vs FP16。部署 LLM 特征提取或排序模型时，可把旋转离线折进权重，线上只保留小 rank 修正。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
低 bit activation quantization 的主要障碍不是 outlier 的大小，而是 outlier 方向与量化器几何不匹配。Hadamard 等旋转只把能量摊平，但没有利用 grouped asymmetric quantizer 已有的“组内常量子空间”：per-group affine zero-point 能免费表示组内共享电平，不进入 INT4 range。因此应把 activation 主能量旋转到这个子空间。

**方法关键点**  
- 将 activation 二阶矩 Σ 的 leading eigenvectors 对齐到 group-constant subspace S = span{u_j}，形式化为 Ky Fan trace maximization，闭式最优解。  
- 结构化旋转 R = H_g D Π G，G = I - WY^T，用 compact Householder WY 表示，rank k 控制成本；无需梯度训练，只用 calibration tokens 的 uncentered second moment。  
- Transformer 部署：R1 折叠进 residual stream 所有相邻权重；R2 作用在 value head 并将转置折进 output projection；R4 在 down-projection 输入在线执行 block Hadamard + rank-k correction。  
- 推导 range law：residual energy 约束组内 range，同时 group size g 决定 metadata 和可对齐方向数。

**关键实验与结果**  
- Llama-3.2-3B W4A4KV4：PPL 8.58（Hadamard 9.04，QuaRot 10.10），8-task avg 61.23（Hadamard 59.29）。  
- Llama-3.1-70B：PPL 3.85，avg 72.46，仅比 bf16 低 0.22 个百分点。  
- Qwen3-30B-A3B MoE：恢复 Hadamard 损失的 85%（k=8 时 avg 68.52 vs bf16 68.71）。  
- Llama-3.1-8B 部署：prefill 1.51×、decode 1.22× vs FP16，peak memory -56.34%，较 Hadamard 仅 +2.35% decode latency。

**最值得记住的一句话**  
量化困难的不是激活值大，而是大能量方向没有落到量化器已经免费表示的组内常量子空间里；旋转应服务于量化器几何，而不是单纯摊平分布。
