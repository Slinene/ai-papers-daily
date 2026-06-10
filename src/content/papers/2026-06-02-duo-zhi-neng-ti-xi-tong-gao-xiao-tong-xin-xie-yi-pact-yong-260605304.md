---
title: What Should Agents Say? Action-state Communication for Efficient Multi-Agent
  Systems
title_zh: 多智能体系统高效通信协议 PACT：用行动-状态记录替代自由文本
authors:
- Chen Huang
- Yuhao Wu
- Wenxuan Zhang
affiliations:
- Singapore University of Technology and Design
arxiv_id: '2606.05304'
url: https://arxiv.org/abs/2606.05304
pdf_url: https://arxiv.org/pdf/2606.05304
published: '2026-06-02'
collected: '2026-06-10'
category: MultiAgent
direction: Agent · 多智体通信协议优化
tags:
- Multi-Agent Systems
- Communication Protocol
- Token Efficiency
- Action-State
- PACT
one_liner: 提出 PACT 协议，将智能体间消息压缩为行动-状态-结果三字段，在保持性能的同时大幅减少 token 消耗
practical_value: '- 在电商推荐的多智能体协作（如 query 改写、策略规划）中，可将智能体间通信设计为“行动-状态-结果”三字段，去除冗余推理，降低上下文长度和
  API 成本。

  - PACT 作为推理时协议，无需更改模型或训练，可直接通过代理钩子集成到现有 Agent 框架（如 LangChain、AutoGen），实现紧凑通信。

  - 对于使用推理模型的 Agent 系统，解耦私有计算与公共通信可以避免将冗长的推理 trace 反复暴露给下游，缓解上下文窗口耗尽风险。

  - 在长上下文任务（如代码生成、对话规划）中，仅传递结构化关键信息能显著减少输入 token，提升解析率，在 SWE-agent 上每解析 token 降低 47%。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
多智能体系统（MAS）中，智能体间通常采用自由形式的自然语言通信，导致 token 消耗爆发式增长、上下文窗口快速耗尽，影响任务性能与推理成本。尤其当推理模型将长思考链转发给下游时，冗余内容会反复被重新处理。现有工作多关注角色与调度，却忽视通信内容本身的设计。本文诊断五种常见通信策略，发现没有单一策略普适，但有效消息始终保留以行动为中心的信息，从而提出一种结构化通信协议。

### 方法关键点
- **通信策略诊断**：在分割证据交互和顺序流水线两种 MAS 设置中，测试完整输出、简洁生成、仅结论、简短摘要、仅制品五种策略，发现制品携带关键任务信息但缺乏行动与状态，导致效率低下。
- **PACT 协议**：将智能体间通信视为公共状态更新问题，要求每个非最终智能体的输出被投影为紧凑的公共消息，仅包含三个字段：**ACTION**（已采取或待执行的动作）、**STATE**（支撑动作的证据或环境反馈）、**RESULT**（动作的产出物）。该投影在发送端进行，禁止中间推理过程进入共享历史。
- **协议属性**：PACT 不限制智能体内部计算，只约束公共通信，实现私有计算与公共状态更新的解耦；协议与具体 MAS 拓扑、角色分配无关，可作为推理时通用干预。

### 关键实验结果
- **MAS 实验**：在两种设置、Qwen3‑8B/14B/32B 模型上，PACT 相比 CoA、TextMAS、Multi‑Agent Debate 等基线，平均减少 token 使用量 38.7%，同时 F1 或准确率持平或提升。例如在 HotpotQA 分割证据交互上，8B 模型 F1 69.9（Token 6,704），优于完整输出的 13,520 Token；在 AIME 流水线上，32B 模型 Tok 减少 20% 以上。
- **真实编码工具**：在 SWE‑bench Verified 上，OpenHands 的解析率从 19.4% 升至 23.0%，每解析 token 降低 10.3%；SWE‑agent 输入 token 减少 50.4%，每解析 token 从 2.46M 降至 1.30M（−47%）。
- **消融实验**：去除 ACTION 或 STATE 字段导致 F1 下降 5 点以上，仅保留 RESULT 性能最低且 token 增加 12.9%，验证三字段的必要性。
