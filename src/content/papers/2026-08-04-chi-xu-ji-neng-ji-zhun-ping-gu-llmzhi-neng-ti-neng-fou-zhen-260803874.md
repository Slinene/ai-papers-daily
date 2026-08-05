---
title: 'ContinualSkillBench: Can LLM Agents Truly Evolve Their Capabilities?'
title_zh: 持续技能基准：评估LLM智能体能否真正进化其能力
authors:
- Tianyi Guan
- Yiding Wang
- Haotong Yang
- Siyuan Cao
- Shirui Liu
- Yi Hu
- Jiaqi Li
- Muhan Zhang
affiliations:
- Institute for Artificial Intelligence, Peking University
- Beijing Institute for General Artificial Intelligence
arxiv_id: '2608.03874'
url: https://arxiv.org/abs/2608.03874
pdf_url: https://arxiv.org/pdf/2608.03874
published: '2026-08-04'
collected: '2026-08-05'
category: Agent
direction: Agent连续技能学习评估
tags:
- Agent Skill Evolution
- Continual Learning
- In-Context Learning
- Benchmark
- LLM Agents
- Skill Library
one_liner: 构建动态评估框架，揭示顺序执行提升性能但技能库维护未显著超越纯上下文学习，技能泛化仍难
practical_value: '- **纯上下文学习可替代复杂技能库**：在电商Agent的工作流中，对于简单的顺序任务（如用户意图识别→商品推荐→生成文案），直接利用对话历史和反馈的上下文学习表现与维护显式技能库相当，可以简化系统设计，避免技能库膨胀。

  - **警惕技能碎片化**：弱模型容易生成大量任务特定技能且复用率低，导致检索负担加重。可以设计技能合并策略（如定期聚类相似技能并泛化）或设置技能池容量限制，通过淘汰低频技能来维持效率。

  - **任务流设计需注入技能依赖结构**：通过构建任务依赖图并按拓扑排序安排任务顺序（难度递进 + 技能复用），能显著提高技能覆盖率和转移机会，这在推荐系统的多阶段流程（召回→粗排→精排→策略）中可借鉴，使上游产出的特征或知识能被下游利用。

  - **评估指标可移植**：任务重用率和核心技能覆盖率可作为量化连续学习环境质量的指标，用于检测推荐序列中是否存在有效的知识迁移路径。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
当前LLM智能体依赖外部技能库解决复杂任务，但手动构建成本高昂。关键问题是：智能体能否在连续任务流中，仅凭借任务描述和反馈自主进化技能，并将经验固化为可复用的能力？现有评估多在孤立任务上测试，缺乏对序列化技能学习的系统性检验。

## 方法
- 构建 **ContinualSkillBench**：涵盖法律、金融、医疗、数学、办公5个领域，每个领域由100个相互关联的子任务组成。
- 通过LLM识别任务所需核心技能，构建有向依赖图，并采用带难度约束的贪心拓扑排序，使任务按技能依赖递进排列。
- 每个子任务执行三回合交互：接收指令→执行→基于反馈反思，反思时可创建/修改技能（`Create Skill` / `Modify Skill`）。
- 对比**独立执行**（每任务重置历史与技能库）、**顺序执行**（保持技能库）和**纯上下文学习**（保留历史但禁止修改技能库）三种条件。
- 评价指标包括原始奖励与归一化奖励（仅比较双方均有有效输出的任务子集）。

## 关键结果
- 在GPT-4o、GPT-5.3-Codex和Claude 4.7 Opus上，顺序执行在14/15模型-领域组合中提升归一化奖励，平均相对增益16.9%。
- 消融实验：纯上下文学习（ICL）平均归一化奖励0.605与技能维护（0.602）相当，表明增益主要来自历史上下文和反馈，而非技能抽象化。
- 显式技能库对需精确输出或固定流程的任务（如法律条文匹配、医疗诊断程序）有选择性帮助，但在开放式评价任务中反而可能因过度适配历史评分而降低性能。
- GPT-4o跨5领域累积384项技能但复用率低，GPT-5.3-Codex仅205项却调用更频繁，体现出弱模型更易造成技能碎片化。
- 任务结构性分析显示，69.5%的任务至少复用了先前的一项核心技能，平均35.5%的技能需求有历史对应项，证明基准设计有效提供了技能转移机会。

> **一句话**：智能体能通过连续交互实现性能提升，但将经验稳固为可泛化的技能仍是开放难题。
