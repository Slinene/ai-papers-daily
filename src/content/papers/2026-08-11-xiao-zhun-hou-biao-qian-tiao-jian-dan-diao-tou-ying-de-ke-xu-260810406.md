---
title: Post-Calibration Reliability Reranking of Relevance Decisions via Label-wise
  Monotone Projection
title_zh: 校准后标签条件单调投影的可靠性重排序
authors:
- Inwoo Tae
- Yongjae Lee
affiliations:
- UNIST
- LinqAlpha
arxiv_id: '2608.10406'
url: https://arxiv.org/abs/2608.10406
pdf_url: https://arxiv.org/pdf/2608.10406
published: '2026-08-11'
collected: '2026-08-12'
category: RecSys
direction: 后校准可靠性重排 · 标签条件单调投影
tags:
- post-calibration
- reliability reranking
- label-wise monotone projection
- fallback routing
- relevance prediction
- selective prediction
one_liner: 用标签条件单调函数将校准置信度映射为正确性可靠性，不改原始预测，改善搜索/推荐系统的 fallback 路由和选择性预测
practical_value: '- **搜索/电商相关性预测的 fallback 路由**：校准后的置信度仍然隐藏标签条件的可靠性差异，可用标签独立单调函数重排预测风险，在预算有限时提高自动采纳的准确率。

  - **不改模型只改下游使用方式**：MRP 不修改原始预测和类概率，仅附加一个可靠性分数，适合已有校准管线的在线系统无侵入式升级。

  - **单调点阵实现**：采用 logit 域单调增量参数化，保证置信度越高可靠性越高的直觉，工程上简单、可解释、训练稳定。

  - **消融实验结论**：增益主要来自标签条件残差信号，而非全局置信度再映射，意味着可以在每个决策标签上单独建模可靠性曲线，而不是重新校准置信度。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
搜索、产品搜索、QA 检索等系统常为每个 query-candidate 对输出 relevance 标签和置信度，下游根据置信度决定直接采纳、路由到更重模型或转人工。普通校准让置信度与平均正确率对齐，但**同一置信度下不同预测标签的残差可靠性可能显著不同**，导致系统对某些决策过度信任或过早保守退出。该问题在固定决策（不改 top-1 预测）的 post-calibration 场景中尚未被专门处理。

## 方法
提出 **Label-wise Monotone Reliability Projection (MRP)**，不修改校准后的类概率向量和预测标签，仅学习标签条件单调函数 \(T_k(c)\) 将校准置信度 \(c\) 映射为决策正确率 \(q\)。
- **固定决策协议**：保持基础模型的 top-1 预测不变，后验校准器仅调整置信度。
- **标签条件单调曲线**：为每个预测标签 k 学习一个单调递增函数 \(T_k(c)\)，用二阶差正则平滑。
- **单调点阵实现**：在置信度轴上设 J=8 个节点，用 softplus 增量参数化保证单调，logit 域线性插值后 sigmoid 输出。
- **损失函数**：二值交叉熵拟合正确性 \(Z\)，加正则项。
- **可靠性重排序**：按估计错误概率 \(1 - T_{d(x)}(\hat{c}^A(x))\) 降序排列，用于 fallback、审核或选择性使用。
- **不改变**预测标签、类概率、全量准确率、ECE。

## 实验
- **6 个数据集**：Amazon ESCI、MSLR-WEB10K、Alloprof-Rerank、ESCI-Rerank-US、WANDS、SciDocs，覆盖产品搜索、Web 搜索、QA 检索、电商重排、科学检索。
- **基校准器**：Uncal.、Temperature Scaling、DIAG、Spline、h-cal、SMART。
- **核心指标**：正确性 NLL（NLLcorrect）、AUPR-Error、AURC、预算 fallback 下的选择性准确率 SelAcc@τ。
- **关键结果**：MRP 在所有数据集上平均改善 NLLcorrect 和 AURC，AUPR-Error 在多数数据集提升，尤其当标签条件残差信号强（如 MSLR-WEB10K，AUPR-Error 从 0.653 升到 0.906）；fallback 模拟中，保留最可靠 10% 时平均 SelAcc 提升 7.6 个百分点。
- **消融**：共享 1D 曲线或仅标签截距无法提升 AUPR-Error 和 AURC，证明增益源于**标签条件置信度-可靠性曲线**，而非全局置信度再映射。

## 核心结论
校准不能终结可靠性问题；相同置信度下不同 relevance 决策的残差正确率仍有差异，用标签条件单调投影可有效改善后校准预测的可靠性排序。
