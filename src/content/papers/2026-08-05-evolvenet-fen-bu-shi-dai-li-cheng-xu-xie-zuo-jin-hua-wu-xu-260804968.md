---
title: 'EvolveNet: Collaborative Harness Evolution for Agent Self-Improvement'
title_zh: EvolveNet：分布式代理程序协作进化，无需共享原始数据即可聚合经验
authors:
- Jun Nie
- Yonggang Zhang
- Qianshu Cai
- Yiu-ming Cheung
- Xinmei Tian
- Bo Han
affiliations:
- Hong Kong Baptist University
- University of Science and Technology of China
- The Hong Kong University of Science and Technology
arxiv_id: '2608.04968'
url: https://arxiv.org/abs/2608.04968
pdf_url: https://arxiv.org/pdf/2608.04968
published: '2026-08-05'
collected: '2026-08-06'
category: Agent
direction: 代理协作进化 · 程序聚合
tags:
- collaborative-harness-evolution
- program-aggregation
- agent-self-improvement
- scope-typed
- evidence-guided
- distributed
one_liner: 将代理程序（harness）的本地进化成果跨客户端聚合，通过范围类型与行为证据解决程序编辑冲突
practical_value: '- **分布式 Agent 策略协同**：不同商家、品类或地区的推荐/搜索 Agent 可在本地数据上独立优化自己的 harness（提示、工具调用、校验规则），仅将编辑增量与行为证据上传，中心无需触碰原始数据，适合隐私敏感或数据隔离场景。

  - **冲突解决与多域融合**：聚合时采用范围类型（GLOBAL vs. HOME）与域守卫（guard），使针对特定品类的策略仅在对应条件下激活，避免跨域冲突；此设计可直接用于多域
  Agent 的 prompt/workflow 聚合，如搜索广告的多行业模板合并。

  - **安全回滚机制**：行为门控（验证集上增益必须 ≥ 回退）保证合并不会导致整体性能退化，可借鉴到线上 Agent 的自动化更新管线，实现有保障的持续进化。

  - **并行搜索加速**：本地进化并行化，迭代轮次受最慢客户端而非总搜索时间限制，适合需要频繁迭代的电商/广告系统，可在不增加串行深度的前提下利用多团队并行实验。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
LLM Agent 的能力不仅取决于模型，更取决于其外围程序（harness）——构成上下文、调用工具、校验结果与失败恢复的可执行代码。现实部署中，不同用户、组织或环境产生分散的经验流，因隐私或归属无法集中池化。传统集中式进化无法利用这些孤岛数据，而 EvolveNet 提出一种新的范式：将经验提取前移至数据本地，服务器聚合的是本地进化后的程序编辑（delta），而非原始工作负载，实现跨部署的协作式程序自我改进。

**方法关键点**
- **本地进化与广播**：服务器广播共享 harness，各客户端在本地工作负载上独立进化，产生专业化的程序变体，并返回与基线的 diff 及行为证据（哪些样例被修复、哪些被破坏）。
- **范围类型聚合**：服务器将各客户端的编辑拆解为“机制”（如执行重试规则、Schema 探测等），根据行为证据将机制分为 GLOBAL（跨域有效）或 HOME(域)（仅适用于原域），用域守卫条件隔离，避免冲突。全球域机制直接嵌入共享程序，归属域机制以条件分支保留。
- **证据引导的采纳**：仅当机制有至少两个域的证据支持或针对域无关故障时才提升为全局；单条证据机制被丢弃；域归属机制以其原始客户端实现为准，不做改写，保留已测增益。
- **行为门控**：合并后的候选程序在独立验证集上通过逐项比较（修复项数 ≥ 破坏项数）方可提交，否则回滚至上一轮共享程序，保证轨迹不退化。

**实验结果**
在五个设置（BIRD 文本到 SQL、DS-1000 数据科学编码、LiveCodeBench 竞争编程、SWE-bench 软件工程、ClawEval 代理工作流）上，EvolveNet 均提升了共享 harnessing 的准确率：
- BIRD：57.3% → 70.7%
- DS-1000：55.5% → 68.5%
- LiveCodeBench：33.3% → 66.7%
- SWE-bench：37.5% → 57.5%
- ClawEval：65.8 → 74.1（平均分）
其中 DS-1000（异构度最高）显示聚合带来的增益最大（+13.0），且保留不同客户端发现的互补机制，合并程序比仅路由最强专家高 9.0 点。消融表明范围条件贡献 2.0 点额外提升，且聚合优于简单委托（保留所有专家并调度）。

**核心启示**
分布代理的共享改进载体可以是可执行程序本身，通过基于证据的“作用域”聚合与行为门控，在不泄露原始数据的前提下有效积累多源经验。
