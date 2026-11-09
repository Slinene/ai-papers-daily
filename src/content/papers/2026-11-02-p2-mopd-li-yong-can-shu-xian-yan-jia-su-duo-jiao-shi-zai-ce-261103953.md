---
title: 'P^2-MOPD: Accelerating Multi-Teacher On-Policy Distillation via Parameter
  Priors'
title_zh: P2-MOPD：利用参数先验加速多教师在线策略蒸馏
authors:
- Sinuo Wang
- Jiacheng Lu
- Zeyu Zhang
- Maojia Song
- Rui Sun
- Beidi Luan
- Yutong Xie
- Jing Li
- Daxin Jiang
- Qi Wu
affiliations:
- Australian Institute for Machine Learning, Adelaide University
- StepFun
- Shanghai Jiao Tong University
- Singapore University of Technology and Design
- Mohamed bin Zayed University of Artificial Intelligence
arxiv_id: '2611.03953'
url: https://arxiv.org/abs/2611.03953
pdf_url: https://arxiv.org/pdf/2611.03953
published: '2026-11-02'
collected: '2026-11-09'
category: Training
direction: 多教师蒸馏 · 参数先验融合
tags:
- Multi-Teacher Distillation
- On-Policy Distillation
- Parameter Priors
- Task Arithmetic
- LLM Training
one_liner: 将学生与专家参数的线性组合视为可微模型，联合优化混合系数与学生权重，使专家作为参数先验，大幅加速多教师在线蒸馏并提升恢复率
practical_value: '- 多领域专家整合：推荐、广告、搜索等垂直领域用 RL 训练出的专家模型，可用「可训练学生 + 可学习混合系数 + 冻结专家参数」做
  on-policy 蒸馏，融合成一个通用模型；比纯 task arithmetic 更灵活，学生不必被困在专家参数张成空间内。

  - 训练加速：把专家参数作为先验注入可微线性组合，联合优化混合系数和学生权重，在相同初始化下只需一半训练步数就能超过 MOPD 最终平均恢复率；适合算力有限的业务模型整合。

  - 工程细节：先用 task arithmetic 初始化学生（TA init）作为共享起始点，再让学生可训练，专家权重保持冻结；每个教师只监督学生自己生成的轨迹，更贴近线上真实分布。

  - 可复用结论：多教师在线蒸馏通常存在各领域能力恢复不均衡问题，P2-MOPD 能更平衡地恢复多个专家能力，1.7B 模型平均恢复率达 94.7%，明显高于 MOPD
  的 80.9%，适合需要同时保留多个业务能力的场景。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
多教师在线策略蒸馏（MOPD）能整合多个领域专家模型，但训练慢、各专家能力恢复不均衡；task arithmetic 虽免训练，却只能停留在冻结学生与专家参数的线性张成空间内，表达力受限。

## 方法关键点
将学生与多个专家参数的线性组合视为一个单一可微模型，在同一个 on-policy distillation 目标下，**联合优化混合系数和学生权重**；专家权重保持冻结，充当参数先验。由于学生仍然可训练，模型不必受限于专家参数张成空间，从而兼顾了 task arithmetic 的初始化和蒸馏的训练灵活性。

## 关键结果
在 Qwen3-1.7B 和 Qwen3-4B 四个领域设置中，从相同初始化出发，P2-MOPD 只需一半训练步数就超过 MOPD 的最终平均恢复率；训练结束时，1.7B 模型平均恢复率达到 94.7%，MOPD 为 80.9%，且各专家能力恢复更均衡。
