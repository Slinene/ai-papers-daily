---
title: 'Blind Variation, Selective Retention: Improving Creative Idea Generation in
  AI Scientists'
title_zh: 盲变异与选择性保留：提升AI科学家创意想法生成
authors:
- Guowei Xu
- Jiaru Zou
- Mete Erdogan
- Haotian Ye
- Pan Lu
- James Zou
affiliations:
- Stanford University
arxiv_id: '2611.12184'
url: https://arxiv.org/abs/2611.12184
pdf_url: https://arxiv.org/pdf/2611.12184
published: '2026-11-08'
collected: '2026-11-12'
category: Agent
direction: Agent 创意生成与选择性验证
tags:
- BVSR
- AI Scientist
- LLM
- Idea Generation
- Selective Retention
- Creativity
one_liner: 受认知框架BVSR启发，生成阶段限制任务信息提升创意，选择阶段利用历史验证结果筛选候选
practical_value: '- 在生成广告文案、商品标题、搜索query等创意任务时，可以故意只给模型稀疏、抽象的任务描述（盲变异），避免提供具体数据、指标和基线导致生成内容锚定常见套路。

  - 构建两阶段LLM工作流：第一阶段用有限上下文做多样化生成（exploration），第二阶段用之前候选的线上/实验反馈训练筛选器或prompt few-shot，低成本淘汰低效候选（exploitation），类似bandit思想。

  - 对于自动化A/B测试创意生成，可以将历史成功/失败案例作为选择性保留的输入，让模型先预测候选成功率，只对高潜候选进行昂贵评估。

  - 在Agent做自动化实验或生成推荐策略时，把exploration和exploitation显式分离：生成提案时少给任务细节以增加diversity，验证时充分利用已积累的任务经验提高precision。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：AI科学家在创意生成阶段通常被提供尽量多的任务信息，导致模型锚定在熟悉方法上，提案新颖性和非显而易见性不足。灵感来自认知科学中的盲变异与选择性保留（BVSR）框架。

**方法关键点**：
- 将发现过程分为两个阶段：盲目变异（Blind Variation）和选择性保留（Selective Retention）。
- 生成阶段：故意只给模型有限、抽象的任务描述（如只给目标名称，不给具体数据/指标/基线），促使模型自由探索多样性提案。
- 选择阶段：利用同一任务上先前已验证的提案及其结果，让模型学习成功/失败模式，从新提案中筛选高潜候选，减少昂贵实验评估成本。
- 可插入现有AI科学家工作流，无需改变底层模型。

**关键结果数字**：
- 在5个proposer模型、12个科学任务上评估。
- 限制任务信息显著提升提案原创性和非显而易见性，高创意高实用提案占比超过现有SOTA prompting baseline。
- 选择性保留能丢弃一半候选，同时保留大部分顶尖表现提案。
- 集成到AI科学家工作流后，在基因表达分析、药物反应预测、异常检测、缩放定律发现和脑活动预测任务上取得更强发现。
