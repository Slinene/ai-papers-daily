---
title: 'Cognitive Extensions for Dual-Process Language Agents: Memory and Self-Reflection
  in Interactive Environments'
title_zh: 双过程语言智能体的认知扩展：交互环境中的记忆与自我反思
authors:
- João Meneses dos Santos
- Arlindo L. Oliveira
affiliations:
- Instituto Superior Técnico, Universidade de Lisboa, Portugal
- INESC-ID, Lisboa, Portugal
arxiv_id: '2609.19128'
url: https://arxiv.org/abs/2609.19128
pdf_url: https://arxiv.org/pdf/2609.19128
published: '2026-09-16'
collected: '2026-09-17'
category: Agent
direction: Agent 执行控制与记忆增强
tags:
- Language Agent
- Dual-Process
- Memory Module
- Self-Reflection
- ScienceWorld
- LLM
one_liner: 为 SwiftSage 双过程 agent 加入自适应记忆与自我反思模块，在 ScienceWorld 上提升任务成功率与效率
practical_value: '- 在电商/推荐 Agent 中加入轻量执行时校验（SRM 思路）：调用工具前检查商品 ID、参数格式、API 返回，拦截无效动作，降低错误率与
  token 成本。

  - 长会话推荐系统可借鉴显著性门控记忆：只存储用户偏好突变、任务失败原因等关键事件，触发式检索而非全量上下文，避免长对话遗忘与上下文膨胀。

  - 双过程架构可解耦推理与响应：快速动作提议器即时回复用户，慢规划器异步优化推荐策略或营销动作，兼顾体验与决策质量。

  - 增加无进展检测：当推荐 Agent 重复推荐或反复询问时强制执行反思/切换策略，防止陷入无效循环，提升多轮交互成功率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

动机：LLM agent 在交互环境中脆弱，常因长程状态跟踪、动作有效性、失败恢复不足而失效；失败多发生在执行时而非规划阶段，仅靠扩大提示难以解决。

方法：扩展 SwiftSage 双过程架构（快速动作提议器 + 慢规划器），加入两个模块：Adaptive Memory Module (AMM) 负责显著性门控的情景存储与触发式检索；Self-Reflection Module (SRM) 进行有限执行时验证与纠正干预。两模块以 feature-flag 形式嵌入同一执行基底，支持受控消融。

结果：在 ScienceWorld 四组配置中，完整系统取得最佳：平均最终得分 64.62，成功率 43.17%，成功步骤效率 19.33 步；SRM 单独贡献最强，表明执行时控制是主导瓶颈，AMM 在运行循环稳定后价值更明显。
