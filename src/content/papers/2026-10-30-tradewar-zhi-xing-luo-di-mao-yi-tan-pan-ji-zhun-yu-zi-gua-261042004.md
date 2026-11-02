---
title: 'TradeWar: A Benchmark for Execution-Grounded Trade Negotiation with Adaptive
  LLM Agents'
title_zh: TradeWar：执行落地贸易谈判基准与自适应 LLM Agent
authors:
- Xiangyu Kong
- Ruirui Yang
- Xia Hou
affiliations:
- College of Computer Science, Beijing Information Science and Technology University
arxiv_id: '2610.42004'
url: https://arxiv.org/abs/2610.42004
pdf_url: https://arxiv.org/pdf/2610.42004
published: '2026-10-30'
collected: '2026-11-02'
category: MultiAgent
direction: LLM 多智能体自适应谈判与执行反馈
tags:
- LLM Agents
- Multi-Agent Negotiation
- Execution-Grounded
- Benchmark
- Adaptive Strategy
- Theory of Mind
one_liner: 提出执行导向的多国贸易谈判基准 TradeWar 和自适应智能体 TACTIC，用结算结果驱动跨轮策略优化
practical_value: '- 谈判类 Agent 不能只看 agreement rate：业务上应定义“执行后收益”指标（如 EHI），把对话策略与最终结算、履约结果绑定，避免高成交低价值。电商价格谈判、广告位协商、供应链协同都能复用。

  - TACTIC 不更新 LLM 权重，靠跨 episode 经验、对手建模和结算反馈形成策略迭代闭环。工程上可用外部 memory / replay buffer
  沉淀历史会话与成交结果，在 prompt 中注入 refined strategy，成本低且可控。

  - 交互记忆 + CoT 并不足够应对延迟执行反馈；推荐系统中曝光→点击→转化同样是延迟反馈，建议把多轮交互后的实际结果作为显式状态纳入策略更新，而不是只积累对话文本。

  - 论文通过 technology-controls 和 energy-crisis 冲击测试鲁棒性，说明构建环境模拟器并加入外部 shock 训练，能提升 Agent
  面对政策、流量或供给突变的韧性，适合电商大促、广告库存异常等场景。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有多轮谈判基准主要评估 agreement rate，忽略了谈判承诺执行后是否真正创造价值。为了弥补这一空缺，论文提出 TradeWar，一个多国仿真基准，将谈判对话转化为具体关税与贸易份额政策，结算时强制容量与网络约束，并用 Economic Health Index (EHI) 评估执行后经济收益。

**方法关键点**：针对执行落地任务，论文提出 TACTIC，一种面向国际贸易的 trade-aware 自适应整合与 theory-of-mind agent。它不更新基础 LLM 权重，而是跨 episode 利用先前经验、对手行为和过去结算结果迭代优化谈判策略。对比方法包括零样本 CoT 的 PromptLLM 和带交互记忆的 MemoryLLM。

**关键结果数字**：PromptLLM 虽然达到 75% 的 agreement rate，但最终 EHI 只有 57.1（×100），而 TACTIC 达到 68.8。在 20 个连续 episode 和 3 个随机种子上，TACTIC 的 EHI 从 58.2 提升到 73.2，相比之下没有跨 episode 更新的消融版本只有 65.2。在技术封锁和能源危机冲击下，TACTIC 的性能下降也小于 PromptLLM 和 MemoryLLM。结果表明，仅靠 CoT 推理和交互记忆不足以解决延迟执行反馈，而基于结算结果的适应性优化能显著改善长程谈判表现。
