---
title: 'Thinking Inertia: LLMs Keep Thinking When Told Not To'
title_zh: 思考惯性：LLM 被要求不思考时仍在思考
authors:
- Dianqiao Lei
- Kevin Qinghong Lin
- Pan Lu
- Philip Torr
- James Zou
affiliations:
- Tsinghua University
- University of Oxford
- Stanford University
arxiv_id: '2610.11765'
url: https://arxiv.org/abs/2610.11765
pdf_url: https://arxiv.org/pdf/2610.11765
published: '2026-10-07'
collected: '2026-10-13'
category: Eval
direction: LLM 推理行为评估与指令遵循
tags:
- LLM
- thinking mode
- instruction following
- evaluation
- reasoning
- no-thinking
one_liner: 系统评估 LLM 的“不思考”能力，提出三层指标并发现显式禁用推理无法可靠消除思维惯性
practical_value: '- 在电商/Agent 系统中若依赖“禁用 thinking”来节省推理开销，不能只看模型设置或提示词，需用空思考率、问题-预答相关度、显式推理率等指标做线上回归，才能避免隐性推理延迟。

  - 对搜索推荐 query 改写、客服 Agent 等场景，把开放生成改成先给候选答案或多选题形式，可显著提高“直接给答案”的合规率，减少推理 token 与耗时。

  - 评估 LLM 输出是否真的“无推理”时，可复用 LLM-as-judge 的 Explicit Inference Rate 指标，业务侧能低成本监控模型行为。

  - 若业务需要高准确度且答案空间开放，要接受“禁止推理”会带来准确率下降的 trade-off，设计时需评估延迟、成本与效果。'
score: 7
source: huggingface-daily
depth: abstract
---

## 动机
LLM 越来越多地提供显式“思考模式”，但“不思考”模式却缺乏系统研究。已有工作常用禁用思考模式或短轨迹作为“不思考”的代理指标，但这些并不可靠：禁用模式仍可能输出推理，长轨迹也可能只是填充文本而非真实推断。

## 方法关键点
论文将任意 LLM 响应规范化为“预答案轨迹 + 最终答案”，并提出三层评估指标：
- Empty-Thinking Rate：严格只输出答案的合规率；
- 指令感知的 Question–Pre-answer Relevance：问题与预答案轨迹的语义相关度；
- LLM-as-judge 的 Explicit Inference Rate：检测可见的显式推理。
这三层指标能区分“纯答案输出”“相关但非推理文本”“显式推理”。作者在 6 个 LLM、6 种提示干预、3 类问题（布尔、多选、开放）上评估。

## 关键结果
显式“不思考”控制无法可靠消除可见推理，模型表现出“思考惯性”：即使严格禁止，显式推理仍持续存在，且答案空间越开放越明显。准确率在布尔和多选任务上相对稳定，但开放式任务中“纯答案合规”与准确率存在 trade-off。将同样问题改写成提供候选答案的形式，能显著提高纯答案输出的比例。

结论：不思考是一项非平凡能力，不能仅靠模型设置或指令假设其生效，需要与推理能力一同系统评估。
