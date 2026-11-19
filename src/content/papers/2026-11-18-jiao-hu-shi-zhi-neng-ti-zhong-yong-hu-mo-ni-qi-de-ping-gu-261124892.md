---
title: On Evaluating User Simulators for Interactive Agents
title_zh: 交互式智能体中用户模拟器的评估研究
authors:
- Hengguang Zhou
- I-Hung Hsu
- Li Chen
- Priyanshi Shrivastava
- Anastasios Angelopoulos
- Wei-Lin Chiang
- Ion Stoica
- Cho-Jui Hsieh
affiliations:
- UCLA
- Arena
arxiv_id: '2611.24892'
url: https://arxiv.org/abs/2611.24892
pdf_url: https://arxiv.org/pdf/2611.24892
published: '2026-11-18'
collected: '2026-11-19'
category: Eval
direction: 用户模拟器元评估与保真度度量
tags:
- User Simulator
- Meta-evaluation
- Interactive Agents
- Fidelity
- Fault Injection
- LLM Agents
one_liner: 通过故障注入揭示现有用户模拟器评估指标存在盲区，提出群体级与轨迹级保真度评估套件
practical_value: '- 构建对话式推荐/客服 agent 的用户模拟器时，不要只依赖整体相似度或效用分，应主动注入已知失败模式（目标漂移、约束遗漏、过早结束、接受坏结果）做故障注入测试，检验指标能否捕获。

  - 将用户模拟器保真度拆成 population-level（群体交互模式）和 trace-level（个体目标、约束、persona），分别度量；尤其在多轮推荐对话中，要检查模拟用户是否坚持原始需求而非被
  agent 带偏。

  - 若用用户模拟器评测 agent，必须先验证模拟器本身对真实用户的还原度，否则可能得到误导性结论——文中发现某些模拟器甚至偏好接受破损工作的异常群体。

  - 可复用其扰动方法：收集少量真实多轮会话，构造带故意失败的评估集，用于定期回归测试模拟器质量，避免线上效果与离线评测背离。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：用户模拟器为交互式 agent 提供了可扩展的离线评估方式，但如何评估模拟器本身的质量研究不足，现有评估框架能否可靠检测模拟用户行为中的关键失败尚不清楚。

**方法关键点**：论文对评估指标本身做元评估：故意扰动模拟重放，引入目标改变、遗漏约束、过早停止、接受破损工作等 10 类失败，检验指标是否惩罚。发现先前三种方法仅检测到 5-6 个扰动，联合分数甚至偏好被指示接受破损工作的异常群体。基于此提出新评估套件，结合模拟器评估 agent 的效用与两类真实用户保真度：population-level 保真度评估集体交互模式，trace-level 保真度评估个体用户的目标、约束与 persona 保持。

**关键结果数字**：新套件在相同检测标准下识别出全部 10 类扰动。在 351 个真实多轮会话（348 名用户、23 种语言，任务覆盖全栈 web 应用、游戏、设计资产、自动化工作流）上评估 6 个用户模拟器，发现 population-level 度量可能漏掉错误目标、约束忽略或行为偏离角色，证明需要从多粒度综合评估模拟器保真度。
