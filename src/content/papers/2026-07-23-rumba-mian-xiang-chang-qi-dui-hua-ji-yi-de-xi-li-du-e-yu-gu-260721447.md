---
title: 'RUMBA: Russian User Memory Benchmark'
title_zh: RUMBA：面向长期对话记忆的细粒度俄语评估基准
authors:
- Elizaveta Shevtsova
- Inna Glebkina
- Mark Baushenko
- Pavel Gulyaev
- Alena Fenogenova
affiliations:
- DAIMLD
arxiv_id: '2607.21447'
url: https://arxiv.org/abs/2607.21447
pdf_url: https://arxiv.org/pdf/2607.21447
published: '2026-07-23'
collected: '2026-07-25'
category: Eval
direction: 长期记忆与对话系统诊断评估
tags:
- Long-term Memory
- Benchmark
- Temporal Reasoning
- Conversational AI
- Russian NLP
- Memory Evaluation
one_liner: 提出多维度诊断性长期记忆基准 RUMBA，涵盖俄语及英文，细粒度分解问题类型以分析记忆机制薄弱点
practical_value: '- **记忆模块评估框架可复用**：在构建个性化推荐或客服 Agent 的记忆模块时，直接借鉴 RUMBA 的细粒度提问分类（语义类型、会话范围、时序推理、时间表达明确性），设计针对性测试集，暴露模型在跨
  Session 信息整合、偏好更新与遗忘方面的短板。

  - **时序推理诊断切片**：电商场景中用户偏好随时间变化（如兴趣漂移、短期促销影响），利用基准中的 temporal reasoning 切片，检验模型是否能正确区分陈旧信息与最新意图，优化记忆更新与淘汰策略。

  - **多语言对齐下的英语子集可直接利用**：论文提供对齐的英语子集，可以立即用于评估现有英语对话推荐系统的长期记忆能力，无需额外标注，快速定位检索与推理瓶颈。

  - **记忆机制选型参考**：论文对比不同记忆实现（如 KV cache、RAG、上下文打包等）在不同问题切片下的表现，结论可指导在资源与延迟约束下选择更适合电商场景的记忆架构。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有长期记忆基准以英语为主，依赖聚合检索指标，无法细粒度诊断长上下文、时序信息与推理的交互缺陷。RUMBA 旨在构建面向俄语的诊断性基准，并提供统一方法学，以支持跨语言的记忆机制分析。

**方法关键点**：
- 构建带有时间戳的多轮用户‑助手对话，并基于对话生成需跨会话检索、组合和推理的 QA 对。
- 设计细粒度问题分类体系，从语义类型（事实、偏好等）、会话范围（单/多 session）、时序推理（无/相对/绝对）及时间表达明确性四个维度标注每个问题。
- 提供对齐的英语子集，确保方法学跨语言可比。
- 评估多种记忆系统（RAG、KV cache 增强、长上下文模型等），按问题切片分析表现。

**关键结果**：
- RUMBA 能有效暴露不同记忆机制在特定切片上的失败模式，例如绝对时间推理题显著拉低部分模型得分。
- 英语子集结果与俄语保持趋势一致，验证基准的跨语言稳定性。
- 长上下文模型在单纯检索题上表现尚可，但涉及跨 session 推理与时间冲突时准确率骤降，凸显现有记忆更新机制的不足。
