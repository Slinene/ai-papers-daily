---
title: 'DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding'
title_zh: DeaMoE：面向小批量快速解码的高效 MoE 结构
authors:
- Zewen Jin
- Shen Fu
- Zeping Duan
- Shannon Wang
- Weihao Wu
- Chengjie Tang
- Congkun Ai
- Ping Gong
- Zijian Dai
- Youhui Bai
affiliations:
- University of Science and Technology of China
- Institute of Artificial Intelligence, Hefei Comprehensive National Science Center
- Shanxi University
arxiv_id: '2608.14385'
url: https://arxiv.org/abs/2608.14385
pdf_url: https://arxiv.org/pdf/2608.14385
published: '2026-08-14'
collected: '2026-08-17'
category: LLM
direction: 高效 MoE 解码架构 · 小批量推理
tags:
- MoE
- small-batch decoding
- expert loading
- parameter sharing
- inference optimization
- LLM serving
one_liner: DeaMoE 将专家分组为部门，共享大部分参数并设计两级路由，在小批量解码下降低专家权重加载，实现最高 2 倍加速
practical_value: '- 若业务用 DeepSeek-V3/Qwen3 等大 MoE 做实时 query 改写、广告文案生成或 Agent tool
  call，小批量延迟不达标时，可考虑 DeaMoE 式重组：把 256/384 个 experts 分成 8/16 个 departments，共享 FFN 主矩阵，每个
  expert 只保留 [hffn, hffn] 私有矩阵；在总参数和 FLOPs 不变的前提下，A40 上可获得 1.3–2.0× TPOT 加速。

  - 改造时用 group-limited top-k 软约束控制每个 token 激活的 department 数，不要强制覆盖 kdept 个 department；ablation
  显示 strict coverage 会扰动路由偏好并提高 loss，软约束下平均激活 3.95/4 个 department 已足够。

  - 私有 expert 矩阵用 torch.nn.init.eye 做 identity 初始化，而不是随机初始化；在 factorized 结构下可显著降低预训练
  loss（2.504 vs 2.530），避免随机初始化扭曲共享 backbone 表示。

  - 工程实现可沿用 vLLM Grouped GEMM primitives，只改 token indexing 支持 hierarchical routing；注意收益与
  expert 大小和 GPU 带宽强相关，H100 上小 expert 模型可能回退，优先用于大 expert MoE 和带宽受限硬件。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
MoE 模型越来越多用于实时交互应用（代码补全、语音助手、音视频多模态系统），严格延迟约束下常采用小批量解码（4–128 tokens/step）。此时推理从 compute-bound 变为 memory-bound：每步只处理少量 token，但每 token 激活多个 expert，expert 权重分散且复用率低，延迟被反复加载 expert 参数主导。已有后训练压缩会损失质量，预训练细粒度 expert 依赖推理并行、在小批量下不可用，因此需要直接减少 per-step expert loading。

**方法关键点**
- **结构**：把 n 个 experts 分组为 m 个 departments；同一 department 内 experts 共享大 gate/up/down 投影矩阵，每个 expert 只保留小的私有矩阵 A_i_g、A_i_u、A_i_d 来体现差异化。
- **两级路由**：先由 router 选择 department，同一 department 的所有 token 先统一做共享大矩阵计算，再分配给具体 expert 做私有变换，避免共享大矩阵的重复加载。
- **非线性连接**：department 与 expert 投影之间插入 SiLU，避免连续线性映射；ablation 显示 SiLU 优于 GeLU、RMSNorm 和去掉非线性。
- **预算匹配**：通过 group top-k 限制每 token 激活的 department 数，保证与 standard MoE 的总参数和 per-token FLOPs 相当；DeaMoE 配置对 DeepSeek-V3、Qwen3-235B-A22B 等模型 FLOPs/Params 比例约 1.0。
- **训练 recipe**：私有 expert 矩阵用 identity 初始化，而非随机初始化；soft group-limited top-k 优于 strict department coverage。

**关键实验**
在 110B tokens RedPajama-v1 上预训练 7.3B DeaMoE 与 Baseline-7B：下游 10 个 benchmark 整体可比，PTB 和 WikiText-2 的 PPL 更低。端到端 vLLM 在 A40 上，DeaMoE 最高获得 1.33× TPOT 加速（batch 32）；在 20ms TPOT 预算下，吞吐提升 1.83×。微基准中，DeepSeek-V3 配置在 A40 和 H100 上峰值加速分别为 2.00× 和 1.97×；Qwen3-235B-A22B 配置分别达 1.74× 和 1.60×。

**最值得记住的一句话**
DeaMoE 不是让 expert 变小，而是让 expert 权重更可复用：通过 department 共享 + 两级路由，把小批量 MoE 解码的权重加载瓶颈转化为结构性的内存流量下降。
