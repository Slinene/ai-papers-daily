---
title: Transferring an analysis of human brain organization to language models
title_zh: 将人脑皮层组织分析迁移到语言模型
authors:
- Donghyeok Lee
- Sangwon Yu
- Sangkwon Park
- Hye Youn Park
- Munyoung Chang
- Sungroh Yoon
affiliations:
- Interdisciplinary Program in Artificial Intelligence, Seoul National University
- Department of Electrical and Computer Engineering, Seoul National University
- Upstage AI
- Seoul National University Bundang Hospital
- Seoul National University College of Medicine
arxiv_id: '2611.24626'
url: https://arxiv.org/abs/2611.24626
pdf_url: https://arxiv.org/pdf/2611.24626
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: LLM 推理区域定位与权重嫁接
tags:
- LLM interpretability
- cortical gradients
- model grafting
- reasoning
- weight transfer
- training dynamics
one_liner: 用脑皮层梯度分析法定位 LLM 中可迁移的推理相关权重区，嫁接可提升数学推理且干扰低
practical_value: '- 可借鉴 diffusion-map 表征梯度分析，对电商/广告模型的 embedding 或 attention 层做功能分化诊断，定位与特定业务能力（如价格敏感、促销规则、品牌偏好）相关的连续层区间，避免全模型盲目调整。

  - 权重嫁接可作为一种低成本的跨模型能力迁移手段：把精调专家模型（如推理、医学）的关键 span 嫁接到线上 serving 模型，相比全量合并或蒸馏更轻量，且干扰更小；在多场景推荐/广告模型中可尝试迁移特定场景能力。

  - 训练早中期 checkpoint 的 span 已具备迁移价值，说明无需等收敛即可做 region overlap 检测与中间阶段嫁接，节省迭代成本；对需要数学/逻辑推理的智能客服、广告出价策略等场景，可只微调定位到的相关
  span，降低灾难性遗忘。

  - 通过 region overlap 程度预测迁移效果，可作为模型能力迁移前的筛选指标，减少无效实验。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**  
人类皮层发育中功能系统逐渐分化，推理能力的提升是否也对应 LLM 内部的区域重组？借鉴神经科学方法有助于定位与推理相关的权重区域。

**方法关键点**  
用 diffusion-map embedding 刻画皮层组织，对三个模型家族的 base 与 reasoning-trained 版本做表征梯度分析，发现整体梯度结构大体保留，但存在连续层 span 的局部变化。将该 span 权重嫁接到 instruction-tuned host 模型，并对比不同区域重叠度、不同训练阶段的嫁接效果。

**关键结果数字**  
嫁接该 span 平均提升数学推理成绩，且区域重叠度越高提升越明显；相比嫁接其他位置，能保留更多已解决的问题。训练过程中，该 span 在早期性能快速上升时逐步形成，中间阶段的 checkpoint 嫁接同样有效。此外，同一分析还能在医学模型中定位可迁移 span。整体表明存在一个推理相关区域，其权重能以较低干扰提升宿主的数学推理能力。
