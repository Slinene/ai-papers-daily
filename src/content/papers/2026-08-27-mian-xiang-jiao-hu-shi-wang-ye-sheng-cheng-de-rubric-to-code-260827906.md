---
title: Rubric-to-Code Credit Assignment for Reinforcement Learning
title_zh: 面向交互式网页生成的 Rubric-to-Code 奖励归因强化学习
authors:
- Rui Jin
- Jikai Chen
- Yihan Chen
- Hao Zhou
- Demin Zhu
- Kaichen Yang
- Dong Wang
- Chenyi Zhuang
affiliations:
- Inclusion AI, Ant Group
- Zhongnan University
arxiv_id: '2608.27906'
url: https://arxiv.org/abs/2608.27906
pdf_url: https://arxiv.org/pdf/2608.27906
published: '2026-08-27'
collected: '2026-08-31'
category: Training
direction: 强化学习细粒度信用分配
tags:
- RCCA
- GRPO
- credit assignment
- web app generation
- reinforcement learning
- code generation
one_liner: 将 rubric 级功能反馈转化为局部代码优化信号，替代 GRPO 的序列级统一 advantage，显著提升交互式网页生成成绩
practical_value: '- 对电商详情页、活动页、推荐卡片等多组件生成任务，可用 rubric 并让评估器输出「哪个 span/组件负责该问题」的文本归因，再把归因对齐到
  token/组件级 advantage，替代 GRPO 的全局 uniform advantage，提升 RL 训练信号粒度。

  - 工程上构建分层 reward：先分离格式、语法、运行时、功能目标，避免不可执行样本污染功能学习；在广告创意/推荐文案生成中可拆成合规、语法、核心卖点、转化目标等层级。

  - 若已有描述性评估（如 rubric 写明某功能缺失原因），不要只取总分；可把解析出的 DOM 片段、状态更新、事件处理等代码块与 rubric 关联，做细粒度
  credit assignment，提高样本效率。

  - 该方法依赖可执行/可静态分析的代码结构；在推荐/广告生成文案或 item 序列时，可替换为标题、卖点、CTA、图片选择等结构化组件，并做组件级归因。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：交互式网页应用生成需要满足多个用户侧功能要求，这些要求通常对应局部代码区域（事件处理、状态更新、DOM 片段、CSS 选择器）。标准 GRPO 把所有结构化结果压缩成单一序列级奖励，并将 advantage 均匀施加到所有 token，削弱了信用分配。

**方法关键点**：RCCA 围绕显式 functional rubrics 构建训练任务；使用 hierarchical reward 分离格式、源码、运行时和功能失败；把 evaluator 生成的 textual attributions 对齐到负责的代码 span 和生成 token，从而将 rubric 级反馈转化为局部优化信号。

**关键结果**：Ling-RCCA-Flash 在 MiniAppBench 上得 41.25，较 Ling-3.0-Flash 提升 32.20 分，略超 Claude Opus 4.5；在 ArtifactsBench 上得 76.19，较 SFT 模型提升 4.48 分，并超过 GPT-5 3.64 分，成为官方 leaderboard 设置下的新高分。
