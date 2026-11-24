---
title: 'NoeVera: Can Knowledge Guide Experiments and Experiments Refine Knowledge?'
title_zh: NoeVera：知识能否引导实验、实验能否反哺知识？
authors:
- Pinaki Prasad Guha Neogi
- Spyros Mastorakis
- Ankur Mallick
- Saravan Rajmohan
- Victor Rühle
affiliations:
- Microsoft M365 Copilot Research
- The Ohio State University
arxiv_id: '2611.29255'
url: https://arxiv.org/abs/2611.29255
pdf_url: https://arxiv.org/pdf/2611.29255
published: '2026-11-22'
collected: '2026-11-24'
category: Agent
direction: Agent 证据留存与选择性仿真
tags:
- LLM serving
- RAG
- Agentic Memory
- Knowledge Distillation
- Simulation
- Evidence Provenance
one_liner: 保留证据与适用条件的三平面 Second Brain Agent，用知识引导仿真实验并写回 scoped evidence，比 BO 更少调用达到近优配置，过泛化仅
  8%
practical_value: '- 将知识库拆成 Evidence / Synthesis / Agent Memory 三平面：所有合成结论必须保留 support
  set 指向原始证据；在电商实验平台可把策略结论绑定适用条件（类目、用户分群、时间窗、投放位置），避免一个实验结论被误用到不同场景。

  - 用 scoped evidence record 存实验发现：记录 workload、hardware、config、tool、observation、provenance，并在检索时做
  applicability check；对推荐/广告 A/B 实验同样可把实验结果写成带适用范围的条目，后续策略搜索时先查可直接复用/部分匹配/不匹配，不匹配则降级为历史上下文并加
  caveat。

  - 决策感知检索 + 混合召回：BM25 / dense / graph / code / evidence atoms 多路召回后，按 authority、applicability、lifecycle
  排序并组装固定 token budget 的 evidence pack；在业务 Agent 中可用类似方式给 LLM 提供证据包，并做 coverage check，让模型有足够证据再决策，减少幻觉。

  - 选择性调用实验/评估：仅当 query profile 要求量化且证据包没有直接适用估计时才调用 simulator/评估工具，避免无谓调用；该策略在论文中把仿真时间降到
  27%，同时保持 97% 质量，对成本敏感的推荐 Agent 有直接参考价值。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 服务系统优化瓶颈已从“预测给定配置性能”转移到“决定该调查什么”：哪些机制、哪些配置值得测试、决策需要哪些证据。知识散落在论文、代码、benchmark、历史实验中，各自有假设和可靠性。检索片段可能提到正确机制但 workload 不匹配；仿真估计不说假设；无记忆 agent 每次重建上下文。

## 方法关键点
- **三平面 Second Brain**：Evidence Plane 保存 source cards、briefs、原始指针和 authority signals（strength/role/corroboration/freshness/applicability）；Synthesis Plane 选择性提炼 claims/concepts/techniques/decision matrices，每个 synthesis object 有 support set 指向证据；Agent Memory Plane 记录路由/审查/使用记录，推理时禁用。
- **决策感知检索**：query profiling + 混合检索（BM25/dense/graph/code/evidence atoms）→ authority/applicability/lifecycle 加权排序 → 预算证据包 P(q,u) 并做 persona-specific coverage check。
- **Agentic reasoning**：controller 协调 scout/investigator/synthesizer，区分 supported observation 与 inferred recommendation；仅当需要量化且证据包无直接适用估计时才调用 Vidur/GAUSS。
- **闭环写回**：实验发现写成 scoped evidence record e_t=(workload, hardware, config, tool, observation, provenance)，检索时做 applicability check，冲突证据并存。

## 关键结果
- 配置搜索：NoeVera+V 中位 6 次仿真调用达到 5% 最优（IQR 4-9），对比 BO 9、ReAct+V 15、random 12；A100 上吞吐 1.31× vLLM default，全部满足 SLO；换 GAUSS 中位 7 次。
- 证据复用：evidence records 过泛化率仅 8%，Mem0 28%、plain chunk 33%；可复用 follow-up 质量 +0.09 vs Mem0 +0.03；50 查询流中仿真调用从 1.4 降到 0.5（-64%）。
- NoeVeraBench：总体 0.80 vs ReAct+V 0.62、Hybrid RAG+V 0.59；证据演化 0.71 vs Hybrid RAG 0.41，prompt matching 后仍有 +0.08 显著优势。成本 $0.35/query，构建成本 $294 摊销 $0.38-0.64/query。

**最值得记住的一句话**：知识组织是一等设计决策——把证据、合成、使用记忆分离，并把实验结论写成带适用条件的 scoped record，才能安全复用并减少不必要的探索。
