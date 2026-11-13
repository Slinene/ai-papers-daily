---
title: Factored One-sided Adam-Moment for Practical and Scalable SOAP
title_zh: Factored One-sided Adam-Moment：实用可扩展的 SOAP 轻量优化器
authors:
- Jaemyung Yu
- Byeongho Heo
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2611.16905'
url: https://arxiv.org/abs/2611.16905
pdf_url: https://arxiv.org/pdf/2611.16905
published: '2026-11-11'
collected: '2026-11-13'
category: Training
direction: 二阶优化器 · SOAP 轻量化
tags:
- Training
- Second-order optimizer
- SOAP
- LLM pre-training
- Kronecker-factored
- Muon
one_liner: 将 SOAP 精简为输入侧预条件与分解二阶矩，以近 AdamW 成本实现 SOAP 级预训练质量
practical_value: '- 训练/微调大 Transformer（含搜索推荐里的 LLM 重排、Agent 模型）时，若 SOAP/Muon 类二阶优化器内存或耗时不可用，可把
  Q/K/V/O、MLP 等矩阵参数换成 FOAM，embedding、lm-head、norm、bias 仍走 AdamW；这样优化器状态约减半，并省掉输出侧
  m^2 因子与一次 eig。

  - 更省内存的 Adam 做法：在输入侧 eigenbasis 旋转后，用行均值 r、列均值 c 外积 + trace 归一化 τ=tr(R)/(||r||1||c||1)
  替代 dense v。安全前提是旋转后 V 近 rank-1（论文约 0.84-0.90）；不要在 Adam 原始 g^2 坐标上直接做 Adafactor 式分解（rank-1
  share 仅 0.54-0.63，损失更大）。

  - 工程上，eig 刷新用 off(Q^T R Q) <= tol 的 skip rule（pf=10, tol=0.1），后期大幅减少 n^3 分解；注意 R
  和 QR 在 ≥7B 时需要层内分布式切分。

  - 大 batch/弱扩展训练可用 FOAM 替代 AdamW 保持质量：2M tokens/step 时 FOAM 3.364 vs AdamW 3.956，达到同质量
  wall-clock 约 1/3；业务上因加速加大 batch 时，优先考虑矩阵预条件优化器，但 embedding 侧仍需 AdamW。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
SOAP/Shampoo 在 transformer 预训练上比 AdamW 收敛更快，但 SOAP 优化器状态约为 AdamW 的 4.5 倍，双侧 Kronecker 因子需要两次 eigendecomposition，wall-clock 显著更慢。问题是：能否保留 SOAP 收益，接近 AdamW 成本？

**方法关键点**  
- 仅输入侧预条件：只保留 R=G^T G 与 QR=eigh(R)，丢弃输出侧 L。Hessian 结构显示输出侧曲率近对角，输入侧承载主要曲率结构；状态从 2mn+2m^2+2n^2 降到 mn+2n^2+(m+n)，eig 从两次到一次。  
- 分解二阶矩：在输入旋转坐标下，用行均值 r、列均值 c 的 EMA，加上 trace 归一化 τ=tr(R)/(||r||1||c||1) 重建 vrot≈τ r c^T；K-FAC 假设下可精确恢复 dense 二阶矩。  
- 特征基刷新采用 Purifying Shampoo 的 off-diagonal ratio skip rule，后期稀疏触发 eig。

**关键实验**  
FineWeb 预训练 GPT-2 124M/350M/760M，1x Chinchilla。760M 验证损失：SOAP 2.791，FOAM 2.796，Muon 2.806，AdamW 2.847；FOAM 优化器状态 11.87 GiB vs SOAP 23.73；wall-clock 到 AdamW 最终 loss 为 10.53h，接近 AdamW 的 10.55h，而 SOAP 需 22.66h。峰值内存仅比 AdamW +7.4%。消融显示仅输入侧预条件比仅输出侧好约 0.02 nats，分解几乎无 loss；K-FAC 违反 15-20%，对更新影响约 0.002 nats。大 batch 下 2M tokens/step FOAM 3.364 vs AdamW 3.956。ViT-Tiny 与 GPT-2 XL 1.56B 也验证了排序。

最值得记住的一句话：SOAP 的质量瓶颈主要在输入侧曲率，旋转到输入侧 eigenspace 后二阶矩接近 rank-1，所以“仅输入侧因子 + 行/列分解 + trace 归一化”能以近 AdamW 成本拿到 SOAP 级收益。
