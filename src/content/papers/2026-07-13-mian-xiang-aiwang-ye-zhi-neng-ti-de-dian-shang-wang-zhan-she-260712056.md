---
title: 'Designing Agent-Ready Websites for AI Web Agents: A Framework for Machine
  Readability, Actionability, and Decision Reliability'
title_zh: 面向AI网页智能体的电商网站设计框架
authors:
- Said Elnaffar
- Farzad Rashidi
arxiv_id: '2607.12056'
url: https://arxiv.org/abs/2607.12056
pdf_url: https://arxiv.org/pdf/2607.12056
published: '2026-07-13'
collected: '2026-07-15'
category: Agent
direction: Agent 可执行性设计提升任务可靠性
tags:
- AI Agent
- Web Design
- E-commerce
- Agent Usability
- Decision Reliability
one_liner: 提出三个维度的agent-ready网站设计框架，使AI浏览器代理任务成功率从49.3%提升至89.3%
practical_value: '- **结构化产品页提升Agent抓取**：用明确的data-属性、语义化HTML标签（如<price>、<feature>）标记商品信息，可大幅降低Agent提取详情失败的PARTIAL率（本实验中从43次降至3次），电商平台可据此优化前端代码生成或模板，让模型更快更准获取信息。

  - **动作线索设计减少无效步骤**：在关键决策点提供Agent可识别的action cue（如显式按钮“比较所选”或结构化选项列表），使平均步骤从9.31降到6.49，可直接应用到产品比较、多约束筛选环节，提升多步骤任务的完成效率。

  - **证据信号增强决策可靠性**：为价格、库存、促销等动态信息添加时间戳和状态标签（如price-valid-until），Agent可以利用这些证据判断信息时效，避免基于过期数据做决策，对秒杀、闪购场景尤其重要。

  - **可执行性指标体系借鉴**：框架定义的agent interpretability、executability、decision reliability三维度，可转化为前端质量评估指标，用于A/B实验对比不同页面方案对Agent性能的影响，驱动迭代优化。'
score: 9
source: arxiv-cs.HC
depth: abstract
---

**动机**：AI浏览器代理正成为用户在线购物的重要中介，但现有网站仅为人眼优化，缺乏机器可读的结构、语义清晰度和决策所需证据，导致Agent任务失败率高。

**方法**：提出agent-ready网站设计框架，围绕三个维度：(1) Agent可解释性——通过语义HTML标签与约束属性提升机器可读及语义清晰度；(2) Agent可执行性——在界面中嵌入动作线索、简化导航步骤、暴露操作入口；(3) Agent决策可靠性——为动态信息附加时效证据、库存状态信号等上下文可靠性标识。

**实验**：构建同一电商网站的人机双版本，在相同商品目录、库存和流程下，用GPT-4.1、Gemini-2.5 Flash、Grok-4 Fast三个浏览器代理各执行5类任务（产品查找、详情提取、比较、多约束选择、下单），共300次运行，对比PASS/PARTIAL/FAIL率。

**结果**：agent-ready版本严格成功率89.3%，远超基线49.3%（150次中PASS 134 vs 74），PARTIAL从43次骤降至3次，平均步骤数从9.31降到6.49，且token消耗更低。增益最大任务为复杂信息提取与多约束选择，表明结构化线索与可靠性信号显著提升代理决策质量。
