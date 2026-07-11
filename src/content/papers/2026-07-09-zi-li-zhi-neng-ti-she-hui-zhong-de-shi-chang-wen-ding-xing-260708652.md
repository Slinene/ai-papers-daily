---
title: 'Formal Mechanisms for Market Stability in Self-Interested Agent Societies:
  A Marketplace Simulation Study'
title_zh: 自利智能体社会中的市场稳定形式化机制：市场模拟研究
authors:
- Eugene Ng Yi Sheng
- Bingquan Shen
affiliations:
- DSO National Laboratories
- National University of Singapore
arxiv_id: '2607.08652'
url: https://arxiv.org/abs/2607.08652
pdf_url: https://arxiv.org/pdf/2607.08652
published: '2026-07-09'
collected: '2026-07-11'
category: Other
direction: 多智能体博弈 · 市场机制设计
tags:
- multi-agent
- market stability
- mediation
- adversarial robustness
- LLM agents
- social dilemma
one_liner: 在 LLM 驱动的市场仿真中，调解机制能有效抵御对抗攻击，维持多智能体合作稳定
practical_value: '- 电商平台存在大量自利卖家与买家 agent（如自动调价、自动选品），借鉴调解（Mediation）机制设计平台的治理层，在出现恶意行为时维持交易生态稳定。

  - 构造对抗性红队测试流程可用于压力测试推荐系统或 Agent 编排中的协调策略，用 LLM 驱动的攻击者迭代优化攻击 Prompt，发现系统软肋。

  - 将生产互补性与社交网络约束引入 Agent 市场模拟，可建模推荐生态中的双边匹配与信息传播，用于模拟 UGC 社区、直播带货等场景的协同演化。

  - 面临不可完全消除恶意行为时，系统设计应追求“可弯不可折”（bent but not broken）的弹性目标：允许局部效用下降，但保持整体不崩溃的恢复能力。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：自利智能体在重复社会困境中常因个体理性而背叛，导致合作崩溃。若不加干预，多智能体市场将陷入相互剥削。该研究追问：在无限制通信之上叠加何种形式化机制，足以让自利智能体社会维持市场稳定？以及这些机制对对抗性攻击有多强的韧性？

**方法**：构建包含 18 个 LLM 智能体（DeepSeek-V3）的市场仿真，各智能体具有互补生产专长，必须在受限社交网络内交易以获取效用。实验分两阶段：(1) 在逐渐注入恶意智能体（troll）的 200 轮中对比八种监管条件，发现调解（Mediation）机制表现最优；(2) 在此基础上，用迭代 Prompt 优化的 LLM 驱动恶意智能体对调解机制进行红队攻击，测试其稳健性。

**关键结果**：最优攻击（v6 版）仅使诚实智能体效用降低 13.3%，未能导致市场崩溃；调解机制即使面对持续对抗压力也能恢复合作。将对抗稳健性定义为机制在优化攻击下仍能维持诚实智能体正向效用的能力，验证调解可被弯曲但无法被折断。
