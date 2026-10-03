---
title: Prefill-Free Cross-Family KV Cache Transfer for Heterogeneous Multi-Agent LLMs
title_zh: 异构多智能体 LLM 的免预填充跨家族 KV 缓存迁移
authors:
- Vincent-Daniel Yun
- Woosang Lim
- Haneul Yoo
- Sungjoo Yoo
- Murali Annavaram
- Sai Praneeth Karimireddy
affiliations:
- University of Southern California, USA
- Seoul National University, Republic of Korea
- New York University, USA
arxiv_id: '2609.32259'
url: https://arxiv.org/abs/2609.32259
pdf_url: https://arxiv.org/pdf/2609.32259
published: '2026-09-28'
collected: '2026-10-03'
category: MultiAgent
direction: 多智能体异构 LLM 缓存迁移
tags:
- KV cache transfer
- multi-agent LLM
- heterogeneous models
- prefill-free
- efficient inference
one_liner: 冻结两端模型，通过结构对齐、映射与校准实现跨家族 KV 缓存迁移，免预填充加速异构多智能体通信
practical_value: '- 多角色 Agent 系统若采用不同模型家族（如大模型做规划、小模型做执行），在共享长上下文（如用户历史、商品列表、prompt
  模板）时，优先用 KV cache 迁移替代重新 prefill，可显著降低首 token 延迟。

  - 跨模型 KV 对齐可采用“冻结两端 + 小型映射器/校准器”的方式，不扰动原有模型权重，部署风险低；若要落地，可在固定模型对（如主链路模型↔轻量 reranker）预训练映射器。

  - 长上下文收益更大（32K 下加速 10.7×），适合电商会话中拼接长商品序列、多轮决策历史；短上下文也有收益但需评估额外映射开销。

  - 该方法与文本通信在多智能体基准上表现持平，说明在可靠映射下可无精度损失换取推理加速，适合对延迟敏感的在线 Agent 编排。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：异构多智能体系统按角色分配不同模型家族，但文本通信要求接收方重新 prefill 发送方已处理的共享上下文，造成冗余。复用发送方 KV cache 可避免，但跨家族迁移必须解决 tokenization、模型深度和 KV 表征差异。

**方法关键点**：HeteroFold 冻结发送方和接收方模型，三步完成免预填充跨家族缓存复用：①对齐模型结构，处理层数与维度差异；②将发送方 cache 映射到接收方表征空间；③校准映射结果以保持接收方行为。

**关键结果数字**：在六个传输方向、四个长上下文基准上全部取得最佳 cache-transfer 性能，多数短上下文设置也最优；多智能体基准上与文本通信表现持平。32K 上下文长度下，Llama-3.1-8B→Ministral-3-14B 传输比 Native Prefill 快 10.7×，比 SOTA 免预填充基线 Dense Latent 和 KV Ridge 快 1.18–1.47×。
