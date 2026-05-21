---
title: Mid-Training with Self-Generated Data Improves Reinforcement Learning in Language
  Models
title_zh: 用自生成多样化解题轨迹增强大语言模型的强化学习推理
authors:
- Aswin RRV
- Jacob Dineen
- Divij Handa
- Mihir Parmar
- Ben Zhou
- Swaroop Mishra
- Chitta Baral
affiliations:
- Arizona State University
- Google Cloud AI Research
- Google DeepMind
arxiv_id: '2605.08472'
url: https://arxiv.org/abs/2605.08472
pdf_url: https://arxiv.org/pdf/2605.08472
published: '2026-05-07'
collected: '2026-05-21'
category: Training
direction: 自生成多样化解题轨迹增强RL推理
tags:
- Mid-Training
- Self-Generated Data
- Reinforcement Learning
- Compositional Reasoning
- Policy Gradient
- Mathematical Reasoning
one_liner: 自生成多样化解题轨迹指导中期训练，提升后续强化学习的推理性能和策略组合能力
practical_value: '- 在RL微调前，用启发式提示生成多种正确推荐理由或对话策略，进行多样化监督训练，可拓宽探索空间并提升RL最终性能。

  - 借鉴“固定训练量下，多样化比增加任务数更有效”的结论，在生成数据时，为同一用户或商品生成多个正确但风格不同的响应，而非追求更多样本。

  - 使用规则验证器+奖励模型筛选自生成数据，可确保多样性与正确性的平衡，可用于Agent多智体协作策略生成。

  - 理论分析指出多模态策略分布有助于梯度更新，可在策略网络中设计多分支输出或温度控制，避免模式崩塌。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：强化学习（RL）提升大语言模型推理能力，但效果受限于训练数据多样性。针对数学问题可用多种解题方法，若模型仅见过有限方法，RL难以进一步改进。为此，研究在RL之前，用模型自身生成的多种正确解法进行中期训练（mid-training），以丰富策略先验知识。

**方法**：
- 基于波利亚解题启发式（类比、分解重组等），为每个训练问题构造few-shot prompt，生成多条候选解答。
- 用规则验证器保证答案正确，再用奖励模型评估解答对启发式的遵循度，最终每个问题保留多个不同解法，构成数据集DPólya。
- 在基础模型上用该数据进行标准监督微调（mid-training），然后应用GRPO进行RL训练。
- 理论分析表明，多模态输出分布使策略梯度更新更有效，促进不同解法的组合。

**结果**：
- 在Llama 3.2-3B-Instruct上，mid-training后RL在六个数学基准上pass@k全面提升，尤其在pass@64时，如AIME 2025从12.84%升至18.66%，MATH-500从87.76%升至88.94%。
- RL训练后生成的推理链中出现解法组合行为，组合比例随训练解法数增加而升高（n=16时达56.7%），且组合未在mid-training中显式出现。
- 对比蒸馏更强模型的数据，自生成数据多样性更高（Vendi Score 13.81 vs 10.95），下游性能更优。
- 在代码生成和叙事推理等跨领域任务上，mid-trained模型同样优于vanilla RL，显示解题策略的可迁移性。
- 固定训练步数下，学习多解法（每问题16种解法，共463题）比学习更多单解法问题（7408题单解法）效果提升约7%。

总结：用自我引导的多样化解题轨迹进行中期训练，能有效增强RL的推理表现，并促进策略组合，为提升LLM推理能力提供了新的训练范式。
