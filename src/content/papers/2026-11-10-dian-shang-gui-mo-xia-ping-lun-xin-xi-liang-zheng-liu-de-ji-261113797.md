---
title: Auditing LLM Pseudo-Label Distillation for Review Informativeness at E-Commerce
  Scale
title_zh: 电商规模下评论信息量蒸馏的审计：LLM伪标签、时间泛化与上下文效应
authors:
- M. Emin Dogan
- Cansu Er
- Aysenur Kulunk
- M. Furkan Eseoglu
- H. Bahadir Sahin
affiliations:
- Analytics Department, Hepsiburada
arxiv_id: '2611.13797'
url: https://arxiv.org/abs/2611.13797
pdf_url: https://arxiv.org/pdf/2611.13797
published: '2026-11-10'
collected: '2026-11-12'
category: Eval
direction: LLM 伪标签蒸馏审计 · 时间泛化评估
tags:
- LLM distillation
- pseudo-label
- review informativeness
- temporal evaluation
- CORN loss
- teacher fidelity
one_liner: 对534万条土耳其评论做LLM伪标签蒸馏审计，发现教师保真度不等于编辑对齐，上下文增益随评估人群变化
practical_value: '- 用 LLM 伪标签蒸馏轻量编码器做评论信息量评分，可直接迁移到电商评论区排序、垃圾评论过滤、商品详情页内容理解；单 L4 学生管道
  50.2 倍加速，适合大规模离线批量打分。

  - 严格新 SKU 时间切分是关键：训练/验证按时间分割且实体不重叠，能暴露时间偏移和实体泛化问题，推荐系统离线评估应引入同样严格的数据隔离，避免高估模型效果。

  - 教师保真度（student-teacher agreement）不能替代编辑对齐（human agreement），务必单独做人工盲审；尤其上下文前缀（如类目）的收益可能只在特定评估人群上成立，需分场景验证后再上线。

  - 序数回归损失 CORN 比交叉熵对上下文差异更敏感，若任务标签是离散等级（如信息量分级），建议用 CORN 训练以便捕获细微的分布偏移。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：电商评论的信息量对购买决策重要，人工标注成本高，用 LLM 伪标签蒸馏小模型可规模化，但学生的教师一致性与编辑一致性可能并不等价。

**方法关键点**：在 534 万条土耳其市场评论上，用 Gemini 3.1 Flash-Lite 生成硬标签，蒸馏到紧凑编码器。评估分两条线：一是严格新 SKU 时间切分测试教师保真度；二是由一位公司注释员在 16000 条时间序列子集上做教师标签盲审，衡量编辑一致性。同时对比是否使用 H3 类目前缀作为上下文，以及 CORN 与交叉熵损失的差异。

**关键结果**：完整新 SKU 测试上，H3 前缀略微提升教师保真度；但在时间审计子集上，H3 前缀反而降低与 Gemini 和注释员的一致性，且 CORN 的配对差异比交叉熵更清晰。单 L4 学生管道处理速度比教师管道快 50.2 倍。
