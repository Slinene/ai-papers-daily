---
title: On-Policy Delta Distillation
title_zh: 在线策略增量蒸馏
authors:
- Byeongho Heo
- Jaehui Hwang
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2607.15161'
url: https://arxiv.org/abs/2607.15161
pdf_url: https://arxiv.org/pdf/2607.15161
published: '2026-07-16'
collected: '2026-07-17'
category: Training
direction: LLM训练 · 推理蒸馏
tags:
- On-Policy Distillation
- Delta Signal
- LLM Reasoning
- Post-training
- Distillation
one_liner: 用教师与其基模型输出的差异（delta信号）替代直接模仿，更高效传递推理能力增益
practical_value: '- 在基于LLM的推荐或Agent模型中，可以将教师模型设置为经任务指令微调的强版本，基模型为原始预训练版本，蒸馏时拟合两者输出logits之差（delta信号），更聚焦于任务特定的推理模式迁移，避免直接模仿可能引入的冗余信息。

  - 对于对话式推荐或多步推理Agent，delta信号能显式捕捉“推理策略增益”，训练更稳定，且论文表明仅需短暂后训练即可大幅提升性能，适合业务快速迭代。

  - 若搜索推荐业务中使用强化学习（如RLHF）存在奖励设计困难或训练噪声大，可尝试OPD²替代，直接用token级监督，工程实现简单，无需单独的价值网络或偏好数据。

  - 蒸馏过程中需要教师和基模型的双重前向计算，实际部署时可缓存基模型在训练数据上的输出分布，减少计算开销。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：常规在线策略蒸馏（OPD）直接让学生模仿教师输出分布，但教师分布中大部分知识来自预训练，只有推理调优带来的变化才是需要迁移的“增益”，直接模仿效率低且引入噪声。  
**方法**：提出delta信号，即教师与其指令微调前的基模型输出logits之差，该差量仅反映推理训练带来的能力变化。学生模型通过在线生成响应，最大化在每个token上在该差量分布下的对数概率（即奖励为delta信号）。该框架称为OPD²，无需额外奖励模型，继承OPD的token级监督优势。  
**结果**：在数学（GSM8K、MATH）、科学（GPQA）和代码推理（HumanEval)等基准上，OPD²一致优于常规OPD，使用Llama3-8B/70B等模型在少量训练步数内即获得显著提升，例如在GSM8K上8B模型提升约2-3个百分点，且收敛更快。
