---
title: Delegating or Doing? Understanding User Behavior in Hybrid Human-Agent Interfaces
title_zh: 委托还是亲为？理解混合人-代理界面中的用户行为
authors:
- Gavin Raine Dizon
- Tyrone Justin Sta Maria
- Jordan Aiko Deja
- Yasuyuki Sumi
affiliations:
- Future University, Hakodate
- De La Salle University
arxiv_id: '2608.19551'
url: https://arxiv.org/abs/2608.19551
pdf_url: https://arxiv.org/pdf/2608.19551
published: '2026-08-20'
collected: '2026-08-23'
category: Agent
direction: 人机混合界面委托行为研究
tags:
- LLM Agent
- Human-Agent Interaction
- Delegation
- User Study
- MCP
- Interaction Effort
one_liner: 研究发现LLM代理混合界面主要降低交互努力而非提升速度，委派行为个体差异远大于任务差异
practical_value: '- 在电商后台、内容管理或广告投放工具等混合GUI+Agent场景中，提供“委托+直接操作”模式可显著降低点击、翻页、滚动等物理交互成本，但不应指望它缩短任务完成时间；可将降低操作负担作为体验优化指标，而非单纯追求效率。

  - 委派行为个体差异大（ICC=.50），远超任务类型差异，说明用户对Agent信任/偏好分化明显。在Agent产品设计中，可支持个性化默认模式（AI-First
  vs 手动优先），或基于用户历史委派行为动态调整界面默认入口与交互引导。

  - 未发现CRUD操作类型（如高风险删除）与委派行为的相关性，用户不会系统性回避高风险委派。因此在设计商品下架、删除等高危操作的Agent能力时，应把风险控制内置到执行流程（如确认、回滚、权限校验），而不是假设用户会因风险而避免使用Agent。

  - 通过MCP连接LLM agent，可快速为已有系统增加自然语言操作能力，复用现有API。对于电商/推荐工程团队，这是低成本为内部工具或运营后台增加Agent交互的路径。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM代理越来越多嵌入应用，用户既可手动操作也可对话委派，但混合模式下用户如何平衡两种模态仍缺乏实证理解。

**方法**：构建基于Web的内容管理系统，通过Model Context Protocol (MCP)连接LLM agent，支持GUI操作、对话委派或两者混合。进行between-subjects实验N=73，比较三种交互模式：Traditional-Only、AI-First、Hybrid；覆盖16个CRUD场景，记录任务完成时间、交互日志和委派行为。

**结果**：AI辅助显著减少点击、页面导航和滚动，表明交互努力降低；但任务完成时间在组间无显著差异。CRUD操作类型与委派行为无显著关系，用户没有系统性回避高风险操作。委派行为在参与者间的差异远大于任务间，个体差异解释了约一半的助手使用方差（ICC=.50）。

**结论**：混合人机界面主要收益是减少交互努力而非提升速度，委派行为更多反映用户个体特质而非任务需求。
