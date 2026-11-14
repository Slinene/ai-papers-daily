---
title: 'LiveGeo: Benchmarking Geographic Agents in Continuously Evolving Worlds'
title_zh: 持续演化世界中的地理智能体基准测试
authors:
- Pengcheng Zhou
- Xuanyu Liu
- Yanchen Yin
- Tianjie Ju
- Bobo Li
- Shengqiong Wu
- Hao Fei
- Mong-Li Lee
- Wynne Hsu
affiliations:
- National University of Singapore
- Zhejiang University
- Beijing University of Posts and Telecommunications
- University of Oxford
arxiv_id: '2611.17267'
url: https://arxiv.org/abs/2611.17267
pdf_url: https://arxiv.org/pdf/2611.17267
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: LLM 地理智能体动态决策评估
tags:
- Agent Benchmark
- LLM
- Dynamic Environment
- Geographic Agents
- Reliability
one_liner: 构建 GeoWorld 持续演化地理环境与 LiveGeo 基准，评估 LLM 智能体动态可靠决策，发现静态强不等于动态可靠
practical_value: '- 动态环境仿真思路：可借鉴 GeoWorld 的“统一时间线 + 多事件独立演化 + 可验证状态历史”，在电商/推荐场景构建用户偏好、库存、价格、营销活动随时间变化的模拟器，用于离线评估策略的动态鲁棒性。

  - 主动信息获取与证据校验：LiveGeo 要求 Agent 在决策前查最新信息并验证先前证据是否失效，对应推荐系统中实时特征新鲜度、缓存失效机制、动态重排序，工程上可设计“先查后策”的
  Agent workflow。

  - 静态指标无法揭示动态风险：论文发现静态任务表现好的模型在动态场景不一定可靠，提醒在推荐/广告评估中加入时间演化测试集或仿真环境，避免仅看离线 AUC/CTR
  而忽略分布漂移下的性能退化。

  - 开源平台可扩展：GeoWorld 代码与基准开放，可作为构建推荐策略仿真器的基础，加入自定义事件类型和任务，用于在线学习、AB 测试模拟等研究。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**  
现有 LLM Agent 评估大多在固定地理状态上推理和规划，忽略真实世界持续演化，无法衡量 Agent 在动态环境下的可靠决策能力。  
**方法关键点**  
提出 GeoWorld 平台：一个可控、持续演化的地理环境，基于真实地理结构，允许多类事件（天气、交通、地点状态、城市事件、参与者状态）沿统一时间线独立演化，并保留可验证状态历史。在此之上构建 LiveGeo 基准，将地理任务置于演化环境中，要求 Agent 主动获取任务相关信息、核查先前决策支持证据是否仍然成立、必要时修订计划。评估关注静态与动态任务表现、动态可靠性、证据获取与转化瓶颈。  
**关键结果**  
即使前沿 LLM 在静态任务上也表现挣扎，没有模型能在所有任务上一致领先；静态性能强不保证动态可靠性。进一步分析指出瓶颈在于 Agent 难以将获取的证据转化为有效决策，并在世界演化时维持正确性。发布 LiveGeo 与 GeoWorld，提供可扩展基础设施用于下一代可靠行动智能体研究。
