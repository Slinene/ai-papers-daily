---
title: When Should AI Agents Ask? Clarification Requests Under Limited Human Attention
title_zh: 何时 AI 代理应该提问：有限人类注意力下的澄清请求
authors:
- Hanzhao Wang
- Shengjie Liu
- Zhengchao Wang
affiliations:
- The University of Sydney Business School, The University of Sydney
- Amazon
arxiv_id: '2610.41129'
url: https://arxiv.org/abs/2610.41129
pdf_url: https://arxiv.org/pdf/2610.41129
published: '2026-10-30'
collected: '2026-11-02'
category: MultiAgent
direction: 多智能体共享人类注意力时的提问协调
tags:
- AI agents
- human-AI collaboration
- clarification requests
- dynamic programming
- shared attention
- approximate DP
one_liner: 提出 Pairwise Coordination Policy 协调多智能体共享有限人类注意力时的提问时机与排序，成本接近最优
practical_value: '- 在多个 AI agent 并行处理推荐/广告/生成任务且需要人工确认偏好、约束或补全信息时，不要逐个 agent 独立决定是否提问；PCP
  用成对任务延迟矩阵估计全局等待成本，能显著降低人工等待与任务闲置带来的总成本。

  - 工程上可以先离线计算单任务和双任务的最优策略与成本表，运行时仅根据当前待解决需求做组合近似，避免动态规划维度爆炸；适合作为 agent 调度与澄清模块嵌入现有
  LLM agent 框架。

  - 业务中可复用“先做不依赖缺失信息的部分，再决定 search 或 ask”的框架：如果 agent 有其他可做工作，提前提问可能反而降低总延迟；若可通过查询历史记录/知识库低成本解决，则优先
  search，否则 ask。

  - 人类注意力是瓶颈时，不要用 agent-by-agent 排序，而应基于所有等待问题动态调整优先级；PCP 的近似保证和合成基准上的 0.07% 最优差距说明这种成对近似已经足够用于实际调度。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：多个 AI agent 同时执行任务，共享一个注意力有限的人类监督者。每个 agent 可能缺少偏好、约束或规格说明，需要选择自主搜索、向人类提问，或先做不依赖缺失信息的部分。如何跨 agent 协调这些决策，降低整体延迟成本，是尚未系统研究的问题。

**方法关键点**：将问题建模为动态规划，证明单独按每个 agent 自身不确定性决定是否提问不是最优；等待问题的排序必须全局考虑。提出 Pairwise Coordination Policy (PCP)，利用精确的单任务和双任务问题，估计任务对在共享人类时的相互延迟。理论保证：当最多两个需求未解决时 PCP 精确最优；当所有未解决需求必须由人类解决时，成本最多为最优的 2 倍。

**关键结果**：在 864 个合成算例上，PCP 与最优成本的平均差距为 0.07%，相比三种常用提问规则平均降低成本 18–31%。在 LLM 案例研究中，agent 正确完成所有任务，PCP 在所有测试设置下取得最低平均成本。
