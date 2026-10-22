---
title: 'Ask to Distill: Learning to Synthesize Data for On-Policy Distillation'
title_zh: Ask-to-Distill：学习为策略蒸馏合成数据
authors:
- Jiashuo Sun
- Hao Zhang
- Xueqiang Xu
- Heng Wang
- Yixuan Xie
- Pengcheng Jiang
- Zhenrui Yue
- Jiajun Fan
- Peiran Li
- Ge Liu
affiliations:
- University of Illinois Urbana-Champaign
- The Hong Kong University of Science and Technology
- Texas A&M University
arxiv_id: '2610.27450'
url: https://arxiv.org/abs/2610.27450
pdf_url: https://arxiv.org/pdf/2610.27450
published: '2026-10-19'
collected: '2026-10-22'
category: Training
direction: LLM蒸馏 · 合成数据优化
tags:
- On-Policy Distillation
- Synthetic Data
- Question Generation
- Distributional Supervision
- Student-Teacher
one_liner: 用教师-学生分布分歧作为无答案信号，训练合成器生成能暴露教师监督的问题，提升on-policy蒸馏效率。
practical_value: '- **无标注数据价值评估**：在电商搜索/推荐中，当用LLM生成训练样本（如query改写、商品描述、用户意图）时，可借鉴教师-学生分歧+兼容性作为样本价值代理，无需人工标注或正确答案即可筛选高价值样本。

  - **低成本的迭代数据合成**：冻结学生-教师对计算奖励，避免每个候选样本都更新学生模型，大幅降低合成数据筛选的计算开销，适合业务中大规模生成候选后过滤。

  - **分布诱导器思路**：将生成器训练为“引出教师知识”的提问者，可迁移到Agent场景——让模型学会生成能暴露教师策略优势的任务，用于自我提升或策略蒸馏。

  - **长度与多样性控制**：在合成训练数据时加入长度惩罚和多样性奖励，可防止模型退化到短平快样本，保证覆盖长尾场景，对推荐系统的长尾物品描述生成有参考价值。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：On-policy distillation (OPD) 在极少训练问题上就能有效，提示问题作为分布知识转移的载体。如何评估新生成问题的价值且无需正确答案，并学习生成更好的问题？

**方法关键点**：提出 Ask-to-Distill (A2D)，将合成问题视为分布诱导器，优化其促使教师监督沿学生轨迹暴露的程度。用学生初始化的合成器生成问题，通过冻结的学生-教师对计算分布代理奖励，无需参考答案、正确性奖励或每候选学生更新。奖励 = 教师-学生分歧 × 教师概率质量与学生候选支持的兼容性，再加上长度和多样性控制项。生成问题经过去重和过滤形成 prompt-only bank，用于标准 OPD。

**关键结果**：在数学推理、代码生成、agentic 任务上，A2D 相比未优化的学生生成 prompt 和 KL-filtered 真实问题，平均性能和教师差距恢复均提升，匹配或超过真实 bank OPD；信号分析表明优化的问题能从更短学生回应中引发更密集监督和更多总信号。
