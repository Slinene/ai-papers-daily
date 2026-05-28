---
title: 'CORE: Contrastive Reflection Enables Rapid Improvements in Reasoning'
title_zh: CORE：对比反思实现推理快速改进
authors:
- Linas Nasvytis
- Simon Jerome Han
- Ben Prystawski
- Satchel Grant
- Noah D. Goodman
- Judith E. Fan
affiliations:
- Stanford University
arxiv_id: '2605.28742'
url: https://arxiv.org/abs/2605.28742
pdf_url: https://arxiv.org/pdf/2605.28742
published: '2026-05-27'
collected: '2026-05-28'
category: Reasoning
direction: 对比反思驱动的模型自改进
tags:
- Contrastive Reflection
- Insight Discovery
- Non-parametric Learning
- Verifiable Rewards
- External Memory
- Reasoning Efficiency
one_liner: 对比成功与失败推理轨迹生成可复用自然语言洞察，以更高样本、rollout和上下文效率实现冻结LLM的快速自改进。
practical_value: '- **非参数记忆与洞察抽象**：可借鉴CORE的“洞察记忆”设计，将模型犯错时的经验对比生成可复用自然语言策略，替代直接存储原始轨迹，降低存储与检索成本，特别适合电商场景中重复性任务（如商品描述生成、客服SOP）。

  - **效用感知检索**：结合语义相似度与经验效用分数进行检索，能避免引入无效或有害的上下文。在推荐或Agent任务中，可以跟踪不同提示/工具调用的成功频率，动态调整其检索权重，提升鲁棒性。

  - **失败驱动的反思与准入测试**：CORE只在失败时触发反思，并通过简单pass@1验证洞察有效性，这一约束可迁移到Agent工作流中：当模型输出被用户驳回时，对比成功的交互生成修正规则，并仅当规则能立即解决当前问题才加入知识库，防止噪声积累。

  - **上下文效率优势**：CORE用极少令牌（平均0.92k）实现优于全轨迹RAG的性能，对生产系统至关重要。在生成式推荐或对话Agent中，可考虑将大量交互压缩为短洞察，大幅降低推理延迟和成本。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：现有基于可验证奖励的语言模型自改进方法（如GRPO、GEPA）通常需要大量训练样本和数千次rollout，成本高昂且难以快速适应新任务。相比之下，人类能从少数对比反思中快速提炼可复用策略。CORE借鉴认知科学中对比学习与多记忆系统理论，旨在通过生成和利用紧凑的自然语言洞察，实现更高样本、rollout和上下文效率的模型自改进。

**方法关键点**：
- CORE是一种非参数算法，冻结模型权重，维护两个外部记忆：**rollout记忆**（存储成功轨迹）和**洞察记忆**（存储自然语言策略）。
- **对比反思**：模型解题失败时，将其不成功轨迹与语义相似问题的成功轨迹进行对比，生成候选洞察；仅当洞察在准入测试中帮助解决原问题且表现优于基线时，才存入洞察记忆。
- **效用感知检索**：洞察检索结合邻居问题上的历史效用估计与探索奖励（UCB风格），并在评估时仅使用效用分数。
- **失败偏置采样**：训练时优先采样模型准确率低的问题，加速弱点覆盖。

**关键结果**：在Matchstick Arithmetic、MathGAP、Tower of Hanoi、ZebraLogic四个任务上，使用GPT-OSS-120B，CORE在10样本设定下，用仅350次rollout就在所有任务上超越GRPO、GEPA、Episodic RAG、MemRL等基线的最优表现，最终平均准确率提升59.9%。上下文效率方面，CORE平均添加0.92k token，仅为RAG方法的1/36。消融实验证实，对比反思和效用检索都对性能至关重要。
