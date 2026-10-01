---
title: Fractional State Space Transition for Long Sequence Modeling
title_zh: 分数阶状态空间转移用于长序列建模
authors:
- Ivan Kobyzev
- Abbas Ghaddar
- Ali Nasiri-Sarvi
- Lifeng Shang
- Yufei Cui
affiliations:
- Huawei Noah's Ark Lab, Montreal Research Center, Canada
arxiv_id: '2609.36314'
url: https://arxiv.org/abs/2609.36314
pdf_url: https://arxiv.org/pdf/2609.36314
published: '2026-09-27'
collected: '2026-10-01'
category: LLM
direction: 长序列建模 · 分数阶状态空间
tags:
- SSM
- Fractional Dynamics
- Long Sequence Modeling
- Power-law Memory
- Selective State Space
- Language Modeling
one_liner: 用分数阶动力学替换指数遗忘，通过有限指数模态近似实现高效选择性SSM长序列建模
practical_value: '- **用户长期行为序列建模可直接借鉴**：电商/广告场景通常有数月甚至跨年的点击、浏览、购买序列，传统 SSM/RNN 的指数衰减会快速抹掉早期兴趣。FRAC
  的分数阶动力学生成幂律记忆，能在更长时间范围保留历史影响，适合作为用户长期兴趣记忆模块。

  - **多时间尺度记忆银行的具体实现**：将状态转移分解为 log-spaced 指数衰减模态，用可学习 α_t 控制衰减强度，并用 token-dependent
  λ_t 做选择性调制。这种设计与用户行为中不同时间尺度模式（如近期强兴趣、历史稳定偏好）天然对齐，可直接嵌入现有 user encoder。

  - **工程实现与训练效率**：FRAC 保持一阶仿射递归，可用 chunked parallel scan 并行训练/prefill，自回归解码有界状态，且有
  custom Triton kernel。对需要低延迟、长序列增量更新的推荐/广告检索系统来说，架构可迁移。

  - **读写对齐技巧**：read/write 路径共享 softmax(-α_t log τ_m + g(u)_m) 的对数时间尺度寻址，能提升信息写入和读取的一致性。在用户行为表示中可类比为让不同时间尺度的兴趣槽位在写入和读取时使用同一套寻址逻辑，增强记忆可检索性。

  - 若业务序列普遍较短或已由 Transformer 覆盖，收益可能有限；但对长上下文行为建模和实时增量计算场景值得尝试。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**

SSM 把整个序列历史压缩进有界循环状态，因此内部 memory law 直接决定长上下文能力。现有主流 SSM 如 Mamba、Gated DeltaNet 均基于 ODE 微分方程及其离散化，其底层动力学天然带来指数遗忘：过去输入的影响随时间指数衰减。这对需要在广泛时间范围内保留非平凡影响的序列并不理想。分数阶微分方程（FDE）在物理和数学中被用于建模遗传效应，其解依赖完整历史且核函数具有重尾特性，但 FDE 非马尔可夫、不直接兼容有限状态循环层。

**方法关键点**

- 从 Caputo 分数阶导数（0<α<1）的线性系统出发，其齐次解为 Mittag-Leffler 函数，渐近衰减为 t^{-α}，比指数衰减慢得多。
- 利用 diffusive representation 将 Mittag-Leffler 核表示为连续指数衰减的混合，然后在有限时间范围用对数间隔的有限指数模态之和（Sum-of-Exponentials）近似，得到一个一阶 ODE memory bank。
- 对 memory bank 做 ZOH 离散化，得到每个模态的递归：s_{t,m}=ρ_{t,m}s_{t-1,m}+β_{t,m}u_t，其中 ρ=exp(-Δ/τ_m)，β=(1-ρ)/λ。
- 引入选择性：Δ_t、λ_t、α_t 由输入投影得到，分别控制步长、时间尺度缩放和长记忆强度；α_t 经 sigmoid 限制在 (0,1)，λ_t 经 softplus 保证正。
- 读/写权重采用 softmax(-α_t log τ_m + g(u)_m) 的对数时间尺度寻址，使信息写入和读取在模态银行上对齐。
- 整体保持一阶仿射递归，可用 chunked parallel scan 训练和 prefill，自回归解码拥有有界状态缓存。

**关键实验与结果**

- 在 heavy-tail 合成外推任务上，模型仅在 512 长度训练，FRAC 在 128K 评估时的性能下降最小，显著优于 Attention、Mamba2/3 和 GDN。
- 1.3B 参数 LLM 从零预训练 100B FineWeb-Edu tokens，序列长度 4K：FRAC 在 NIAH 长上下文外推至 64K 时衰减最慢；LongBench 平均 17.9，比最强线性 baseline GDN 的 16.0 高 1.9%，在 8/14 任务上最优；LM Harness 平均 55.1，仅比 Transformer 低 0.2；Recall-Retrieval 平均 36.4，排名第三。
- DNA 建模上，7M 参数 HG38 模型在 64K 序列长度下，FRAC 的 perplexity 低于 Mamba3 和 GDN，且优势随上下文变长而增大。

最值得记住的一句话：用分数阶动力学替换 ODE 的指数遗忘，通过在 log 时间尺度上的有限指数模态近似实现一种可扩展、可并行的选择性 SSM，为长上下文序列建模提供了新的记忆规律先验。
