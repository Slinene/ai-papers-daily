---
title: Rethinking Heterogeneous System Disaggregation for Subquadratic Attention
title_zh: 重新思考面向子二次注意力的异构系统解聚
authors:
- Arya Tschand
- Yaosheng Fu
- Vikram Sharma Mailthody
- Nicolai Oswald
- Po-An Tsai
- Ritchie Zhao
- Oreste Villa
- Vijay Janapa Reddi
- Karu Sankaralingam
affiliations:
- Harvard University
- NVIDIA
arxiv_id: '2609.13134'
url: https://arxiv.org/abs/2609.13134
pdf_url: https://arxiv.org/pdf/2609.13134
published: '2026-09-11'
collected: '2026-09-14'
category: LLM
direction: LLM 推理 · 子二次注意力异构解聚
tags:
- subquadratic attention
- heterogeneous disaggregation
- LLM serving
- energy efficiency
- sparse attention
- inference
one_liner: 提出按二次/子二次注意力拆分 decode 的细粒度异构解聚方案，显著提升子二次注意力 LLM 的吞吐与能效
practical_value: '- 若业务中采用线性/稀疏/滑动窗口等子二次注意力 LLM 做在线推理（如 query 理解、生成式推荐、Agent 工具调用），可将
  KV 检索类算子（如 top-k 选择）部署在 DRAM 带宽大的 LPX 类设备，将静态内存的注意力+FFN 部署在 SRAM 算力设备，降低跨设备通信并提升
  tokens/J。

  - 稀疏注意力 decode 可拆成两阶段：top-k 选择需要扫描全量 KV，但计算轻；top-k 注意力+FFN 内存占用固定。这一特性可指导推理系统的流水线设计，避免将
  KV 索引放在算力型 GPU 上造成内存瓶颈。

  - 系统解聚不应按 attention/FFN 操作类型，而应按算数强度与内存占用拆分；对于混合注意力架构（部分层 dense，部分层子二次），可把 dense
  层放在 GPU、子二次层放在低功耗设备，实现能耗与延迟的更好折中。

  - 论文主要是底层系统优化，与推荐/广告算法逻辑无直接关系，可借鉴点主要在工程部署和硬件选型。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：前沿 LLM 越来越多采用 subquadratic attention 降低推理内存与计算，但现有推理系统以 dense attention 为中心做解聚，未利用子二次注意力的算术强度和内存占用特点。

**方法关键点**：提出 SQD（SubQuadratic Disaggregation），按二次/子二次注意力拆分 decode 而非按算子类型。对于稀疏注意力，将 decode 拆为 top-k 选择（需索引全量 KV，计算轻但内存访问大）和 top-k 注意力+FFN（内存占用静态）；对于线性与滑动窗口注意力，拆为 dense 注意力层和子二次注意力层+FFN，分别适配不同硬件特性。

**关键结果**：在 8×B200 异构系统代理上，相对最强 GPU-only 基线，tokens/J 平均提升：GLM 5.2 高 53%，Nemotron 3 Ultra 高 31%，Gemma 4 31B 高 56%；在 Rubin+LPX 固定功率预算模型中，可达 1.2–1.5 倍更紧延迟和最高 3.6 倍吞吐。实验还揭示下一代异构系统的芯片与互连配置建议。
