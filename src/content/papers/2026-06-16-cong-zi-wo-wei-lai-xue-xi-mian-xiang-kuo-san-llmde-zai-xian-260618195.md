---
title: 'Learning from the Self-future: On-policy Self-distillation for dLLMs'
title_zh: 从自我未来学习：面向扩散LLM的在线策略自蒸馏
authors:
- Yifu Luo
- Zeyu Chen
- Haoyu Wang
- Xinhao Hu
- Yuxuan Zhang
- Zhizhou Sha
- Shiwei Liu
affiliations:
- Tsinghua University
- Technical University of Munich
- Nanyang Technological University
- University of British Columbia
- University of Texas at Austin
arxiv_id: '2606.18195'
url: https://arxiv.org/abs/2606.18195
pdf_url: https://arxiv.org/pdf/2606.18195
published: '2026-06-16'
collected: '2026-06-17'
category: Training
direction: 扩散LLM后训练 · 在线自蒸馏
tags:
- OPSD
- dLLM
- self-distillation
- diffusion models
- reasoning
- sample efficiency
one_liner: 首个面向扩散大语言模型的在线自蒸馏框架，通过后缀条件化与步骤级监督实现高效后训练
practical_value: '- 若业务中采用扩散模型做生成式推荐（如商品语义ID序列生成），可借鉴d-OPSD的后缀条件化设计：将已生成的未来token作为条件，为当前token提供稠密监督，无需额外的前缀特权信息。

  - 步骤级监督（step-level KLD）比token级监督更适配迭代去噪训练过程，可在扩散推荐模型的微调中替换逐token loss，提升生成质量与训练效率。

  - 该方法样本效率极高（仅需RLVR 10%的优化步数），在大规模推荐模型训练中可大幅降低算力成本，适合资源受限场景的模型后训练。

  - 自未来经验蒸馏的思路可推广至其他序列生成任务，例如用llm生成搜索query时，利用模型自身后续生成的内容作为监督信号，强化长程一致性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有在线策略自蒸馏（OPSD）成功应用于自回归LLM的后训练，但其前缀条件化与token级监督与扩散LLM的任意顺序生成特性冲突，无法直接迁移。

**方法**：提出d-OPSD，专为扩散LLM设计的自蒸馏框架。核心改动两点：
- **后缀条件化教师**：将原本提供前缀特权信息的教师构造改为利用模型自身生成的答案尾部作为条件，让学生从“自我未来经验”中学习，即学会利用后续生成的tokens修正前序输出。
- **步骤级监督**：放弃token级KL散度，改为在每个去噪步骤上计算模型分布与教师分布间的差异，使得训练损失自然对齐dLLM的迭代去噪过程。

训练时，学生模型采样一条完整序列，其尾部作为教师条件，头部作为学习目标，在多个噪声步骤上逐步蒸馏。

**结果**：在数学、代码等四个推理基准上，d-OPSD一致优于RLVR（如GRPO）和SFT基线，达到更高准确率的同时，仅需RLVR约10%的优化步数，样本效率显著提升。
