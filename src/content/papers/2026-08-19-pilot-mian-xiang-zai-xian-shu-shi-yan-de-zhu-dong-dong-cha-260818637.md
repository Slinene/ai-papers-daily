---
title: PILOT Technical Report
title_zh: PILOT：面向在线树实验的主动洞察学习智能体技术报告
authors:
- Jiuning Lin
- Ruiquan Lan
- Xiaodong Zhu
- Bin Zhang
- Chengyu Lai
- Chuxin Chen
- Dimin Wang
- Hongtao Cheng
- Jialin Zhu
- Lingqing Zhang
affiliations:
- Taobao
arxiv_id: '2608.18637'
url: https://arxiv.org/abs/2608.18637
pdf_url: https://arxiv.org/pdf/2608.18637
published: '2026-08-19'
collected: '2026-08-20'
category: MultiAgent
direction: Agent 多角色实验优化 · 决策树个性化
tags:
- LLM Agent
- Controlled Experiment
- Recommender Optimization
- Decision Tree
- Memory
- A-B Testing
one_liner: PILOT 用三角色 LLM 智能体将推荐实验从被动调参升级为主动假设检验与人群级决策树个性化，搜索效率提升 40pp
practical_value: '- **给实验平台加“守卫层”**：在真实推荐系统上做 Agent 自主实验，先实现确定性 Action Enumerator
  + Manager Guard + State Committer；LLM 只从合法候选里选，状态写入和统计判断都不经过 LLM，能显著降低越权和误用风险。

  - **用 PolicyTree 做人群级策略个性化**：把策略打成 bundle，用 split/prune/hashSplit/updateStrategy
  作为原子动作；先做特征质量预筛和 hashSplit 小流量探测，再进入全桶 A/B 验证。适合猜你喜欢、会员分层、广告人群包等配置迭代。

  - **记忆分成“策略证据”和“方法论”两层**：策略效果只记录成 bundle 对比，并标注因果/诊断证据角色；单次实验只产生 draft，跨任务一致才升 supported/approved。可避免把一次
  lucky run 当成全局经验，减少 LLM 幻觉决策。

  - **强制“假设先行”的 planner proposal**：每个候选必须带可证伪假设、拒绝条件、证据引用和结果后的下一步计划，否则不分配流量；这比事后总结轨迹更可控，适合把实验参数搜索交给
  LLM 时的工程约束。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：现有 agentic 推荐优化大多是被动响应指标变化，无法主动设计受控实验、在用户分群层面做个性化，也不能把实验方法论沉淀复用。PILOT 面向 Taobao 首页猜你喜欢场景，用三角色 LLM 智能体在受约束控制循环里做主动实验管理。

**方法关键点**：
- **受限控制循环**：确定性服务生成合法命令包络（legal-command envelope），LLM 只能从中选择；State Committer 是唯一状态写入方，Statistics Engine 产生不可变决策证书。LLM 拥有判断权，但不拥有执行和统计权限。
- **Experiment Manager**：负责全生命周期 task intake → playbook → 观察治理 → 异常恢复 → 扩容 → 复盘；使用 look/wave/epoch/search iteration 四层时间概念；证书为 promote/reject/continue。
- **Search Planner**：PolicyTree 把用户映射到策略 bundle，原子动作只有 split/prune/hashExpand/collapse/updateStrategy；经过特征质量预筛、候选边界生成、历史去优先级；可选 hashSplit 小流量探测；每个 proposal 必须携带可证伪假设、拒绝条件、证据引用和下一步计划。
- **Memory Curator**：维护 Strategy Evidence 与 Methodology Experience 两个存储，记录 bundle 对比效果与方法论来源；跨任务 fork-merge 隔离，confidential 置信度按 draft→supported→approved 演进。

**关键结果**：5 个实验桶在线 A/B，对比 ROAM。PILOT 的 IPV +1.40%（ROAM +1.00%）、Core IPV +1.60%（+0.90%）、交易数 +0.96%（+0.60%）、交易额 +1.50%（+1.13%）；搜索效率从 53.3% 提升到 93.3%（+40pp），全程无人工干预。

最值得记住：让 LLM 只负责“测什么、为什么”，统计结论、状态推进和权限边界全部交给确定性服务，这是把实验智能体安全推上生产的关键。
