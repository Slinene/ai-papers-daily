---
title: 'Edit the Bits, Diff the Codes: Bitwise Residual Editing for Visual Autoregressive
  Models'
title_zh: 编辑比特，差分代码：视觉自回归模型的位级残差编辑
authors:
- Shengqiang Zhang
- Ruotong Liao
- Volker Tresp
- Barbara Plank
- Hinrich Schütze
affiliations:
- LMU Munich
- Munich Center for Machine Learning (MCML)
arxiv_id: '2606.13558'
url: https://arxiv.org/abs/2606.13558
pdf_url: https://arxiv.org/pdf/2606.13558
published: '2026-06-11'
collected: '2026-06-14'
category: Multimodal
direction: 视觉自回归模型的训练无关编辑
tags:
- image editing
- visual autoregressive
- bitwise-residual
- training-free
- Bernoulli guidance
- residual code
one_liner: 在视觉自回归模型中引入位级伯努利引导与多尺度残差码重注入，实现背景保持的精准图像编辑。
practical_value: '- 训练无关的编辑思路可直接用于电商商品图的快速迭代，无需微调生成模型。

  - 位级伯努利引导的闭式信任区域优化可作为其他生成任务（如图文匹配）的安全采样策略。

  - 多尺度残差码的门控注入方法能保证编辑区域外像素完全一致，适合生成式推荐的视觉保真需求。

  - 源-目标对比的负向引导技巧可复用到文本到图像生成的控制中，提升语义对齐。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有视觉自回归（VAR）图像编辑方法忽略了两大原生结构——逐位伯努利预测头与多尺度残差码场，导致语义对齐与背景保持难以兼得。

**方法**：提出BitResEdit，将编辑分解为BitEdit与ResEdit。BitEdit在采样决策时，利用源-目标对比构建负向引导，倾斜CFG后的逐位log-odds，并通过闭式伯努利KL信任区域约束更新幅度。ResEdit在码组合阶段，将采样的比特转为多尺度连续残差，用定位掩码门控，通过生成器的原生尺度求和重注入，实现编辑区域外的精确保留。两者耦合，在决策与组合层面协同控制。

**结果**：在PIE-Bench上，基于Infinity-2B，BitResEdit在相同骨干的VAR编辑器中取得最强文本对齐，编辑区域CLIP得分比最强基线高+1.07，背景保持指标具有竞争力。消融表明BitEdit与ResEdit在目标对齐与背景保持上互补。
