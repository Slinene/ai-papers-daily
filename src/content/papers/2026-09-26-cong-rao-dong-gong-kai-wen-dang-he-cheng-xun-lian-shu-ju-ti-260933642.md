---
title: 'Learning to Learn from Context: Synthetic Training from Perturbed Public Documents'
title_zh: 从扰动公开文档合成训练数据提升大模型上下文学习能力
authors:
- Haoyi Wu
- Yang Xiao
- Yusong Sun
- Wenyang Hui
- Zhaokai Luo
- Chengyue Jiang
- Mu Chuan
affiliations:
- AllSpark Team
arxiv_id: '2609.33642'
url: https://arxiv.org/abs/2609.33642
pdf_url: https://arxiv.org/pdf/2609.33642
published: '2026-09-26'
collected: '2026-09-29'
category: Training
direction: LLM 合成数据与上下文学习训练
tags:
- synthetic data
- context learning
- SFT
- RL
- long context
- data augmentation
one_liner: 用少量扰动公开文档合成10k上下文推理样本，将35B模型CL-bench从13.7%提升至24.6%，媲美万亿参数模型
practical_value: '- 用于电商知识库/RAG 助手训练：把产品说明、活动规则、广告政策等内部文档做同义改写/扰动，再生成需逐段推理的问答，只保留“去掉文档就答不对”的样本，可低成本造出强迫模型依赖上下文而不是记忆的数据。

  - 两阶段训练：SFT 提升基础上下文跟随，再接 rubric-reward RL 用评分准则作奖励，在少量数据（10k）下把小参数 MoE 模型拉到接近大模型；适合业务中无法大规模标注的场景。

  - 过滤机制可复用：用改写前后答案变化、引用证据检查等方法自动筛选高质量上下文依赖样本，避免合成数据里混入可通过参数知识回答的“伪上下文”样本；对长商品描述、多轮
  Agent 工具结果等场景尤其有价值。

  - 观察到的迁移：改进集中在长上下文理解、指令遵循和推理，对代码和知识影响小。如果业务目标是让模型在复杂上下文里做推荐决策/政策合规，可比通用知识注入更精准。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：真实任务要求 LLM 从特定上下文完成任务，但人类标注上下文数据昂贵；公开高质量文档多被预训练见过，直接训练会奖励记忆而非上下文学习。方法：构造合成管线，先对源文档进行改写降低记忆风险；再生成需要基于文档推理的问题和评分标准；用文档作为上下文作答；只保留确实依赖文档的样本。无人工标注，从3.5k文档生成约10k样本。结果：SFT 将 Qwen3.6-35B-A3B 在 CL-bench 从 13.7% 提高到 22.8%，再经 rubric-reward RL 到 24.6%，与超万亿参数 Qwen3.8-2.4T（23.9%）相当；并在长上下文理解、指令遵循、推理上产生迁移，代码和知识基本持平。
