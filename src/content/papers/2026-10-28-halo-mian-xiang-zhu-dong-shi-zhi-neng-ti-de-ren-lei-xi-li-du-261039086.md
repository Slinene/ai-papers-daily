---
title: 'HALO: Human-Grounded Granular Evaluation of Proactive Agents'
title_zh: HALO：面向主动式智能体的人类细粒度评估
authors:
- Wenqi Pei
- Xinyu Wang
- Jinrui Liu
- Cynthia Zhuge
- Jie Sheng
- Zihan Wang
- Tenghao Huang
- Muhao Chen
affiliations:
- University of California, Davis
- 2077AI
- University of Southern California
arxiv_id: '2610.39086'
url: https://arxiv.org/abs/2610.39086
pdf_url: https://arxiv.org/pdf/2610.39086
published: '2026-10-28'
collected: '2026-11-02'
category: Eval
direction: 主动式Agent评估与人类诊断
tags:
- Proactive Agents
- Human Evaluation
- Benchmark
- Over-proactivity
- Timing-Intensity
- Reasoning Effort
one_liner: 提出HALO-Arena与HALO-8K，以人类细粒度诊断评估主动Agent是否、何时、多大程度干预，发现过度主动占拒绝主因
practical_value: '- 做主动推荐/push/智能客服时，别只看点击或二分类接受率；可仿照 HALO 把拒绝原因细拆为 timing（过早/过晚）和
  intensity（过度/不足），重点监控 Premature+Excessive 的比例，因为该研究发现 61.20% 拒绝来自过度主动。

  - 在 Agent 介入前，先强制做证据检索：区分 structured DB 与 unstructured docs，记录 retrieval rounds；这能帮助判断是否已有足够信息，避免仅凭当前上下文过早干预。

  - 设计决策时显式建模 action level / scope，而不是单一动作；允许系统选择“保持沉默/仅提醒/部分代劳/完全代劳”，配合人类诊断校准阈值。

  - 可借鉴 4 类主动需求分类（Dependency, Blockage, Risk, Opportunity）为推荐/营销触发场景做需求建模，例如缺货补货提醒（Blockage）、价格风险（Risk）、关联购买（Opportunity）。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：现有主动Agent评估多用自动分数或二分类判定，缺少对证据使用和干预质量的细粒度人类诊断。
方法：提出 HALO-Arena，覆盖 Dependency、Blockage、Risk、Opportunity 四类主动需求，10 个日常领域、50 个个人环境；场景要求模型先从 structured databases 或 unstructured documents 检索证据，再判断是否干预及干预范围。构建 HALO-8K：10 个模型 × 400 场景的 8,000 条回复，由 20 位专家标注 action level、acceptability 和人类诊断；拒绝回复细查 timing、intensity 等问题，并记录 reasoning tokens 与 retrieval rounds 衡量 effort。
关键结果：最佳闭源模型 acceptability 72.88%，最佳开源 56.63%；过度主动是主要失败模式，Premature timing 或 Excessive intensity 占拒绝样本 61.20%。进一步分析围绕干预与克制平衡、证据获取、timing/intensity 校准。
