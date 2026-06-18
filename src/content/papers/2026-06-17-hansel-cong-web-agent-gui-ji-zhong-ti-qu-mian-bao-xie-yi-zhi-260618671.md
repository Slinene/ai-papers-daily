---
title: 'HANSEL: Extracting Breadcrumbs from Web Agent Trajectories for Interactive
  Verification'
title_zh: HANSEL：从 Web Agent 轨迹中提取面包屑以支持交互式验证
authors:
- Yujin Zhang
- Daye Nam
affiliations:
- University of California, Irvine
arxiv_id: '2606.18671'
url: https://arxiv.org/abs/2606.18671
pdf_url: https://arxiv.org/pdf/2606.18671
published: '2026-06-17'
collected: '2026-06-18'
category: Agent
direction: Agent 可解释性与交互式验证
tags:
- Web Agents
- Verification
- Human-AI Interaction
- Explainability
- Trajectory Summarization
- Evidence Extraction
one_liner: 从 Web agent 多步操作轨迹中提取关键证据页面，以交互式视图呈现，将验证从被动阅读变为主动探查
practical_value: '- **Agent 验证界面设计**：在电商搜索或比价 agent 中，可将 agent 访问过的关键页面（如带有特定过滤、排序、搜索词的状态）以可交互形式呈现给运营或审核人员，而非展示全量日志，快速验证推荐结果是否正确。

  - **证据缺失显式标记**：当 agent 输出无法对应到任何已访问页面时，自动标记“无证据”状态，防止 agent 幻觉导致错误决策（如商品推荐理由不实），这类似推荐系统中对黑盒结果增加可追溯性。

  - **关键状态保留和重放**：借鉴其保留页面状态（过滤条件、查询词、滚动位置）的做法，在 agent 辅助的搜索推荐管道中，可记录并复现关键决策点的上下文，方便线下复盘和规则优化。

  - **轨迹压缩与证据聚焦**：将 agent 全量操作日志压缩 61.6% 但仍保持高 precision/recall，这一思路可用于生成式推荐 agent
  的行为总结，减少人工审核成本，同时定位关键推荐依据。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：AI Web agent 能完成复杂多步任务（如搜索商品、比价、下单），但其输出难以验证。现有可解释方法（全量轨迹、截图、LLM 摘要）将验证视为被动阅读，用户需在海量日志中自行寻找依据或盲信解释，效率低且易遗漏错误。需要一种交互式证据提取机制，让用户主动探查 agent 决策过程。

**方法关键点**：
- 系统输入：Web agent 的完整操作轨迹（含步骤、访问页面及状态）。
- 证据页面提取：基于轨迹内容（如 URL 变化、DOM 差异、任务相关性）识别对最终答案有贡献的页面，并提取其中高相关的片段和关键状态（过滤条件、搜索词、滚动位置等）。
- 交互式呈现：将提取的证据页面以可导航、可交互的视图展示，保留页面实时状态，并高亮 evidence snippet；当答案无法关联到任何页面时，显式标记 gap。

**关键结果**：
- 在 45 个任务上，证据页面识别的精确率 83.7%，召回率 88.8%，同时轨迹体积压缩 61.6%。
- 用户研究（14 人）中，HANSEL 显著降低验证耗时与感知负担，可用性、易验证性、错误识别率均显著优于标准 agent 界面。
- 将验证从被动审阅转变为交互式探查后，人对 agent 的监督效率大幅提升。
