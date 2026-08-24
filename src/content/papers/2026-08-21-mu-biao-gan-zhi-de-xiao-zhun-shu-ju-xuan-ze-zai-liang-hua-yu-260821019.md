---
title: Target-Aware Calibration Data Selection for Preserving Uncertainty in Quantized
  Language Models
title_zh: 目标感知的校准数据选择：在量化语言模型中保持不确定性
authors:
- Zhen Yang
- Sizai Hou
- Kaiwen Zheng
- Yaofang Liu
- Liang He
- Yixuan Chen
- Kangning Cui
affiliations:
- Yale University
- The Hong Kong University of Science and Technology
- The Hong Kong University of Science and Technology (Guangzhou)
- City University of Hong Kong
- Shanghai Institute of Optics and Fine Mechanics
arxiv_id: '2608.21019'
url: https://arxiv.org/abs/2608.21019
pdf_url: https://arxiv.org/pdf/2608.21019
published: '2026-08-21'
collected: '2026-08-24'
category: LLM
direction: LLM 量化校准与不确定性保持
tags:
- Quantization
- Uncertainty Preservation
- Calibration Data Selection
- Post-Training Quantization
- DPQ
one_liner: 提出 DPQ 配方族，用全精度预测选择高不确定样本与通用锚点构建目标对齐的量化校准集，保持不确定性行为。
practical_value: '- 在电商/广告/Agent 场景部署量化 LLM 时，如果下游逻辑依赖 confidence/abstention（例如低置信度转人工、拒答策略、阈值决策），校准时必须针对业务目标分布选择数据，不能复用通用随机校准集。

  - 可直接借鉴 DPQ 的“高 doubt 样本 + 通用锚点”思路：用全精度模型对线上日志打分，筛选边界难例（低 margin、高 entropy、错分类样本）加入校准数据，再混合一定比例通用样本，以保持量化后模型在关键决策边界附近的不确定性排序。

  - 不同部署目标需要不同校准配方：如果关心“可回答性边界”（如 FAQ/客服拒答），可增加高怀疑样本比例（类似 DPQ-r75）；如果更关心广泛分类/选择题场景，应选用较温和或单信号（confidence-only
  / entropy-only）的校准集。

  - 该方法属于轻量预量化数据选择，不改量化算法，可配合 GPTQ/AWQ 等主流 PTQ 框架，工程改造成本低，便于在推理优化阶段做 A/B 对比验证。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：量化在 LLM 部署中普遍使用，但量化会改变模型的不确定性行为（confidence、margin、abstention），而这一目标在现有量化校准数据选择中很少被单独优化。不同部署场景强调输入分布的不同区域，单一校准配方难以适配所有不确定性保持目标。作者将校准数据选择形式化为“目标依赖的不确定性保持”问题，定义分布保持与边界保持风险，并给出 mixture-mismatch 论证说明不存在通用最优校准集。

**方法关键点**：提出 DPQ（Doubt-Preserving Quantization），一种轻量预量化方案族。核心是利用全精度模型预测结果，构造与目标对齐的校准混合数据：选取高怀疑（high-doubt）样本（如低 margin、高 entropy、错误预测等）与通用锚点样本按照一定比例混合，再进行量化校准。不同目标对应不同比例或单一信号变体，例如 DPQ-r75、DPQ-r50、confidence-only、entropy-only。

**关键结果**：在 8 个语言模型、9 个 NLP 基准和 22 个对比方法上，最优固定配方随保持目标变化。DPQ-r75 在 SQuAD2 可回答性边界保持上最优；DPQ-r50、confidence-only、entropy-only 等较温和或单信号变体在广泛多项选择 QA 行为保持上更好。结论：量化校准数据应针对部署所需保持的具体全精度分数行为选择，而不是作为固定工程细节。
