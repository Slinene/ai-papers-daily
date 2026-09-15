---
title: 'Dream-RSI: Recursive Self-Improvement through Evolving Worlds'
title_zh: Dream-RSI：通过演化世界实现递归自我改进的探索框架
authors:
- Tong Zheng
- Xidong Wu
- Zheng Zhang
- Zhankui He
- Chaoyi Zhang
- Benjamin Coleman
- Ruoqiao Wei
- Di Bai
- Haolin Liu
- Rui Liu
affiliations:
- Google
- University of Maryland, College Park
- Google Deepmind
- University of Virginia
arxiv_id: '2609.14858'
url: https://arxiv.org/abs/2609.14858
pdf_url: https://arxiv.org/pdf/2609.14858
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: Agent 探索策略递归自改进
tags:
- recursive self-improvement
- exploration policy
- replay simulator
- off-policy evaluation
- coding agent
- GPU kernel
one_liner: 用历史发现树构建重放模拟器，以离线低成本反馈迭代优化探索策略，降低发现成本并提升质量
practical_value: '- 把探索策略从底层 coding agent 中拆出，做成可编程 orchestration layer；业务中的 Agent
  搜索/推荐策略也可分离“生成/排序核心”与“探索策略”，便于低成本切换和迭代。

  - 利用已积累的发现树/用户交互轨迹构建 replay simulator，进行 off-policy 评估，避免每次探索策略变更都跑线上长链路；对电商搜索、推荐
  Agent 的策略选型、prompt/工具调用组合优化尤其划算。

  - 采用 log replay + dreaming 方式生成即时低延迟反馈，适合需要大量策略试错的场景（如广告出价、商品推荐 query 生成），可降低在线
  A/B 成本。

  - 自改进 loop 中将新发现不断并入 simulator pool，形成持续扩大的离线评估环境；对应业务可把每次线上实验数据沉淀为可复用的策略仿真器。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：递归自我改进依赖高效探索，但固定探索策略难以随搜索空间扩展，在线策略优化面临长周期、昂贵反馈。

方法关键点：Dream-RSI 保留底层 coding agent 不变，增加轻量可编程编排层；核心思路是把历史发现树积累为 replay simulator，在模拟器上“做梦”获取即时、低成本的 off-policy feedback，用于评估和优化探索策略；优化后的策略重新上线继续发现，扩增模拟器池，形成递归自改进循环。

结果：在算法工程、数学优化、GPU kernel 工程等任务上，达到竞争性或更优的发现质量，并在多个设置下显著降低发现成本。
