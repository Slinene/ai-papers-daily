---
title: 'Codifying the Judge: Scalable Evaluation via Program Distillation'
title_zh: 将评判逻辑代码化：通过程序蒸馏实现可扩展评估
authors:
- Tzu-Heng Huang
- Shengqi Qiu
- Frederic Sala
affiliations:
- University of Wisconsin-Madison
arxiv_id: '2607.22561'
url: https://arxiv.org/abs/2607.22561
pdf_url: https://arxiv.org/pdf/2607.22561
published: '2026-05-28'
collected: '2026-07-29'
category: Eval
direction: 评估 · 程序蒸馏
tags:
- Program Distillation
- LLM-as-a-judge
- Evaluation
- Reward Model
- Scalability
- Program Synthesis
one_liner: 将LLM评判逻辑蒸馏为可解释的程序委员会，实现低成本、透明评估，匹配13B模型性能，并产生廉价奖励信号
practical_value: '- 在推荐系统的离线评估或奖励信号生成中，可借鉴程序蒸馏思路：用少量 LLM 标注数据蒸馏出可解释的程序化评判器，替代昂贵 API，大幅降低标注成本（如
  reward model 训练）。

  - 程序委员会聚合和置信度回退路由可迁移到多模型融合场景：多个简单规则/模型组成委员会，低置信度样本自动升级至复杂模型，平衡成本与质量。

  - 程序化评判透明可编辑，适合电商推荐中需要业务解释性的场景：评估标准（如“推荐理由是否吸引点击”）可直接编码为规则，方便运营调整。

  - 用于 reward model 蒸馏时，程序标签成本仅为专有 LLM 的 1/100，且性能更优，可为推荐系统的生成式奖励训练提供高效方案。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：LLM-as-a-judge 面临推理成本高、延迟大、决策不透明和系统性偏见等挑战，限制其在大规模评估中的可扩展性与可靠性。
方法：提出 PAJAMA 系统，通过程序蒸馏将 LLM 评判逻辑合成为一组可执行的程序化评委（programmatic judges），对候选样本直接评分。采用委员会机制聚合多个程序决策，并引入置信度估计，对低置信度样本可选回退到 LLM 进行最终裁决。整套流程无需在评估阶段调用 LLM，程序本身透明、可检查且可编辑。
结果：在五个评估数据集和四个模型家族上，程序化评委能匹配 13B 规模 LLM 评判的准确率。当用程序输出作为路由信号时，PAJAMA 同时提升准确率和吞吐量，推进 Pareto 最优曲线。在 RewardBench 上，从程序裁决蒸馏出的奖励模型性能超过用专有 LLM 标签训练的模型，API 成本降低两个数量级。
