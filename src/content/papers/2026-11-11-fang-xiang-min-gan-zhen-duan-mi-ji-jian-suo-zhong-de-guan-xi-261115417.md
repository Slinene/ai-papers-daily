---
title: 'When Direction Matters: Diagnosing Relational Instruction Following in Dense
  Retrieval'
title_zh: 方向敏感：诊断密集检索中的关系指令遵循
authors:
- Zhanyu Wu
- Richong Zhang
affiliations:
- Beihang University, Beijing, China
- Zhongguancun Laboratory, Beijing, China
arxiv_id: '2611.15417'
url: https://arxiv.org/abs/2611.15417
pdf_url: https://arxiv.org/pdf/2611.15417
published: '2026-11-11'
collected: '2026-11-13'
category: Eval
direction: 指令遵循密集检索诊断
tags:
- Dense Retrieval
- Instruction Following
- Relational Reasoning
- Benchmark
- Evaluation
one_liner: 密集检索器处理方向性关系指令时存在系统性缺陷，SwitchIR 基准定位原因并验证可微调修复
practical_value: '- 在召回/检索链路引入自然语言指令（如“为农村诊所找远程医疗方案”）时，用方向翻转对（“A导致B” vs “B导致A”）构建困难负样本，检验模型是否真正编码关系方向，而不是靠词面或属性
  cues 通过。

  - 排查指令遵循失败时，采用 margin decomposition：分别计算方向敏感 query-document 交互和方向无关 pair preference
  的贡献；若后者过强，说明模型被通用相似度主导，需加强指令对齐训练。

  - 诊断性微调可用较少数据让模型学会关系方向并跨关系家族泛化，较大模型泛化更强；业务上可对因果、时序、包含等特定关系做小规模指令微调，提升客服问答/商品知识召回。

  - 用 LLM 辅助构建评测数据时，人工复核方向性样本，因为 LLM 本身可能忽略方向翻转；可借鉴 SwitchIR 的对照结构设计回归测试集，持续监控线上指令检索质量。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

## 动机

密集检索越来越强调能依据自然语言指令进行条件检索，但实际能力未经验证。该工作定位到一个具体弱点：当目标由词汇或属性线索区分时模型表现不错，一旦相关性取决于同一实体的方向性关系（如“A导致B” vs “B导致A”），模型就不可靠。

## 方法关键点

提出 SwitchIR 诊断基准，固定 query-document 对，翻转关系方向构造 Relational Flip，并与 Constraint Shift、Explicit Filtering 两类线索可用的对照条件比较。在代表性双塔和晚交互检索器上评测，同时构建 LLM 辅助、人工复核的现实变体。进一步用精确的 margin decomposition 把得分拆为方向敏感交互和方向不变 pair preference 两部分，定位失败原因；最后通过诊断性微调检验模型的可学性与跨关系家族泛化。

## 关键结果

主要联合指标在两个线索可用对照上很高，在 Relational Flip 上持续很低；LLM 辅助现实变体保持同样顺序。margin decomposition 显示，仅当方向敏感交互超过方向不变偏好时，两个方向才能都正确；实际中方向敏感变化常见，但对齐的交互通常太弱，无法克服方向不变的 pair 偏好。微调后模型可习得关系行为并跨关系家族泛化，较大模型泛化更强。
