---
title: 'Dion3: Full-Stack Orthogonal Updates'
title_zh: Dion3：Muon 优化器全栈正交更新加速
authors:
- Noah Amsel
- Jack Zhang
- Kwangjun Ahn
- Ali Naeimi
- Austin Feng
- Berlin Chen
- Tri Dao
- John Langford
affiliations:
- New York University
- Princeton University
- NVIDIA
- Yale University
- Microsoft Research
arxiv_id: '2608.11612'
url: https://arxiv.org/abs/2608.11612
pdf_url: https://arxiv.org/pdf/2608.11612
published: '2026-08-11'
collected: '2026-08-17'
category: Training
direction: Muon 优化器全栈加速与分布式优化
tags:
- Muon
- Newton-Schulz
- Optimizer
- Distributed Training
- Gram Newton-Schulz
- Training Efficiency
one_liner: 提出 Gram Newton-Schulz、对称 GEMM 核、分数行选择更新和 megabatching，将 Muon 优化器步时最多降低
  6 倍且保持/提升模型质量
practical_value: '- Gram Newton-Schulz 可作为标准 Newton-Schulz 的 drop-in 替换，在权重矩阵 aspect
  ratio 高（如 MLP/MoE 权重）时显著减少 FLOP，适合推荐/广告模型中常见的宽矩阵，无需改变训练流程。

  - 分数行选择 + error feedback 是实用的加速技巧：每次只正交化动量矩阵中 ℓ1 范数最大的 f 行，学习率按 η/√f 缩放，在资源受限时可将优化器计算量降低约
  1/f²，且不损害甚至轻微提升模型质量。

  - Megabatching 策略对 FSDP 下的通信优化很有价值：按矩阵形状分组做 all-to-all，减少通信轮次至 O(1)，在中小模型通信瓶颈场景（如
  1B 模型 8 卡）可降低 35% 优化器步时，值得工程实现借鉴。

  - 自定义对称 GEMM 核（CuteDSL）利用对称性只计算下三角并复制到上三角，在 Hopper/Blackwell 上获得近 2× 速度，适合集成到训练框架中以加速大量对称矩阵乘法。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
Muon 优化器在 LLM 训练中比 AdamW 需要更少的步数，但其每步的 Newton-Schulz 正交化是 O(n³) 的矩阵运算，随模型规模增长开销迅速上升，且在分布式训练中需要额外的 all-to-all 通信，严重限制了 Muon 的可扩展性。

## 方法关键点
- **Gram Newton-Schulz**：将正交化从大矩阵 X 转移到小的对称 Gram 矩阵 XXᵀ 上迭代逼近 (XXᵀ)⁻¹/²，数学上与标准 Newton-Schulz 完全等价，但大幅减少矩形矩阵乘法；对 aspect ratio α>1 的矩阵节省显著，如 α=4 时节省 55% FLOP。
- **对称 GEMM 核**：用 CuteDSL 实现对称矩阵乘法，只计算下三角并转置复制到上三角，在 Hopper/Blackwell 上相比 cuBLAS 获得约 2× 加速。
- **Dion3 更新规则**：每步只选择动量矩阵中 ℓ1 范数最大的 f 行（推荐 f=1/4 或 1/8）进行正交化，其余行不更新，配合 error feedback 对未选中行不衰减动量；学习率按 η/√f 缩放保持有效步长一致。
- **Megabatching 通信**：将同形状矩阵打包成单个 all-to-all，把通信轮次从 O(N/world_size) 降至 O(1)，在通信瓶颈场景下效果显著。

## 关键实验
在 1B 参数稠密 Transformer 上训练 100B tokens ClimbMix：Dion3 f=1/8 最终验证 loss 2.181，优于 NorMuon 的 2.194；f=1/4 在 3B-14B 模型上一致优于 NorMuon，14B 验证 loss 2.162 vs 2.189，下游平均准确率 +0.7 个百分点。优化器步时方面，7B 模型 4×GH200 上 Muon 为 AdamW 的 26×，Dion3 全栈降至 4×；在 MoE/更高 aspect ratio 架构上 Gram-NS+对称核单独就能获得 2× 加速。

最值得记住的一句话：Gram Newton-Schulz 把正交化从大矩形矩阵搬到小对称 Gram 矩阵，分数行选择进一步压缩，二者叠加实现最多 6× 优化器加速且不损失甚至提升训练质量。
