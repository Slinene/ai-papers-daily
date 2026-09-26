---
title: 'Jev-Mobile: Jev as an Executor for Mobile GUI Agents'
title_zh: Jev-Mobile：将 Jev 作为移动 GUI Agent 的执行器
authors:
- Linghua Zhang
affiliations:
- Rice University
arxiv_id: '2609.30186'
url: https://arxiv.org/abs/2609.30186
pdf_url: https://arxiv.org/pdf/2609.30186
published: '2026-09-24'
collected: '2026-09-26'
category: Agent
direction: Agent 分层执行 · 高低频解耦
tags:
- Mobile GUI Agent
- VLM
- Structured Action Space
- Efficiency
- Hierarchical Agent
- AndroidWorld
one_liner: 在移动 GUI Agent 中把 VLM 高频规划改为低频目标设定，由轻量 Jev 在结构化动作空间中高频执行，实现成功率相近、延迟与成本大幅下降
practical_value: '- **高低频分离策略可迁移到电商 Agent**：将昂贵 LLM 的职责限制在设定子目标或局部状态，把高频操作交给轻量决策模型或规则系统，在结构化候选空间内做选择，可大幅降低
  API 成本与延迟。

  - **结构化动作空间是落地关键**：用 accessibility tree / DOM / schema 预先枚举可执行动作，而不是让 LLM 自由生成坐标或文本，能减少非法动作并简化执行器模型设计；在移动端自动化、RPA、购物助手中可复用。

  - **单次 LLM 决策驱动多步执行**：借鉴“一次规划、多次执行”的模式，让 LLM 输出局部目标或子任务序列，由轻量执行器完成中间交互，避免每步都带全量上下文调用
  VLM。

  - **评估指标同时看成功率与效率**：业务部署中不仅关注任务完成，也要跟踪端到端时长和模型调用成本；即使成功率略降，成本/延迟大幅下降的方案可能更值得上线。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有移动 GUI Agent 几乎每一步都依赖 VLM 同时做规划和动作接地，推理延迟高、API 成本大。
**方法**：Jev-Mobile 将范型改为“低频 VLM 规划 + 高频轻量执行”。VLM 只负责设定局部目标；accessibility tree 提供结构化可执行动作空间；Jev 作为快速 typed 决策模型在该空间内反复选择动作。这样一次 VLM 决策可支持多个 GUI 动作，减少昂贵 VLM 推理并保持自适应交互。
**结果**：在 AndroidWorld 全任务集上，Jev-Mobile 成功率为 79%，SeeAct-V 为 78%，Step-wise VLM 基线为 84%；在成功轨迹中，相对 Step-wise VLM，平均端到端执行时间降低 32.7%，平均模型 API 成本降低 73.4%。表明高层 VLM 推理与低层动作执行解耦可显著提升效率且保持任务性能。
