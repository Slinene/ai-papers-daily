---
title: 'When Agentic Retrieval Fails Silently: Framework and Production Evidence from
  a Creative AI Assistant'
title_zh: Agentic 检索静默失败：LARA 框架与 Adobe Express 生产证据
authors:
- Yan
- Liang
- Anuj Agarwal
- Aditya Reddy Cheruku
affiliations:
- Adobe
arxiv_id: '2610.30423'
url: https://arxiv.org/abs/2610.30423
pdf_url: https://arxiv.org/pdf/2610.30423
published: '2026-10-21'
collected: '2026-10-23'
category: Eval
direction: Agentic Retrieval 评估归因
tags:
- Agentic Retrieval
- Evaluation
- Attribution Gap
- Production Metrics
- RAG
- Lineage Schema
one_liner: 提出 LARA 三层评估与四字段血缘 schema，解决 agentic 助手检索归因缺失，并用 Adobe Express 生产数据验证
practical_value: '- 不要用 assistant-wide CTR/reformulation 作为检索指标；只在 retrieval 触发的 turn
  上计算，并把 reformulation 拆成 Search Reformulation 与 Downstream Correction，避免把生成润色误判为检索失败。

  - 至少先加 returned_asset_ids（检索触发时的完整排序列表），这是解锁 Layer 1 离线评估的最高价值单一字段；再加 retrieval_id
  / consumed_asset_id / source_retrieval_id 做跨 turn、跨 session 归因，纯日志改动无需新模型。

  - 对电商/Agent RAG 场景，显式打 retrieval role tag（direct retrieval、retrieve-then-act、reference
  input 等），并分开统计 GPR、ACR、ORF、UOR，不要把 UOR 当成成功或放弃。

  - 关注 Layer 0 planner routing：如果检索触发率极低，先估算 missed-retrieval rate，用 ground-truth
  intent 对照 planner 决策；否则再好的 Layer 1 也只覆盖极少流量。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

传统 CTR、MRR、NDCG 依赖三个假设：用户看见排序结果、马上采取行动、后续行为反映检索质量。Agentic 助手中检索输出先被 generation 层消费，三个假设都被破坏：agent 先读结果（who）、动作与检索在时间上分离（when）、检索结果与模型自身知识混合（what caused it），形成 attribution gap。已有工作没有解决生产环境中的检索归因问题。

## 方法关键点

LARA 框架分三层独立测量，并用四字段 lineage schema 连接：

- **Layer 1 检索质量**：null rate、precision@K、NDCG@K，基于 server-side logs + offline relevance labels，在检索触发时计算，独立于用户行为；CTR 降级为辅助信号。
- **Layer 2 参与与结果**：GPR（用户后续使用返回 asset）、ACR（agent 在同一请求内消费返回 asset）、ORF（显式检索失败信号：Search Correction / Search Reformulation / Agentic Rejection）、UOR（无任何使用或失败证据），按 retrieval role 分别报告。
- **Layer 3 产品成功**：task completion、export/share rate，通过 source_retrieval_id 把成功事件关联回具体检索。
- **四字段 lineage schema**：retrieval_id、returned_asset_ids（触发时完整排序列表，最高价值单点改变）、consumed_asset_id、source_retrieval_id，再加上 retrieval role tag；全部是 logging 添加，不引入新模型。
- 跨层诊断表：低 Layer 1 + 低 ORF 对应模型掩盖的静默检索失败；高 ORF + 低 Layer 1 且 Downstream Corrections 高对应生成失败等。

## 关键实验与数字

Adobe Express 用同一检索基础设施服务 gallery search 和 agentic assistant，同一用户群体。2026 年 8 月数据显示：

- Chat reformulation rate 44.4% vs gallery 33.1%，方向与朴素预期相反：chat 的 reformulation 主要是生成润色（如“make it bluer”），不是检索失败，说明同一行为信号在两种 surface 上含义完全不同。
- 检索只在 0.31% 的 in-scope assistant prompts 触发；null rate 1.51%，每个返回 grid 约 1.05 次点击。
- 10.7% chat prompts 有检索意图（方向性），与 0.31% 触发率之间的 gap 指向 missed retrieval。
- 当前 lineage fields 尚未实现，Layer 2 均为 timing-based inference；returned_asset_ids 可解锁大部分 Layer 1。

## 最值得记住的一句话

当检索只在 0.31% 的 assistant prompts 触发，真正的问题不是检索是否排得好，而是它是否被调用。
