---
title: 'INFUSER: Influence-Guided Self-Evolution Improves Reasoning'
title_zh: 影响引导的自我进化提升推理能力
authors:
- Siyu Chen
- Miao Lu
- Beining Wu
- Heejune Sheen
- Fengzhuo Zhang
- Shuangning Li
- Zhiyuan Li
- Jose Blanchet
- Tianhao Wang
- Zhuoran Yang
affiliations:
- Yale University
- Stanford University
- University of Chicago
- Toyota Technological Institute at Chicago
- University of California, San Diego
arxiv_id: '2606.09052'
url: https://arxiv.org/abs/2606.09052
pdf_url: https://arxiv.org/pdf/2606.09052
published: '2026-06-08'
collected: '2026-06-09'
category: Training
direction: 自我进化训练 · 影响引导课程学习
tags:
- Self-Evolution
- Influence Function
- Co-Training
- RLVR
- Curriculum Learning
- Reasoning
one_liner: 提出INFUSER框架，用影响分数指导生成器与求解器协同进化，无需外部教师，大幅提升数学和通用推理性能。
practical_value: '- **影响分数作为合成数据质量度量**：使用开发集梯度与合成样本引起的模型更新方向的余弦相似度来评估单个样本的训练价值，可借鉴到推荐系统的样本筛选或Agent领域的数据蒸馏，替代简单的难度或困惑度指标。

  - **生成器-求解器协同进化范式**：将生成训练数据与模型训练建立成双层博弈，让生成器根据求解器当前能力实时调整输出，这类似推荐系统中召回与排序的联合优化或Agent多体协作的场景，可以通过更小的开发集引导数据生成远离分布外噪声。

  - **DuGRPO稳定连续奖励训练**：针对影响分数这类连续且带噪声的奖励，提出组内+批内双重归一化，避免低方差组的噪声放大和高方差组的梯度主导。在推荐模型的强化学习微调（如GRPO）中，当奖励函数从离散点击变为连续业务指标时，可直接复用该归一化技巧。

  - **文档池作为可持续课程来源**：利用无结构化文档（如教材）作为生成器输入，无需昂贵的人工标注，结合影响引导就能自动形成难度适中的课程。电商场景中可用商品描述、用户评论等非结构化文本，生成多模态问题-答案对，持续提升对话Agent或推荐解释生成的质量。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：现有LLM自我进化方法依赖外部监督或难度启发式，但难度不一定对应训练效用，且缺乏对外部知识源的扎实利用。本文提出INFUSER，将自我进化建模为生成器与求解器的协同双层博弈，用影响分数直接衡量每个生成问题对求解器在目标分布上改进的程度，从而构建真正的自适应课程。

**方法关键点**
- **双层博弈框架**：生成器从文档池采样文档，生成问答对作为求解器的训练课程；求解器在此课程上通过RLVR（基于规则验证的强化学习）优化。生成器的目标不是产出能答对较多的问题，而是让求解器更新后能在目标分布（如科学推理开发集）上表现更好。
- **优化器感知的影响分数**：对于每个生成的问题，计算求解器在其上训练的AdamW更新方向，再与开发集上的参考梯度计算余弦相似度，作为该问题的影响分数。该分数直接作为生成器的强化学习奖励，引导生成器产出真正有助于求解器进步的样本。
- **DuGRPO生成器更新**：针对连续、噪声大的影响奖励，设计双重归一化的GRPO变体，同时考虑组内标准差与批次平均标准差，避免低方差组的噪声放大和高方差组的梯度主导。

**关键结果**
- 在Qwen3-8B-Base上，INFUSER在14个基准的8个上取得最优，通用推理和数学物理类别相对提升均超20%（如GPQA-Diamond +23.4%，SuperGPQA +23.4%），且模型规模从4B到8B的增益衰减极小。
- 8B协同进化生成器在数学和编码上显著优于冻结的32B思考模型，证明自适应课程比静态大模型生成更有效。
- 消融实验确认：移除生成器协同进化、换成静态生成器或直接训练开发集均导致性能下降；DuGRPO和优化器感知影响分数对稳定训练至关重要。
