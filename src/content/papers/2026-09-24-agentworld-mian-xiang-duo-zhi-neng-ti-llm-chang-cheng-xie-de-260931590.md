---
title: 'AgentWorld: Benchmarking Long-Horizon Collaboration of Multi-agent LLMs'
title_zh: AgentWorld：面向多智能体 LLM 长程协作的基准评估
authors:
- Raphael Shu
- Yusen Zhang
- Young Min Cho
- Jin Mo Yang
- Yuan Yuan
- Wenliang Zheng
- Sharath Chandra Guntuku
- Lyle Ungar
- Zhou Yu
- Rui Zhang
affiliations:
- OpenAgents
- Columbia University
- University of Pennsylvania
- Seoul National University
- Penn State University
arxiv_id: '2609.31590'
url: https://arxiv.org/abs/2609.31590
pdf_url: https://arxiv.org/pdf/2609.31590
published: '2026-09-24'
collected: '2026-09-28'
category: MultiAgent
direction: 多智能体长程协作评测基准
tags:
- Multi-Agent
- Benchmark
- Long-Horizon
- Collaboration
- LLM
- CCE
one_liner: 提出AgentWorld长程多智能体协作基准与CCE因果协作指标，最佳模型任务成功率仅52.0%
practical_value: '- 多智能体业务链路（如营销活动生成、选品+文案+投放协作）不要只靠聊天历史维持长程计划；应引入显式共享计划/看板/JSON 状态，每轮或每阶段强制更新，否则
  50+ 轮后计划会漂移。

  - 评估智能体流水线时引入 CCE 式因果追踪：记录各 agent 的 action 及其依赖关系，区分对最终结果有因果贡献的步骤和“忙忙碌碌但无效”的动作；可用于优化
  planner-retriever-ranker/推荐解释链路中的资源分配。

  - 在角色非对称的多 agent 系统中，角色混淆是主要失败源；通过 role-specific system prompt、独立工具权限和结构化输出约束来减少越权/重复劳动。

  - 长时任务需要 memory 管理：对共享状态做定期摘要或 checkpoint，并在关键节点触发 re-plan；否则 LLM 在长上下文/多轮中容易丢失早期目标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有多智能体基准多集中在竞争、<20 步短程，或只聚合个体能力，无法单独衡量 LLM 智能体的真实协作能力。

**方法**：AgentWorld 提供 100 个人工标注任务及 100 个增强变体，构建 MMORPG 沙盒，任务需 50+ 轮交互、3-20 个角色/能力非对称的智能体，在 blackbox 设定下只能通过消息通信、联合规划与资源共享；除二元成功率外，提出 CCE（Causal Collaboration Effectiveness）图指标，追踪动作间因果依赖，量化团队努力中真正贡献结果的比例。

**结果**：在 Gemini 3 Flash、Claude Haiku 4.5、GPT-5 Mini、DeepSeek R1-70B 上，最佳模型任务成功率仅 52.0%，主要失败模式包括通信中断、角色混淆、无法在长程中维持共享计划。基准已开源。
