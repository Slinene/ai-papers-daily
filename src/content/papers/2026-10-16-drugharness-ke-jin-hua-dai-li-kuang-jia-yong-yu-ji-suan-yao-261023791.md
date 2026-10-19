---
title: 'DrugHarness: An Evolvable Agent Harness for Computational Drug Discovery'
title_zh: DrugHarness：可进化代理框架用于计算药物发现
authors:
- Yuxing Chen
- Zhisheng Zhang
- Cheng Tang
- Wei Li
- Minghui Zhang
- Ziyan Huang
- Shaocong Wei
- Jiawei Chen
- Junru Hu
- Hongze Zhu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- China Pharmaceutical University
- University of the Chinese Academy of Sciences
- Shanghai Jiao Tong University
- Westlake University
arxiv_id: '2610.23791'
url: https://arxiv.org/abs/2610.23791
pdf_url: https://arxiv.org/pdf/2610.23791
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能进化 · 科学执行
tags:
- Agent
- Skill Evolution
- Drug Discovery
- Scientific Agent
- Conditional Skill Induction
one_liner: 通过条件技能归纳与独立审核，构建可进化的科学代理框架，显著提升分子筛选与优化能力
practical_value: '- 可借鉴“技能库+独立审核”机制：从执行轨迹和结果反馈中归纳候选策略，由独立 review agent 做来源核验与定向试跑后入库。在电商推荐
  Agent 中可先由 critic LLM 评估新策略，再利用历史日志或小流量实验验证，避免噪声策略直接上线。

  - 为技能绑定可观察的适用条件（applicability conditions），仅在满足条件时激活。推荐场景中可将策略与用户群、场景、上下文绑定，避免全局误用；类似规则引擎中的条件触发，但由
  LLM 自动归纳条件。

  - 环境保留候选、结果、产物的关联 lineage，便于回溯和提炼技能。推荐系统可构建“推荐轨迹-用户反馈-候选集”的 lineage store，用于策略诊断、归因和持续优化。

  - 分离“执行”与“技能审核”两个角色，防止自我强化偏差。在推荐 Agent 中设置独立策略评估器，对生成的新策略做验证后再上线，能降低风险并提高策略质量。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：计算药物发现要求 agent 组合科学操作并适应不断变化的证据和约束，但现有 agent 通常固定技能，难以从任务经验中进化。

**方法关键点**：DrugHarness 是一个可进化 agent 框架，环境集成 80+ 科学操作、生物医学资源和任务专用代码，并保留候选、结果、产物之间的关联。从执行轨迹与结果反馈中，框架归纳带适用条件的 action hypotheses，包含推荐动作和支持证据。独立 review agent 通过来源核验和定向执行试验评估候选技能，通过的技能进入技能库指导后续任务，并根据反馈持续修订。

**关键结果**：无进化版本已在 MolBench 上超过 MolClaw-CC，亲和力比较准确率提升 10.8 个百分点，平均 top-3 active hits 提高 55%。回顾性评估显示，进化使 Qwen 的亲和力比较准确率从 62.2% 提升到 81.1%，优化成功率从 79.5% 提升到 87.2%。在前瞻 HPK1 研究中，DrugHarness 获得比 Biomni 更优的 median docking score；合成化合物达到 14.19 nM 的细胞 IC50，比最佳输入参考提升 2.64 倍，活性与药物化学家设计的化合物相当。
