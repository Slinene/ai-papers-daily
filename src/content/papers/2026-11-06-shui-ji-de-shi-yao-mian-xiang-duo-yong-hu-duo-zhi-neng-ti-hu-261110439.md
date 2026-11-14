---
title: Who Remembers What? Multi-Granularity Memory Extraction for Multi-User, Multi-Agent
  Interaction
title_zh: 谁记得什么：面向多用户多智能体交互的多粒度记忆提取
authors:
- Yunzhe Wang
- Mesut Erhan Unal
- Sheng Zhang
- Shabnam Ghadar
- Peng Tang
affiliations:
- AWS Agentic AI
- University of Southern California
arxiv_id: '2611.10439'
url: https://arxiv.org/abs/2611.10439
pdf_url: https://arxiv.org/pdf/2611.10439
published: '2026-11-06'
collected: '2026-11-14'
category: MultiAgent
direction: 多智能体记忆共享与隐私
tags:
- multi-agent memory
- privacy
- self-evolving agents
- cross-learning
- memory scoping
- LLM agents
one_liner: 提出四作用域记忆系统 MIXUA，在跨用户跨智能体学习中同时提升任务通过率、偏好保持和隐私保护
practical_value: '- 记忆作用域拆分：将跨用户/跨渠道的 Agent 记忆拆成 PAIR / USER / AGENT / GLOBAL 四类。在电商多租户
  Agent 或广告投放助手中，用户偏好（USER）、特定渠道或模型配置的注意事项（AGENT）、单用户单渠道会话上下文（PAIR）、通用可复用业务知识（GLOBAL）分开存储、分开检索，可以同时保住个性化与跨用户知识迁移。

  - 隐私隔离用“构造性流”而不是依赖 LLM 自觉：把轨迹分成 reusable 和 protected 两条流，protected 流只能写 PAIR/USER，不能写
  AGENT/GLOBAL。这对应多商家推荐系统中敏感 PII、商家机密绝不能进入共享记忆。生产环境建议用隔离写入通道和流标签强制边界。

  - 定期 store review 重新定级/合并：每个 round 结束后让 LLM 以全量 store 视角 re-scope 每条 memory，并合并重复条目。可借鉴为异步记忆整理任务，降低
  cross-scope 泄漏，提升偏好保持。

  - 各 scope 独立 retrieval budget：区分 USER/PAIR 等记忆的字符预算，防止通用任务经验挤占个人偏好上下文。在低预算下仍能接近满预算的收益，适合成本敏感场景。文件式检索可省
  token 但会牺牲偏好保持，需要按场景取舍。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 self-evolving agents 多在单一用户-单一智能体或单用户多智能体团队内共享经验；跨用户跨智能体群体学习缺乏细粒度受众控制，容易造成隐私泄露或偏好丢失。

**方法关键点**  
- 将记忆条目按受益对象与披露边界分配四种作用域：PAIR、USER、AGENT、GLOBAL，读者只能访问自己所属的 USER/AGENT/GLOBAL 和自己的 PAIR，不读其他用户/其他 pair。  
- 写入采用 dual-stream：每个轨迹拆成 reusable 和 protected 两条流，由隔离 writer 写；protected 流只能落 USER/PAIR，从机制上防止隐私进入共享作用域。  
- 每条 memory 记录 situation、lesson、scope、provenance；检索时按 situation 与任务 prompt 的相似度，在各 scope 预算内召回。  
- 可选的 periodic store review 以全 store 视角重新设定作用域、合并重复条目。  
- 测试基准 CROSSLEARNBENCH 组合 7 个 agent 任务集并注入合成 PII 和用户文档偏好。

**关键结果**  
5 用户 × 7 harness，MIXUA 相比 no memory 通过率最高 +16.3pp（72.0→89.8），比纯 GLOBAL 高约 5pp；在完全由其他用户+其他 agent 尝试过的任务上 +13.9；随机任务的新任务上 +10.1，约为 GLOBAL-only 的 2 倍。偏好保持最高 90%，隐私探针在禁止作用域发现 planted PII 的比例 ≤0.02%。消融显示去掉 GLOBAL 收益从 15.3 掉到 9.0，去掉 USER 偏好保持从 90% 掉到 81%；AGENT 和 PAIR 在专门探针上作用显著。

**最值得记住的一句话**  
在跨用户跨 agent 的集体学习中，memory 的 audience scope 和 disclosure boundary 必须一起学习，否则要么泛化不足，要么隐私泄漏。
