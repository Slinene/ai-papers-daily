---
title: 'Ask Before You Optimize: Dynamic Pre-Formulation Clarification for Interactive
  Optimization'
title_zh: 先澄清再优化：动态预建模澄清的交互式优化框架
authors:
- Sihan Ge
- Yichen Lin
- Chenyu Zhou
- Jianghao Lin
- Tao Yao
- Dongdong Ge
affiliations:
- Cardinal Operations
- Shanghai Jiao Tong University
arxiv_id: '2609.05258'
url: https://arxiv.org/abs/2609.05258
pdf_url: https://arxiv.org/pdf/2609.05258
published: '2026-09-03'
collected: '2026-09-07'
category: Agent
direction: LLM Agent 交互式优化澄清
tags:
- LLM
- Agent
- Clarification
- Benchmark
- Operations Research
one_liner: 提出OR-Clarify基准与InterOPT两阶段框架，在优化建模前主动识别缺失槽位并决定追问或停止
practical_value: '- 在营销/广告预算分配、促销优化等业务自动化中，将需求澄清抽象为“槽位恢复”：预定义目标函数、约束、业务规则等关键槽位，用多选或填空式追问替代开放问答，可显著降低交互成本并减少错误建模。

  - 借鉴 InterOPT 的两阶段设计：先识别 formulation-critical 未解决槽位，再依据槽位覆盖度/信息增益决定继续追问还是停止，避免过度打扰用户；可嵌入电商广告计划
  Agent 的需求确认环节。

  - 用“silent assumptions”指标兜底：跟踪模型未经用户确认就默认的关键假设，在生成广告投放模型或 SQL 前强制校验，防止预算、排期等约束被静默填错。

  - 对交互式推荐/搜索澄清场景：当用户 query 或目标模糊时，可以基于预定义维度（价格带、类目、目标 KPI）生成候选澄清项，而不是直接生成推荐或优化方案，提升准确率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：真实 OR 需求常不完整，缺少目标函数、约束或业务规则会直接改变最终数学模型；但现有 LLM 建模评估大多假设输入已完整，忽略智能体在建模前是否知道何时需要澄清。

**方法**：论文构建 OR-Clarify 基准，任务只给出部分公开问题描述，隐藏结构化槽位，通过有限轮次与模拟用户交互来评估智能体。指标包含槽位恢复率、停止行为、静默假设和交互成本，支持开放回答与选项式澄清两种模式。提出的 InterOPT 采用两阶段框架：先识别尚未解决的 formulation-critical 缺口，再根据这些缺口决定是否继续追问下一题或停止。

**关键结果**：在选项式实验中，InterOPT 的精确槽位恢复率显著超过所有基线；在开放回答场景下与已有强方法保持可比。论文将 OR 辅助重新定义为“选择性完整性决策”：需要时澄清、准备好时停止，并量化仍缺失的信息。
