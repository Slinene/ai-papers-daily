---
title: 'Architecting for Hardware Diversity: Meta''s End-to-End Co-Design for High-Performance
  AI Training on AMD GPUs'
title_zh: Meta 面向 AMD GPU 的端到端协同设计与高性能 AI 训练
authors:
- Haoyu Zhang
- Arshad Rahman
- Adnan Aziz
- Ajith Prabhudev
- Amin Farmahini
- Ben Rhoads
- Benson Ma
- Brian Shi
- Cen Zhao
- CK Luk
affiliations:
- Meta
- AMD
arxiv_id: '2610.22230'
url: https://arxiv.org/abs/2610.22230
pdf_url: https://arxiv.org/pdf/2610.22230
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: 异构 GPU 训练协同优化
tags:
- DLRM
- AMD GPU
- GEMM
- Kernel Optimization
- Agentic Workflow
- Hardware Co-design
one_liner: 通过硬件-模型协同设计、Origami 分析性能模型与 agentic kernel 优化，使 MI350X 在 DLRM 训练吞吐达 B200
  的 101%
practical_value: '- 硬件-模型协同设计：若业务有 AMD MI350X 或其他大 HBM 加速器，不要直接移植 CUDA kernel / 模型配置；应利用更大
  HBM 扩大 per-GPU batch size、减少 activation checkpointing，并尝试扩大 embedding 表、序列长度或 hidden
  dim，可同时获得吞吐和模型质量收益（论文报告 20% 提速、>0.1% NE 提升）。

  - 用分析性能模型替代离线 autotuning：推荐模型 GEMM 形状多且不规则，Origami 用硬件参数化 tile 模型微秒级选择 kernel，精度达
  93%；可将类似思路用于自有训练框架的 kernel 选择或 Triton autotune 配置，避免维护海量 lookup table。

  - 把 AMD 多 chiplet 的坑写进 agent skills：atomics 在 MI350X 上高竞争下可慢 10×，应优先用 shared memory
  树归约 / 寄存器 cache 替换全局 atomic；把这类优化编码为 agentic workflow 技能，可自动修复长尾 kernel（论文中 JFA
  提速 2.3×、端到端 25%）。

  - Triton kernel 的硬件适配经验：AMD 64 线程 wavefront 不同于 NVIDIA warp，建议更大的 num_warps、浅 pipeline（num_stages≈2）、用
  PID swizzle 改善 L2 locality，并启用 matrix_instr_nonkdim=16 / fast_expf 等；这些可作为跨 GPU
  平台的 kernel 调优 checklist。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
Meta 部署异构 GPU 集群（NVIDIA、AMD、MTIA）以降低成本和避免供应商锁定，但长期 NVIDIA 特定优化阻碍性能移植。推荐模型训练尤其困难：DLRM 结构多样、kernel 碎片化、矩阵维度不规则。AMD MI350X 与 B200 理论峰值相近（2300 vs 2250 TFLOPS BF16），但 HBM 容量 1.6×（288 vs 180 GB），scale-up 带宽较弱（538 vs 900 GB/s）。直接移植 CUDA 代码性能差。

**方法关键点**
- **硬件-模型协同设计**：利用 MI350X 大 HBM，扩大 per-GPU batch size、减少 activation checkpointing、优化 embedding re-sharding，并支持更长序列、更大 hidden dim 和 embedding table。
- **Origami 分析性能模型**：用 tile 层次、cache hit rate、wave quantization 和 chiplet 映射预测最优 GEMM 配置，微秒级选择，替代离线 autotune，精度 93%。
- **低层库与通信优化**：hipBLASLt/TensileLite 引入 Stream-K、space-filling curve 工作映射；RCCL 采用 collective-specific QP、LL64 协议、Direct AllGather 和 P2P batching，通信从落后 NCCL 2× 缩至 10-15%。
- **Power excursion boost**：利用 OCP 瞬态功耗限制，在 50ms 窗口内提高计算 kernel 频率，GEMM 微基准最高 1.33×、端到端 3-6%。
- **Agentic kernel 工作流**：将 PID swizzle、occupancy hints、MFMA 配置、atomics 树归约等编码为可复用技能，自动分析、匹配、生成并验证；JFA kernel 提速 2.3×，成功率 >80%。

**关键实验结果**
- 生产 DLRM 训练在数万 MI350X 上验证，MI350X 平均吞吐为 B200 基线的 101%。
- 相较直接移植 baseline，端到端吞吐最高提升 1.5×。
- GDPA forward 2.5×、HSTU forward 3.22×；TBE backward 1.87-3.32×；bounds check 树归约 4.26-4.34×。
- rocSOLVER eigen decomposition 在 4K/8K 达到 cuSOLVER 可比较性能，支撑 Shampoo。

**最值得记住的一句话**
异构加速器的训练性能不是靠移植 CUDA 代码，而是靠硬件-模型协同设计 + 分析性能模型 + 可复用 agentic skills 三者结合。
