---
title: Agentic Memory Management Is the Next Frontier of Information Retrieval
title_zh: 智能体记忆管理：信息检索的下一个前沿
authors:
- Qingyao Ai
affiliations:
- Dept. CS&T, Tsinghua University
arxiv_id: '2610.32464'
url: https://arxiv.org/abs/2610.32464
pdf_url: https://arxiv.org/pdf/2610.32464
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent 记忆管理框架与 IR 融合
tags:
- agentic memory
- information retrieval
- continual learning
- memory management
- RAG
one_liner: 提出 AMM 框架，将记忆对象分为 constants、functions、operators，并给出 IR 视角研究议程
practical_value: '- 在电商/广告 Agent 中，可按 constants/functions/operators 分类设计记忆层：用户长期偏好（constants）用于召回与排序；可调用的推荐策略/工具（functions）按需检索；总结、遗忘、合并等记忆操作（operators）显式管理，避免把所有上下文塞进
  prompt 或向量库。

  - 记忆检索不要只做相关性排序，需定义 utility（对下游动作/转化的贡献），可借鉴 learning to rank 或用 LLM 生成候选后重排，对记忆片段做效用打分，提升推荐
  Agent 的决策质量。

  - 混合参数化与非参数化更新：高频短期信号（点击、会话）写入外部记忆实时检索，低频长期偏好定期用 LoRA 等参数化微调固化，兼顾实时性与成本，适合个性化 Agent
  持续学习。

  - 评估 Agent 记忆时，借鉴搜索/推荐的离线-在线评估体系，关注任务完成率、记忆更新效率与长期回报，而不是只看单轮 QA 准确率。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：传统 IR 聚焦于连接人与完成任务所需信息，但 AI agent 越来越多地替用户消费、保留、执行信息，信息管理发生在 agent 内部，即记忆管理。论文认为 IR 社区应在这一新方向上做出独特贡献。

**方法关键点**：提出 agentic memory management (AMM) 的系统级框架，覆盖记忆的结构、分析、组织、存储、检索与使用。核心贡献是将 memory objects 计算性地分为三类：constants（静态事实与偏好）、functions（可调用的工具或流程）、operators（对记忆本身的操作，如总结、更新、遗忘），每类具有不同的检索语义。论文进一步比较 AMM 与传统 IR、RAG、持续学习的关系，并给出研究议程：构建基准、提出记忆效用原则、设计混合参数化与非参数化更新的优化流程。

**关键结果数字**：本文为视角论文，未报告实验数据；主要贡献是概念框架与分类体系，为后续研究提供方向。
