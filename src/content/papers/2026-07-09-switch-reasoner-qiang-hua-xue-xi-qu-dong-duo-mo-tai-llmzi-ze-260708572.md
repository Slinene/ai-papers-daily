---
title: 'Switch-Reasoner: Learn When to Think in Multitask Mixtures via Reinforcement
  Learning'
title_zh: Switch-Reasoner：强化学习驱动多模态LLM自适应选择推理模式
authors:
- Yiyang Fang
- Pei Fu
- Jinjie Li
- Jian Liang
- Wenke Huang
- Ruijie Luo
- Shaojie Zhang
- Jian Luan
- Yi R. Fung
- Mang Ye
affiliations:
- Wuhan University
- Xiaomi Inc
- Wuhan University of Technology
- Nanyang Technological University
- The Hong Kong University of Science and Technology
arxiv_id: '2607.08572'
url: https://arxiv.org/abs/2607.08572
pdf_url: https://arxiv.org/pdf/2607.08572
published: '2026-07-09'
collected: '2026-07-10'
category: Reasoning
direction: 自适应推理模式选择 · 强化学习
tags:
- MLLM
- GRPO
- Adaptive Reasoning
- Reinforcement Learning
- Efficiency
- Regularization
one_liner: 通过GRPO与双层正则化，让多模态LLM学会何时直接回答、何时显式推理，在异构任务中兼顾精度与效率
practical_value: "- **Agent 自适应开销控制**：在搜索推荐 Agent 中，对简单用户意图直接调用推荐 API，复杂意图才触发链式推理，降低\
  \ Token 与延迟成本。  \n- **RL 训练稳定性借鉴**：双级正则（全局模式占比约束 + 样本级收益监督）可防止策略坍缩为“始终详细解释”或“始终简单回复”，适用于对话推荐策略的\
  \ RL 微调。  \n- **虚拟工具抽象**：将“思考”视为工具调用，可与现有的检索、推荐、排序等工具统一管理，便于在 Agent 框架中插拔式扩展推理能力。\
  \  \n- **推理效率优化**：在多任务推荐系统（如商品描述生成、问答推荐）中，可训练模型判断问题难度，仅对必要样本进行深层推理，显著节省推理算力。"
score: 7
source: arxiv-cs.CV
depth: abstract
---

**动机**：现有多模态 LLM 固定“先思考再回答”范式，面对简单图片问答、场景理解等异构任务时大量浪费推理算力，且 RL 训练中采样不平衡易使模型退化为“总是不思考”或“总是思考”。

**方法**：提出 Switch-Reasoner，基于 GRPO 将推理行为建模为虚拟工具调用。模型对每个样本选择**直接回答**或**显式思考后回答**。为稳定该决策，设计双层正则：① 整体层，通过 KL 惩罚平衡两种模式的使用频率；② 样本层，根据“思考带来的收益”提供细粒度监督，鼓励对高收益样本思考、对低收益样本直接作答。适配 GRPO 组内比较优势，实现端到端训练。

**结果**：在 11 个多模态任务上，Switch-Reasoner 在精度持平的前提下显著减少不必要的推理步骤，获得更优的准确率‑效率前沿曲线，消融实验验证了双层正则对训练稳定性的关键作用。
