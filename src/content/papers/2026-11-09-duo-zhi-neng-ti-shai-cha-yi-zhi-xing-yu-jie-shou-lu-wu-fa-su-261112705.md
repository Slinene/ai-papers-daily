---
title: 'Multi-Agent Screening: What Agreement and Acceptance Cannot Tell You'
title_zh: 多智能体筛查：一致性与接受率无法告诉你什么
authors:
- Benjamin Chang
- Dell Zhang
affiliations:
- University of Cambridge
- XSci
arxiv_id: '2611.12705'
url: https://arxiv.org/abs/2611.12705
pdf_url: https://arxiv.org/pdf/2611.12705
published: '2026-11-09'
collected: '2026-11-12'
category: Eval
direction: 多智能体筛查评估 · 召回率估计
tags:
- Multi-Agent Systems
- Recall Estimation
- Incomplete Judgments
- Agentic Retrieval
- LLM-as-a-Judge
one_liner: 证明多智能体筛查中一致性和接受率无法确定召回率，只有审计未通过项才能精确估计，且样本量与 agent 数无关
practical_value: '- 评估多 agent 过滤链路时，不要用 agent 间一致率（agreement）作为质量指标：一致只能说明偏差相似，可能同时漏掉相关内容。应改为审计未通过项来估计召回。

  - 在商品/搜索候选生成、广告审核等场景，若人工只标注通过项，接受率仅反映 precision，无法揭示漏召回。需定期抽样未通过项进行人工复核，构建 recall
  区间。

  - 估计召回所需的未通过项审计样本量不随 agent 数量增长，即使 agent 很多，审计预算也不必线性增加；这对控制多 agent 系统评估成本很有用。

  - 决定是否加第 k+1 个 agent 时，若现有 agent 可互换，可利用命中集合的重叠推导增量价值上限，避免边际收益递减后继续堆 agent。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：多智能体检索、电子发现和 AI 审稿等场景中，agent 先筛查项目，昂贵的人类评估者只判断 agent 通过的项目，形成不完整判断（incomplete judgments）。运营者关心：是否能信任 agent 一致性？漏了多少相关内容？是否值得再加 agent？如何分配审计预算？

方法关键点：论文在无限数据假设下，分析三类证据：agent 间一致性（agreement）、评估者接受率（acceptance）、不同 agent 命中重叠（overlap）。用集合论与概率工具推导这些证据能确定或不能确定什么。

关键结果：一致性仅表明 agent 相互一致，无论 agent 数量多少都不保证正确；接受率给出 precision，但 recall 只有下界；若 agent 命中不是负相关，根据各 agent 找到的相关项可给 recall 上界；若 agent 可互换，可计算下一个 agent 的增量上限；若不对 agent 做任何假设，只有随机审计未通过项才能精确估计 recall，所需审计样本量与 agent 数量无关。论文以 AI 论文评审为例演示这些界限。
