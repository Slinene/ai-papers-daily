---
title: Parallelism, critical windows, and separations among diffusion language models
title_zh: 扩散语言模型的并行性、关键窗口与范式分离
authors:
- Sitan Chen
- Liye Wang
affiliations:
- Harvard University
- Tsinghua University
arxiv_id: '2609.20539'
url: https://arxiv.org/abs/2609.20539
pdf_url: https://arxiv.org/pdf/2609.20539
published: '2026-09-17'
collected: '2026-09-19'
category: LLM
direction: 扩散语言模型并行采样理论
tags:
- diffusion language models
- parallelism
- masked diffusion
- uniform diffusion
- Gaussian diffusion
- critical windows
one_liner: 首次证明均匀/高斯扩散的并行采样步数可随分布内在复杂度缩放，且掩码扩散因关键窗口更窄需更多前向次数
practical_value: '- 在电商/搜索场景用扩散 LM 生成商品文案、Query 补全或推荐语时，优先评估均匀/高斯扩散：其采样前向步数可随分布的 dual
  total correlation 缩放，对属性条件独立、结构化程度高的商品或 Query 分布，可能远低于序列长度，适合低延迟并行生成。

  - 若生成式推荐使用 Semantic ID + masked diffusion，注意掩码扩散在近似 score 下存在 Ω(d) 并行下界；对长 token
  序列且延迟敏感的服务，可尝试用均匀或高斯扰动替代离散“吸收态”，拓宽关键窗口以提升并行度。

  - 工程调优可从“关键窗口宽度”切入：若观察到掩码扩散后期 token 状态突变、需大量去噪步，可借鉴均匀/高斯扩散的连续松弛或噪声调度，避免在窄窗口内做硬离散决策，减少串行步骤。'
score: 6
source: arxiv-stat.ML
depth: abstract
---

**动机**：扩散语言模型（dLLM）以并行生成为卖点，但 masked、uniform、Gaussian 三种主流水线在并行性上缺乏细粒度理论比较。现有工作仅知 masked diffusion 可达到与分布内在复杂度相关的采样步数，本文补齐 uniform/Gaussian 的结果并首次证明范式间分离。

**方法关键点**：以采样所需前向次数度量并行度，引入 dual total correlation 刻画分布内在复杂度；构造一类随机经验测度，对 uniform、Gaussian、masked diffusion 推导并行采样的上下界；进一步分析各范式的 critical window 宽度。

**关键结果**：uniform 与 Gaussian diffusion 可在 O~(dual total correlation) 次前向内采样，不依赖上下文长度；对某随机经验测度族，二者需要 Θ~(√d) 次前向，而 masked diffusion 即使有近似 score oracle 也需 Ω(d) 次，首次建立三种范式的并行性分离。直觉上以为 masked diffusion 的劣势来自必须提前确定 token 值，但证明表明真正原因是其 critical window 渐进更窄，导致去噪过程需要更多串行步骤。
