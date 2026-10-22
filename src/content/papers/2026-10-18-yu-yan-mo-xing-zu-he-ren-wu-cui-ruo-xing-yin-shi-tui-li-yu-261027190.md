---
title: 'On the Fragility of Tasks under Composition: Implicit Budgeting in Language
  Models'
title_zh: 语言模型组合任务脆弱性：隐式推理预算的作用
authors:
- Chenpan Li
- Thies Brockmoeller
- Stefanie Jegelka
- Sharut Gupta
- Nikolaos Karalias
affiliations:
- TU Munich
- MIT CSAIL
arxiv_id: '2610.27190'
url: https://arxiv.org/abs/2610.27190
pdf_url: https://arxiv.org/pdf/2610.27190
published: '2026-10-18'
collected: '2026-10-22'
category: Reasoning
direction: LLM 推理预算与任务脆弱性
tags:
- implicit budgeting
- task composition
- reasoning tokens
- LLM evaluation
- cost-accuracy tradeoff
one_liner: 发现 LLM 在单 prompt 组合多任务时按比例压缩每任务推理 token，导致长推理任务更易出错，并可按脆弱性分组省 43% token
practical_value: '- LLM 工作流（如批量商品属性提取、query 意图分类、评论摘要）避免把需要长 CoT 的高难度任务和简单任务塞进同一个
  prompt；长推理任务单独调用或降低组合度，减少组合脆弱性。

  - 利用 fragility 分组调度：把相似推理预算需求的任务放在同一批 prompt，能在不损失准确率下显著降低 token 成本（论文 43%），适合线上成本敏感场景。

  - 监控单任务在组合前后的 token 消耗与错误率变化，识别“脆弱任务”；对关键链路（如广告文案生成、排序解释）设置每任务最小推理预算或独立验证。

  - 在 Agent 规划时注意每个子任务被隐式压缩，设计更短推理路径或为关键决策提供单独预算/步骤。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代 LLM 常需在一个 prompt 中同时完成多个任务。即使模型能可靠地单独解决每个任务，组合后错误率仍大幅上升，且不能完全用独立错误累积解释。

**方法关键点**：作者在 open-weight 模型和 Claude Opus 5 上对比数学与语言任务在独立执行和组合执行下的表现，重点分析每个任务实际消耗的推理 token。结果指向一种隐式 thinking budget：组合时每个任务获得的推理 token 按同一比例缩减，即使上下文窗口远未用满。需要更长推理轨迹的任务因此更容易低于“必需推理量”而失败，表现更脆弱；而单独执行时非脆弱任务获得过多推理，存在明显计算浪费。

**关键结果数字**：组合会按比例压缩每任务推理 token；按任务 fragility 分组可以操纵隐式预算，在数学和语言任务上减少 43% token 使用，同时保持准确率。
