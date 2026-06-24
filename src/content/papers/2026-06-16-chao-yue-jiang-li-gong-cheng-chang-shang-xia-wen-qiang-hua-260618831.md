---
title: 'Beyond Reward Engineering: A Data Recipe for Long-Context Reinforcement Learning'
title_zh: 超越奖励工程：长上下文强化学习的数据配方
authors:
- Xiaoyue Xu
- Sikui Zhang
- Xiaorong Wang
- Xu Han
- Chaojun Xiao
affiliations:
- OpenBMB
- Tsinghua University
arxiv_id: '2606.18831'
url: https://arxiv.org/abs/2606.18831
pdf_url: https://arxiv.org/pdf/2606.18831
published: '2026-06-16'
collected: '2026-06-24'
category: Training
direction: 长上下文强化学习数据配方
tags:
- long-context
- reinforcement-learning
- GRPO
- data-centric
- agent
one_liner: 以简单的数据配方替代复杂奖励工程，仅用结果奖励GRPO即可大幅提升长上下文推理及Agent任务表现
practical_value: '- 构建面向长文档的推荐/搜索Agent时，可借鉴**检索、多证据合成、推理三类混合数据配方**，提升模型在冗长轨迹中定位、整合关键信息的能力。

  - 仅使用**outcome-based GRPO**，无需复杂奖励工程，工程实现轻量、易迁移，适合业务线快速试错。

  - 14K的小规模高质量数据即可带来显著收益，在业务数据稀缺时尤其有参考价值。

  - 可将该数据范式迁移到**多轮对话推荐、长序列用户行为分析**等Agent任务中，微调模型的长上下文推理能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文推理是LLM作为自主Agent的核心能力，现有RL工作重奖励工程、轻训练数据，导致数据多样性不足。

**方法**：从数据中心视角出发，提出一个**混合三类任务的数据配方**——检索（retrieval）、多证据综合（multi-evidence synthesis）、推理（reasoning），共构造8个数据集约14K样本。训练采用**极简的outcome-based GRPO**，只根据最终答案是否正确给予奖励，无需中间过程监督或复杂奖励函数。

**关键结果**：
- 在Qwen3-4B/8B/30B-A3B上，7个长上下文基准平均提升**+7.2/+3.2/+6.4点**，超越先前RL训练集会。
- 在Agent任务上，以agent-tuned模型为基础继续用该数据配方进行RL训练，GAIA提升**+4.8点**，BrowseComp提升**+7.0点**。

结论：一个精心设计的小规模数据配方，配合最简单的效果奖励，即可在长上下文推理和Agent任务上取得显著且可迁移的增益。
