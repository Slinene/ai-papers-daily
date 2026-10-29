---
title: Test-Time Communication in Trading Agent Swarms
title_zh: 交易Agent群体中的测试时通信研究
authors:
- Avid Fayaz
- Harry Zhang
- Håvard Alstadheim
- Erik Nordlöf
- Vilhelm Karlin
- André Silva
affiliations:
- Infinite Ascent, Stockholm, Sweden
arxiv_id: '2610.37448'
url: https://arxiv.org/abs/2610.37448
pdf_url: https://arxiv.org/pdf/2610.37448
published: '2026-10-27'
collected: '2026-10-29'
category: MultiAgent
direction: 多智能体通信与羊群效应
tags:
- Multi-agent
- Communication
- Trading agents
- Herding
- LLM agents
one_liner: 在无共享目标的交易Agent群体中量化通信带来的过度收敛与语言复用，并提出以无同伴基线衡量羊群效应
practical_value: '- 多智能体系统中，若各Agent目标独立、反馈延迟且噪声大（如电商推荐中的用户偏好各异），通信可能造成不必要的收敛/同质化；可借鉴论文设置“无同伴基线”来测量超额收敛，评估协作机制是否真正带来收益而非仅同步行为。

  - 监控通信中重复短语/决策规则复用可作为早期预警：在电商Agent协作中，可跟踪agent生成内容对同伴消息的n-gram复用率，识别羊群效应或信息级联。

  - 实验设计上，对比隔离、竞争板、协作板、带唤醒pings、共享笔记五种机制，能为业务中选择Agent间通信接口（如共享消息流 vs 共享知识库 vs 定向提醒）提供成本-收益分析框架。

  - 记录每个决策前agent读到的全部内容，对于事后归因和审计推荐/内容生成Agent的行为至关重要，尤其在多Agent联动可能产生协同偏差时。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：以往多Agent通信研究多基于共享目标和快速清晰反馈，而交易场景每个Agent管理独立账户，市场评分滞后且噪声大，群体是独立决策者而非团队，因此收敛是风险而非目标。需要考察测试时通信在无共享目标场景下是否导致羊群效应。

**方法关键点**：200个Agent来自四个模型家族，每组10个，运行于五种通信机制：完全隔离、竞争板（帖子+个体排名）、协作板（帖子+团队得分）、带pings板（帖子+唤醒请求+团队得分）、共享记忆（笔记+个体排名）。实验覆盖7个美股交易日（2026年10月1-9日），每次决策前记录Agent读取的全部内容。

**关键结果**：四个家族中有两个，通信组比隔离组持有更多相同股票；群体收益主要来自成员共同持仓。看到同伴帖子使Agent复用其中8词短语的概率提高7个百分点；未看到同伴帖子的Agent之间因共同输入导致14%的短语共享。但看到帖子当天早晨的交易行为未检测到显著变化。案例研究显示头寸和决策规则在后续几天被采纳，通信组同步卖出频率更高。隔离组同样会收敛到相同股票，有时达到完全一致，因此衡量羊群效应需以无同伴基线为参照计算超额收敛。
