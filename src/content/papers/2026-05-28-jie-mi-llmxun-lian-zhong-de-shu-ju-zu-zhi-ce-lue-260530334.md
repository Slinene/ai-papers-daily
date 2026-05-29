---
title: Demystifying Data Organization for Enhanced LLM Training
title_zh: 揭秘LLM训练中的数据组织策略
authors:
- Yalun Dai
- Yangyu Huang
- Tongshen Yang
- Yonghan Wang
- Xin Zhang
- Wenshan Wu
- Qihao Zhao
- Hao Li
- Yuanyuan Gao
- Kim-Hui Yap
affiliations:
- Nanyang Technological University
- Microsoft Research
- The Hong Kong University of Science and Technology
arxiv_id: '2605.30334'
url: https://arxiv.org/abs/2605.30334
pdf_url: https://arxiv.org/pdf/2605.30334
published: '2026-05-28'
collected: '2026-05-29'
category: Training
direction: LLM数据排序与课程学习
tags:
- Data Organization
- Curriculum Learning
- LLM Training
- Data Ordering
- Folding
- Sharpening
one_liner: 复用预计算样本得分，提出四项数据组织指导原则，实现零额外开销的LLM训练性能提升
practical_value: '- **复用数据选择阶段的样本得分**：在推荐模型或Agent训练中，若已有数据质量/难度打分，可直接用于排序训练样本，几乎零额外成本，提升模型效果。

  - **数据起始与结尾的边界锐化**：训练初期喂低分（简单）样本稳定优化，后期喂高分（高质量）样本冲刺性能，可迁移到生成式推荐或结构化Agent训练的微调阶段。

  - **循环调度防遗忘**：通过折叠式排列让模型周期性回顾全谱样本，避免灾难性遗忘。对于需要维持多任务能力的Agent（如同时做推荐、对话、工具调用），可在持续学习管线中采用类似交错策略。

  - **局部多样性注入**：在保持全局课程趋势的前提下，对相邻小批次进行打乱，增强梯度多样性，提高泛化性。在电商搜索或推荐重排序训练中，可避免同质化样本集中导致的过拟合。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
LLM训练通常只进行1~2个epoch，训练样本的呈现顺序成为影响收敛和最终性能的第一要素。以往数据效率研究大量投入计算资源生成样本级得分（质量、难度等），却仅用于一次性数据筛选，造成信息浪费。本文提出复用这些预计算得分来组织训练数据顺序，以几乎零额外开销提升模型性能，并首次系统地探索数据组织对LLM训练的影响。

### 方法关键点
- **四项指导原则**：1) **边界锐化**（Boundary Sharpening）：训练起始用低分数据稳定优化，结尾用高分数据提升下游表现；2) **循环调度**（Cyclic Scheduling）：避免严格由易到难的排序导致遗忘，通过折叠排列让模型周期性接触全谱数据；3) **课程连续性**（Curriculum Continuity）：通过Z字型排列消除折叠切换时的分布突变，平滑梯度轨迹；4) **局部多样性**（Local Diversity）：在局部窗口内打乱样本顺序，防止mini-batch内同质性过强。
- **实现策略**：基于排序数据集D_sort，通过分段排序（SEG）、折叠排序（FO）、Zig-zag（ZIG）和抖动排序（JIT）分别实例化上述原则，并组合成跨原则策略**STR**（融合G1、G2、G4）和**SAW**（融合全部G1~G4），在训练序列不同区段应用不同排序逻辑。

### 关键实验与结果
- **实验设置**：Mistral架构（160M~1.7B）在FineWeb-Edu上预训练，Qwen3在数学（DeepMath-103K）和代码（OpenCodeInstruct）上进行SFT，对比Random、CL和DELT基线。
- **预训练结果**：在50B token规模下，STR和SAW将平均下游准确率从Random的37.09%分别提升至38.65%和38.78%，且增益随模型尺寸扩大而持续（1.7B时SAW达50.11%，Random仅47.72%）。
- **SFT结果**：数学AIME平均得分从1.30提升至2.53（SAW），代码HumanEval+MBPP平均从55.37提升至60.83（STR）。
- **损失外推**：根据Chinchilla律，数据组织带来的测试损失降低在GPT-3 175B、Llama系列等大规模模型上依然保持。

### 最值得记住的一句话
> 训练数据的呈现顺序是塑造LLM学习轨迹的第一要素，复用预计算得分进行智能排序可带来显著且零额外成本的性能提升。
