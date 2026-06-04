---
title: Failed Reasoning Traces Tell You What Is Fixable (But Not by Reading Them)
title_zh: 失败推理轨迹暗含可修复性，无需阅读文本即可诊断
authors:
- Nizar Islah
- Istabrak Abbes
- Irina Rish
- Sarath Chandar
- Eilif B. Muller
affiliations:
- Mila - Quebec AI Institute
- Université de Montréal
- Polytechnique Montréal
- CHU Sainte-Justine
arxiv_id: '2606.05145'
url: https://arxiv.org/abs/2606.05145
pdf_url: https://arxiv.org/pdf/2606.05145
published: '2026-06-03'
collected: '2026-06-04'
category: Reasoning
direction: 推理模型测试时故障诊断与路由
tags:
- Failure Analysis
- Test-Time Compute
- Trajectory Features
- Routing
- Post-Training Analysis
one_liner: 从失败轨迹的分布特征中提取三个问题级特征，实现测试时故障分类与路由，提升修复成功率12.2%。
practical_value: '- 在 Agent 多步推理或推荐解释生成中，可利用轨迹分布特征（如输出一致性、多样性）区分偶发性失败与结构性失败，从而决定是重试、引导还是更重干预，避免无谓计算。

  - 提出的无训练路由规则直接使用输出级别统计量（无需解析文本），可嵌入到线上系统实现快速失败分类与资源分配，特别适合延迟敏感的电商搜索或对话推荐场景。

  - 特征跨模型家族迁移，意味着对黑盒推理 API 也能通过采样子集构建诊断器，无需访问权重或训练数据，适合在第三方模型上部署。

  - 通过分析不同后训练方法下的失败地形，可指导 fine-tuning 策略：若模型在特定失败类别上聚集，可针对性补充训练数据或调整偏好。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：推理模型测试时失败后，通常只会重采样增加计算，但这样丢弃了失败轨迹中的重要信号。有些失败源于采样不走运（重试有效），另一些是结构性错误（重试无效），还有一些需要改变轨迹而非简单重试。识别失败类型可更有效分配推理预算。

**方法**：提出三个问题级轨迹特征，完全基于失败轨迹的分布特征（如重采样后的答案分布熵、一致性等），不依赖轨迹文本。这些特征反映了可用干预（如重试、引导、纠错）下的可恢复性结构。通过聚类，将失败映射到稳定类别，刻画不同后训练方法的失败地形。进一步，基于特征构建训练无关的路由规则，将失败样本导向合适干预（重试、轻量引导或放弃）。

**结果**：在 GSM8K、MATH 等基准上，三个特征的聚类分类准确率达 84.3±4.3%，比多数类基线高 20%。在部署相关的 Steerable-Hard 子集（重试无效但有限干预可修复）上，路由规则使修复成功率提升 12.2%。特征及路由规则跨两个模型家族迁移有效。
