---
title: 'Generalization Is Stability, Not Accuracy: Multi-Axis Evaluation of LLMs'
title_zh: 泛化是稳定性而非准确率：LLM 的多轴评估
authors:
- Nagham Omar
- Mahmoud Jabarin
- Maya Rozenshtein
- Rom Himelstein
- Avi Mendelson
- Amit LeVi
affiliations:
- Technion – Israel Institute of Technology
arxiv_id: '2610.01428'
url: https://arxiv.org/abs/2610.01428
pdf_url: https://arxiv.org/pdf/2610.01428
published: '2026-09-30'
collected: '2026-10-04'
category: Eval
direction: LLM 泛化评估 · 稳定性度量
tags:
- LLM
- Generalization
- Evaluation
- Stability
- Prompt Variations
- Benchmarking
one_liner: 提出 SAGO 框架，从生成一致性、内部激活、置信度与响应镜像等多轴度量 LLM 对同一输入变体的行为稳定性。
practical_value: '- 业务中评估生成式推荐、Query 改写、Agent 决策时，不要只用单 prompt 准确率；应构造同一意图的多种表达（措辞、长度、格式、噪声），把输出一致性作为上线门槛。

  - 借鉴 SAGO 多轴思想，将内部激活、置信度与生成结果分别监控：它们可能揭示独立失败模式，只盯最终输出会漏掉隐性漂移。

  - 模型升级或微调后，用跨数据集稳定性排名代替单一 benchmark 排名；论文显示跨数据集变化会反转模型排名，单一评估容易误判。

  - 将稳定性测试做成 CI 回归：对固定语义等价集定期跑，捕获 prompt 模板变更或 LoRA 微调带来的泛化退化。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：现有 LLM 泛化评估常以单一 prompt 格式或任务上的聚合准确率代表鲁棒性，混淆了整体 benchmark 性能与真实泛化能力。

方法关键点：提出 Stability-Aware Generalization Objective（SAGO），在单个样本级别、跨多种输入变体、跨模型行为维度度量行为变化。具体维度包括生成一致性、内部激活、置信度和响应镜像，避免把性能压缩成可被窄训练刷高的单一分数。该框架不把泛化当准确率，而是当稳定性：同一输入的不同语义等价表达下，模型行为变化越小，泛化越好。

关键结果：多款常用模型表现出统计显著且持续的泛化不稳定；没有任何模型在各维度均匀泛化；不同行为轴捕获独立的失败模式；跨数据集变化会反转模型排名。
