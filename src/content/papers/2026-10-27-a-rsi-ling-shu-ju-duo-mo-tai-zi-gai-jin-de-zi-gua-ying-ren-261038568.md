---
title: 'A-RSI: Adaptive Task Refresh for Zero-Data Multimodal Self-Improvement'
title_zh: A-RSI：零数据多模态自改进的自适应任务刷新
authors:
- Yu Liu
- Youxing Li
- Yuedong Tan
- Zhiwei Yang
- Zihan Su
- Hanqi Feng
- Shaojie Zhang
- Libin Liao
- Zihao Wan
- Chenxu Wu
arxiv_id: '2610.38568'
url: https://arxiv.org/abs/2610.38568
pdf_url: https://arxiv.org/pdf/2610.38568
published: '2026-10-27'
collected: '2026-10-31'
category: Training
direction: 零数据多模态自改进训练
tags:
- Self-Improvement
- Adaptive Curriculum
- Multimodal
- Training Dynamics
- Zero-Data
- RLVR
one_liner: 用训练日志中的奖励方差与准确率动态刷新任务池，实现零外部数据的多模态递归自改进
practical_value: '- 在 RLVR/self-play 持续训练中，用训练日志中的 reward variance 和 accuracy 趋势作为任务池刷新信号，替代依赖验证集或线上
  AB，可降低离线指标过拟合风险，适合推荐/广告模型的长期自训练。

  - 任务生成与答案校验解耦：用可执行 program/schema 生成题目并单独审计答案，而不是 self-consistency；电商场景可基于商品 schema、用户行为规则生成可编程校验的合成任务，自动清洗噪声
  label。

  - 维护 model-authored program 库做零外部数据合成，可迁移到商品文案、query 推荐语料增强；用 property-based check
  自动验证 reward 与刷新规则，适合离线规模化生产训练数据。

  - 自适应刷新机制减少人工调参：监控窗口内学习信号下降（如 reward variance 降低或 accuracy 平台期）再触发新任务生成，能平衡训练成本与效果。'
score: 6
source: huggingface-daily
depth: abstract
---

递归自改进不仅要生成有用经验，还需判断当前经验何时失效。已有工作偏重“生成什么”，忽略“何时引入新任务”；同时常用 self-consistency/majority voting 构建目标，使监督依赖模型自身不确定预测。

A-RSI 将两点解耦：训练动态决定何时获取新经验，新任务答案保持独立可校验。具体地，它用静态 model-authored program 库生成多模态问题并由程序推导参考答案；定义任务生成契约，自动验证 reward 与刷新规则的关键性质，并单独审计答案。刷新策略只监控训练日志中的 reward 方差与准确率，不访问验证集或测试集；学习信号下降时刷新任务池。训练不依赖外部样本或人工标注。

在 11 个多模态 benchmark 主套件上，800 个新任务使平均分从 57.77 提升至 61.05。
