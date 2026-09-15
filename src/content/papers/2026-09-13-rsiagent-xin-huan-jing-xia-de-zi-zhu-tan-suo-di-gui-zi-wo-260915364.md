---
title: 'RSIAgent: Autonomous Exploration for Recursive Self-improvement in New Environments'
title_zh: RSIAgent：新环境下的自主探索递归自我改进
authors:
- Sibo Zhu
- Shicheng Fan
- Xinyue Wang
- Wenyi Wu
- Kun Zhou
- Biwei Huang
affiliations:
- Aether AI
- University of California San Diego
- University of Illinois Chicago
arxiv_id: '2609.15364'
url: https://arxiv.org/abs/2609.15364
pdf_url: https://arxiv.org/pdf/2609.15364
published: '2026-09-13'
collected: '2026-09-15'
category: MultiAgent
direction: 多智能体自主探索与递归自我改进
tags:
- Recursive Self-Improvement
- Multi-Agent
- Digital Agents
- Memory Construction
- Code-as-Policy
one_liner: 训练无关多智能体框架，通过 broad-then-deep 探索构建可复用记忆，让开源模型在 OSWorld/ALE 超越 GPT-6
practical_value: '- 多智能体解耦探索与验证：在电商/广告 agent 中可将任务生成、执行、验证三个角色分离，verifier 独立于 actor
  的私有记忆，降低相关错误；尤其适合新平台/新活动页面的自动适配。

  - broad-then-deep 探索策略：先并行跑广泛任务覆盖环境结构和常见操作，再针对高失败率/边界 case 做深度挖掘，可迁移到电商 RPA 或 GUI
  agent 的冷启动记忆构建。

  - 记忆冻结与经验所属学习：每个 actor 对自身经验做蒸馏与冲突消解，再串行合并，避免并发写入冲突；记忆以无 schema 文件形式存储，工程实现简单且易复用。

  - 用 code-as-policy 统一动作接口：在电商自动化中，用 Python/Bash 脚本操作后台或工具，比逐步 GUI 点击更稳定、易修正，且方便沉淀可复用流程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
数字 agent 常需在新环境中操作，接口、工具与失败模式未完全被预训练模型覆盖。现有自适应方法多依赖额外交互数据+人类辅助训练，成本高且难以用于私有或持续变化的环境。训练无关的上下文管理更灵活，但仅记忆成功轨迹不够，需从环境反馈中提炼可复用的因果结构。

**方法关键点**
- 多智能体 harness：curriculum agent 生成探索任务，actor agent 以 code-as-policy 执行并维护可演进记忆，verifier agent 独立依据环境反馈给出 PASS/FAIL 与诊断，三者信息边界隔离。
- 两阶段探索：Broad Recursive Self-exploration (BRS) 并行探索多样方向，快速覆盖环境结构与过程；Deep Recursive Self-exploration (DRS) 顺序聚焦 hard cases、隐藏约束与边界条件，逐步深化记忆。
- 记忆管理：仅 actor 拥有记忆写入权，蒸馏经验并进行冲突消解；并行波次中共享快照、串行合并更新。探索结束后记忆冻结，直接复用于下游任务，不更新模型参数。

**关键实验**
在 OSWorld 2.0 (0808 offline, 82 tasks) 和 Agents' Last Exam (Near-term, 67 tasks) 上，RSIAgent 使用 GLM-5.3 为 actor、Kimi-K3 为 verifier/curriculum，将 OSWorld partial score 从 71.97 提升到 78.98，ALE partial 从 83.75 提升到 84.82，超过 GPT-6 Astra 等闭源模型。消融显示 full RSI 在四个任务上平均 74.54%，优于仅 BRS (65.52%) 或仅 DRS (56.50%)。在 GameCraft-Bench 40 个游戏生成任务上，RSIAgent 一致提升质量且不损坏强基线。失败模式分析指出探索不够针对性、验证不完整、记忆不可靠是主要限制。

**最值得记住的一句话**
训练无关的递归自我改进，通过多智能体分工与 broad-then-deep 自主探索构建可复用因果记忆，能让开源 agent 在新环境中超越前沿闭源模型。
