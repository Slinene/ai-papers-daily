---
title: Accelerating Mixture of Block Attention via Dynamic Routing, KV-Centric Execution
  and Runtime Pipelining
title_zh: 通过动态路由、KV中心执行与运行时流水线加速块混合注意力
authors:
- Yingqi Shi
- Junru Lu
- Yun Liu
- Di Yin
- Xing Sun
affiliations:
- Tencent Youtu Lab
arxiv_id: '2611.26268'
url: https://arxiv.org/abs/2611.26268
pdf_url: https://arxiv.org/pdf/2611.26268
published: '2026-11-18'
collected: '2026-11-21'
category: LLM
direction: 长上下文稀疏注意力 GPU 加速
tags:
- MoBA
- Sparse Attention
- KV Cache
- Dynamic Routing
- GPU Optimization
- Long Context
one_liner: LightningMoBA 用动态路由、KV 中心任务划分与流水线重叠，在 Top-16 稀疏率下将长上下文生成加速 1.2-1.6x
practical_value: '- 若业务中部署长上下文 LLM（如电商 Agent 处理长会话、多商品文档），可借鉴 MoBA 的块级稀疏注意力及动态阈值路由，避免固定
  Top-k 导致的长尾 KV 块浪费，在保持效果同时提升推理吞吐。

  - 工程实现上，KV-centric ownership 将同一 KV block 被多个 query range 命中时的高扇出列拆分为有界任务并复用已加载
  KV tile，可迁移到自研注意力 kernel，减少 HBM 重复读取。

  - Runtime pipelining 把规整 K/V 传输与不规则 query gather 同 Tensor Core 计算重叠，对 GPU 利用率敏感的服务有直接参考；Hopper
  上 1.2-1.6x 加速说明调度优化收益不亚于稀疏率调参。

  - 若用 LLM 做生成式推荐或用户长期行为序列建模，需处理长序列注意力，可考虑动态路由而非固定窗口，兼顾效果与延迟；RULER 分数从 74.42 提升至 75.28
  也说明稀疏化不一定降质量。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长上下文 attention 计算量大，MoBA 通过块级稀疏路由减少 KV 交互，但 FlashMoBA 仍保留固定 Top-k 预算和 query-centric 调度。固定 Top-k 不能适应不同 score 分布，且多个 query range 选择同一 KV column 时，query-range 所有权会导致 KV 复用碎片化。

**方法关键点**：
- **动态路由**：对每个 query 的 block score 做阈值判断，直接输出变长稀疏元数据，保留密度与 GPU 调度粒度解耦。
- **KV-centric ownership**：按 `(query head, KV block)` column 分组被选中的行，将高扇出 column 拆成有界任务，并复用每个任务加载的 KV tile。
- **Runtime pipelining**：在 Hopper 上用流水线把规整 K/V 传输和不规则 query gather 与 Tensor Core 计算重叠，隐藏数据移动开销。

**关键结果**：在五个 checkpoint 上匹配 Top-16 retention 时，LightningMoBA 将端到端生成加速 1.20-1.60x，同时平均 RULER 分数从 74.42 提升到 75.28。
