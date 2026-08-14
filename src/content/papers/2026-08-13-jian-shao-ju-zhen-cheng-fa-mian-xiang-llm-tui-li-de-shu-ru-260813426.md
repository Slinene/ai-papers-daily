---
title: 'Reduced Matrix Multiplication: Input-Adaptive Matrix-Product Reduction for
  LLM Inference'
title_zh: 减少矩阵乘法：面向 LLM 推理的输入自适应矩阵积降维
authors:
- Zixuan Lan
- Yanhong Li
- Jiawei Zhou
affiliations:
- University of Chicago
- Stony Brook University
- Independent Researcher
arxiv_id: '2608.13426'
url: https://arxiv.org/abs/2608.13426
pdf_url: https://arxiv.org/pdf/2608.13426
published: '2026-08-13'
collected: '2026-08-14'
category: LLM
direction: LLM 推理加速 · 动态矩阵乘剪枝
tags:
- LLM Inference
- Matrix Multiplication
- Input-Adaptive Pruning
- Attention Redundancy
- Training-Free
- Kernel Optimization
one_liner: 提出训练无关、输入自适应的 RMM，通过激活 L2 范数 TopK 收缩乘轴，以可预测方式加速 LLM 推理
practical_value: '- 在线服务 LLM 推荐/Agent 时，可优先对 attention 内部 QK^T / PV 做按输入 L2 范数的 TopK
  降维，RR 0.8 左右通常几乎无损；MLP 保持保守，避免模型崩溃。

  - 用 retention ratio 作为统一算力档位，线上可按 QPS/延迟动态调节，获得平滑可控的精度-效率折中，适合流量峰谷调度。

  - 实现时用 Triton 融合 norm+TopK+gather+GEMM，避免选择开销抵消收益；长序列（>2048）下加速更明显，更适合长用户行为摘要/推荐解释生成。

  - 动态 per-token 维度选择比静态子空间更稳；工程上可在 prefill 后固定或定期刷新，减少逐 token TopK 开销。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

动机：Transformer 推理中大量矩阵乘是否有冗余，能否在不改权重、不训练的情况下按输入动态减少 contraction 维度？已有剪枝/稀疏/缓存方法多固定结构或作用于 token/cache，未直接收缩每个 matmul 的共享乘轴。

方法关键点：
- 对任意 Y=AB，按 A 列 L2 范数打分，TopK 选保留维度，得 RMMρ(A,B)=A[:,I]B[I,:]；ρ 为 retention ratio，控制计算量 O(nρdm)。
- 应用于 attention 的 QK^T（head dim）和 PV（token dim），以及 Q/K/V/MLP 线性投影；grouped-query 按 head 独立选。
- 完全 training-free、确定性、逐层逐 token 输入自适应；理论证明 column-norm TopK 最坏情况最优。

关键结果：
- LLaMA 3.1 8B 在 RR=0.5，多任务 QA 平均准确率 59.8，优于 SparseGPT 56.1、Wanda 52.7、SliceGPT 37.0、Magnitude 39.3；全模型 69.8。
- CNN/DailyMail 摘要 RR=0.8 几乎不掉点；RR=0.5 ROUGE-1 34.2，静态 28.0，随机 5.7，H2O 24.4。
- 1B–70B 扫描显示更大模型多数更能承受降低 RR；Qwen3 32B 在 RR=0.5 多数任务仍接近基线。
- RULER 长上下文 5K/15K/30K 在 RR=0.8/0.5 几乎无退化；Qwen2.5-VL 上 POPE RR=0.5 67.3 vs 静态 63.0、随机 1.3。
- 组件分析：attention 侧显著更可剪，MLP 敏感，剪 MLP 高 RR 也塌。
- A100 实测：seq len 4096 端到端 1.40×，QK^T/AV kernel 1.29–1.89×。

最值得记住：注意力侧冗余远高于 MLP，优先剪 attention、保守剪 MLP；activation norm 动态选 dim 是有效且可预测的推理加速杠杆。
