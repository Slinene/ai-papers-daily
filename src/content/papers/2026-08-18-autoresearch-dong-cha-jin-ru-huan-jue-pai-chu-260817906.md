---
title: 'AutoResearch: Insight In, Hallucination Out'
title_zh: AutoResearch：洞察进入，幻觉排除
authors:
- Yiming Ren
- Xiang Liu
- Qumeng Sun
- Xiao Zhang
- Jiahao Li
- Haoyang Zhang
- Junjie Wang
affiliations:
- Infinite Evolution Lab, EvoMap
arxiv_id: '2608.17906'
url: https://arxiv.org/abs/2608.17906
pdf_url: https://arxiv.org/pdf/2608.17906
published: '2026-08-18'
collected: '2026-08-19'
category: MultiAgent
direction: 多智能体科研自动化与幻觉抑制
tags:
- Autonomous Research
- Multi-Agent
- Hallucination Reduction
- Evidence-Based Review
- Idea Generation
- Scientific Workflows
one_liner: 两阶段自主研究系统，用多模型交叉评审和证据驱动执行减少科研幻觉，RSICD Recall 提升至 34.69
practical_value: '- **策略自动化实验的“生成-执行分离”**：将 idea 生成与实验执行拆成两个阶段，生成侧用多模型交叉评审过滤低质量方向，执行侧用独立证据审核把关，可迁移到电商推荐策略的离线实验管理，降低错误策略直接上线的风险。

  - **证据驱动 continue/revise/terminate 决策**：设置审计事件计数与效果基线，当指标不达标或 issue event 增多时自动回退/终止。适合
  Agent 自动化调参、策略探索等场景，避免在无收益方向浪费算力。

  - **跨模型生成 + cross-review 降低幻觉**：在 query 推荐、push 文案等生成任务中，可用多个 LLM 生成候选并交叉评审，只保留有领域知识支撑的结果，减少无根据推荐。

  - **实验分解为可迭代子任务并逐一验收**：将复杂实验拆解为实现、诊断、验证步骤，每个步骤设置独立验收，能提升推荐系统离线实验的可复现性和可追溯性。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：自主研究系统虽能执行长流程，但自动化程度提高不等于科学严谨；生成的想法和实验结论可能缺乏依据，产生幻觉。需要让洞察在实验前有依据、结论在接受前有证据。

**方法关键点**：AutoResearch 采用两阶段架构。Idea Generation 持续整合新兴研究信号与领域知识，识别可迁移的机制性洞察，并通过多模型生成与交叉评审产出有依据、可测试的研究计划。Idea Execution 协调多个 agent 将计划分解为实验，迭代实现与诊断，最后由独立证据评审决定是否接受结论；系统根据证据判断继续、修订或终止研究方向。

**关键结果**：在跨模态检索、系统优化、基准驱动 ML 等场景中产生可衡量进展，并能检测和纠正不可靠结果。RSICD 上，AutoResearch 生成的 idea 将 mean Recall 从 32.84 提升至 34.69，审计确认的 issue events 仅 5 次，其他自治系统为 11–27 次。
