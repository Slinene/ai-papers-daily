---
title: 'Every Edge Needs a Quote: Building a Quote-Grounded Knowledge Graph of Healthcare
  Software Adoption with Language-Model Agents'
title_zh: 每条边都要有引文：用语言模型代理构建医疗软件采用情况的引文支撑知识图谱
authors:
- Juan Felipe Duran
- Arthur Tobler
- Martin Vallières
affiliations:
- Medical Physics Unit, Department of Oncology, McGill University
- Toboggan Labs
arxiv_id: '2610.32781'
url: https://arxiv.org/abs/2610.32781
pdf_url: https://arxiv.org/pdf/2610.32781
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: LLM Agent 构建引文支撑知识图谱
tags:
- knowledge graph
- LLM agents
- information extraction
- attribution
- grounding
- LLM-as-a-judge
one_liner: 构建每边必有逐字引文的知识图谱流程，以确定性爬取、预算化ReAct agent、分层grounding和多模型投票达到0.94精度/0.71召回
practical_value: '- 在商品/品牌关系抽取中，强制每条三元组都有源页面逐字引文，并用字符串匹配定位证据，可大幅提高 KG 可追溯性和线上信任度，适合电商商品知识补全、竞品客户案例采集。

  - 借鉴其分层 grounding：先用宽松抽取器高召回，再用 referent step 读整页解决“只提到一侧”的指代问题，叠加确定性规则过滤明显错误，最后用多模型投票九准则裁决，可复用到商品属性、合作品牌、集成关系等抽取任务。

  - 使用预算化 ReAct agent 搜索全网，配合确定性爬取厂商官网，在成本可控的前提下扩大证据覆盖，可用于监控竞品动态、构建行业采用图谱或生成可引用证据的推荐理由。

  - 用投票生成的置信度分数替代固定规则，在相同精度下保留更多正确关系，并缓解长上下文退化与 run-to-run 方差；工程上可将长文档拆成有界窄模型调用，用字符串匹配证据做锚定。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：医院采购软件需要了解哪些同行在使用、系统如何集成，证据散布在厂商官网、新闻稿和第三方页面。LLM agent 能低成本收集，但提取声明难以验证，错误客户名单会误导买家并损害机构声誉。

**方法关键点**：构建知识图谱的唯一规则是“每条边必须由源页面逐字引文支持”。页面来自对各厂商网站的确定性爬取和一个预算化 ReAct agent 的全网搜索。先用宽松抽取器提出关系及引文，再进入分层 grounding：当引文只提及一侧时由 referent step 读整页补全；确定性检查过滤明显错误；随后五个模型调用在九个准则上投票裁决，并输出置信度分数。

**关键结果**：在 61 个厂商上，管道达到 0.94 精度、0.71 召回（页面级 key，覆盖 6,428 个候选关系）。与 marketplace 策展列表对比得分较低，但保留关系中 89% 在页面上有明确陈述。基于投票的置信度在相同精度下保留更多正确关系，达到 0.90 精度、0.90 召回。作者还指出窄化有界模型调用、字符串匹配证据和投票能缓解长上下文退化与运行间方差。
