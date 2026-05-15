---
title: 'XFP: Quality-Targeted Adaptive Codebook Quantization with Sparse Outlier Separation
  for LLM Inference'
title_zh: XFP：面向LLM推理的质量驱动自适应码簿量化与稀疏异常值分离
authors:
- Thomas Witt
affiliations:
- Gemini Stiftung Leipzig
arxiv_id: '2605.14844'
url: https://arxiv.org/abs/2605.14844
pdf_url: https://arxiv.org/pdf/2605.14844
published: '2026-05-14'
collected: '2026-05-15'
category: LLM
tags:
- LLM
- Quantization
- Codebook
- MoE
- Outlier Separation
- Inference
one_liner: 让操作者设定余弦相似度质量下限，自动决定每层最小位宽，实现消费级GPU上的大模型高效推理
score: 9
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
现有LLM量化（如INT4、NVFP4）对所有层和专家使用统一格式，无法适应MoE中权重分布的显著差异：注意力层存在极端异常值（如49σ），而路由专家分布接近高斯。NVFP4的固定16条目码簿无视实际分布，且其硬件加速在消费级Blackwell（SM120/121）上不可用。校准感知方法（如GPTQ、AWQ）需要数据和手动选择位宽，且通常以固定位宽为目标，无法利用不同组件对量化的容忍度差异。

## 方法关键点
- **分解与码簿**：权重矩阵分解为稀疏fp16异常值残差和密集的N-bit索引张量，索引指向逐群组学习的码簿（组大小128）。支持两种存储模式：V2（每通道独立Lloyd码簿）和V2a（每层32个共享码簿库）。
- **自动位宽选择**：操作者给定两个余弦相似度阈值（严格τ_strict用于注意力和共享专家，懒惰τ_lazy用于路由专家），算法按升序尝试N∈{2,3,4}（V2）或{2,4}（V2a），返回首个满足阈值的最小N。学习码簿时，通过|w-μ|>kσ分离异常值，不依赖Hessian或校准数据。
- **融合解码核**：解包、码簿查找、异常值散射和bf16 GEMM在单个CUDA kernel中完成，支持Activation-row缓存以降低M=1解码的数据流量。
- **H-Process**：对于397B模型，迭代调整两个阈值以刚好填满2×96GB内存，实现约束压缩。

## 关键实验
- Qwen3.5-122B-A10B (TP=2, RTX PRO 6000 Blackwell)：V2自动模式（~3.97有效位）实现138 tok/s单流解码，GSM8K strict-match **94.49%**，比Marlin INT4快**49%** (TP=1)。
- Qwen3.5-397B-A17B (H-Process, τ_strict=0.96, τ_lazy=0.93, ~3.4有效位)：2×96GB工作站达到100.9 tok/s长输出解码，GSM8K strict-match 66.72%，保留全部512个路由专家。
- 编码耗时：122B模型量化~25分钟，加载后缓存；自动位宽选择<1分钟。

**一句话**：XFP将量化从“选位宽承受质量损失”颠覆为“定质量自动推位宽”，让工作站级GPU也能高效运行700GB+的MoE大模型。
