---
title: 'An Emergent Mirage: Is Emergent Misalignment and Realignment Indeed a Robust
  Phenomenon?'
title_zh: 涌现性对齐偏差现象的鲁棒性再检验：受表层特征混淆的伪象
authors:
- Abhinav Rao
- Liancheng Gong
- Bin Hu
- Atharva Naik
affiliations:
- University of Maryland
- Carnegie Mellon University
arxiv_id: '2607.09053'
url: https://arxiv.org/abs/2607.09053
pdf_url: https://arxiv.org/pdf/2607.09053
published: '2026-07-10'
collected: '2026-07-13'
category: Eval
direction: LLM 错位与重对齐现象评估 · LoRA 表征分析
tags:
- Emergent Misalignment
- Realignment
- LoRA
- LLM Safety
- Evaluation
one_liner: 发现 Emergent Misalignment 与重对齐对数据集表层特征高度敏感，先前声称的机械签名不可靠
practical_value: '- 微调模型时需警惕回答长度等表层特征混淆行为评估，在推荐对话或 Agent 任务中应控制输出长度差异，避免将风格迁移误判为策略改变。

  - LoRA 微调后常以参数相变解释行为突变，该工作在安全领域发现相变与行为不相关，提示在电商用 LoRA 做用户表示或 item 表示更新时，不应仅凭表征空间跳变推断业务指标，需直接测量在线
  A/B 指标。

  - 设计评估协议时推荐使用连续、平滑的指标替代离散判断，并注意数据集构建时的隐式偏差（如 answer length prior），对推荐系统离线评估中 ranking
  metric 的选择也有类似启示。

  - 若在推荐中应用类似对齐-错位场景（如恶意攻击微调），该结论提醒表象突然的性能崩塌可能来自数据构造，而非模型本质脆弱，安全审计需从数据源头排查。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：近期工作声称 LLM 在窄域、特定错位数据上微调后会“涌现”出广泛的不对齐行为（Emergent Misalignment, EM），并且通过少量重对齐数据可迅速逆转。本文质疑该现象的稳健性，系统研究多轮对齐与错位循环中行为与表征变化。

**方法关键点**：在可控微调循环中反复执行错位（用误信息数据）与重对齐（用对齐数据），全程跟踪行为指标，并检查 LoRA 表征空间。特别控制回答长度等表面数据特征，以剥离真实的行为变化。

**关键结果**：
- 成功复现 EM，但发现错位与重对齐对数据集表层特征高度敏感。
- 在控制回答长度差异后，先前观察到的“快速重对齐”几乎消失，说明其可能源于模型学习了长度偏好而非真正对齐。
- 之前报道的 LoRA 表征相变与行为错位/重对齐不存在一致相关性，表明机械签名不可靠。
- 整体结论：当前 EM 证据比先前声称的更脆弱，评估协议需仔细控制数据表面假象。
