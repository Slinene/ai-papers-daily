---
title: 'Version- and Scope-Aware Question Answering over Normative Documents: A Deployed
  System and an End-to-End Evaluation at Production Scale'
title_zh: 规范文档问答的版本与适用范围感知系统及生产规模评估
authors:
- Liuyin Wang
- Shuaipeng Jin
- Jiwei Shi
- Jensen Hsu
affiliations:
- Beijing Caizhi Technology Co., Ltd.
- dknownAI
arxiv_id: '2609.18769'
url: https://arxiv.org/abs/2609.18769
pdf_url: https://arxiv.org/pdf/2609.18769
published: '2026-09-16'
collected: '2026-09-17'
category: RAG
direction: 规范RAG · 版本与范围治理
tags:
- RAG
- Normative QA
- Version Control
- Scope Resolution
- Production Evaluation
one_liner: 将显式版本与适用范围规则置于生成前，使规范文档问答得分从88.1提升至97.7
practical_value: '- 对业务知识库问答（平台规则、政策、广告合规）不能只用向量检索 + LLM 生成：必须显式解析文档的生效版本、适用主体/地区/日期，过滤不适用文档后再生成。可直接建模为元数据规则层置于检索与生成之间。

  - 生产级评估避免“拿测试集调参”：分层抽样 200 题、每题绑定 gold 源文档、采样规则不读系统输出，能客观对比不同 RAG 架构；建议业务方也公开部分标注与脚本。

  - 若托管检索服务作为 baseline 得分 88.1，治理系统提升 9.6 点，说明规则性 scope/version 错误是主要损失，值得优先投入。

  - 商业化部署已经验证多租户稳定性（1,126 用户、约 10 万 calls/workday），架构上治理规则应可配置、可追踪，而非写死在 prompt 里。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：规范性文档问答不能只依赖单段落检索，需确认文档版本现行有效、适用范围（地区/主体/日期）以及条款可溯源；托管检索服务降低了搭建成本，但“上传文档即问”是否足够？

**方法关键点**：生产环境约 73,000 份规范文档，从已发布 benchmark 分层抽取 200 问，每题配 gold source document；采样规则不读系统输出/分数。对比两种系统：hosted retrieval service（默认 RAG）与 governed system（生成前通过显式规则解析版本与适用范围，例如过滤、溯源码）。

**结果**：governed system 总分 97.7，hosted service 88.1，差 9.6（基于未四舍五入均值）。问题集、答案文本、分数及复现脚本公开。商业产品自 2026 年 1 月上线，服务 1,126 注册用户，客户包括智谱 AI、乐程健康，2026 年 4 月中旬约 10 万次/工作日调用。
