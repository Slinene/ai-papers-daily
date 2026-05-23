---
title: 'LCGuard: Latent Communication Guard for Safe KV Sharing in Multi-Agent Systems'
title_zh: LCGuard：多智能体系统中安全 KV 共享的隐通信守卫
authors:
- Sadia Asif
- Mohammad Mohammadi Amiri
- Momin Abbas
- Prasanna Sattigeri
- Karthikeyan Natesan Ramamurthy
affiliations:
- Rensselaer Polytechnic Institute
- IBM Research
arxiv_id: '2605.22786'
url: https://arxiv.org/abs/2605.22786
pdf_url: https://arxiv.org/pdf/2605.22786
published: '2026-05-21'
collected: '2026-05-23'
category: MultiAgent
direction: 多智能体安全隐通信优化
tags:
- Multi-Agent Systems
- KV Cache
- Privacy
- Adversarial Training
- Latent Communication
one_liner: 通过对抗训练学习 KV 缓存变换，在保持任务性能的同时降低多智能体隐通信中的敏感信息泄露
practical_value: '- 在多智能体联合推理的电商或客服场景中，若不同 Agent 通过 KV 缓存共享中间推理状态，可借鉴 LCGuard 的对抗训练框架，在缓存传输前插入可学习的表示变换层，降低用户隐私泄露风险。

  - 可以将敏感信息重构成功率作为一种可量化的隐私泄露指标，用于评估和监控分布式 Agent 系统内部的通信安全性。

  - 对抗训练的分治策略（保留任务语义、压制敏感信息）可推广到其他需要交换隐向量的推荐或检索组件中，例如生成式推荐中的 Semantic ID 传递。

  - 工程实现上，LCGuard 的变换模块轻量、可插拔，不改变原有 Agent 结构和推理流程，适合已有流水线的逐步升级。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 多智能体系统越来越多采用 KV 缓存进行隐通信以提升效率，但 KV 缓存可能编码了上下文输入、中间推理状态等敏感信息，形成不透明的泄露通道，现有文本通信无法提供细粒度的安全控制。

**方法**：提出 LCGuard，将共享 KV 缓存视为"隐工作记忆"，在缓存跨 Agent 传输前学习一个表示级变换。核心思想是基于重构定义泄露：若一个对抗解码器能从缓存中重构出 Agent 特定的敏感输入，则视为不安全。进而采用对抗训练，让对手学习重构敏感信息，同时 LCGuard 学习变换以保留任务相关语义并最小化可重构信息。

**关键结果**：在多个模型家族和多智能体基准上，LCGuard 一致降低了基于重构的泄露率和攻击成功率，同时保持了与标准 KV 共享基线相当的任务性能。
