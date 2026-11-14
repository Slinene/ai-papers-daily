---
title: Two mathematical models of knowledge distillation
title_zh: 知识蒸馏的两个数学模型
authors:
- Audrey Xie
- Ludwig Schmidt
- John Duchi
affiliations:
- Stanford University
arxiv_id: '2611.17230'
url: https://arxiv.org/abs/2611.17230
pdf_url: https://arxiv.org/pdf/2611.17230
published: '2026-11-12'
collected: '2026-11-14'
category: Training
direction: 知识蒸馏优化理论
tags:
- Knowledge Distillation
- SGD
- Optimization Landscape
- Generalized Linear Models
- Matrix Approximation
- Theory
one_liner: 用广义线性模型与 rank-1 矩阵近似证明蒸馏主要加快优化而非提升泛化
practical_value: '- 蒸馏收益主要是优化加速而非更好的泛化；在标签数据充足的电商/广告场景，用小模型蒸馏大模型不要期待最终指标显著超同结构硬标签训练，更适合用来缩短训练时间、加速实验迭代。

  - 若目标是快速拿到可用的 student，可先用教师软标签做若干 epoch 预热，再切回 hard label 或混合目标微调；理论支持软标签降低了优化难度，但最终精度仍由监督目标决定。

  - 对 CTR/CVR 这类 GLM 模型，蒸馏在 SGD 下能渐进更快收敛；在特征规模大、训练成本敏感时，可把教师 logits 当作稳定的 soft target，提高训练前期稳定性。

  - 论文对 rank-1 矩阵近似的分析提示，低秩/双塔/embedding 蒸馏时教师 target 的结构会影响收敛速度；实践中可观察教师输出的谱属性，但也需结合线上实验验证。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

动机：知识蒸馏为何有效，存在“提升泛化”与“改善优化”两种解释，近期实证显示充足数据下蒸馏学生未必超过同结构监督训练。

方法关键点：作者提出两个可分析的数学模型：一是用 SGD 训练广义线性模型（GLM），二是用梯度下降做 rank-1 矩阵近似，分别在带蒸馏和不带蒸馏的目标下比较收敛速度与最终解。

关键结果：理论证明蒸馏让学生模型以更快的速度达到可用性能，但不改变渐近最优解；收益来自更易优化的景观，而非更好的泛化。真实数据实验验证了理论预测。
