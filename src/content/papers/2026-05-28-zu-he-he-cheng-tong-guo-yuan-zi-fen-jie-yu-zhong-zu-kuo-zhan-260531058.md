---
title: 'Combinatorial Synthesis: Scaling Code RLVR via Atomic Decomposition and Recombination'
title_zh: 组合合成：通过原子分解与重组扩展代码 RLVR 规模
authors:
- Jiasheng Zheng
- Boxi Cao
- Boxi Yu
- Yuzhong Zhang
- Jialun Cao
- Yaojie Lu
- Hongyu Lin
- Xianpei Han
- Le Sun
affiliations:
- Chinese Information Processing Laboratory, Institute of Software, Chinese Academy
  of Sciences
- University of Chinese Academy of Sciences
- Lero the Research Ireland Centre for Software, University of Limerick
- The Chinese University of Hong Kong, Shenzhen
- The Hong Kong University of Science and Technology
arxiv_id: '2605.31058'
url: https://arxiv.org/abs/2605.31058
pdf_url: https://arxiv.org/pdf/2605.31058
published: '2026-05-28'
collected: '2026-06-05'
category: Training
direction: 代码 RLVR 数据生成 · 原子分解重组
tags:
- RLVR
- Code Generation
- Data Augmentation
- Atomic Decomposition
- Verifiable Rewards
- LLM Training
one_liner: 提出原子分解与重组框架，通过分解并受控重组生成新颖、高难度代码任务，提升 RLVR 训练的可扩展性
practical_value: '- **数据增强思想可迁移至推荐/Agent 场景**：在生成推荐 Query、Agent 指令或测试用例时，可将现有数据分解为原子元素（如商品属性、用户意图、操作序列），再通过受控重组生成多样化的新样本，提升训练数据的覆盖度和难度。

  - **组合式合成解决多样性瓶颈**：业务中常遇到训练样本同质化问题，借鉴原子分解思路，设计可组合的原子单元与约束规则，可系统性生成大量不同难度梯度的样本，用于模型能力爬坡。

  - **自动生成高质量验证测试**：ADR 同步生成代码与对应单元测试的思路，可迁移到 Agent 任务中自动构造评估用例，例如在生成式推荐中自动生成商品描述并附带可验证的约束条件，实现自动化评测。

  - **RLVR 训练范式在非代码领域的延伸**：论文证明了可验证奖励与合成数据的结合能稳定提升模型能力，若能在电商 Agent 任务中定义可自动验证的奖励信号（如订单成功率、交互符合业务规则），则可套用类似框架进行大规模
  RL 训练。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：强化学习与可验证奖励（RLVR）是提升 LLM 代码能力的核心范式，但其扩展受限于缺乏足够困难且新颖的可验证代码任务。现有基于启发式种子扩展的合成方法难以保证生成任务的新颖性和难度，导致训练数据价值无法随合成量线性增长。

**方法**：提出原子分解与重组（ADR）框架。将现有代码任务自动分解为原子元素（如数据结构、算法逻辑、输入输出约束），然后通过受控的原子选择与组合规则生成全新任务，并自动生成对应的验证单元测试。该过程可系统性地生成大量原创、高难度且多样化的代码任务。

**结果**：实验表明，ADR 生成的任务在原创性、难度、多样性和测试质量上均优于现有基线。在算法编程、工具使用、数据科学等多个下游领域，使用 ADR 合成数据进行 RLVR 训练能持续带给模型更大的代码能力提升，验证了该方法对扩展 RLVR 规模的有效性。
