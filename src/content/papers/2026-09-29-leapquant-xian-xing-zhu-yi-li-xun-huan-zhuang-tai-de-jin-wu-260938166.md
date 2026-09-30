---
title: 'LeapQuant: Efficient Linear Attention with Accurate Recurrent State Quantization'
title_zh: LeapQuant：线性注意力循环状态的近无损量化与高效推理
authors:
- Yi Pan
- Haocheng Xi
- Kan Zhu
- Xingyang Li
- Yibo Wu
- Mayank Mishra
- Hongtao Zhang
- William X. Zheng
- Baris Kasikci
- Song Han
affiliations:
- UC Berkeley
- University of Washington
- MIT
- Perplexity AI
- NVIDIA
arxiv_id: '2609.38166'
url: https://arxiv.org/abs/2609.38166
pdf_url: https://arxiv.org/pdf/2609.38166
published: '2026-09-29'
collected: '2026-09-30'
category: LLM
direction: 线性注意力状态量化 · 推理加速
tags:
- linear attention
- quantization
- recurrent state
- LLM serving
- INT8
- outlier compensation
one_liner: 通过 per-window 量化与 Compensator Tokens 实现 GDN/KDA 状态 8-bit 近无损，端到端加速 1.47×
practical_value: '- **长序列用户行为模型的状态压缩**：电商/推荐中常用线性注意力或 SSM 建模用户长序列行为，其 recurrent state
  是显存带宽瓶颈。可直接借鉴 per-window 量化：窗口内保持低比特边界状态 + 高精度 buffer 更新，仅在窗口边界重建量化，避免逐 token 误差累积；p=16、INT8
  的配置可直接实验。

  - **用低秩补偿 token 处理状态 outlier**：用户序列或 LLM agent 长轨迹的状态矩阵常有少数行/列异常值，直接量化会放大误差。可以学
  Compensator Tokens：拟合 r=4 的 FP16 低秩成分保留高精度，残差做 channel-wise smoothing 后再量化；对电商场景中的行为状态矩阵同样适用。

  - **长上下文 LLM serving 显存优化**：如果业务中部署 hybrid 线性注意力模型（如 Qwen3.5、Kimi、GLM 系列），对 recurrent
  state 做 8-bit 量化可降低 prefix caching 状态存储 41–56%，直接提升单卡并发；端到端吞吐提升 1.23–1.65×，在长 reasoning/Agent
  任务里收益明显。

  - **工程超参决策参考**：窗口长度 p=16 是精度与 kernel 速度的甜点，过长会导致 buffer 读取增多、kernel 提速下降；Compensator
  Token 数量 r=4 精度饱和，r 超过 8 会暴露计算开销。这些经验可直接用于自研线性注意力推理内核的量化配置。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**

近期 LLM 广泛采用 Gated DeltaNet (GDN) 和 Kimi Delta Attention (KDA) 等线性注意力替代标准注意力，将上下文压缩为固定 size 的 recurrent state，大幅降低长上下文计算成本。但推理时每个 decode step 都要从 HBM 读写完整 state，带宽瓶颈显著，且 prefix caching 下 state 占用大量显存。对 state 做量化是自然选择，但逐 token 量化会累积舍入误差，state 中的 outlier 行/列也导致 naive 量化严重掉点。

**方法关键点**

- **Per-window 量化**：每 16 个 token 只在窗口边界量化一次 state；窗口内保持低比特边界状态 fixed，用高精度 buffer 存储 token updates，输出从 fixed state 和 buffer 计算。误差累积频率降低 p 倍。
- **Compensator Tokens**：用 rank-r（r=4）FP16 低秩项 ˜K˜U⊤ 拟合 state 的主导结构，残差再量化。这些 rank-one 项与真实 token update 同构，可直接纳入 decode kernel 的更新路径，无需额外状态更新。
- **Residual smoothing**：对残差按 key 行均值幅度做可逆缩放，平滑 channel 间 outlier，再执行 INT8 量化。
- 三部分均 training-free，无需校准数据。

**关键实验**

在 Qwen3.5-9B、Qwen3.5-35B-A3B、Kimi-Linear-48B-A3B 上，12 个 model-task 对结果显示：8-bit LeapQuant 平均准确率 75.5%，与 FP32 持平；而 BF16 per-step 只有 68.7%，FP8 per-step 34.2%，INT8 per-step 26.3%。6-bit 和 4-bit 下 LeapQuant 分别保持 72.4% 和 60.4%，远超 baselines。状态内存减少 3.4×，prefix caching 下显存降低 41–56%；kernel 加速 2.05–3.70×，端到端推理加速 1.47×。消融显示 per-window 将 INT8 AIME 从 7.1% 恢复到 82.4%，加上 Compensator Tokens 到 86.6%，smoothing 后回到 87.9% 的 FP32 水平，同时 kernel 加速 2.52×。

**最值得记住的一句话**

对线性注意力 recurrent state，与其逐 token 量化，不如按窗口量化并保留少量高精度低秩补偿 token，可在 8-bit 下近无损且显著加速。
