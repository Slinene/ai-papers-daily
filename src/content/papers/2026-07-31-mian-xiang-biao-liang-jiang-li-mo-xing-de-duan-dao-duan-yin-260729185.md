---
title: Learning Latent Reasoning Traces for Scalar Reward Models End-to-End
title_zh: 面向标量奖励模型的端到端隐式推理学习
authors:
- Sanwoo Lee
- Clive Bai
- Hsiu-Yuan Huang
- Kun Liang
- Weijie Liu
- Yunfang Wu
affiliations:
- Peking University
- Tencent
arxiv_id: '2607.29185'
url: https://arxiv.org/abs/2607.29185
pdf_url: https://arxiv.org/pdf/2607.29185
published: '2026-07-31'
collected: '2026-08-03'
category: Training
direction: 奖励模型 · 隐变量训练
tags:
- Latent Variable
- Reward Model
- End-to-End Training
- RLHF
- Reasoning Trace
- OOD Generalization
one_liner: 将推理链视为隐变量，端到端最大化标量RM的数据似然，统一生成与判别目标，提升OOD泛化。
practical_value: '- **搜索/推荐排序模型中的奖励建模**：可借鉴隐变量框架，将生成式推理与标量打分联合优化，避免生成器与判别器目标割裂，提高打分的鲁棒性和分布外泛化能力。

  - **简化训练流程**：使用REINFORCE将生成器的优化目标直接对齐到下游标量RM的对数似然，无需外部教师模型或手工设计的奖励（如Kendall’s τ），减少超参数和数据处理开销。

  - **数据清洗trick**：利用浅层文本特征训练轻量MLP集成，过滤掉模型易拟合的简单样本（低损失），保留更具泛化价值的困难样本，可迁移到偏好数据或标注数据的质量筛选。

  - **在线RLHF中的长度控制**：LatentRM在RLHF中生成更短的回复，同时保持高胜率，有效抑制“奖励过度优化”和长度作弊，这对对话系统或生成式推荐中的对齐训练有借鉴意义。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**：传统标量奖励模型（scalar RM）容易过拟合表面模式，在复杂或分布外任务上泛化差；生成式RM虽有推理能力，但自然语言评分缺乏灵活性和概率可解释性。现有的混合方法将推理生成和标量打分作为多任务并行训练，但辅助目标（如Kendall’s τ）与最终对数似然并不一致，导致推理不能最优地服务于奖励预测。

**方法关键点**
- 将推理链作为**离散隐变量 z**，构建条件生成模型 p(y|x,z)，目标为最大化边缘似然 log p(y|x)。
- 通过ELBO推导，设定推理网络等于先验 pθ(z|x)，得到简洁目标：max E_z[log pφ(y|x,z)]，其中 θ 是生成器参数，φ 是标量RM参数。
- **端到端联合训练**：生成器每个提示采样多条推理链，标量RM依据Plackett-Luce损失更新；生成器使用REINFORCE，以每条推理链下标量RM的对数似然作为奖励，均值减基线降低方差。
- 标量RM从推理链末尾的`<score_i>`标记前提取隐状态，经共享线性头输出奖励分数，实现灵活打分。
- 训练数据构建时，引入基于浅层特征的集成过滤，丢弃40%易拟合样本，提升训练集质量。

**关键实验结果**
- ID测试集：LatentRM在多个领域（通用、数学、STEM、对抗性）的Kendall’s τ和log-likelihood上均超过ScalarRM、生成式RM和多任务RM。
- OOD基准：RM-Bench准确率82.8%，PPE Correctness 72.1%，显著优于所有基线，尤其在推理密集域（MATH 92.7%）和抵抗风格偏误（Hard子集81.3%）方面表现突出。
- RLHF对齐：使用LatentRM进行GRPO训练后，策略模型在长度受控胜率上超越基于其他RM的策略（最高58.5%），同时生成平均长度更短（1289 tokens vs 1474 tokens），有效抑制奖励黑客行为。

**核心结论**：将推理显式建模为隐变量并端到端优化标量RM的似然，能使生成器专注于产生真正有信息量的推理，而非简单的口头评分，显著提升奖励模型在分布内外的泛化性与对齐能力。
