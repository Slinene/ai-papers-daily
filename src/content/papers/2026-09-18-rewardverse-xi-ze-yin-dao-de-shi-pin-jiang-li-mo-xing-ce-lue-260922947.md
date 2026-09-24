---
title: 'RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling'
title_zh: RewardVerse：细则引导的视频奖励模型策略优化
authors:
- Zhenchen Tang
- Yang Li
- Songlin Yang
- Bo Peng
- Xiaotong Zhao
- Shuai Li
- Haotian Fan
- Alan Zhao
- Jing Dong
affiliations:
- New Laboratory of Pattern Recognition, Institute of Automation, Chinese Academy
  of Sciences
- School of Artificial Intelligence, University of Chinese Academy of Sciences
- The Hong Kong University of Science and Technology
- Tencent
arxiv_id: '2609.22947'
url: https://arxiv.org/abs/2609.22947
pdf_url: https://arxiv.org/pdf/2609.22947
published: '2026-09-18'
collected: '2026-09-24'
category: Eval
direction: 视频生成奖励建模 · Rubric 引导优化
tags:
- Reward Model
- Rubric
- RLHF
- Video Generation
- Scalar Drift
- Policy Optimization
one_liner: 提出动态 rubric 中间表示与两阶段 RGPO 训练，缓解视频奖励模型标量漂移，点/对偶评估达 SOTA
practical_value: '- 若在搜索/推荐里用 LLM-as-judge 或 reward model 评估生成内容（广告文案、标题、推荐理由、短视频素材），不要把质量直接映射成单
  scalar；先生成针对 query/商品类目的动态 rubric，再基于 rubric 打分，可缓解不同 prompt/类目间的分数漂移，使 RL/排序信号更稳定。

  - RGPO 两阶段训练可迁移：先用一批人工/规则 seed rubrics warm up scorer 对齐人类评分，再联合微调 rubric generator
  生成 query-adaptive criteria，避免直接联合训练导致 rubric 崩坏或打分不稳定。

  - Self-evolving seed rubrics 类似于软知识蒸馏/增强：可让 rubric generator 在少标注下扩展评价准则；在电商类目多、标注贵场景可以用
  seed rubric + 自演化减少人工规则成本。

  - 该框架给奖励判断带来可解释中间表示，便于审核、错误归因和人工校准；上线 reward model 前可把它作为诊断 scalar drift 的工具。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：视频生成 RL 依赖稳定 reward model，但现有方法直接把复杂主观视频质量映射成单一 scalar，导致 scalar drift——同一质量在不同 prompt 下分数坍缩或漂移，奖励不可靠。

方法：RewardVerse 引入动态 rubric 作为 evaluation query 与 scorer 之间的中间表示：先根据 query 生成显式评价准则，再进行 rubric-guided scoring，为 scalar 提供语义锚点。RGPO 分两阶段训练：先用 self-evolving seed rubrics warm up scorer，再联合优化 rubric generator 与 scorer，使 rubric 生成 query-adaptive，并持续对齐人类评分。

结果：在 EvalVerse 16 维 benchmark 及外部数据集上，RewardVerse 缓解 scalar drift，在 pointwise 与 pairwise 评估均达 SOTA，并为视频生成 RL 提供更鲁棒、可解释的 reward 信号。
