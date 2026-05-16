---
title: A Hierarchical Language Model with Predictable Scaling Laws and Provable Benefits
  of Reasoning
title_zh: 具有可预测缩放定律及推理可证明益处的层级语言模型
authors:
- Jason Gaitonde
- Frederic Koehler
- Elchanan Mossel
- Joonhyung Shin
- Allan Sly
affiliations:
- Duke University
- University of Chicago
- MIT
- Princeton University
arxiv_id: '2605.13687'
url: https://arxiv.org/abs/2605.13687
pdf_url: https://arxiv.org/pdf/2605.13687
published: '2026-05-13'
collected: '2026-05-16'
category: LLM
tags:
- LLM
- Scaling Laws
- Reasoning
- Hierarchical Models
- Broadcast Process
- Context Length
one_liner: 用树广播过程定义合成语言，精确分析上下文长度与推理的作用，证明有限上下文导致统计不一致且 O(log n) 记忆的推理即可精确采样
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**  
现代大语言模型中，上下文窗口长度是核心设计参数，但究竟多少上下文才能忠实复现全局语言分布仍缺乏严格理论。现有理论多关注最坏情况表达能力，而实际训练得到的模型行为与统计分布的对齐未被定量刻画。该工作引入一类由树广播过程生成的层级合成语言，其分布可精确分析，从而首次给出上下文长度与推理作用在自回归生成中的定量缩放定律和严格下界。

**方法关键点**
- **数据模型**：定义 (d, h, κ, ν)-广播过程，在 d-ary 树上从根先验向下通过噪声信道传播，叶节点构成观测序列；研究两种实例：Ising 广播过程（软约束）和着色广播过程（硬约束）。
- **理论分析替身**：提出 k-gram ansatz，用仅依赖前 k 个 token 的最优自回归过程代替 transformer，推导生成序列的分布统计量。
- **下界**：证明对于 Ising 过程，有限上下文造成生成序列的总和方差对数线性于上下文深度，且峰度趋于高斯，远弱于真语言的多尺度长程相干；对于着色过程，在冻结区间有限上下文几乎必然产生不一致的序列，给出 Ω(n) 的上下文长度下界。
- **上界**：引入推理记忆模型，证明仅需 Θ(log n) 比特的工作记忆即可从真语言中精确采样，实现指数级改善。

**关键结果数字**
- 在 d=3, h=8, ρ=0.9 的 Ising 实验中，非推理 transformer 的 log 归一化方差和峰度随上下文减小偏离真值，与理论渐近线吻合；推理模型即使上下文仅 64 远小于总长 6561，仍接近真值。  
- 在 d=4, h=6, q=3 的着色实验中，非推理模型小上下文几乎完全不生成有效序列（有效率接近 0），而推理模型几乎总是有效（接近 1）。  
- 理论上，方差对数标度斜率为 log(dρ²)，峰度趋于高斯峰度 3；推理记忆只需 O(h log(d|Σ|)) 比特。  
- 核心启示：**“有限上下文自回归在层级语言中产生可预测的统计失真或逻辑不一致，而极少量可写记忆的推理即可恢复真实分布。”**
