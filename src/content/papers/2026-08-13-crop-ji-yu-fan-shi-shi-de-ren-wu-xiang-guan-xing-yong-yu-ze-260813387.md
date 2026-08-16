---
title: 'CROP: Task Relevance via Counterfactuals for Selective On-Policy Distillation'
title_zh: CROP：基于反事实的任务相关性用于选择性在线蒸馏
authors:
- Enhan Li
- Junhao He
- Hongyang Du
affiliations:
- The University of Hong Kong
arxiv_id: '2608.13387'
url: https://arxiv.org/abs/2608.13387
pdf_url: https://arxiv.org/pdf/2608.13387
published: '2026-08-13'
collected: '2026-08-16'
category: Training
direction: LLM 在线蒸馏中的 token 级样本选择
tags:
- On-policy distillation
- Counterfactual
- Task relevance
- Selective distillation
- Token-level supervision
one_liner: 提出 CROP，通过反事实敏感性边际度量 token 级任务相关性，优化选择性在线蒸馏的监督分配
practical_value: '- 在业务 LLM 蒸馏或微调中，可借鉴 CROP 对 token 级监督进行加权：仅重点关注与当前任务语义相关的 token，降低无关
  token 的学习干扰。

  - 利用构造「原始-释义-反事实」三元组来校准 token 敏感度，可用于评估指令中哪些部分真正驱动任务输出，辅助 prompt 精简或数据筛选。

  - 方法不依赖外部标注，完全基于模型内部行为，适合线上持续学习或无法大量标注的推荐/Agent 场景。

  - 可迁移到生成式推荐，例如对用户 query 或 item 描述生成时，判断哪些 token 影响最终推荐结果，提升蒸馏数据质量。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：在线蒸馏（OPD）对响应 token 平均分配监督，忽略 token 间实际训练价值差异；现有选择性方法侧重优化需求（如不确定性、师生分歧），缺少对任务相关性的直接刻画。

方法关键点：CROP 通过反事实敏感性边际将任务相关性操作化。对每个源 prompt，构建经过验证的「原始-释义-反事实」三元组，固定学生 rollout，测量每个响应位置对任务相关条件变化的敏感性，并用对语义保留改写的敏感性进行校准。具体地，计算 token 在反事实变换下输出的变化，减去在释义变换下的变化，得到 margin 作为该 token 的任务相关性得分，据此选择性分配蒸馏监督。

关键结果：在两个师生设置中，CROP 相较于最强非 CROP 选择器，综合性能分别提升 1.92 和 2.96 分；匹配选择对照显示 CROP 选中的监督位置优于随机或最低相关性选择；消融验证了反事实敏感性和释义校准两个组件的价值。
