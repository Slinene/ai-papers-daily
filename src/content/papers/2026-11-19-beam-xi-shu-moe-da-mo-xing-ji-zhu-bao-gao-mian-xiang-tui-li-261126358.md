---
title: Beam Model Technical Report
title_zh: Beam 稀疏 MoE 大模型技术报告：面向推理与 Agent 优化
authors:
- Reflection Team
- Adam Abdulhamid
- Osama Abuelsorour
- Yasmin Alameddine
- Carlo Alfano
- Duarte Alves
- Brandon Amos
- Selvaraj Anandaraj
- Arseni Anisimovich
- George Antoniadis
affiliations:
- Reflection AI
arxiv_id: '2611.26358'
url: https://arxiv.org/abs/2611.26358
pdf_url: https://arxiv.org/pdf/2611.26358
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: 稀疏 MoE 大模型推理与 Agent 优化
tags:
- MoE
- LLM
- speculative decoding
- RL
- long context
- agentic
one_liner: 501B 总参稀疏 MoE，面向编码推理与 Agent 场景，以 3-4x 更低推理成本实现前沿水平
practical_value: '- MoE 稀疏激活（23.4B/501.3B）适合大规模在线推理服务，尤其电商搜索中 LLM 作为 query 改写、商品属性抽取或
  Agent 决策推理器时，可通过 gating 降低每 token 激活参数、配合 FP8/NVFP4 量化减少 KV cache 和算力，显著降低推理成本（模型本身
  3-4x 更低）。

  - 大规模异步 RL 训练框架（10.5K GPU 集群、100M rollouts）可迁移到电商 Agent 策略优化：例如导购对话、自动选品或搜索策略参数优化，利用异步
  rollout + verifiable reward（如成交、点击、转化）持续训练策略，前提是能构建反馈闭环。

  - 1M 长上下文通过两阶段 midtraining 扩展，对电商知识库场景（海量商品 SKU、长规则文档、用户历史）有用，可用 correctness-anchored
  数据（产品参数、订单、约束）稳定扩展窗口，避免只用通用语料。

  - 投机解码 drafter 用于提升在线 LLM 推理吞吐，对电商中高频调用 LLM 生成文案、推词、搜索建议的场景可以直接采用类似小模型 drafter 加速，但需注意延迟与成本权衡。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：当前大模型在 coding/reasoning/agentic 任务上推理成本高，Beam 目标提供前沿推理能力同时大幅降低推理计算。

**方法关键点**：
- 架构：sparse MoE，501.3B 总参数，23.4B 活跃参数，1M token 上下文窗口，通过两阶段 midtraining 扩展，使用 verifiable correctness-anchored 数据。
- 预训练：23.8T 高质量 token。
- 后训练：大规模全异步 RL，10.5K GB300 GPU 集群，4 周生成超 100M rollouts，能力随 RL compute 提升持续提高，未见饱和。
- 推理优化：硬件-模型协同设计，FP8/NVFP4 量化，1.93B 参数 speculative decoding drafter（DFlash 2）。
- 安全：有害请求拒绝/转话题率 88.9%，无害请求遵从率 81.5%，在开放权重模型 Pareto 前沿最高。

**关键结果**：推理计算比其他同类模型少 3-4 倍，达到前沿推理水平；RL 规模为开放实验室最大之一；能力随 RL compute 增长无明显平台期。
