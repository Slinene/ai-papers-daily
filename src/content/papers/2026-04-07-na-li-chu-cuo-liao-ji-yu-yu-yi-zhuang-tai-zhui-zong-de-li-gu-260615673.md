---
title: Where Did It Go Wrong? Process-Level Evaluation of Web Agents with Semantic
  State Tracking
title_zh: 哪里出错了？基于语义状态追踪的Web代理过程层评估
authors:
- Jiwan Chung
- JiHyuk Byun
- Vibhav Vineet
- Seon Joo Kim
affiliations:
- Yonsei University
- Microsoft Research
arxiv_id: '2606.15673'
url: https://arxiv.org/abs/2606.15673
pdf_url: https://arxiv.org/pdf/2606.15673
published: '2026-04-07'
collected: '2026-06-17'
category: Eval
direction: Web Agent 过程评估与技能诊断
tags:
- Web Agent
- Process Evaluation
- Semantic MDP
- Trajectory Analysis
- Skill Decomposition
one_liner: 提出基于语义MDP的过程评估基准WebStep，通过技能分解与分叉分析定位Agent在探索与执行上的细微差异
practical_value: '- **多步交互Agent的过程监控**：电商搜索、推荐场景中Agent需多轮导航（如筛选商品、填写订单），可借鉴WebStep构建语义状态机，跟踪关键语义转移（如“已选品类”、“完成比价”），而不仅是最终转化，实现细粒度诊断。

  - **技能分解定位薄弱环节**：将Agent能力拆解为探索（信息搜集）与执行（提交操作）等技能，按动作类型统计成功率，可发现模型在“过滤条件设置”强但在“最终下单”弱，从而定向优化提示或微调数据。

  - **分叉分析定位关键错误**：追踪任务失败前状态分叉点，识别导致失败的决定性错误（如遗漏必填项），分析该错误是否为Agent特有，有助于集中修复高频Agent特异性缺陷，而非泛泛优化整体能力。

  - **难度自适应评估**：任务难度缩放设计可揭示Agent在不同复杂性下的表现分化，用于制定上线策略：简单任务用低成本Agent，复杂任务触发更强大的模型或人工兜底。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有Web Agent评估只看任务最终成功与否，忽略交互过程信息，无法指导如何改进。需一套自动化的过程层评估方法，以精细定位Agent在长序列多步操作中的不足。

**方法**：构建WebStep基准，含1,800个控制难度的任务实例。每个网站内置确定性语义MDP，Agent在GUI上操作时，后台自动记录高阶语义状态和转移，无需人工标注。基于此语义轨迹，引入过程指标（探索覆盖率、执行准确率）、技能分解（按动作类型如过滤、提交统计成功率）、分叉分析（定位导致任务失败的关键状态分叉点）等分析手段。

**结果**：
- 过程指标揭示成功率为31-33%的三个Agent在探索和执行力上差异显著，终结导向评估无法分辨。
- 技能分解显示同一网站内排名反转：Housing任务上，OpenAI CUA在commit动作比Qwen3.5高23.7%，但在filtering动作低15.6%，指明了具体提升技能。
- 分叉分析表明失败的决定性错误是Agent特异性的，非共享缺陷。
- 难度升高时，Agent表现分化加剧：简单任务成功率相近，复杂任务中探索需求增加时差距迅速拉大。
