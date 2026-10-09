---
title: 'MARGIN: Runtime Confidence Calibration for Multi-Agent Foundation Model Coordination'
title_zh: MARGIN：多Agent基础模型协调的运行时置信度校准
authors:
- Joss Armstrong
affiliations:
- Ericsson
arxiv_id: '2605.22949'
url: https://arxiv.org/abs/2605.22949
pdf_url: https://arxiv.org/pdf/2605.22949
published: '2026-10-07'
collected: '2026-10-09'
category: MultiAgent
direction: 多Agent置信度在线校准
tags:
- confidence calibration
- multi-agent systems
- foundation models
- online learning
- distribution shift
one_liner: 提出 MARGIN，通过运行时增量归一化按置信度分段学习模型特定校准，无需重训或留出校准集，提升多Agent决策准确率
practical_value: '- 多模型投票/加权融合场景（如多个LLM生成推荐理由、多路召回结果合并）可用 MARGIN 的思路：按置信度分桶跟踪近期准确率与声称置信度的比值，用比值修正该桶的置信度，稀疏桶向模型级估计收缩，避免单个桶样本过少导致校准不稳定。

  - 适用于需要在线适应 workload 变化的系统：无需重训模型或留出固定校准集，只需在每次获得正确性反馈后更新对应置信度桶的统计量，适合电商/广告中持续流入标注数据的场景。

  - 工程实现上，可维护滑动窗口或指数衰减的准确率/置信度比率，对每个 responder 分别维护，用校正后的分数作为加权依据；冷启动时使用模型级估计作为先验，逐步过渡到分桶校准。

  - 注意前提：必须能获得候选答案的正确性反馈（如用户点击、转化作为隐式反馈），否则该方法不可直接用；对于无反馈的推荐排序阶段，可考虑用代理指标替代。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：协调异构基础模型答案时，不同模型的自报置信度含义不一致，且工作负载变化使静态校准失效。需要一种运行时校准方法，在不重训模型、不要求留出校准集的前提下，根据已观察到的答案结果学习模型特定的置信度修正。

方法关键点：MARGIN 在运行时跟踪各模型的近期准确率和声称置信度，按置信度分桶（confidence bands）；用桶内准确率与声称置信度的比值作为修正因子，对报告置信度进行校正；对样本稀疏的桶，将其校正向模型级估计收缩，避免过度拟合；校正后的分数用于加权候选答案进行集体决策。

关键结果：在 BigCodeBench 上，模型平均置信度与准确率负相关，正确/错误响应对中选择更自信的响应者表现低于随机。与五个在线校准基线（接收相同反馈并保留学习状态）对比，MARGIN 在两个代码生成分布转移和一个问答转移中取得更低的后转移期望校准误差，另一个问答对比不明确。在代码生成协调实验中，校准改善了正确响应排序，在三个基准中的两个上答案选择准确率分别提高 4.3 和 14.0 个百分点。
