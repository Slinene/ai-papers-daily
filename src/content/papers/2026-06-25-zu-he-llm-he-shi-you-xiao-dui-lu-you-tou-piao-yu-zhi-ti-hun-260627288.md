---
title: When Does Combining Language Models Help? A Co-Failure Ceiling on Routing,
  Voting, and Mixture-of-Agents Across 67 Frontier Models
title_zh: 组合 LLM 何时有效？对路由、投票与智体混合的共同失败天花板分析
authors:
- Josef Chen
affiliations:
- KAIKAKU
arxiv_id: '2606.27288'
url: https://arxiv.org/abs/2606.27288
pdf_url: https://arxiv.org/pdf/2606.27288
published: '2026-06-25'
collected: '2026-06-26'
category: Eval
direction: 多模型 LLM 集成评估 · 共同失败率上限
tags:
- co-failure
- β-ceiling
- multi-LLM ensemble
- routing
- voting
- mixture-of-agents
one_liner: 多模型 LLM 增益上限由所有模型全错的 β 率决定，而非平均错误相关性 ρ，67 模型实验发现 β 被低估约 2.5 倍
practical_value: '- 在推荐系统的多模型集成（多召回/多排序融合）前，估计共同失败率 β，直接判断增益天花板，避免在 β 较高的场景中投入无效集成。

  - 选择集成模型时，主动降低 β 而非只看平均错误相关性 ρ；优先选择低 ρ 的异质模型组合，远离高 ρ 自集成（如 Self-MoA），以提升集成上限。

  - 若无法实现精确的查询级路由（如实时预测每条 query 的最佳模型），应谨慎使用投票或级联，单最佳模型可能更优；可利用 Clopper–Pearson 原理用少量带标注样本评估集成潜力。

  - 评估多路召回或 LLM 投票策略时，直接统计所有通道同时失效的样本比例（即 β），针对这些“硬样本”做定向优化，如增加多样性信号或引入外部校验。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多模型 LLM 系统（路由、投票、MoA 等）常用来突破单模型精度，但缺乏有效的增益上限诊断。常用指标平均成对错误相关性 ρ 不能刻画所有模型同时出错的概率 β，而 β 才是真正的天花板。

**方法关键点**：定义 β 为所有模型在同一查询上全错的概率，证明任何输出为单一模型答案的策略（路由、投票、级联）准确率都不可能超过 1−β。利用 Clopper–Pearson 区间为 β 提供有限样本下的增益证书。在 67 个前沿模型上实测，用四元相关校准的单因子高斯 copula 预测全错尾部，发现模型池的 β 被系统性低估——在开放式数学上 β=0.052，而 copula 预测仅 0.023，低估约 2.5 倍（90% CI 1.7–3.4）；代码任务 β=0.079；GPQA 自由回答形式 β=0.127。

**关键结果**：在可检查任务中，若无强查询级路由信号，组合模型很少超越单最佳模型；收益来自模型在不同问题上犯错，而非堆加模型数量；异质低 ρ 集成明显优于高 ρ 自集成。
