---
title: Are Performance-Optimization Benchmarks Reliably Measuring Coding Agents?
title_zh: 性能优化基准对编码代理的可靠性审计
authors:
- Zhi Chen
- Zhensu Sun
- Yuling Shi
- David Lo
- Lingxiao Jiang
affiliations:
- Singapore Management University
- Shanghai Jiao Tong University
arxiv_id: '2607.01211'
url: https://arxiv.org/abs/2607.01211
pdf_url: https://arxiv.org/pdf/2607.01211
published: '2026-06-30'
collected: '2026-07-05'
category: Eval
direction: 性能优化 · 基准审计
tags:
- benchmark
- coding agent
- performance optimization
- evaluation
- runtime stability
one_liner: 审计三大代码优化基准，发现运行时波动、评分规则偏差和任务饱和导致代理排名不可靠
practical_value: '- 构建电商/Agent的离线评估流水线时，需确保运行环境一致，多次重复实验以控制随机波动，类似本文对跨机器回放稳定性的检查

  - 评分规则对最终排名影响巨大，应避免像SWE-efficiency那样给极端任务过高权重（如最差任务占58%–83%分数），导致整体分数被少数任务主导

  - 当多个模型/代理已在大部分任务上超过基线（如99.8%任务击败未优化代码），聚合排名掩盖剩余差距，应转向逐任务诊断，识别仍存在可靠改进空间的任务

  - 在报告Agent能力时，可借鉴「可重放有效任务」的概念，只保留那些参考补丁在不同环境下运行稳定的任务，以提供高信噪比的评估信号'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前主流代码性能优化基准（GSO、SWE-Perf、SWE-fficiency）的排行榜分数被广泛用于证明编码代理的进步，但分数可能混合了运行时不确定性、特定基准的评分规则差异，以及任务是否已被多个公开提交解决等因素，导致排名不可靠。

**方法**：对三个基准共740个任务，在四种Google Cloud机器类型上重放官方参考补丁，检查跨环境回放稳定性；分析8个同时出现在GSO和SWE-效率排行榜的公开提交，比较不同评分规则下的排名分歧；检查每个任务最多10个公开提交的结果，统计至少一个提交匹配或超过参考补丁的任务比例。

**关键结果**：仅39/102 GSO任务、11/140 SWE-Perf任务和411/498 SWE-效率任务的参考补丁在所有跨机回放中均符合原始有效性规则，SWE-Perf尤其脆弱（许多参考补丁产生近零运行时变化）；在28个成对提交比较中，9个出现排名翻转，SWE-效率排行榜对最差10个任务赋予58.5%–82.8%的过高分数权重；在可回放有效的450个任务中，85.3%至少有1个提交达到或超越参考补丁，99.8%至少击败未优化基线，表明大量任务已被现有方案解决，剩余真实优化空间有限。
