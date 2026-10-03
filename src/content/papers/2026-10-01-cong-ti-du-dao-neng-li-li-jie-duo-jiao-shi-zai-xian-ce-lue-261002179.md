---
title: 'From Gradients to Capabilities: Understanding Multi-Teacher On-Policy Distillation'
title_zh: 从梯度到能力：理解多教师在线策略蒸馏
authors:
- Siqi Zhu
- Suozhi Huang
- Kaixuan Zhang
- Yuheng Yang
- Zhanyang Jin
- Yihang Sun
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Princeton University
- Westlake University
arxiv_id: '2610.02179'
url: https://arxiv.org/abs/2610.02179
pdf_url: https://arxiv.org/pdf/2610.02179
published: '2026-10-01'
collected: '2026-10-03'
category: Training
direction: 多教师在线蒸馏优化机制
tags:
- multi-teacher distillation
- on-policy distillation
- optimizer analysis
- gradient analysis
- BF16 precision
- top-k KL
one_liner: 通过梯度与优化器分析，揭示损失平均、Adam动量、BF16精度和词汇截断如何影响多教师蒸馏的任务性能。
practical_value: '- 多任务/多领域模型融合时，响应长度差异会通过 token 平均隐式改变各任务损失权重；即使显式平衡域权重，域内长度加权仍通过协方差项影响梯度方向。建议在长度差异大的场景下，优先使用响应级平均或引入长度归一化，并监控各任务有效梯度占比。

  - Adam 的一阶动量会掩盖不同教师/任务之间的梯度差异，更新方向被历史平均对齐；在线学习或需要快速适应新任务信号时，可尝试使用 SGD 或重置一阶矩，实验显示
  SGD 在 PG 损失下四任务均值更高。

  - BF16 存储会隐藏大量 FP32 主权重中的小变化（约97% vs 7-11%），导致模型更新看似稀疏，实际并非如此。评估参数变化或稀疏性时，应基于 FP32
  master weights，避免被低精度舍入误导。

  - top-k 词汇截断虽在梯度方向上与全词汇 KL 高度一致（余弦>0.999），但任务收益取决于损失平均方式；不能仅凭梯度余弦决定是否采用。资源受限时可使用
  top-64 交集 KL，但需针对目标任务调整权重。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
多教师 on-policy 蒸馏（MOPD）利用多个 RL 专家的概率分布训练单个学生模型，以融合数学、代码、指令跟随等能力。但不同教师信号如何组合并转化为参数更新、最终影响任务性能，现有方法缺乏机制层面的理解。本文通过梯度与优化器分析，系统研究损失平均、Adam 动量、数值精度和词汇截断等因素的作用。

## 方法关键点
- **模型与设置**：Qwen3-1.7B 学生，四个领域教师（数学、代码、指令跟随、科学）从同一初始化用 RL 训练；另用 SmolLM3-3B 做诊断。
- **损失平均规则**：对比全局 token 平均（GT）、域 token 平均（DT）、域响应平均（DR），分析隐式加权。推导出域内长度加权通过协方差项 Cov(T,g) 改变梯度方向。
- **词汇监督**：提出 top-k 交集 KL 损失，仅使用学生和教师 top-k 集合的交集，重新归一化概率；与采样 token PG 和全词汇 KL 比较。
- **优化器与精度分析**：固定参数与优化器状态，测量原始梯度、Adam 更新、FP32 主权重与 BF16 模型权重的差异。

## 关键实验
- 在相同响应批次上，DR 与 DT 的原始梯度平均余弦 0.68，但应用 Adam 后更新余弦升至 0.96；Adam 一阶矩对齐了不同监督方向的更新。
- BF16 舍入后，约 97% 的 FP32 主权重已改变，但仅 7-11% 的 BF16 权重可观察到变化。
- 不同教师梯度在 Adam 更新中的平均余弦 >0.83，重置一阶矩后降至接近 0，说明动量是更新对齐的主因。
- 使用 PG 损失时，SGD 四任务均值优于 Adam（DR: 39.94 vs 38.91，DT: 39.46 vs 38.63，GT: 39.26 vs 38.79）。
- Top-64 交集 KL 梯度与全词汇 KL 余弦 >0.999，但相对于 PG，数学精度在 DR 下 +2.6 个百分点，在 GT 下 -2.1 个百分点，表明梯度方向近似不能预测任务收益。

## 最值得记住的一句话
梯度方向的高近似不保证能力提升，优化器动量与数值精度会深刻重塑监督信号的实际效果。
