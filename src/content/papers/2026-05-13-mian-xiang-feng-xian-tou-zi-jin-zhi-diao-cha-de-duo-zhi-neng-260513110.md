---
title: A Multi-Agent Orchestration Framework for Venture Capital Due Diligence
title_zh: 面向风险投资尽职调查的多智能体编排框架
authors:
- Grigorios Alexandrou
- Katerina Pramatari
affiliations:
- Athens University of Economics and Business
arxiv_id: '2605.13110'
url: https://arxiv.org/abs/2605.13110
pdf_url: https://arxiv.org/pdf/2605.13110
published: '2026-05-13'
collected: '2026-05-16'
category: Agent
tags:
- Multi-Agent
- LLM
- RAG
- OCR
- DueDiligence
- HallucinationMitigation
one_liner: 事件驱动多智能体系统自动整合实时网络检索与官方注册文档解析，并通过结构化回退机制消除金融幻觉
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
风险投资的企业尽职调查长期依赖人工整理碎片化信息，耗时且易引入认知偏差。LLM虽擅长文本合成，但在金融场景面临知识截止、幻觉生成与外部工具调用三大障碍。特别是财务数字的可信度要求极高，需要一种能主动检索、精确提取并显式标记数据缺失的系统化方案。

**方法关键点**
- 事件驱动多智能体编排：基于n8n低代码平台构建DAG流水线，将尽调任务分解为专业子代理（市场情报、竞争分析、新闻信号、财务提取）
- 希腊商业注册局(Γ.E.MH.)财务提取管线：逆向工程前端对后端通信，动态查询隐藏端点获取原始PDF，通过布局感知OCR解析资产负债表与损益表，保留来源引用
- 结构化回退机制：当企业无注册号或文档缺失时，系统先尝试Crunchbase等第三方数据库，若仍为空则直接输出“Not Found”标记，杜绝LLM生成虚假数字
- 合成层：多代理聚合情报生成结构化HTML报告，包含公司概况、市场情报、竞争格局、财务摘要及分析师建议，并附源内联引用

**关键结果**
- 系统已部署于一家希腊风险投资基金，全自动生成包含市场、竞争、财务的可审计报告
- 财务模块针对无Γ.E.MH.号的外国企业，强制输出“Not Found”标记，显式区分官方数据、第三方近似与缺口三种认知状态
- 工作流及代码已开源，支持在自托管n8n实例上复现

**核心洞见**
> “缺失的数字比看似合理但无法验证的数字对投资分析的危害更小”——通过强制标记数据空缺，将幻觉风险转化为显式的审计缺口，是LLM介入高可靠性金融场景的关键设计原则。
