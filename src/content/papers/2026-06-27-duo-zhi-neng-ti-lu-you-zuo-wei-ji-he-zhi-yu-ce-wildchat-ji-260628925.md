---
title: 'Multi-Agent Routing as Set-Valued Prediction: A WildChat Benchmark and Cost-Aware
  Evaluation'
title_zh: 多智能体路由作为集合值预测：WildChat 基准与成本感知评估
authors:
- Ananto Nayan Bala
- Faisal Muhammad Shah
affiliations:
- Ahsanullah University of Science and Technology
arxiv_id: '2606.28925'
url: https://arxiv.org/abs/2606.28925
pdf_url: https://arxiv.org/pdf/2606.28925
published: '2026-06-27'
collected: '2026-06-30'
category: Agent
direction: 多智体路由的集合预测与成本权衡
tags:
- Multi-Agent Routing
- Set-Valued Prediction
- Benchmark
- Cost-Aware
- Supervised Router
- Agent Selection
one_liner: 将多智能体路由建模为集合预测问题，构建基准并引入成本感知评估协议，证明监督路由显著优于零样本 LLM
practical_value: '- 将路由建模为集合预测而非 Top-1 选择，更贴合真实多步查询需求，可直接采用 Precision/Recall/F1/Jaccard
  等集合指标评估。

  - 在固定智能体目录下，简单线性多标签分类器是强实用基线；无需大模型即可获得较高路由精度，适合低延迟场景。

  - 成本约束场景下，在监督打分器之上叠加 Weighted Agent Routing (WAR) 后处理层，能通过成本 tier 阈值调整有效提升效用，且实现轻量。

  - 可借鉴 capability-coverage 仿真方法，在离线评估路由系统时模拟智能体失败对系统鲁棒性的影响。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：多智能体系统需根据用户查询选择合适智能体，且一个查询往往需要多个智能体协作，存在过度选择的执行成本问题，但现有工作很少将路由视为多标签集合预测并引入成本感知评估。

**方法**：基于 WildChat 构建含 3,000 条提示、12 个固定智能体目录的基准，使用 AI 辅助启发式标注并进行多标签重平衡。评估协议综合了集合级指标（Precision、Recall、F1、Jaccard、Exact Match）、延迟、执行导向的能力覆盖仿真，以及基于 ordinal 成本 tier 的约束加权路由设置。对比方法包括最近邻匹配、线性多标签分类、依赖感知基线、微调编码器（BERT）、零样本 LLM，以及提出的 Weighted Agent Routing (WAR) 后处理层——它根据成本 tier 将打分转换为带阈值的选择。

**结果**：监督路由器大幅优于最近邻和零样本 LLM 路由。微调编码器在无约束下达到最高集合精度，线性多标签模型是更实用且强大的基线。在成本约束下，WAR 叠加于强监督打分器上能提升效用，其中 Encoder+WAR 收益最大。该基准和评估协议支持固定目录多智能体路由的精度-成本权衡的复现研究。
