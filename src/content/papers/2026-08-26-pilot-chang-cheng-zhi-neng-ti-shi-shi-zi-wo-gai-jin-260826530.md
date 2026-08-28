---
title: 'PILOT in the Loop: Live Self-Improvement for Long-Horizon Agents'
title_zh: PILOT：长程智能体实时自我改进
authors:
- Yang Xiao
- Yusong Sun
- Haoyi Wu
- Wenyang Hui
- Wen Da
- Zhaokai Luo
- Mu Chuan
- Yao Hu
- Wenjie Li
- Chengyue Jiang
affiliations:
- AllSpark Team
arxiv_id: '2608.26530'
url: https://arxiv.org/abs/2608.26530
pdf_url: https://arxiv.org/pdf/2608.26530
published: '2026-08-26'
collected: '2026-08-28'
category: MultiAgent
direction: Agent 多智体协作与实时自改进
tags:
- agent
- self-improvement
- supervisor-worker
- live-steering
- live-self-evolution
- long-horizon
one_liner: 提出 supervisor-worker 架构，通过 live steering 与 live self-evolution 实现长程智能体实时自我改进，显著提升成功率与
  token 效率
practical_value: '- 将执行与监督分离（supervisor-worker），主 agent 实时 redirect/abort 子 agent，避免单一上下文注意力分散；在电商
  Agent 工作流（自动选品、广告投放、客服）中可引入独立监督者角色，及时纠正长流程偏差。

  - live self-evolution 将运行中暴露的失败模式蒸馏成可复用 skills/memory，形成经验沉淀；推荐系统中可将 bad case /
  成功策略实时固化到知识库或 prompt 中，降低重复错误。

  - 论文观察到输出 token 大幅下降（最多 47.4%），成功评估效率提升 110%+，说明 supervisor 及时中止无望执行可显著降低推理成本；线上
  LLM Agent 可设置 abort 条件，提升 ROI。

  - 方法基于 frozen backbone，无需修改模型权重，适合工程直接复用；可将 PILOT harness 抽象成通用 Agent 编排层，用于搜索推荐场景中的多步
  reasoning / 工具调用。'
score: 8
source: huggingface-daily
depth: abstract
---

**动机**
长程 agent 运行产生大量经验，但多数自改进方法仅在运行结束后处理经验，无法重定向当前运行或立即应用所学教训，导致自改进低效且不可靠。现有架构存在差距：单 agent 自纠正将执行与评估放在同一上下文，注意力分散；子 agent 委派虽分离执行，但主 agent 通常无法实时重定向活跃子 agent。

**方法关键点**
PILOT 提出 supervisor–worker harness，通过两个耦合机制实现 live self-improvement：
1) **live steering**：独立 supervisor 在执行过程中实时重定向或中止活跃 worker；
2) **live self-evolution**：将执行中显现的过程与失败模式蒸馏成可复用 skills 和 memory，形成闭环。
两个机制共同构成“PILOT in the loop”，在运行中同时改进当前任务和持久 harness。

**关键结果数字**
在两个 frozen backbone（GLM-5.1、Kimi-K2.6）和三个基准（Terminal-Bench 2.0、SWE-Bench Pro 等）上，六个配置中五个排名第一。Terminal-Bench 2.0 上，PILOT 比同类 harness 最高提升 9.8 个百分点。自改进设置下，PILOT 分别提升 14.6（GLM-5.1）和 12.4（Kimi-K2.6）个百分点；平均输出 token 分别下降 42.9% 和 47.4%，每百万输出 token 的成功评估次数分别上升 110.3% 和 134.0%。
