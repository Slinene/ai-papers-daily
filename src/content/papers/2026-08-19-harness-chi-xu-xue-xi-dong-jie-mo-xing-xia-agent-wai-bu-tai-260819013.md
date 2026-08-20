---
title: 'Harness Continual Learning: Continual Adaptation Beyond Model Parameters'
title_zh: Harness 持续学习：冻结模型下 Agent 外部状态的持续进化
authors:
- Borui Kang
- Jinrui Gu
- Junhan Lv
- Wenbin Li
- Lei Wang
- Yang Gao
affiliations:
- State Key Laboratory for Novel Software Technology, Nanjing University, China
- University of Wollongong, Australia
arxiv_id: '2608.19013'
url: https://arxiv.org/abs/2608.19013
pdf_url: https://arxiv.org/pdf/2608.19013
published: '2026-08-19'
collected: '2026-08-20'
category: Agent
direction: Agent 持续学习 · Harness 进化
tags:
- Continual Learning
- Agent Harness
- LLM
- Memory
- Routing
- Stability-Plasticity
one_liner: 将持续学习对象从模型参数转向 Agent 外部 harness，通过 guarded evolution 显式控制 harness-level
  遗忘
practical_value: '- 在 Agent 系统中引入 **guarded evolution**：将 harness 更新（prompt、memory、routing
  等）与部署分离，设置历史锚点集（anchor set）作为回归测试，只有通过当前改进、历史保留和有效性检查的新配置才上线，避免线上行为退化。\n- 借鉴四组件设计：**Task
  Interface, Experience Memory, Capability Map, Adaptive Router** 可以映射到电商/搜索推荐系统的
  Agent 编排层，把用户意图解析、历史交互记忆、可用工具/策略注册、决策路由分开管理，便于持续迭代和故障定位。\n- 通过调节 **historical-loss
  tolerance Bn** 控制稳定性-可塑性权衡：在大促等需要快速适应新玩法时放宽 Bn，在稳定期收紧，实现业务节奏的灵活控制，而不是一味追求最新任务的最优。\n-
  利用 LLM 从原始交互中总结抽象记忆、再提炼为可复用内部技能（inner skills），可迁移到自动从用户反馈中提炼推荐策略、生成推送文案或 query 推荐模板，形成持续进化的策略库。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
传统持续学习以模型参数为学习对象，但现代 Agent 系统通过外部 harness（prompts, memories, tools, routing rules）决定行为。即使模型冻结，harness 更新也可能破坏先前可靠的行为——称为 harness-level forgetting。因此需要新范式：在冻结模型下持续更新 harness 并保留旧能力。

## 方法关键点
- 定义 HCL 状态为四个可编辑组件：**Task Interface**（任务解析）、**Experience Memory**（Raw + Abstract 两级记忆）、**Capability Map**（外部工具 + 内部技能）、**Adaptive Router**（检索与组合）。
- 采用 **guarded harness evolution**：分离更新生成与部署。**Continual Optimizer** 从交互反馈生成候选 harness；**Continual Evaluator** 检查三项——当前改进（验证集性能提升 ≥ δ）、历史保留（锚点集上损失 ≤ Bn）、有效性（语法/约束合规），全部通过才提交。
- 通过调节历史损失容差 Bn 显式控制稳定性-可塑性权衡：Bn=0 为 Stability-HCL，Bn=∞ 为 Plasticity-HCL。

## 关键结果
- ALFWorld 六任务流：Plasticity-HCL 最终平均成功率 62.98%，Stability-HCL 61.74%，显著优于 Static Harness (47.12%) 和 RAG (55.56%)。
- 文本推理四任务流（MuSiQue→ProofWriter→GSM8K→HotpotQA）：Plasticity-HCL 平均 64.70%，vs 零样本 45.50%，平均遗忘仅 0.07；Stability-HCL 平均遗忘为 0。
- 多模态四任务流（Detection→Caption→Grounding→VQAv2）：Stability-HCL 平均 68.92%，vs 零样本 39.40%，vs DGG 42.73%。
- 消融显示 Experience Memory 和 Task Interface 更新贡献最大。

**最值得记住的一句话**：将持续学习从参数空间转移到 harness 空间，通过提议-评估-提交的 guarded evolution 显式控制遗忘，为 Agent 持续改进提供了可工程化的框架。
