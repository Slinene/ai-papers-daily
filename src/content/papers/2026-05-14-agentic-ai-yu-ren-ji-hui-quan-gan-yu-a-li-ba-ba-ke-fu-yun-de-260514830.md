---
title: 'Agentic AI and Human-in-the-Loop Interventions: Field Experimental Evidence
  from Alibaba''s Customer Service Operations'
title_zh: Agentic AI 与人机回圈干预：阿里巴巴客服运营的现场实验证据
authors:
- Yiwei Wang
- Chuan Zhu
- Tianjun Feng
- Lauren Xiaoyuan Lu
- Bingxin Jia
affiliations:
- Zhejiang University
- Fudan University
- Dartmouth College
- Alibaba Group Inc.
arxiv_id: '2605.14830'
url: https://arxiv.org/abs/2605.14830
pdf_url: https://arxiv.org/pdf/2605.14830
published: '2026-05-14'
collected: '2026-05-16'
category: Agent
tags:
- Agentic AI
- Human-in-the-loop
- Customer Service
- Field Experiment
- Emotional Escalation
one_liner: 揭示 agentic AI 客服中人工干预效果取决于失败类型与时机，早期介入和整合角色设计更优
score: 8
source: arxiv-cs.HC
depth: full_pdf
---

## 动机
在客户服务场景部署 agentic AI 时，AI 失败不仅带来认知误差，还会引发客户情绪恶化。现有 human-in-the-loop 研究多关注纯技术纠错（如医学影像），但客服环境中人工干预如何影响服务质量、何时有效、如何设计流程，仍缺乏因果证据。

## 方法关键点
- 在阿里巴巴淘宝平台开展随机现场实验，共 647 名客服人员、680,676 次服务对话。
- 处理组工人监督 AI 处理“AI-合格”对话（约 5.8%），并在 AI 失败时介入，同时仍自行处理“AI-不合格”对话；对照组全部由人工处理。
- 采用 worker-level 双重差分估计总效应、直接效应和溢出效应，并用倾向得分匹配构造反事实进行子样本分析。
- 根据升级类型（算法触发技术升级、算法触发情绪升级、人工主动升级、无升级）细分 AI 失败模式。
- 构建对话过程指标（响应延迟、人工对话轮次、消息数）和基于 LLM 的内容评估（信息寻求、方案提供、共情、主动性）衡量干预努力。

## 关键结果数字
- Agentic AI 部署使整体平均对话时长缩短 3.2%（p<0.001），但对重试率和整体评分无显著影响。
- AI-合格对话中，时长降低 16.8%，但顾客评分下降 0.412 分（p<0.001）；AI-不合格对话出现正向溢出，时长降低 1.8%，评分提升 0.091 分（p<0.01）。
- 人工干预有效性高度异质：技术升级时，评分与对照组持平，时长增加 19.1%；情绪升级时评分下降 0.928 分（p<0.001），重试率上升 6 个百分点（p<0.01），时长增加 40.8%。工人投入明显不足（消息数少、共享轮次比例低、主动性差）。
- 人工主动升级（早于算法）显著缓解负面效果：时长仅增 9.5%，评分降幅（0.524）小于情绪升级，重试率下降 3.2 个百分点。
- 整合角色（同一工人同时监督 AI 和人工处理）使处理 AI-不合格对话时注意转移更少，服务速度和质量均受益。
