---
title: 'AdaPRA: Process Reward Agents with Adaptive Rubrics for Data Science'
title_zh: 面向数据科学任务的自适应评分准则过程奖励智能体
authors:
- Atharva Naik
- Vivek Chari
- Pol Llado
- Daniel Fried
- Carolyn Rosé
- Benjamin Van Durme
- Sam Thomson
- Justin Svegliato
affiliations:
- Carnegie Mellon University
- Microsoft
arxiv_id: '2610.33245'
url: https://arxiv.org/abs/2610.33245
pdf_url: https://arxiv.org/pdf/2610.33245
published: '2026-10-22'
collected: '2026-10-29'
category: Agent
direction: Agent 过程监督 · 自适应评估准则
tags:
- Process Reward
- Agent
- Adaptive Rubrics
- Process Supervision
- Data Science
- LLM
one_liner: AdaPRA 用自适应 rubrics 的过程奖励智能体审计并纠正数据科学 agent 的中间过程错误，显著提升排行榜百分位
practical_value: '- 用可执行的检查（而非仅看轨迹）构建过程监督信号：在电商/推荐 agent 中可对召回策略、query 改写、特征拼接等中间步骤做"提交完整性""防泄漏验证""预算利用"等自动核对，提前捕获
  silent errors。

  - 自适应 rubrics：从简单任务或历史成功运行中挖掘 rubric 模板，再按任务难度/失败样本动态调整；对应推荐系统可按场景或品类生成评估检查项，并利用线上
  badcase 持续更新。

  - 跨模型迁移：用强模型运行结果挖掘 rubrics 去监督弱模型，或反之；可用于 reward model 构建、蒸馏或 RLHF，降低人工标注成本。

  - 持久化 workspace 与跨尝试记忆：多次尝试间缓存探索结果、失败原因和已试策略，避免重复跑 baseline 和 EDA；推荐 agent 或搜索 agent
  可复用已尝试的召回/排序策略，优化固定预算利用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**  
数据科学 agent 在端到端 ML 流程中仍与人类水平有较大差距，主要来自过程错误：简化偏差（停在第一个可用 pipeline）、验证不可靠、训练目标不匹配、验证集泄漏、预算利用差（每次尝试重复跑相同 EDA 和 baseline）。这些错误常常是沉默的——提交结果有效但轨迹看不出问题。  

**方法关键点**  
AdaPRA 构建一个持久化编码 agent harness，在同一个任务的多次尝试间积累知识；引入 rubric 引导的过程监督，由过程奖励 agent 通过执行检查来审计轨迹和工作区，并自适应每个任务的 rubrics。rubric 从简单任务播种，能泛化到更难任务，自适应进一步提升性能。  

**关键结果**  
在 DSPredict 基准上，每个任务 5 次尝试，AdaPRA 将 80B Qwen 模型的排行榜百分位在 Easy 上提升 24.5 点、Hard 上提升 14.8 点，同时减少过程错误。用某个基座模型运行结果挖掘出的 rubrics 能监督另一个模型（DeepSeek-V3.2），且 AdaPRA 超过 DataPRM。代码已开源。
