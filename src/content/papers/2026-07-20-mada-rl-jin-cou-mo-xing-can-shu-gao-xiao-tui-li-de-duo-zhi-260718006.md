---
title: 'MADA-RL: Multi-Agent Debate-Aware Reinforcement Learning for Parameter-Efficient
  Reasoning in Compact Models'
title_zh: MADA-RL：紧凑模型参数高效推理的多智体辩论强化学习
authors:
- Martino M. L. Pulici
- Cuong Xuan Chu
- Evgeny Kharlamov
- Zifeng Ding
- Volker Tresp
- Yunpu Ma
affiliations:
- Bosch Center for Artificial Intelligence, Germany
- LMU Munich, Germany
- University of Oslo, Norway
- University of Cambridge, United Kingdom
- Munich Center for Machine Learning, Germany
arxiv_id: '2607.18006'
url: https://arxiv.org/abs/2607.18006
pdf_url: https://arxiv.org/pdf/2607.18006
published: '2026-07-20'
collected: '2026-07-21'
category: MultiAgent
direction: 多智体辩论强化学习 · 参数高效微调
tags:
- Multi-Agent
- Reinforcement Learning
- LoRA
- Reasoning
- Compact Models
- Counterfactual Advantage
one_liner: 通过辩论感知RL训练紧凑模型作为生成器和评论家，利用反事实优势函数让评论家超越生成器共识，参数效率提升16倍
practical_value: '- 多智体辩论可迁移至搜索推荐：让多个生成器提出 query 或推荐理由，评论家评估并修正，RL 优化评论家识别生成器错误，提升整体质量。

  - 参数高效微调：只用 LoRA 适配器微调小部分参数，适合业务中受限的算力 budget，可快速迭代。

  - 反事实优势函数设计：奖励评论家超越生成器共识的改进，而非简单模仿，可借鉴用于推荐系统的多模型融合或排序打分修正，避免平庸共识。

  - 轻量多轮部署协议：训练好的角色可在推理中组合辩论，作为后处理或过滤模块，直接嵌入现有推荐管道。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：紧凑模型（≤4B）推理能力提升训练成本高，需要高效的后训练方法，能在有限预算下缩小与大规模模型的差距。

**方法关键点**：提出 MADA-RL，将紧凑模型拆分为生成器和评论家角色，仅用 LoRA 微调少量参数。核心是**反事实评论家优势函数**：将评论家的优势定义为自身奖励减去生成器集成在实例上的准确率，从而激励评论家改进生成器共识，而不是简单重复正确答案。训练时通过辩论感知的 RL 信号优化角色。部署时采用轻量多轮辩论协议：生成器提出答案，评论家判断并修正，多轮交互提升最终输出。

**结果**：在五个数学推理基准上，DeepSeek-R1-Distill-Qwen-1.5B 准确率从 39.9% 提升至 41.9%（+2.0 点），可训练参数量仅是全量微调基线的 1/16，位于准确率-参数量帕累托前沿。消融实验表明，反事实优势函数带来最高的评论家改进率，确认其效果。
