---
title: 'ReNIO: Reweighting Negative Trajectory Importance for LLM On-Policy Distillation'
title_zh: 重加权负轨迹重要性用于LLM同策略蒸馏
authors:
- Chen Lin
- Kedi Chen
- Wei Zhang
affiliations:
- East China Normal University
- Shanghai Innovation Institute
arxiv_id: '2606.23104'
url: https://arxiv.org/abs/2606.23104
pdf_url: https://arxiv.org/pdf/2606.23104
published: '2026-06-21'
collected: '2026-06-26'
category: Training
direction: LLM同策略蒸馏负轨迹重加权
tags:
- on-policy distillation
- negative trajectory
- LLM reasoning
- token-level reweighting
- student-teacher ratio
one_liner: 发现错误轨迹在蒸馏中优于正确轨迹，提出用学生-教师概率比加权负轨迹，无需最终答案即可提升推理蒸馏效果
practical_value: '- 在电商搜索推荐或Agent的LLM推理训练中，可借鉴“错误样本更有信息量”的发现，主动提升错误轨迹权重，避免模型退化到保守短答案

  - 利用学生-教师概率比作为错误倾向的隐式信号，无需人工标注或最终答案标签，适合在线策略环境下的自动样本加权

  - 方法仅依赖前缀概率，支持prefix训练模式，适合资源受限或需要快速迭代的线上蒸馏场景，无需等待完整轨迹

  - 对于需要自我反思的推荐解释或广告文案生成，可借助ReNIO保留探索性边界行为，防止过拟合安全但平庸的输出'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：标准同策略蒸馏(OPD)平等对待所有学生生成输出，但过滤实验显示仅用错误输出训练的模型反超仅用正确输出训练的模型。分析表明正确输出导致推理链缩短、反思减弱，而错误输出保留探索性行为。因此需自动识别并加权负轨迹，但直接依赖最终答案正确性需要完整rollout，成本高且破坏OPD的prefix训练优势。

**方法**：提出ReNIO（重加权负轨迹重要性）。核心是利用每一步的学生token概率与教师概率之比，定位导致错误的关键token，并聚合得到样本权重。该权重天然赋予可能负轨迹更高权重，无需观察最终答案对错。由于只用前缀条件概率，该方法保留OPD的prefix训练优势，避免完整rollout。

**结果**：在数学推理（GSM8K、MATH等）和代码生成基准上，ReNIO在OPD和同策自蒸馏(OPSD)中均取得显著提升，如Qwen3-1.7B相对提升8.90%，R1-Distill-Qwen-7B相对提升10.00%。
