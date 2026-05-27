---
title: Natural Language Query to Configuration for Retrieval Agents
title_zh: 自然语言查询到检索智能体配置的动态选择
authors:
- Melissa Z. Pan
- Negar Arabzadeh
- Mathew Jacob
- Fiodar Kazhamiaka
- Esha Choukse
- Matei Zaharia
affiliations:
- UC Berkeley
- University of Washington
- Microsoft Azure Research - Systems
arxiv_id: '2605.27361'
url: https://arxiv.org/abs/2605.27361
pdf_url: https://arxiv.org/pdf/2605.27361
published: '2026-05-26'
collected: '2026-05-27'
category: Agent
direction: 检索智能体配置优化
tags:
- Query2Conf
- Retrieval Agents
- Configuration Optimization
- Cost-Quality Tradeoff
- Workload-Specific Characteristics
- Pareto Frontier
one_liner: 提出 BRANE：用 LLM 提取查询特性并训练 per‑configuration 预测器，在推理时按准确率目标选择管道配置，大幅节省成本
practical_value: '- **动态配置替代固定管道**：电商搜索、客服问答等场景可对每个查询动态选择检索策略、LLM、文档数等，用 BRANE 的成本‑质量帕累托曲线在满足准确率目标时降低成本。

  - **LLM 生成的 workload‑specific 二值特征**：比通用嵌入更能捕捉查询细粒度差异（如 FinanceBench 领域），可直接用作路由器的输入，节省特征工程成本。

  - **轻量 per‑configuration 预测器**：使用 tabular 模型（如 LightGBM）在小样本（几百条）下效果优于端到端微调 BERT
  或 Qwen‑4B，适合需要快速冷启动的垂直领域。

  - **模糊帕累托剪枝**：在配置空间大时，只保留接近帕累托前沿的配置训练预测器，大幅减少训练和推理开销，适合多检索器、多 LLM 的商业系统。

  - **无损重标定**：上线后只需调整 λ 即可在准确率和成本之间切换，无需重新训练，适合随时切换预算模式（如大促期间优先准确，日常优先成本）。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现代检索智能体（如 RAG 系统）有许多可配置选项：LLM 型号、检索器、返回文档数、合成策略等。通常这些是为整个工作负载固定调优，但不同查询的最优配置差异极大——简单的查询无需复杂管道，而复杂推理需要多步检索。静态配置会浪费成本或损失准确率。该工作提出 **Query2Conf** 问题：给定自然语言查询和准确率目标，从预定义的配置空间中选择满足目标且成本最低的管道。

### 方法关键点
- **查询表征**：用 LLM（如 GPT‑5‑mini）从少量样本中自动提出 workload‑specific 的二值特征（如 `involves_regional_cuisine`），然后用更便宜的 LLM 为所有查询打标，形成特征向量 `F(q)`。
- **Per‑configuration 预测器**：对每个经模糊帕累托剪枝保留的配置 `c`，训练一个轻量分类器（逻辑回归、树模型等），输入 `F(q)`，输出 `c` 能正确回答查询的概率。
- **推理时选择**：对于目标准确率，通过拉格朗日松弛选择使 `ˆp_c(f(q)) – λ·cost(c)` 最大的配置。λ 离线标定，线上可无训练重配。
- **模糊帕累托剪枝**：只保留与帕累托前沿在准确率容差 τ_acc 和成本容差 τ_cost 内接近的配置，将需训练的预测器数量减少一个数量级。

### 关键实验
- **数据集**：MuSiQue（多跳 QA）、BrowseComp‑Plus（深度研究）、FinanceBench（金融 QA）。
- **对比基线**：静态最优配置（Murakkab）、LLM‑only 路由（Carrot）、规则调度（METIS）、检索策略选择（Adaptive‑RAG）、端到端微调 LLM。
- **核心结果**：
  - 在匹配最高准确率配置的精度下，BRANE 在 MuSiQue 节省 89.4%、BrowseComp‑Plus 节省 81.7%、FinanceBench 节省 8.1% 的成本。
  - LLM 生成的 workload‑specific 特征是唯一在三个基准上均达到 100% 准确率目标的表征方式；通用嵌入在 BrowseComp‑Plus 和 FinanceBench 上无法达到该目标。
  - 轻量 per‑configuration 预测器在几乎全部成本节省单元格上优于端到端微调的 BERT/Qwen‑4B，特别是在小样本下。

### 核心一句话
> 将查询离散化为 workload‑specific 的二值特征，再为每个管道配置训练一个轻量校正预测器，可以在不牺牲准确率的前提下将检索智能体的服务成本降低最高 89%。
