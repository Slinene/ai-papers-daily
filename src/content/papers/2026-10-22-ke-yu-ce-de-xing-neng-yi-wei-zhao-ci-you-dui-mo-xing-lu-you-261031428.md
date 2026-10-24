---
title: Predictable performance is suboptimal, and what it means for model routing
title_zh: 可预测的性能意味着次优：对模型路由的启示
authors:
- Guanhua Zhang
- Moritz Hardt
affiliations:
- Max Planck Institute for Intelligent Systems, Tübingen
- Tübingen AI Center
arxiv_id: '2610.31428'
url: https://arxiv.org/abs/2610.31428
pdf_url: https://arxiv.org/pdf/2610.31428
published: '2026-10-22'
collected: '2026-10-24'
category: LLM
direction: 模型路由与级联优化
tags:
- model routing
- performance prediction
- self-confidence
- cascades
- LLM
one_liner: 证明性能预测仅在模型次优或预测器容量大时才优于模型自置信度，级联路由同理
practical_value: '- 模型路由基线选择：将候选模型自身的 self-confidence（输出概率）作为默认路由依据，不要盲目训练额外性能预测器；当模型已通过微调接近任务最优时，复杂预测器增益很小。

  - 如果业务中必须使用预测器（如小模型 + 大模型级联），把预测器资源分配给最弱的模型或最难的子任务，因为预测器优势与模型次优性正相关，模型越好增益越少。

  - 重校准可复用：训练出的性能预测器若优于模型自置信度，可通过 recalibration 将该优势直接转化为模型 log loss 改进，类似用预测器蒸馏/矫正模型的不确定性估计，提升线上校准和风险控制。

  - 级联路由设计：优先提升第一级模型本身（微调、领域适配）而非仅优化路由策略；当第一级模型足够强时，基于 self-confidence 的阈值路由与预测器路由差距缩小，工程更简单且更稳定。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM 能力与成本差异推动了自适应模型路由，通常依赖训练单独的性能预测器判断模型是否能正确回答。但预测器何时比模型自身的不确定性（self-confidence）更有用？本文以模型给出答案的概率为基线进行理论分析。

**方法关键点**：
- 首先证明任何优于模型自置信度的性能预测器，都可以通过重校准（recalibration）将其优势完全转化为模型 log loss 的改进，预测器优势等于 log loss 改善。
- 考虑预测器额外参数后，推导出优势上界由模型在任务上的次优性 + 预测器参数量带来的增益决定。
- 扩展到两模型级联：第一模型预测失败时路由到更强模型。

**关键结果**：
- 在 16 个语言模型、4 个基准上的实验表明：更次优的模型，预测器相对自置信度的优势更大；模型经过微调变好之后，优势缩小。
- 级联路由也呈现同样两个模式：基于预测器的路由在模型更次优时比基于置信度的路由提升更多，微调后差距减小。

结论：性能预测的价值与模型次优性紧密相关；对接近最优的模型，自置信度已足够，额外预测器增益有限。路由系统设计应更关注模型本身能力提升。
