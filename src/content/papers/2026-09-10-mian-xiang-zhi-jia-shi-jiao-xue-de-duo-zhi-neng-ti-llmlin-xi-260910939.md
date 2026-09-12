---
title: Evaluating Scaffolding-Oriented Multi-Agent Large Language Model System for
  Clinical Interview Training
title_zh: 面向支架式教学的多智能体LLM临床访谈训练系统评估
authors:
- Luming Yang
- Haoxian Liu
- Siqing Li
- Rong Jia
- Yue Xiao
- Guanhua Chen
- Li Lu
affiliations:
- The Ohio State University
- Hong Kong University of Science and Technology
- Southern University of Science and Technology
- Johns Hopkins University
- Guangzhou Medical University
arxiv_id: '2609.10939'
url: https://arxiv.org/abs/2609.10939
pdf_url: https://arxiv.org/pdf/2609.10939
published: '2026-09-10'
collected: '2026-09-12'
category: MultiAgent
direction: 多智能体协作 · 教育训练
tags:
- multi-agent
- LLM
- scaffolding
- role-play
- dialogue evaluation
- clinical training
one_liner: 多智能体 AI 标准化病人系统通过患者/导师/逐轮评估分工与渐进式提示，提升医学生沟通、共情与病史采集过程质量，但不抬高诊断准确率
practical_value: '- 多智能体角色分离：患者 / 导师 / 逐轮评估 agent 各司其职，避免单模型同时扮演多角色导致目标冲突。电商客服培训、对话式推荐沙盒可拆分为用户模拟、导购教练、质检
  agent，提升训练可控性。

  - 过程性反馈不透露总分：turn-level evaluator 只反馈行为进展，不暴露最终分数，减少 reward hacking。推荐 Agent 训练中可引入仅过程奖励或隐藏最终指标，让模型更关注交互质量。

  - 苏格拉底式提示与渐进信息披露：tutor agent 用追问引导而非直接给答案，可用在智能导购 / 客服培训中，通过逐步追问用户需求、商品属性，训练 Agent
  的提问与推理能力。

  - 细粒度评估指标：OSCE 对齐的沟通、共情、病史采集行为分项改进，即使诊断准确率无差异。电商对话系统可借鉴构建 turn-level 过程评估，衡量提问覆盖率、共情表达等，而不仅看转化。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：临床教育需要可扩展的标准化病人训练，传统 SP 成本高，案例学习又缺乏实时沟通压力。
方法关键点：构建 scaffolding-oriented 多智能体 LLM AI-SP 平台，包含患者 agent 模拟对话、tutor agent 用苏格拉底式提示引导病史采集/推理/共情但不泄漏诊断、turn-level evaluator agent 监测过程且不透露总分；对照组采用结构化渐进信息披露而非 LLM。随机对照 N=100 医学生，两轮学习后进入仅患者环境考试，采用 OSCE 规则评分。
结果：最终诊断准确率组间无显著差异；多智能体 AI-SP 显著提升最终考试总分，最明显和一致的增益在沟通、可观察共情表达、特定病史采集行为。说明专业 LLM agent 能提高模拟访谈过程质量，而非抬高考试成绩。同步发布多专家标注数据集，含转录、checklist 注解、逐轮评估、OSCE 对齐评分，可用于教学型 AI-SP 系统和临床推理训练研究。
