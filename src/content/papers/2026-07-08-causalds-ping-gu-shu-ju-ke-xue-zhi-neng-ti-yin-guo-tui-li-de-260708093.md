---
title: 'CausalDS: Benchmarking Causal Reasoning in Data-Science Agents'
title_zh: CausalDS：评估数据科学智能体因果推理的合成基准
authors:
- Andrej Leban
- Yuekai Sun
affiliations:
- Department of Statistics, University of Michigan
arxiv_id: '2607.08093'
url: https://arxiv.org/abs/2607.08093
pdf_url: https://arxiv.org/pdf/2607.08093
published: '2026-07-08'
collected: '2026-07-10'
category: Eval
direction: 因果推理基准 · 数据科学Agent评估
tags:
- Causal Reasoning
- Benchmark
- Data-Science Agent
- Tool Use
- Abstention
- LLM
one_liner: 提出通过合成结构因果模型与真实背景故事评估LLM在数据科学管线中的因果推理、工具使用与弃权能力
practical_value: '- 在电商搜索推荐中，可借鉴其**合成SCM+观测噪声**生成评估数据的方法，构建针对因果推断类A/B测试分析、归因模型的离线评测集，避免使用线上真实数据时的数据泄露与鹦鹉风险。

  - **弃权作为第一类评分结果**的设计可直接迁移到Agent辅助的数据分析产品中：当置信度不足或信息缺失时，要求Agent主动声明“无法回答”，提升输出可靠性，尤其适用于策略归因、指标异动分析等易出错的场景。

  - 联合评估**因果推理+编码+工具使用**的框架，能用于筛选适合数据科学Agent的LLM，确保其在推荐系统复杂分析（如效果评估、特征因果效应）中既能写出正确的分析代码（如do-calculus实现），又能正确调用pandas、因果库等工具。

  - 故事与数据成对生成、覆盖Pearl三层问题的方法，可以启发设计**多层级因果问答**的评测体系，检验Agent在描述性、预测性、反事实任务上的表现，避免仅关注预测准确率而忽略因果推理深度。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有LLM评测基准割裂，因果推理基准缺乏真实数据分析，数据分析基准缺乏因果生成结构，且多基于模板变化而非系统合成。数据科学Agent需同时具备因果推理、编码、工具使用与不确定性量化能力，却无对应评测。  
**方法**：引入CausalDS，每个实例由**采样的结构因果模型(SCM)**、合成观测数据及模拟真实领域的自然语言故事构成；可选从真实数据分布初始化组件，保持经验结构同时完全合成以避免“因果鹦鹉”。从每个场景派生任务覆盖Pearl三层（关联、干预、反事实），预测任务通常在第一层。多数任务包含编码环节，模型需使用多个工具处理**观测噪声**（由观测模型生成）。关键设计：将**弃权**（识别问题无有效答案）作为主要评分结果之一。  
**结果**：基准设计本身未报告模型性能数字，但提供跨符号因果推理、数据科学实操、不确定性估计、弃权判断和工具使用的统一评估框架，期望暴露LLM在真实因果分析中的薄弱点。
