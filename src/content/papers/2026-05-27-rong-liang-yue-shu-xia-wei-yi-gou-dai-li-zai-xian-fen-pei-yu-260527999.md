---
title: Learning to Assign Prediction Tasks to Agents with Capacity Constraints
title_zh: 容量约束下为异构代理在线分配预测任务
authors:
- Shang Wu
- Saatvik Kher
- Padhraic Smyth
affiliations:
- University of California, Irvine
arxiv_id: '2605.27999'
url: https://arxiv.org/abs/2605.27999
pdf_url: https://arxiv.org/pdf/2605.27999
published: '2026-05-27'
collected: '2026-05-28'
category: Agent
direction: Agent上下文任务分配与在线优化
tags:
- task assignment
- capacity constraints
- contextual bandits
- online learning
- human-AI collaboration
- LLM routing
one_liner: 提出在线上下文多臂赌博框架，在代理容量约束下动态学习其专长并路由任务，显著优于非上下文基线
practical_value: '- 在电商客服/专家系统路由中，可以将不同技能的人工客服和AI客服视为异构代理，利用在线上下文学习（如用户意图、商品品类）分配任务，同时通过虚拟队列强制满足每个代理的工作量上限，防止过载。

  - 在多LLM推荐生成场景中，各LLM对不同类目或用户群体的表现存在差异，可借鉴在线树模型估计上下文奖励，结合队列惩罚项（`at = arg max(μ_a(x_t)
  - η Q_t,a)`）实现轻量级路由，满足API调用容量限制。

  - 工程实现上，贪婪策略在容量约束下已具有与汤普森采样相当的探索效果，可降低在线推理的复杂度；虚拟队列机制简单易集成，适合实时决策。

  - 核心洞察：当代理的专长在上下文中互补时，联合策略可以超越单个最佳代理的边际性能，这是仅靠离线或非上下文路由无法捕获的，为“人机互补”或“多模型路由”提供了理论支撑。'
score: 10
source: arxiv-cs.HC
depth: full_pdf
---

**动机**：在医疗影像诊断、LLM路由等实际场景中，AI和人类代理在不同上下文中表现出差异化的专长，且每位代理存在工作负荷限制（如防止疲劳）。传统离线学习或忽略上下文的随机分配难以适应分布漂移和容量约束，导致整体表现受限。为此，需要在满足长期容量约束的前提下，在线学习代理的上下文相关性能并动态分配任务，以最大化总体准确率。

**方法关键点**：
- 问题建模为上下文多臂赌博（contextual MAB），奖励为分类准确率二值信号。
- 使用逻辑回归（拉普拉斯近似高斯后验）或随机森林（自举集成）在线估计每个代理的上下文条件奖励 `μ_a(x)`。
- 通过虚拟队列 `Q_{t,a}` 追踪实际分配与目标容量 `α_a` 的偏差，决策时融入惩罚项 `η Q_{t,a}`，形成调整奖励 `μ_a(x_t) - η Q_{t,a}`，等价于动态学习影子价格。
- 实现汤普森采样（TS）和贪婪策略两种探索方式，后者在容量约束的隐式探索下表现出与TS相近的性能。

**关键实验**：
- 数据集覆盖图像（Camelyon17、ImageNet16H）、表格（Bank、Credit、Coupon、Cardio）、文本（MMLU）等多种模态。
- 基线为非上下文随机分配（按固定容量概率）。
- 主要结果：在所有数据集上，上下文策略（逻辑/树，TS/贪婪）均系统性地降低错误率。例如，在Camelyon17上，当Agent 1容量为0.5时，树型贪婪策略使错误率从非上下文的≈0.25降至≈0.20；在Bank数据集上，错误率从≈0.35降至≈0.16。当容量恰好匹配代理专长分布时，组合策略可超越最佳单代理的边际错误率（如MMLU上LLaMA-13B单代理0.53，组合后最低≈0.50）。微批量实验表明，中等批量大小可进一步平衡探索与延迟。

最值得记住的一句话：在线学习代理的上下文专长，并在容量约束下动态路由，可以获得超越非上下文分配的系统性增益，甚至在代理能力互补时，组合表现优于任何单个代理。
