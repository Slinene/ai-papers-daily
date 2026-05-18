---
title: 'CLOVER: Closed-Loop Value Estimation \& Ranking for End-to-End Autonomous
  Driving Planning'
title_zh: CLOVER：面向端到端自动驾驶规划的闭环价值估计与排序
authors:
- Sining Ang
- Yuguang Yang
- Canyu Chen
- Yan Wang
affiliations:
- University of Science and Technology of China
- Tsinghua University
- Beihang University
arxiv_id: '2605.15120'
url: https://arxiv.org/abs/2605.15120
pdf_url: https://arxiv.org/pdf/2605.15120
published: '2026-05-14'
collected: '2026-05-18'
category: Other
direction: 端到端自动驾驶规划 · 闭环价值估计
tags:
- Closed-Loop
- Value Estimation
- Ranking
- End-to-End Planning
- Self-Distillation
- Proposal Selection
one_liner: 闭环价值估计与排名框架，通过生成-打分自蒸馏解决训练评估不匹配，在NAVSIM达94.5 PDMS新SOTA
practical_value: '- 在推荐或Agent动作生成中，可借鉴“生成-打分”闭环自蒸馏：用业务规则（如CTR、合规性）过滤生成候选，构建伪专家样本，提升生成器对真实评估指标的覆盖。

  - 打分器直接预测多维业务指标子分数（如转化率、GMV、停留时长），代替单一价值模型，实现多目标可解释排序，且便于在线调整权重。

  - 采用保守更新与稳定性正则，防止生成器在弱监督下过拟合；仅当打分器选择的目标在真实评估下统计显著优于当前策略时才更新，降低风险。

  - 理论分析不完美打分器的改善条件，可推广至电商推荐中打分模型存在噪声时，如何判断是否进行策略迭代，提升在线安全性。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：端到端自动驾驶规划常基于模仿单条日志轨迹训练，但评测却使用安全性、可行性、进度、舒适度等规则指标，造成训练-评估不匹配。轨迹接近演示路径仍可能违反规则，而远离演示的替代轨迹反而有效且得分更高。该问题对基于候选选择的规划器尤为突出，需要候选集覆盖率和排序质量双重保障。

**方法**：提出CLOVER框架，采用轻量生成器-打分器架构。生成器产生多样化候选轨迹，打分器预测规划指标各子分数用于推理时排序。为扩展候选支持，利用评估器过滤构造伪专家轨迹，并以集合覆盖损失训练生成器。随后进行保守闭环自蒸馏：打分器在生成的候选上拟合真实评估子分数，生成器则基于教师选择的top-k及向量帕累托目标进行微调，并加入稳定性正则化。论文还分析了不完美打分器何时能提升生成器：当打分器选择的目标在真实评估下统计富集且更新足够保守时，改善是可靠的。

**结果**：在NAVSIM上，PDMS达94.5，EPDMS达90.4，创下新SOTA；在更具挑战的NavHard分割上，EPDMS为48.3，持平最强已报道结果；在nuScenes开环评测中，L2误差和碰撞率均为最低。
