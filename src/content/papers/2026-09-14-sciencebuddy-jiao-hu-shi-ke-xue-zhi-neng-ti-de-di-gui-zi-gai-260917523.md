---
title: 'ScienceBuddy: Recursive-in-Recursive Self-Improvement for Interactive Scientific
  Agents'
title_zh: ScienceBuddy：交互式科学智能体的递归自改进
authors:
- Shuhan Xue
- Jianyuan Zhong
- Ziyuan Nan
- Wenbin Li
- Zhaochen Yu
- Jinchao Ding
- Qiang Gao
- Pengyu Zhan
- Yuntong Zhang
- Tian Cheng
arxiv_id: '2609.17523'
url: https://arxiv.org/abs/2609.17523
pdf_url: https://arxiv.org/pdf/2609.17523
published: '2026-09-14'
collected: '2026-09-16'
category: Agent
direction: 科学智能体 · 递归自改进
tags:
- Scientific Agents
- Recursive Self-Improvement
- Reinforcement Learning
- Harness Evolution
- Interactive Workspace
one_liner: 发布 ScienceBuddy 科学工作空间，以递归内外双循环耦合 harness 演化与模型强化学习
practical_value: '- **将用户反馈转化为训练任务与评估 rubrics**：电商/推荐 Agent 可借鉴，把用户点击、拒绝、改写等交互行为和执行结果自动转成带评分的训练样本，持续优化推荐策略，而非只靠离线日志。

  - **内外双循环解耦模型与工具链迭代**：内层固定模型优化工具/harness，外层在改进后的 harness 下训练模型。业务上可先完善 Agent 的工具调用、API
  接口、记忆管理等，再逐步 RL 训练模型，降低同时改动带来的不稳定。

  - **多模态工作空间 + 模块化工具集成**：ScienceBuddy 的 224 tools / 22 modules 架构启示电商 Agent 平台可将商品图、评论、表格、用户序列等不同模态数据统一接入，按任务模块化编排工具，支持快速扩展。

  - **执行证据纳入持续学习**：把 Agent 执行过程中的中间步骤、失败信号作为训练经验，可用于改进搜索推荐 Agent 的 query 改写、商品对比、决策链路，提升可解释性与可靠性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有科学 Agent 多为固定模型，难以从研究者日常协作中持续改进。作者认为智能体应像人类一样通过长期经验积累提升能力。

**方法关键点**：ScienceBuddy 是一个交互式科学工作空间，支持多模态文档、图像、表格、生物序列，集成 224 个工具、22 个功能模块，覆盖基因组学、分子/癌症生物学、药理学、生物成像、文献检索等。其核心是 **recursive-in-recursive self-improvement**：内层递归在模型固定时改进 harness（工具、任务定义、评估 rubrics），外层递归在改进后的 harness 下用强化学习训练模型。harness 演化塑造训练经验，模型学习又为 harness 调整创造新机会，形成双层协同进化。工作空间将研究者的请求、反馈和执行证据转化为任务与评估标准，用于持续学习。

**关键结果**：论文展示了研究者交互、harness 改进和模型学习的 case studies，基准案例覆盖四类科学任务家族；通过发布产品形态的 ScienceBuddy，将这一范式开放给科学社区，朝向 discovery intelligence 迈进。
