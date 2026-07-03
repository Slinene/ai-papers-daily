---
title: 'DemoPSD: Disagreement-Modulated Policy Self-Distillation'
title_zh: DemoPSD：基于分歧调制的策略自蒸馏
authors:
- Yunhe Li
- Hao Shi
- Wenhao Liu
- Mengzhe Ruan
- Hanxu Hou
- Zhongxiang Dai
- Shuang Qiu
- Linqi Song
affiliations:
- City University of Hong Kong
- Tsinghua University
- Shenzhen University of Advanced Technology
- Chinese University of Hong Kong, Shenzhen
arxiv_id: '2607.02502'
url: https://arxiv.org/abs/2607.02502
pdf_url: https://arxiv.org/pdf/2607.02502
published: '2026-07-02'
collected: '2026-07-03'
category: Training
direction: LLM自蒸馏与探索保持
tags:
- On-Policy Self-Distillation
- Privileged Information Leakage
- Reverse-KL Barycenter
- Exploration Preservation
- LLM Reasoning
- Adaptive Distillation
one_liner: 通过自适应混合教师与学生分布的反向KL重心目标，缓解特权信息泄露并保持探索能力
practical_value: '- **自适应蒸馏强度**：当教师模型（带特权信息）与学生模型（无特权信息）的 token 级分布出现较大分歧时，自动降低教师信号的权重（通过
  α_t 控制），避免学生学到不可迁移的捷径。这一 trick 可直接迁移到搜索/推荐中的蒸馏场景，例如知识蒸馏精排模型时，若教师模型访问了后验特征（如点击后行为），可对分歧大的样本或位置减弱蒸馏力度。

  - **保持策略熵防止坍缩**：DemoPSD 训练过程中保持了比 SDPO 高 33-98% 的策略熵，从而保留了探索能力，提升 best@16 效果。在强化学习推荐或对话策略训练中，可以借鉴这种通过调整蒸馏目标来维持策略多样性、避免过早收敛到次优解的方法。

  - **反向KL重心作为蒸馏目标**：使用 π_target ∝ (π_teacher)^{1-α}·(π_student)^α 的几何混合替代直接匹配教师分布，比算术平均能产生更锐利且规避模式坍塌的训练信号。对于多任务推荐模型蒸馏，可以类似地对不同任务专家模型的
  logits 做几何加权，兼顾多目标。

  - **EMA 参考模型稳定训练**：计算分歧时使用学生模型的指数移动平均副本作为参考，避免训练不稳定。在在线学习或持续自蒸馏的推荐系统中，引入 EMA 教师可以平滑目标，减少噪声干扰。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
On-policy self-distillation (OPSD) 通过将同一模型的特权版本（如看到正确答案）作为教师，为学生（仅见问题）提供稠密 token 级监督，大幅提升样本效率。但最近研究发现，教师分布受特权信息污染，导致学生过拟合训练分布、丧失探索能力，并出现**特权信息泄露**：学生学到仅在训练时存在的捷径，泛化受损。现有方法多依赖间接代理（如教师熵、样本正确性）决定何时蒸馏，而非直接度量特权信息对预测的影响。

## 方法
DemoPSD 的核心是**选择性采纳教师指导**：当教师和学生的 token 级分布一致时，学生直接模仿教师；当分布严重分歧时（表明教师被特权信息过度影响），则更多依赖学生自身推理。
- **分歧度量**：用 Jensen-Shannon 散度计算教师分布与无特权学生分布之间的差异 d_t。
- **泄漏衰减系数**：α_t = f(d_t)，由重缩放的 sigmoid 映射得到，范围 [0, α_max]，分歧越大 α_t 越大。
- **反向KL重心目标**：蒸馏目标构建为学生与教师的几何加权混合：π_target ∝ (π_teacher)^{1-α_t}·(π_student)^{α_t}，等价于最小化 (1-α_t)KL(q||π_teacher) + α_t KL(q||π_student) 的反向KL重心。
- 使用 EMA 副本计算学生分布以稳定训练；梯度中教师信号按 (1-α_t) 缩放，自动抑制高分歧位置的泄漏。

理论上证明了：(1) 泄漏衰减：有效泄漏率被缩放为 (1-α_t)^2 · ||教师-学生 log 比||^2，严格小于标准 OPSD；(2) 探索保持：在一定协方差条件下，目标熵严格位于学生熵与教师熵之间，从而比完全匹配教师保留更多探索。

## 关键实验
- 数据集：SciKnowEval 四个科学领域（生物学、化学、材料科学、物理学）作为训练与域内评估，GPQA Extended 作为分布外测试。
- 基模型：Qwen3-4B-Instruct。
- 对比基线：GRPO（仅结果奖励）与 SDPO（标准自蒸馏）。
- 结果：DemoPSD 在 mean@16 上平均较 SDPO 提升 1.68，best@16 提升 2.82；训练熵较 SDPO 高出 33-98%；在 GPQA 上 SDPO 精度随训练下降，DemoPSD 则保持稳定且平均高出 7.91 个百分点。
- 敏感性：超参数 β（控制 α_t 对分歧的灵敏度）在 [25,100] 内均能匹敌或超越 SDPO。

## 核心一句话
DemoPSD 用**教师-学生分歧动态调制蒸馏目标权重**，在保持稠密监督的同时，自动抑制特权信息带来的有害捷径，从而兼顾训练效率、熵保留和泛化能力。
