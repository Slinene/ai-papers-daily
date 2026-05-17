---
title: Explainable Detection of Depression Status Shifts from User Digital Traces
title_zh: 用户数字痕迹中抑郁状态变化的可解释检测
authors:
- Loris Belcastro
- Francesco Gervino
- Fabrizio Marozzo
- Domenico Talia
- Paolo Trunfio
arxiv_id: '2605.14995'
url: https://arxiv.org/abs/2605.14995
pdf_url: https://arxiv.org/pdf/2605.14995
published: '2026-05-14'
collected: '2026-05-17'
category: LLM
direction: 可解释抑郁状态变化检测·时间轨迹分析
tags:
- explainability
- mental health
- BERT
- LLM
- temporal trajectory
- change point detection
one_liner: 融合多BERT模型信号与LLM生成可读报告，实现抑郁状态变化点的可解释检测与分析
practical_value: '- 多源BERT信号融合构建用户状态轨迹，可迁移至电商用户兴趣演化建模，捕捉兴趣变化

  - LLM生成可读报告的方式为推荐系统提供可解释性思路，自动生成推荐理由

  - 变化点检测算法能识别用户偏好突变，应用于实时推荐策略动态调整

  - 时间分段轨迹分析适用于处理非平稳用户行为序列，可借鉴至时间感知推荐模型'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：用户每天产生的数字痕迹（社交媒体、聊天等）带有时间戳，可能反映心理状态。需要从这些时间序列中自动检测抑郁状态的变化（改善、恶化、稳定），并提供可解释的分析。

**方法**：提出一个可解释框架。首先，使用多个基于BERT的模型从不同维度（如情感、情绪、抑郁严重度）提取互补信号。然后将这些信号按时间聚合，构建用户级时间轨迹。通过变化点检测算法找出轨迹中的显著转折点。最后，引入大语言模型（LLM）生成简洁的人类可读报告，描述心理状态信号的演变并突出关键转变，增强可解释性。

**结果**：在两个社交媒体数据集上的评估表明，该方法生成的报告比直接让LLM报告更连贯、信息更丰富，覆盖更多用户历史，时序连贯性更强，且对变化点的识别更敏感。消融实验证实了时间建模和轨迹分段的关键作用。整体上，该方法提供了随时间变化的心理状态信号的可解释视图，可用于研究和决策支持。
