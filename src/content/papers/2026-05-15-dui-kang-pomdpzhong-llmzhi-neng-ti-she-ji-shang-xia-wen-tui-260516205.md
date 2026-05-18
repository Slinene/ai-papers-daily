---
title: 'Context, Reasoning, and Hierarchy: A Cost-Performance Study of Compound LLM
  Agent Design in an Adversarial POMDP'
title_zh: 对抗POMDP中LLM智能体设计：上下文、推理与层次结构的成本效益研究
authors:
- Igor Bogdanov
- Chung-Horng Lung
- Thomas Kunz
- Jie Gao
- Adrian Taylor
- Marzia Zaman
affiliations:
- Carleton University
- Defence R&D Canada
- Cistel Technology
arxiv_id: '2605.16205'
url: https://arxiv.org/abs/2605.16205
pdf_url: https://arxiv.org/pdf/2605.16205
published: '2026-05-15'
collected: '2026-05-18'
category: Agent
direction: LLM Agent 架构设计：上下文工程与层次分解优于深度推理
tags:
- LLM Agent
- POMDP
- Hierarchical Decomposition
- Deliberation Cascade
- Context Engineering
- Cost-Effectiveness
one_liner: 在对抗性部分可观察环境中，程序化状态抽象与无推理工具的层次分解性能最佳，推理跨层次分布导致性能级联下降。
practical_value: '- 在构建推荐或电商Agent时，优先实现**程序化状态跟踪层**（如用户行为序列压缩、环境状态摘要），而非将原始日志直接输入LLM。论文表明状态抽象比原始观察提升76%平均回报且成本效益高。

  - 对于多Agent系统，采用**层次化分解**（主Agent协调多个专业化子Agent），但避免在每个子Agent中嵌入复杂的自我反思工具，否则可能引发“推理级联”，导致性能显著下降和令牌成本激增。

  - 成本优化时，**上下文工程**（特征提取、状态压缩）的性价比通常高于增加推理步骤（如CoT、自我批评），尤其在高吞吐量在线推理场景。

  - 将推理工具集中在顶层协调器而非分发给底层执行器，以保持系统稳定性和效率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：复合LLM智能体在对抗性、部分可观察顺序环境中的设计涉及上下文表示、推理机制和任务分解，但缺乏成本与性能权衡的实证指导。

**方法**：在CybORG CAGE-2 POMDP环境中，对5个模型家族、6个模型进行12种配置的3475次实验，控制上下文（原始观察 vs 程序化状态跟踪与压缩历史）、推理（自我提问/批评/改进工具，可选CoT）和层次结构（单体ReAct vs 层次分解），采用令牌级成本核算。

**关键结果**：程序化状态抽象使每令牌回报最高，平均回报提升最高76%；将推理工具分布到层次子代理中导致性能显著下降（平均回报恶化最高3.4倍，令牌消耗增加1.8-2.7倍），形成“推理级联”；层次分解无推理工具时性能最佳，上下文工程比深度推理更具成本效益。结论：在结构化对抗POMDP中，应优先投资程序化基础设施和清晰的任务分解，而非深度单代理推理。
