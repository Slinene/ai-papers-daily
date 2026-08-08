---
title: On-Policy Delta Distillation for Multilingual Math Reasoning
title_zh: 面向多语言数学推理的在线策略增量蒸馏
authors:
- Byeongho Heo
- Jaehui Hwang
- Sangdoo Yun
- Dongyoon Han
affiliations:
- NAVER AI Lab
arxiv_id: '2608.05802'
url: https://arxiv.org/abs/2608.05802
pdf_url: https://arxiv.org/pdf/2608.05802
published: '2026-08-05'
collected: '2026-08-08'
category: Training
direction: LLM 后训练 · 多语言蒸馏
tags:
- On-Policy Distillation
- Multilingual Reasoning
- Delta Distillation
- LLM Post-training
- Qwen3
one_liner: 提出 On-Policy Delta Distillation (OPD^2)，用教师模型与基模型的概率差作为学习信号，在多语言数学推理上优于
  OPD
practical_value: '- **Delta 信号可引入推荐 Agent 训练**：电商搜索/推荐中，若已有强监督教师模型（如大模型生成的推理路径），可直接使用
  OPD^2 的 delta 蒸馏技巧（教师 vs 基模型概率差）替代传统 RL，训练轻量 Agent，提升token级反馈效率。

  - **多语言场景可用单语数据提升跨语言性能**：实验表明英语蒸馏可泛化到韩语/日语，但需防语言漂移。类似地，若以英语搜索日志训练问答Agent，需混合目标语言数据保持语言一致性。

  - **在线采样+教师反馈框架适合动态数据流**：推荐系统常面临分布漂移，OPD 的在线策略生成思想可迁移至用户反馈动态更新下的模型滚动训练，用当前模型生成样本再让教师打分，提升样本利用率。

  - **概率差作为学习信号可借鉴至对比学习**：电商搜索中，正负样本概率差可类似 OPD^2 构造细粒度标签，训练学生模型区分优劣结果，尤其适合 beam search
  中的候选排序。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：On-Policy Distillation (OPD) 是 LLM 后训练中强化学习的替代方案，利用学生在线生成样本并让教师提供 token 级概率反馈，提升数据与计算效率。但 OPD 在多语言环境下的效果未被充分探索。近期提出的 On-Policy Delta Distillation (OPD^2) 使用教师模型与其基模型的概率差（而非师生差）作为学习信号，在英文推理上显著优于 OPD，但其多语言适用性未知。

**方法关键点**：将 OPD 和 OPD^2 应用于 Qwen3 模型，在英文、韩语、日语数学推理任务上训练。核心改进在于 OPD^2 的 delta 信号：计算教师（已微调的推理模型）与其基模型（未微调）在 token 上的概率差，使学生学习到因微调带来的提升部分，而非直接模仿教师概率。训练采用在线策略，学生生成响应，教师和基模型同时前向计算概率差作为监督目标。

**关键结果**：OPD^2 在所有语言上均优于原始 OPD，在韩语和日语上提升尤为显著（例如韩语数学基准 GSM8K 变体上，OPD^2 比 OPD 高约 5-10% 准确率）。同时，仅用英文数据训练的 OPD 也能提升韩语和日语性能，但响应会向英文偏移，说明多语言数据对维持目标语言生成能力至关重要。OPD^2 总体上缩小了英韩性能差距。
