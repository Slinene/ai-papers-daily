---
title: 'Distance generalization in transformers: why bother with positional encoding?'
title_zh: Transformer 中的距离泛化：何必费心使用位置编码？
authors:
- Daniel Henrik Nevermann
- Claudius Gros
affiliations:
- Institute for Theoretical Physics, Goethe University Frankfurt, Germany
arxiv_id: '2609.11913'
url: https://arxiv.org/abs/2609.11913
pdf_url: https://arxiv.org/pdf/2609.11913
published: '2026-09-10'
collected: '2026-09-11'
category: Training
direction: Transformer 距离泛化 · 位置编码消融
tags:
- distance generalization
- positional encoding
- RoPE
- ALiBi
- NoPE
- synthetic tasks
one_liner: 系统考察 RoPE/ALiBi/NoPE 在合成延迟复制任务上的距离泛化，发现位置编码效果有限且数据多样性影响关键。
practical_value: '- 在推荐/搜索序列建模中，如果序列长度固定且 token 间距离范围有限，NoPE 可能足够，可移除位置编码以降低模型复杂度和训练成本。

  - 训练数据中覆盖的 token 间距离多样性对距离泛化至关重要：构建行为序列样本时，应刻意采样不同间隔的交互对，避免模型只见过短距离依赖。

  - 距离迁移学习可能为负，说明模型在特定距离上过拟合；上线前需评估用户行为序列分布与训练分布的偏移，尤其是时间间隔分布变化。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：长度泛化已被深入研究，但距离泛化（固定上下文长度下改变 token 间距离）鲜有系统分析，可能揭示不同的失败模式。

方法：构建两个合成延迟复制任务（完整复制与选择性复制），固定上下文长度，在训练与推理之间改变源 token 到目标 token 的距离。比较 RoPE、ALiBi 与 NoPE 三种方案在未见过距离上的表现，并分析训练数据中距离多样性的影响，以及距离迁移学习的正负效应。

关键结果：论文未给出具体数值，但通过消融实验指出：位置编码（RoPE/ALiBi）相对 NoPE 并未一致提升距离分辨率；训练时覆盖更多距离可显著改善泛化；距离迁移学习可能带来正面或负面效果，取决于具体条件。作者强调需进一步理解 transformer 内部的距离表示机制。
