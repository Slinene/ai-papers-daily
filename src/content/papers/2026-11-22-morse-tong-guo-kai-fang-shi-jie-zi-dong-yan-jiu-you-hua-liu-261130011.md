---
title: 'MORSE: Optimizing Streaming Memory Design via Open-World Auto-Research'
title_zh: MORSE：通过开放世界自动研究优化流式记忆设计
authors:
- Ce Zhang
- Jianshu Zhang
- Jinxi He
- Xiyuan Yang
- Pan Wang
- Han Liu
- Katia Sycara
- Yaqi Xie
affiliations:
- CMU
- Northwestern
- UIUC
- Pitt
arxiv_id: '2611.30011'
url: https://arxiv.org/abs/2611.30011
pdf_url: https://arxiv.org/pdf/2611.30011
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 自动研究优化流式记忆
tags:
- Streaming Memory
- Auto-Research
- Recursive Self-Improvement
- Video-Language Model
- Agent
- Harness Optimization
one_liner: 用重复失败驱动在线搜索外部解决方案，自动进化流式视频记忆 harness，达到最高准确率
practical_value: '- 失败模式聚类 + 外部知识检索：推荐/搜索系统用 LLM Agent 做 query 改写、选品、召回策略时，可以把线上 badcase
  按原因聚类，自动检索内部实验报告/论文/开源实现来生成修复策略，而不只是依赖 prompt 模板或人工规则。

  - 冻结大模型骨干、只优化外围 memory/retrieval 策略：类似在电商 RAG/推荐 Agent 中冻结 LLM，重点优化记忆写入/淘汰和检索策略，可降低在线改造成本与风险。

  - 分层 revision 筛选：先筛质量提升、再在精度容差内找更低延迟版本，这个流程可直接用于推荐系统 Agent 的多目标上线评估（如先保证 CTR/GMV
  不降，再优化 RT 和成本）。

  - Open-world auto-research 思想：将内部失败信号与外部论文/代码库连接做自动 troubleshooting，适合建设推荐/搜索系统
  Agent 的自动化调优基础设施，减少手工迭代。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：流式视频理解需要在单遍、有界帧存储下决定保留哪些证据，未来问题未知。现有递归自我改进(RSI)自动设计存储证据的 harness，但修复依赖编辑器先验知识和预定义工具，遇到反复失败缺少外部知识支撑。

**方法关键点**：MORSE 是开放世界自动研究框架。编辑器按原因聚类训练轨迹中的失败，在线搜索论文、模型卡、代码，适配方法或使用预训练感知模型；引入新感知能力时能修订存储/检索证据策略，服务冻结的视频语言模型。验证时先选提升答案质量的修订，再在容差内寻找更快修订。

**关键结果**：三个流式视频基准上，在每个冻结骨干对比中取得最高答案准确率。OVO-Bench 上 Qwen3-VL-8B harness 平均 0.30 秒回答，准确率 75.1%，比同骨干次优高 3.1 个百分点。
