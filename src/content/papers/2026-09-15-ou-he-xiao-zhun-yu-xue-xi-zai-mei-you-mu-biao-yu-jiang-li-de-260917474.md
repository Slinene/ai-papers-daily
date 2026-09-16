---
title: 'Coupled Calibration and Learning: Mitigating Teacher Bias in LLM Distillation
  without Target-Domain Reward Feedback'
title_zh: 耦合校准与学习：在没有目标域奖励反馈的情况下缓解LLM蒸馏中的教师偏差
authors:
- Haichen Hu
- Yuheng Zhang
- David Simchi-Levi
affiliations:
- MIT
- UIUC
arxiv_id: '2609.17474'
url: https://arxiv.org/abs/2609.17474
pdf_url: https://arxiv.org/pdf/2609.17474
published: '2026-09-15'
collected: '2026-09-16'
category: Training
direction: LLM蒸馏中的教师偏差校准
tags:
- LLM distillation
- teacher bias
- calibration
- covariate shift
- reward feedback
one_liner: 提出CCL算法，通过源域反馈校准教师再训练学生，消除教师偏差且收敛到最优学生
practical_value: '- 跨域蒸馏推荐系统时，若目标场景无奖励反馈（如新业务、冷启动），可利用源场景已有反馈先校准教师模型，再生成伪标签训练学生，避免教师偏差直接迁移。

  - 采用迭代耦合优化：每轮用源域反馈校准教师，再用校准后的教师训练学生，学生更新后反哺下一轮校准，适合在线迭代冷启动。

  - 注意直接模仿教师（监督微调）在分布偏移下可能持续偏离最优策略，即使教师奖励更高；需要主动校准而非单纯正则化匹配。

  - 工程上可借鉴 token-level branching 思想，对生成序列进行部分采样和校准，降低方差并稳定训练。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM蒸馏通常直接模仿教师，但教师的系统偏差和错误也会被传递。在协变量偏移下，教师对目标问题的可靠性未知，且目标域没有奖励反馈，问题更严重。

**方法关键点**：提出 Coupled Calibration and Learning (CCL) 算法，核心是耦合教师校准与学生更新。每轮迭代先用源问题上的奖励反馈校准教师，再用校准后的教师在目标问题上训练学生；更新后的学生又影响后续校准。通过 token-level branching 实现控制校准误差。

**关键结果**：在自回归策略框架下，证明输出学生的期望平均 KL 散度到 oracle student 以多项式速率收敛到零（oracle 在学生类内最大化真实参考正则化目标奖励）。同时证明与正则化直接匹配的分离：即使教师获得比所有学生策略更高的正则化目标奖励，其误差仍可能保持非零。算法无需目标域奖励反馈即可克服教师偏差，恢复最优学生。
