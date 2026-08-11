---
title: 'MetaStrategy: Generative Ranking with Executable LLM Strategies'
title_zh: 元策略：基于可执行LLM策略的生成式排序
authors:
- Chengyu Lai
- Jiuning Lin
- Zhibo Xiao
- Xiaodong Zhu
- Ruiquan Lan
- Bin Zhang
- Zihong Huang
- Wendong Zhang
- Chuxin Chen
- Yinjiang Cai
affiliations:
- Taobao & Tmall Group of Alibaba
- Wuhan University
- The University of Hong Kong
- University of Cambridge
- Alibaba
arxiv_id: '2608.09440'
url: https://arxiv.org/abs/2608.09440
pdf_url: https://arxiv.org/pdf/2608.09440
published: '2026-08-10'
collected: '2026-08-11'
category: GenRec
direction: LLM策略生成· Generator-Evaluator架构
tags:
- LLM Strategy Generation
- Reinforcement Learning
- On-Policy Distillation
- Curriculum Learning
- Industrial Recommender System
- Generator-Evaluator
one_liner: 用LLM生成结构化排序策略而非物品序列，通过生产路径重放与蒸馏实现零延迟个性化排序
practical_value: '- **LLM生成策略而非列表**：用带类型JSON控制多目标权重、内容类型偏好等，通过编译器注入现有Generator，避免直接生成物品序列带来的集成难题。电商/广告混合流可直接复用这一思路，将LLM作为策略层，不侵入精排队列。

  - **生产路径重放训练**：重放真实请求日志，让LLM策略与现有Generator在同一Evaluator下原子竞争，反馈信号来自当前生产栈而非用户模拟器。推荐系统可借鉴此方法，低成本获得高保真离线RL训练环境。

  - **自竞争课程缓解策略坍缩**：将LLM频繁输出的编译后策略冻结为新Generator加入竞争池，迫使策略持续探索。在推荐、广告出价策略优化中，可照搬此机制防止模型退化为少数极端组合。

  - **评估器路由的奖励增强在线蒸馏**：对每个请求，用Evaluator选择最优教师，结合教师token差异与自身GE奖励进行蒸馏，将4B策略压缩至0.8B。多目标排序模型压缩中，可按此方式保留教师间的互补性与在线分布匹配。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
工业推荐榜单需同时调控多业务目标、内容类型、密度约束等，传统策略层由固定公式或人工规则组成，缺乏个性化。现有生成式推荐直接输出物品序列，难与成熟的预测模型、过滤规则和护栏集成。本文提出让LLM生成一个可执行的*排序策略*（如目标权重、类目偏好、打散约束等），交由已有生产排序器执行，既保留LLM的联合决策能力，又兼容现有系统的所有控制面。

**方法关键点**
- **结构化策略生成**：LLM基于用户意图、实时行为和候选概览，输出一个带类型约束的JSON bundle，包含目标权重调整、内容类型/类目偏好、体验约束、顶部CTR开关五组动作。
- **验证-编译-隔离**：JSON经过解析、模式校验，再由确定性编译器映射为某个独立Generator的运行时参数。该Generator不修改线上其它Generator，只在GE（Generator-Evaluator）架构下原子竞争。
- **生产路径重放环境**：离线训练时，重放线上请求日志的候选集和粗排分，但调用*当前在线*的精排、规则和Evaluator进行重排，获得列表级评分。每个episode是单步上下文决策，奖励由选择、相对排名和基线提升三部分组合。
- **自竞争课程**：将策略频繁输出的编译后配置冻结为新Generator加入下一轮训练，迫使策略持续避开已探索模式，缓解Evaluator代理偏差导致的坍缩。
- **评估器路由的奖励增强在线蒸馏**：同时采样学生和多个教师的策略，在同一请求的原子竞争中用Evaluator选择最优教师，将其与学生的token log-prob差异作为KL正则项与原有RL奖励混合，更新0.8B学生，保证教师信号来自最优且匹配学生采样分布。
- **差分触发近线部署**：线上请求的同步分支直接查表，LLM在近线分支仅在上下文差异超阈值时才刷新策略并异步发布到线上表，实现零RT增量。

**关键实验**
在淘宝首页猜你喜欢86k请求重放数据集（65,536条训练，8,192验证/测试）上，对比生产基线（Greedy、自回归生成式重排GNR、非自回归NAR、单目标扰动）和多个LLM变体。最终0.8B路由OPD学生在增量GE提升上获得+0.73%，远超4B RL策略。线上7天A/B测试：曝光PV+1.49%，点击PV+2.11%，详情页IPV+3.12%，交易额+2.83%，广告消耗+0.87%，且在线响应时间无增长。

**核心洞见**
“我们不生成物品列表，生成的是排序系统的配置指令。” —— 将LLM定位为策略参数生成器而非序列决策者，是在工业系统落地的关键。
