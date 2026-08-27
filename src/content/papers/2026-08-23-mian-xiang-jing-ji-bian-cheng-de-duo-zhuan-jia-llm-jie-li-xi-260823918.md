---
title: 'MARS: Multi-Specialist LLM Relay System for Competitive Programming'
title_zh: 面向竞技编程的多专家 LLM 接力系统 MARS
authors:
- Andrei Mikhailov
- Mikhail Burtsev
- Alsu Sagirova
affiliations:
- MIRAI
- London Institute for Mathematical Sciences
- AXXX
arxiv_id: '2608.23918'
url: https://arxiv.org/abs/2608.23918
pdf_url: https://arxiv.org/pdf/2608.23918
published: '2026-08-23'
collected: '2026-08-27'
category: MultiAgent
direction: 多智能体接力与专家检索
tags:
- multi-agent
- RAG
- competitive programming
- code generation
- specialist agents
one_liner: MARS 用主题专家接力+RAG 检索算法理论，在 CodeContests 以 3.3 倍更低成本逼近 CodeSIM
practical_value: '- 在电商/广告 Agent 系统中，把通用 planner/coder/debugger 角色改成按业务域或环节划分的专家（如召回专家、创意生成专家、竞价策略专家），每个专家挂载领域知识库，用检索决定每次任务激活哪些专家。

  - 采用 RAG 为专家注入领域理论或历史案例，而不是单纯依赖 LLM 通才能力；在推荐/搜索场景可检索历史成功策略、类目知识或用户画像模板。

  - 引入 sandbox 验证环节：每轮让候选方案在业务仿真器或离线评估集上跑分，专家根据结果保留、修复或转交，类似代码沙箱换成广告投放模拟或推荐 A/B 估计器。

  - 专家间用结构化 packet 传递候选方案、验证结果、错误信息和下一步期望，降低多 agent 沟通成本；最后设一个固定 infrastructure-fixer
  pass 统一输出格式，可借鉴到 agent 输出治理。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 在竞技编程中仍存在明显失败模式，现有多 agent 管线把工作分给通用 planner、coder、debugger，且算法技巧选择完全交给骨干模型，缺乏真正的领域专精。

**方法关键点**：MARS 是 prompt-only 框架，每个 agent 是算法主题专家（动态规划、图、字符串、几何等），并用算法理论语料通过 RAG 做知识 grounding。给定问题后，检索选出相关专家组成小团队；starter 先写 C++17 初稿，后续每轮在沙箱中用公开样例运行候选解，当前专家可以选择保留、修复或把草稿转交给下一位专家，并传递结构化 packet。最后有一个 infrastructure-fixer pass 统一处理 boilerplate。

**关键结果**：在 CodeContests 测试集上，使用 Gemma 4 的 MARS 达到 0.624±0.006 通过率，平均每个任务 2.3 个 pipeline stages，相比直接提示提升 14.4 个百分点；以 3.3 倍更低的墙钟成本接近 CodeSIM 的 0.731，并且单任务 token 开销方差显著更小。
