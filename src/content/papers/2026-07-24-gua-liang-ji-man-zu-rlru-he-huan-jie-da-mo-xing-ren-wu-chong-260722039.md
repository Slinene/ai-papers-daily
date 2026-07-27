---
title: 'Enough is as good as a feast: A Comprehensive Analysis of How Reinforcement
  Learning Mitigates Task Conflicts in LLMs'
title_zh: 适量即满足：RL如何缓解大模型任务冲突的全面分析
authors:
- Zixuan Ren
- Jinliang Lu
- Junhong Wu
- Yang Zhao
- Dai Dai
- Hua Wu
- Haifeng Wang
- Chengqing Zong
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Baidu Inc.
arxiv_id: '2607.22039'
url: https://arxiv.org/abs/2607.22039
pdf_url: https://arxiv.org/pdf/2607.22039
published: '2026-07-24'
collected: '2026-07-27'
category: Training
direction: RL训练范式减轻任务冲突
tags:
- model merging
- task conflicts
- reinforcement learning
- supervised fine-tuning
- on-policy training
- advantage decay
one_liner: 发现RL训练通过on-policy数据、优势衰减与正负联合优化显著减轻模型合并时的任务冲突
practical_value: '- 当需要将多个专用LLM（如电商中的推荐解释生成、查询改写、商品文案生成）合并为一个部署模型时，优先使用RL（如GRPO、PPO）训练各子任务，可大幅降低合并后的性能退化，减少多模型维护成本。

  - 训练数据生成采用on-policy方式（模型自身采样+奖励打分）而非静态SFT数据集，能有效减小参数更新幅度，从而降低跨任务参数冲突。

  - 同时利用正样本（高奖励）和负样本（低奖励）进行联合优化，而不是像SFT仅依赖正例，这有助于学习更无偏的更新方向，提升不同任务模型合并时的兼容性。

  - 在实际工程中，可结合参数平均或TIES等免训练合并策略，直接集成RL-trained任务专家模型，成本低且效果稳定，特别适合希望快速融合多个LLM能力的推荐或Agent系统。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
模型合并能够将多个专用LLM整合为一个统一模型，是降低多模型部署成本的有效途径。然而，合并时参数干扰会导致严重的性能下降（任务冲突），现有研究多聚焦于设计更好的合并策略，却忽略了上游训练范式的影响。SFT与RL作为LLM后训练的两大范式，哪一种更有利于后续合并？该问题在以往工作中被忽视，但这直接决定了合并后模型的质量。

**方法关键点**
- 在数学推理、代码生成、指令遵循、逻辑谜题、排序五个任务上，分别用SFT和RL（GRPO）训练Llama-3.1-8B等基座模型，然后进行两两模型合并。
- 对比四种合并策略：简单平均、TIES、Task-Arithmetic、DARE，并扩展至PPO、REINFORCE++等RL算法以及Llama-3.2-3B、Mistral-Small-24B等不同基座。
- 从三个维度揭因：（1）on-policy数据使梯度更新幅度更小，减少覆盖其他任务知识；（2）RL优化目标的固有特性——优势函数随训练衰减，自动限制冲突更新；（3）正负样本联合优化让模型学会无偏的参数更新方向，提升合并鲁棒性。

**关键结果**
- RL-trained模型合并后性能保持远优于SFT：TIES合并下GRPO平均下降仅7.1%，而SFT下降19%；指令遵循任务上GRPO仅降0.3%，SFT降28.7%。
- 不同RL算法、基座模型、合并方法下结论一致。
- 冲突范数（conflict norm）增长趋势：RL明显慢于SFT，且参数更新范数（||Δθ||）始终更小（如数学任务RL为0.78 vs SFT的6.5）。
- 消融实验：去掉负样本的RL-Pos合并后性能退化加重，验证了正负联合优化的关键作用。

**核心一句话**
RL训练天然适合模型合并，因其on-policy数据、衰减的优势更新和正负联合优化共同抑制了跨任务参数冲突。
