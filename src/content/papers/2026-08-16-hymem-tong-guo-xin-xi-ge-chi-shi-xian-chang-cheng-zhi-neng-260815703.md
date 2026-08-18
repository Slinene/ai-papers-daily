---
title: 'HyMem: Hierarchical Context Management for Long-Horizon Agents via Information
  Isolation'
title_zh: HyMem：通过信息隔离实现长程智能体的分层上下文管理
authors:
- XinQi Wang
- Jinwei Xiao
- Sijia Cui
- Hongming Zhang
- Yanna Wang
- Qingyang Zhang
- Bo Xu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Nanjing Artificial Intelligence Research of IA
arxiv_id: '2608.15703'
url: https://arxiv.org/abs/2608.15703
pdf_url: https://arxiv.org/pdf/2608.15703
published: '2026-08-16'
collected: '2026-08-18'
category: Agent
direction: Agent 长程上下文分层隔离
tags:
- Context Management
- Long-Horizon Agents
- Hierarchical Memory
- Information Isolation
- LLM Agents
- Training-free
one_liner: 提出训练无关的分层上下文隔离框架 HyMem，将规划、执行、子任务推理与结构化记忆分离，显著提升长程 agent 的 Pass@1
practical_value: '- 把 planner 与 executor 上下文彻底拆开，执行结果只回传 schema 化 `RESULTS/RETURN`，原始工具输出、重试和中间推理留在临时
  context；适合电商导购 Agent 在多轮搜索与商品比较时，防止详情页噪声淹没主任务。

  - 复杂子任务用独立的 isolated reasoning session 处理，返回结论+证据+confidence，主 planner 不累积推理过程；可直接用于优惠计算、多条件筛选、价格/评论冲突验证等需要多跳分析的导购场景。

  - 结构化记忆分三类：episode/working/tool memory，fold 时只保留里程碑、当前目标和可复用工具经验；可用于长会话用户偏好记忆与跨会话召回。

  - 确定性 fold triggers（planner ctx 利用率>0.99、连续失败>=3、tool calls>=10 等）可照搬，训练无关、即插即用；适合在现有
  ReAct/搜索推荐 Agent 上快速压测上下文稀释问题。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
LLM agent 在长程任务中因上下文稀释（context dilution）性能下降。ReAct 等扁平上下文把高层规划信号与密集执行轨迹混在一起，关键信息密度随交互步下降。已有压缩/检索方法通常在信息混合后处理，容易丢失推理链或时间逻辑，治标不治本。

**方法关键点**
- typed context isolation：将 planner/executor/isolated reasoning/memory 分在不同上下文空间，只允许 schema 约束消息跨边界。
- planner 只保留任务、结构化记忆和 typed returns；executor 使用全新上下文执行有界工具循环，通过 relevance-conditioned distillation 过滤原始输出，仅返回 `<RESULTS>`。
- isolated reasoning 处理多跳子任务，内部推理不进入主上下文，返回 `<RETURN>`（结论、证据、来源、置信度、假设）。
- 结构化记忆：episode/working/tool 三类，fold 时联合重写，并按需不对称注入。
- fold 触发条件：context 利用率>0.99、executor 调用>=5、连续失败>=3、planner turns>=8、tool calls>=10 等确定性规则。
- 训练无关，frozen LLM 推理期控制。

**关键实验**
在 GAIA 和 Browsecomp-plus 上，DeepSeek-V4 下 HyMem 平均 Pass@1 分别达到 66.7% 和 61.3%，超过最强 baseline 6.1 和 4.7 个百分点；Browsecomp-plus hard 子集从 14.0% 提升到 30.0%。消融显示，移除 isolated reasoning 或 memory management 在 GAIA 上均导致 18.6pp 的下降；同时 planner context 增长远慢于总上下文，资源消耗无明显增加。

**最值得记住的一句话**
不是压缩上下文长度，而是从源头限制什么信息能进入决策上下文。
