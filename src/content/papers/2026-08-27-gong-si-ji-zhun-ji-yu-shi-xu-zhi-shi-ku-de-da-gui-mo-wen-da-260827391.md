---
title: 'CorporateBench: Large-Scale Q&A Benchmarking with Temporal Knowledge Bases'
title_zh: 公司基准：基于时序知识库的大规模问答评测基准
authors:
- Sil Hamilton
- Albert Yu Sun
- Oscar J. Romero
- Carl-Leander Henneking
- David Mimno
- Bishan Yang
- Igor Labutov
affiliations:
- Epiq AI Labs
- Cornell University
arxiv_id: '2608.27391'
url: https://arxiv.org/abs/2608.27391
pdf_url: https://arxiv.org/pdf/2608.27391
published: '2026-08-27'
collected: '2026-08-29'
category: Eval
direction: 企业级LLM文档QA评测
tags:
- LLM
- Benchmark
- Question Answering
- Temporal Knowledge Base
- Long Context
one_liner: 提出企业级文档问答基准CorporateBench，用230k+文档与时序知识库保证跨文档一致性，揭示LLM长上下文性能下降
practical_value: '- 可借鉴用「时序知识库 + 合成企业文档」方案低成本构造大规模、多跳、跨文档一致的评测集，尤其适合电商场景中的商品详情、订单日志、客服会话等长文档数据，规避隐私问题。

  - 文档-问题比高达87.6的压力测试，能暴露真实RAG/Agent在大量文档下的检索、路由、工具调用瓶颈；建议在业务评测中加入类似高比例多跳问题，而不仅是单文档Extractive
  QA。

  - 其两个评测维度（信息抽取与知识库查询）可迁移为电商知识库Agent的能力分级：从抽取字段到执行SQL/Cypher查询、时间约束推理，验证模型在长上下文下的稳定性。

  - 结论提示落地中不能只依赖单模型超长上下文，需结合索引/分片/检索或路由机制，尤其当语料规模超过10万文档时性能下降明显，应配套ragas式证据追踪和一致性校验。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM在企业级文档问答上能力增强，但真实评估困难：企业不愿共享内部通信，合成数据集又过于简单。现有多文档QA基准的文档-问题比例低，难以模拟企业复杂推理需求。

**方法**：提出CorporateBench，一个人工验证的多任务QA基准，语料超过230,000篇文档，接近企业通信网络规模。通过四个合成生成的企业（员工12到10,000人）从时序演化的知识库中采样文档，保证跨文档逻辑一致性。评测覆盖信息抽取和知识库查询两个维度，文档-问题比高达87.6，远高于以往最接近的EKRAG（1.5）。

**关键结果**：对五个LLM进行评测，发现随着输入规模接近现实规模，模型性能持续下降。该基准为LLM开发者提供企业沟通推理度量，填补评测生态关键空白。
