---
title: Reinforcement Learning Elicits Contextual Learning of Unseen Language Translation
title_zh: 基于强化学习的上下文语言学习实现未见过语言翻译
authors:
- Hanxu Hu
- Zdeněk Šnajdr
- Pinzhen Chen
- Jannis Vamvas
- Rico Sennrich
affiliations:
- University of Zurich
- ETH Zurich
- Queen’s University Belfast
arxiv_id: '2606.06428'
url: https://arxiv.org/abs/2606.06428
pdf_url: https://arxiv.org/pdf/2606.06428
published: '2026-06-03'
collected: '2026-06-05'
category: Other
direction: 语言翻译 · 低资源强化学习
tags:
- reinforcement learning
- low-resource translation
- in-context learning
- meta-learning
- chrF reward
- LLM
one_liner: 用轻量翻译指标做奖励，RL训练LLM学会从上下文中提取语言知识，泛化到全新语言。
practical_value: '- **弱奖励信号的RL优化**：使用chrF这类粗糙指标也能有效驱动LLM学习复杂技能，类似地，在电商场景中可以直接用点击率、转化率等业务指标作为奖励，对推荐Agent进行RL策略优化，即使没有精细标注。

  - **上下文利用的元学习**：RL训练让模型掌握“从上下文快速学习语言”的元能力，这可以迁移到推荐场景——让Agent学会根据少量用户行为或商品描述在上下文中即时调整策略，而不是死记硬背历史数据。

  - **低资源泛化**：在冷启动物品或小众品类推荐中，可借鉴该方法，用少量示例作为上下文，通过RL强化模型对结构化信息的提取与利用，降低对大量标注数据的依赖。

  - **训练范式选择**：与监督微调相比，RL避免了对特定领域数据的过拟合，提升了零样本迁移能力，这对需要快速适应新业务场景的电商Agent有参考价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM翻译低资源语言的方法（继续训练或内联语法书）容易过拟合特定语言，零样本迁移能力差。要大规模翻译极度低资源语言，LLM需要掌握利用上下文语言知识的元技能，而非简单记忆。

**方法**：将未见过语言翻译建模为上下文学习任务，提供一个包含目标语言语法书等丰富语言信息的提示。使用轻量级表面翻译指标chrF作为奖励，通过强化学习（RL）训练LLM，让模型从上下文中提取并应用相关语言规则。

**关键结果**：在完全未见过的语言上，RL训练模型的翻译质量显著优于上下文学习基线（平均+3.4 chrF）和监督微调（平均+1.6 chrF）。分析表明，基于结果的RL不仅适用于数学、编程等推理任务，也能有效促进从上下文中学习语言，模型学会了忽略不相关上下文并关注关键语言特征。
