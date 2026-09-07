---
title: Necessary or Sufficient? Evaluating LLM Explanations With Behavioural Evidence
title_zh: 评估LLM解释的必要性与充分性：基于行为证据
authors:
- Urja Pawar
- Rajitha Ramanayake
- Nabeel Kemal
- Ashwin Kandath
- Owen O'Neill
- Guillaume Bourgeon
- Houssem Chatbri
affiliations:
- BNY
arxiv_id: '2609.05385'
url: https://arxiv.org/abs/2609.05385
pdf_url: https://arxiv.org/pdf/2609.05385
published: '2026-09-04'
collected: '2026-09-07'
category: Eval
direction: LLM解释可靠性评估 · 黑盒干预
tags:
- LLM explanations
- necessity
- sufficiency
- black-box evaluation
- agent oversight
- counterfactual
one_liner: 用黑盒干预度量LLM解释因子的必要性与充分性，发现Top-3因子与行为影响仅中等相关且漏报明显
practical_value: '- 对带解释的LLM推荐/决策组件不要直接信任其cited factors：落地前用离线黑盒干预抽检，分别计算必要性（改因子输出变）和充分性（只留因子输出不变），用Spearman相关与未引用因子超越率做健康度指标。

  - 在Agent oversight或风险提示场景，可把这类行为证据测试做成回归评估：每次prompt或模型版本更新后跑一批case，若Top-3因子与实际影响相关性明显下降，说明解释质量漂移，需触发人工审查。

  - 电商推荐/广告中若用LLM生成“为什么推荐该商品/广告”的解释，可借鉴充分性分数筛选真正稳定的因子；充分性高的因子更适合作为后续规则、动态定价或供给控制的依据，而不是直接相信模型口述的原因。

  - 模型给出的Top-3因子漏报率较高（advisor场景约58%），因此除Top-3外应保留更多候选因子并通过干预分数排序，再决定哪些进入监控或诊断面板。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

动机：Agent workflow 中LLM组件常同时输出动作建议与解释因子，操作者会用这些因子做监控、诊断或升级判断。但“模型说的重要因素”是否真的驱动了行为，缺少黑盒验证。该工作区分两种解释：必要性（改变该因子会改变输出）和充分性（只保留该因子、移除其他可变信息仍能保持输出），并用受控黑盒干预测量。

方法关键点：在两类合成场景——顾问推荐和prompt危害/风险判定——让模型输出决策及Top-3影响因子。对每个因子做干预：改变它测必要性，保留它并移除其他可变成分测充分性；统计输出变化/保持频率得到分数，再与模型引用的排序计算Spearman相关，并统计未引用因子是否超过最低引用因子。

关键结果：8个Claude/GPT/Gemini模型上，顾问推荐中引用排序与必要性、充分性的平均Spearman相关分别为0.349和0.354；prompt监控为0.431和0.580。顾问场景57.6%（必要性）和58.1%（充分性）的回答中，至少一个未引用因子得分超过最低引用因子；prompt监控对应为25.8%和8.9%。结论：Top-3因子含有一定信息，但不能可靠识别实际影响最强的因子，尤其顾问推荐中漏报明显。
