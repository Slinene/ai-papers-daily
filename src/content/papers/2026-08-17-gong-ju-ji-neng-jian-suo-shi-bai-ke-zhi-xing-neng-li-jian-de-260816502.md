---
title: 'When Tool-Backed Skill Retrieval Fails: Source-Style Collapse in Executable
  Capability Retrieval'
title_zh: 工具技能检索失败：可执行能力检索中的源风格坍缩
authors:
- Yiqi Liu
- Joseph James
- Yang Wang
- Chenghao Xiao
- Chenghua Lin
affiliations:
- University of Manchester
- University of Sheffield
- Shanghai University of Finance and Economics
arxiv_id: '2608.16502'
url: https://arxiv.org/abs/2608.16502
pdf_url: https://arxiv.org/pdf/2608.16502
published: '2026-08-17'
collected: '2026-08-18'
category: Agent
direction: Agent 工具检索的源风格坍缩与路由
tags:
- Tool Retrieval
- Source-Style Shift
- TF-IDF Routing
- Dense Retrieval
- RAG
- Agent
one_liner: 固定工具库下 dense retriever 会因 query 源风格偏移而覆盖崩溃，TF-IDF 路由+少样本修复可显著恢复覆盖。
practical_value: '- 在多源工具库/API 注册中心上线前，用 query-side TF-IDF 质心距离对流量做源风格监控，设置 safe/unsafe
  band 做路由护栏，成本极低且能避免线上 candidate coverage 崩溃。

  - 不要用 naive 混合训练或平衡重加权来解决多源 drift，它会损害原本匹配源的覆盖；更划算的做法是保留多个 retriever checkpoint，做
  source-aware routing，并对 mismatched 流量用 20 条左右 matched examples 做短时继续微调。

  - 检索层是 agent 执行链路的入口，评估时优先看 coverage 或 coverage-weighted top-1 proxy，而不是只看 covered
  query 上的 reranker 精度；未覆盖 query 必须直接记为失败，否则会掩盖系统风险。

  - 把工具/API 重渲染成标准化 skill card 并不能消除源风格坍缩，说明问题在 query-tool pairing 习惯和措辞分布，而不只是 schema
  格式；做 skill 库时不要把格式归一化当成语义漂移修复。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
Agent 从短小手工工具列表转向大型外部能力池后，检索层决定下游 planner 能看到哪些可执行工具。一旦 gold tool 没进候选池，reranker/planner 无法恢复，因此工具检索门控成为系统性风险点。本文在固定 tool corpus 下发现：在 ToolRet 上 fine-tune 的 dense retriever 在同源流量保持高覆盖，但在同语料不同 source style 的 query 上覆盖几乎归零，且词法重叠更高的 APIGen 反而崩溃更严重。

### 方法关键点
- 将工具/API 渲染成 executable skill card，使用 BGE-M3 + MNRL 做 dense retrieval，candidate depth 固定为 20。
- 定义 source-style collapse：同一 tool corpus 下，query 的措辞、verbosity、schema 引用和 query-tool pairing 习惯随上游生成源变化，导致窄域 dense retriever 覆盖崩溃。
- 提出 ToolScout：用 query-side TF-IDF 质心距离作为 mismatch detector；超出安全带则路由到 aggregate-trained checkpoint；获得少量 matched supervision 后做 short continuation fine-tuning。
- 通过 skill-card 重渲染、BM25 fusion、mixed-training reweighting、hard-negative ablation 等控制实验排除替代解释。

### 关键实验
- FT-1100 在匹配 toolbench 覆盖 91.8%，但 APIGen 0.7%、ToolACE 0.0%、UltraTool 8.3%。
- 在 4996 mixed-query stream 上，FT-1100 覆盖仅 22.3%；TF-IDF 路由提升到 86.1%，接近 aggregate retriever 的 85.2%。
- 20 条 matched examples 将 5 个 collapsed sources 的 coverage-weighted top-1 proxy 从 1.3% 修复到 53.9%。
- Skill-card 重渲染后崩溃仍存在，覆盖仅 21.7%，证明不是原始 API schema 格式问题。

### 一句话
检索层决定 agent 能否执行，固定工具库下 fine-tune 的 retriever 会因 query source style 偏移而沉默失效，TF-IDF 质心距离是便宜有效的路由护栏。
