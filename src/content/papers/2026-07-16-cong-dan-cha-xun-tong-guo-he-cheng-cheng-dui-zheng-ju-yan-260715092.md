---
title: 'Rubrics on Trial: Evolving Rubrics from a Single Query via Synthetic Pairwise
  Evidence'
title_zh: 从单查询通过合成成对证据演化评分标准
authors:
- Haocheng Yang
- Licheng Pan
- Xiaoxi Li
- Zhichao Chen
- Zhiheng Zhang
- Yuan Lu
- Haoxuan Li
- Hao Wang
affiliations:
- National University of Singapore
- Xiaohongshu Inc.
- Zhejiang University
- Peking University
- Shanghai University of Finance and Economics
arxiv_id: '2607.15092'
url: https://arxiv.org/abs/2607.15092
pdf_url: https://arxiv.org/pdf/2607.15092
published: '2026-07-16'
collected: '2026-07-18'
category: Eval
direction: LLM评估 · 查询到评分表自动演化
tags:
- Rubric Evolution
- Synthetic Data
- Pairwise Preference
- LLM Evaluation
- Query-Only
- No Annotation
one_liner: 提出仅依赖查询通过合成成对证据自动演化出有效检验标准的框架，无需外部标注或训练。
practical_value: '- 可复用其筛选机制（非判别性、过度具体、仅风格项）自动构建推荐/Agent输出评估标准，减少人工设计成本。

  - 合成成对证据的方法可迁移至电商搜索建议、商品描述生成等场景的评估，通过LLM自我对抗生成偏好对来验证评分维度的有效性。

  - 无需人工标注的特性适合快速迭代的推荐系统评估，用于监控在线生成的回答质量或作为Reward Model的轻量替代。

  - 演化式构建评分表的思路可启发生成式推荐的自动元评估，例如逐步添加描述商品推荐理由的检查项。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：构建查询特定评分标准（rubric）对LLM训练与评估至关重要，但现有方法依赖人工评分、偏好数据或采样响应。直接查询生成评分标准可能产生无用项：无法区分回答质量、奖励非必要风格或惩罚有效替代策略。

**方法**：提出Rubrics on Trial框架，仅凭单个查询，从空集开始自动演化评分标准集，无需外部标注或模型训练。核心步骤：(1) 生成候选评分项；(2) 通过LLM合成评分条件响应对（一个满足条件、另一个有意违反），构建成对偏好证据；(3) 利用合成证据验证候选项的有效性——筛除非判别性、过度具体和仅风格项；(4) 保留通过验证的评分项，迭代扩展评分集。

**结果**：在MixEval、RewardBench等五个偏好基准的七个评估集上，该方法平均准确率最高，并在六个子集上领先，证明无需任何人工信号即可演化出可靠的评分标准。
