---
title: 'One Symptom, Three Levers: A Critical Review of On-Policy Self-Distillation'
title_zh: 一个症状，三个杠杆：在策略自蒸馏批判性综述
authors:
- Justin Robert
- Raheel Qader
affiliations:
- OVHai LLM
arxiv_id: '2608.25936'
url: https://arxiv.org/abs/2608.25936
pdf_url: https://arxiv.org/pdf/2608.25936
published: '2026-08-25'
collected: '2026-09-09'
category: Training
direction: LLM 训练 · 在策略自蒸馏
tags:
- On-Policy Self-Distillation
- LLM
- Reasoning
- Collapse
- Privileged Information
- Survey
one_liner: 系统化梳理OPSD的坍缩失败模式，提出信号位置、特权信息、动态衰减三杠杆框架
practical_value: '- 若用 OPSD 微调生成式推荐/搜索 Agent（如 query 改写、商品文案生成），可用模型自身作 teacher 并注入业务侧特权信息（用户真实意图、最终成交商品），但必须监控生成多样性（熵、n-gram
  新颖度）以防坍缩。

  - 借鉴三个杠杆做训练设计：`where`——损失只加权关键 token（如最终答案/决策 token）而非全序列平均；`what`——teacher 的特权信息粒度要渐进揭示，避免过度强条件导致模型只学会抄捷径；`when`——蒸馏信号随训练衰减，后期保持与
  base policy 的 KL 约束。

  - 对 Agent 搜索/推荐，坍缩类比于动作空间收窄：训练时环境反馈或 oracle 路径会诱导窄策略，需加入熵正则或行为多样性约束。

  - 没有新实验，但提供统一术语与诊断清单，适合作为生产 LLM 微调前的风险自查。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**
On-policy distillation 让 teacher 对模型自身生成逐 token 打分，兼具模仿学习的稠密监督与 RL 的在线采样，但需要更大模型作 teacher。OPSD 去除该成本：teacher 是模型自身，仅用测试时不可见的特权信息（参考解、计划、环境反馈）增强；teacher 并不更强，只是信息更多。早期在数学推理上以远少生成 token 达到接近 RL 的精度。

**方法关键点**
该综述不做新实验，把 OPSD 的主要失败模式——坍缩（模型推理路径逐渐收窄）——视为一个症状，由三个杠杆控制：(i) 信号施加位置（token 加权方式）；(ii) teacher 所见内容（特权信息性质）；(iii) 信号变化时机（teacher 动态与指导衰减）。范围限定在数学推理，因为该方法起源于此且失败模式记录最充分。

**关键结论**
作为结构性贡献：统一不同论文中名称各异的现象，区分已确认结论与仍存争议之处。已确认：特权信息加剧坍缩；坍缩源于同一不对称性产生的偏置；仅靠 token 平均加权不足以解决。争议点：如何最优设置三杠杆、坍缩与准确率下降的因果关系仍需实验验证。
