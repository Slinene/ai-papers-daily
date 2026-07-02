---
title: 'SkillHone: A Harness for Continual Agent Skill Evolution Through Persistent
  Decision History'
title_zh: SkillHone：基于持久化决策历史的持续Agent技能进化框架
authors:
- Zhiwei Li
- Yong Hu
affiliations:
- Tencent Inc.
arxiv_id: '2606.08671'
url: https://arxiv.org/abs/2606.08671
pdf_url: https://arxiv.org/pdf/2606.08671
published: '2026-06-22'
collected: '2026-07-02'
category: Agent
direction: Agent技能持续进化 · 决策历史持久化
tags:
- Agent Skill Evolution
- Decision History
- MultiAgent
- LLM Agent
- Continual Learning
- Practice Feedback
one_liner: 通过持久化决策历史与角色分离子代理实现Agent技能的持续进化，超越商业deep-research agent
practical_value: '- **技能进化与搜索推荐系统结合**：将技能看作搜索推荐中的策略、召回规则或排序配置，用 SkillHone 的持久化历史管理这些策略的迭代，避免无效回退，每次修改都可追溯其诊断依据与实证反馈，适用于广告出价策略动态调整、推荐模型在线更新。

  - **角色分离子代理用于多智体协作**：引入 diagnosis、revision、evidence 等子代理分工，可迁移到电商 Query 改写或搜索建议生成场景，一个代理诊断当前
  query 性能短板，另一个根据历史修订记录提出新的改写方案，通过实践探针评估后合入主流程。

  - **实践探针机制做离线评估**：在推荐系统中可抽检历史曝光样本作为探针，每次技能更新后重跑探针并比对效果，实现低成本、可复现的离线迭代，比全量 A/B 实验更快反馈。

  - **决策历史作为知识资产沉淀**：主动记录 agent 的决策过程（如为什么使用某个召回通道、为什么排序公式这样调参），形成可检索的知识库，让后续模型或工程师快速理解历史优化逻辑，减少重复实验。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有Agent技能进化方法只在单次运行内优化，仅保留最终产物，丢弃诊断、修订、被拒方案等决策历史，导致后续迭代需要重复之前推理，限制了技能长期进化。

**方法关键点**：SkillHone 提出持久化决策历史的持续技能进化框架。核心设计包括：1）将技能修订与评估侧的实践反馈证据配对，记录结构化的历史（诊断→修订→证据→结果）；2）采用角色分离的子代理（diagnosis、revision、evidence）在实践探针上运行候选技能，依据历史决策提出修订，实现跨会话的细化；3）使用红化报告技术防止代理过拟合到特定探针。整个过程无需预集成搜索栈，仅靠迭代优化即提升深度研究能力。

**关键结果**：在GAIA基准上超越商业deep-research agent（+15.8分），在WebWalkerQA-EN上提升3.2分，且优于先前技能进化方法。内部工具分析场景中平均提升18.8个点，验证了持久化历史对跨任务技能进化的增益。
