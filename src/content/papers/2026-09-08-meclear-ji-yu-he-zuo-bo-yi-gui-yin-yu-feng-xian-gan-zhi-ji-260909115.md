---
title: 'MeClear: Cooperative Game-Theoretic Attribution and Risk-Aware Memory Clearance
  for Long-Horizon LLM Agents'
title_zh: MeClear：基于合作博弈归因与风险感知记忆清除的长程 LLM 智能体框架
authors:
- Boyu Yang
- Jiazheng Sun
- Zilong Lu
- Zhi Qiu
- Xin Peng
- Jun Zheng
affiliations:
- Fudan University
- Beijing Institute of Technology
arxiv_id: '2609.09115'
url: https://arxiv.org/abs/2609.09115
pdf_url: https://arxiv.org/pdf/2609.09115
published: '2026-09-08'
collected: '2026-09-09'
category: Agent
direction: LLM Agent 长期记忆清理与归因
tags:
- LLM Agents
- Memory Management
- Shapley Attribution
- Cooperative Game Theory
- Long-Horizon
one_liner: 用合作 Shapley 归因识别负效用记忆并做最小化清除，任务恢复率 82.3%，比 LOO 高 25.5 个百分点
practical_value: '- 在电商/Agent 长期用户记忆（偏好、历史行为）中，不要只按 embedding 相似度检索；可以对候选记忆做留一法或 Shapley
  效用归因，识别“语义相关但实际降低决策质量”的记忆后再过滤。

  - 对于多证据交互产生的冲突或冗余，单条删除往往不敏感，可借鉴采样 Shapley 分摊效用，定位需要同时抑制的记忆组合；工程上适合离线/近线计算，避免在线高成本。

  - 采用“暂态清除”而非永久删除：查询级最小清除 + 清除后上下文验证任务恢复，避免污染持久记忆库，便于线上 A/B、审计和回滚。

  - 可抽象成 memory gate/scrubber 模块：在 RAG/Agent memory 召回后、拼入上下文前加一层 risk-aware memory
  clearance，保持召回 recall，同时提升下游稳定性和任务完成率。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：长程 LLM Agent 依赖外部记忆保存用户偏好和任务知识，但传统检索只优化语义相关性，容易把过期、误导或冲突的证据放进上下文，损害下游任务效用。

方法关键点：MeClear 采用任务条件的记忆清除框架。先用 Leave One Out 筛选，再用采样合作 Shapley 归因把下游效用分摊到相互作用的证据上，解决单条删除无法发现的冗余冲突 masking。根据归因排名，执行 query-scoped 最小清除策略，通过嵌套过滤在清除后的上下文上验证任务恢复情况，且不永久修改持久记忆库。

关键结果：在 10 个长对话记忆池上，MeClear 达到 85.9% 的目标召回率和 82.3% 的整体任务恢复率，比 Leave One Out 基线提升 25.5 个百分点。
