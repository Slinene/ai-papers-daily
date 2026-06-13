---
title: 'From Passive Generation to Investigation: A Proactive Scientific Peer Review
  Agent'
title_zh: 从被动生成到主动调查：一种主动式科学同行评审智能体
authors:
- Haishuo Fang
- Yue Feng
- Iryna Gurevych
affiliations:
- Ubiquitous Knowledge Processing Lab (UKP Lab), Technical University of Darmstadt
- National Research Center for Applied Cybersecurity ATHENE, Germany
- School of Computer Science, University of Birmingham
arxiv_id: '2606.13349'
url: https://arxiv.org/abs/2606.13349
pdf_url: https://arxiv.org/pdf/2606.13349
published: '2026-06-11'
collected: '2026-06-13'
category: Agent
direction: 主动式评审Agent · 结构化日志引导
tags:
- Peer Review
- Reinforcement Learning
- Large Language Model
- Proactive Investigation
- MDP
one_liner: 将论文评审建模为MDP，用结构化日志引导LLM主动调查疑点，8B模型性能超越大模型prompt方法39%
practical_value: '- **主动调查机制可复用至客服/推荐Agent**：将多步信息收集建模为MDP，Agent可自主决定何时查询知识库、调用工具或请求用户反馈，结构化日志作为工作区记录证据与假设，提升信息获取的针对性和深度。

  - **结构化日志是轻量级记忆增强方案**：类似Scratchpad或流式笔记，在Agent内部维护一个不断更新的JSON或键值结构，用于追踪状态、中间发现和待验证项，可有效避免长上下文遗忘，在电商导购中实现多轮推理和偏好追踪。

  - **RL优化Agent调查策略有直接迁移潜力**：利用RL对“调查”动作（如查看详情、对比商品、查看评论）进行奖励驱动优化，使Agent学会在何时做何种调查以最大化下游任务收益，适用于电商比价、商品推荐等需主动探索的场景。

  - **小模型+SFT+RL可超越大模型Prompt**：对于特定垂直领域的Agent任务（如客服、合规检查），用8B模型经监督微调加RL训练，可在成本敏感的生产环境中替代闭源大模型的Prompt工程，获得更高性价比。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有LLM评审系统被动生成评论，缺乏像人类评审员那样主动调查论文可疑点的能力，导致评论缺乏具体证据支撑。**方法**：将主动调查过程形式化为马尔可夫决策过程（MDP），提出ProReviewer智能体。核心是一个持续更新的**结构化评审日志**，作为工作区记录已收集的证据和中间发现，指导智能体在何处进行下一步调查（如检查实验部分验证某声明）。智能体基于8B基座，先经监督微调（SFT）获得基本评审行为，再通过强化学习（RL）优化调查策略，以提升评审质量。**结果**：在五个评审质量维度上，ProReviewer平均得分最高，相比更大的前沿LLM的prompt方法提升达39%，相比最强微调基线提升16%；人工评估中赢得最高胜率，证明了小模型结合主动调查和RL优化的有效性。
