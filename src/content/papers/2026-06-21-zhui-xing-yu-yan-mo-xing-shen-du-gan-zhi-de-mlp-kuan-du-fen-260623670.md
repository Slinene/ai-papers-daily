---
title: Tapered Language Models
title_zh: 锥形语言模型：深度感知的 MLP 宽度分配
authors:
- Reza Bayat
- Ali Behrouz
- Aaron Courville
affiliations:
- Mila
- Cornell University
- Université de Montréal
- CIFAR AI Chair
arxiv_id: '2606.23670'
url: https://arxiv.org/abs/2606.23670
pdf_url: https://arxiv.org/pdf/2606.23670
published: '2026-06-21'
collected: '2026-06-23'
category: LLM
direction: 语言模型架构优化 · 深度感知容量分配
tags:
- LLM
- Architecture
- MLP
- Tapering
- Parameter Efficiency
- Depth-aware
one_liner: 在总参数固定下，让 MLP 宽度随层深递减（余弦锥形）可免费提升 Transformer 等模型的困惑度与下游性能
practical_value: '- **免费性能提升**：在训练推荐领域的 Transformer 模型（如 CTR 预估、行为序列建模）时，可将 MLP 中间宽度按余弦锥形从底层向顶层递减，在零额外参数和计算下获得困惑度或下游指标提升。

  - **超参搜索技巧**：锥形范围（起始宽度倍数->结束宽度倍数）和衰减形式（余弦 vs 线性）可视为新的架构超参，直接用固定总预算的缩放实验快速寻优，无需改动训练流程。

  - **与现有架构解耦**：方法不依赖特定注意力机制，可直接叠加到 Gated Attention、Hope-attention、Titans 等变体上，方便复用到自研或改进的推荐模型。

  - **强化学习 Agent 内部模型**：若 Agent 内部使用 Transformer 作为策略或值函数网络，锥形 MLP 同样可作为低成本的结构性改进，在不增加推理成本的前提下提升模型容量利用效率。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有语言模型（Transformer、循环、记忆变体）一律沿深度均匀分配参数，但大量证据表明后期层主要精炼残差流，贡献递减。在固定参数预算下，反向分配（前重后轻）能否更好？

方法：提出锥形语言模型（Tapered Language Models, TLMs），在总参数量固定时，让参数承载组件沿深度单调递减。MLP 是天然载体，因其在所有现代 LM 中参数占比高，宽度可作为单一变量调节。采用平滑余弦调度（cosine schedule），用起始/结束宽度倍数控制锥形范围。实验在 150M、440M、1B 规模下，覆盖 Transformer、Gated Attention、Hope-attention、Titans 四种架构，以均匀宽度为基线，保证参数量和 FLOPs 完全相同。

结果：440M Transformer 上，余弦锥形将验证困惑度从均匀基线的 16.28 降至最低 14.44（锥形范围 1.5→0.5），线性锥形也优于均匀；反向分配（后重前轻）则损害性能。所有规模与架构下，锥形 MLP 宽度一致提升困惑度与下游基准（MMLU、HellaSwag 等），且零额外成本，证明深度感知容量分配是一个简单、架构无关的设计杠杆。
