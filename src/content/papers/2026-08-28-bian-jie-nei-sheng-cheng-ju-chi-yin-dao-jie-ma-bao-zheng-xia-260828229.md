---
title: 'Stay Within Your Bounds: Distance-Guided Decoding for Guaranteed Context-Free
  Grammar Compliance'
title_zh: 边界内生成：距离引导解码保证上下文无关文法合规
authors:
- Vincenzo Collura
- Karim Tit
- Eleonora Giunchiglia
- Mike Papadakis
- Maxime Cordy
affiliations:
- University of Luxembourg
- Imperial College London
arxiv_id: '2608.28229'
url: https://arxiv.org/abs/2608.28229
pdf_url: https://arxiv.org/pdf/2608.28229
published: '2026-08-28'
collected: '2026-08-31'
category: LLM
direction: LLM 约束解码 · CFG 合规
tags:
- grammar-constrained decoding
- context-free grammar
- pushdown automata
- beam search
- structured generation
- lookahead
one_liner: 用基于下推自动机的有界摘要与距离上界做 lookahead 剪枝，保证 LLM 输出一定被目标 CFG 接受
practical_value: '- 在 Agent 需要输出 JSON/SQL/查询计划等结构化内容时，可借鉴 distance-guided 可达性摘要替代只看
  next token 是否可行的局部约束，避免生成长前缀后因 tokenizer-grammar 不匹配或 token 预算耗尽而无法到达接受状态。

  - 离线预计算有界下推摘要和距离上界标签，在线解码时直接用于 horizon-aware pruning，比每次暴力做可完成性检查更适合低延迟线上结构化生成。

  - 对电商/广告场景中要求模板或 DSL 合规的文案、推荐解释、规则策略生成，可以定义目标 CFG 后复用该框架，将语法合法从“尽量”变成“保证”。

  - 若业务已有 JSON Schema 或 SQL 语法约束，可考虑把 grammar 编译为 PDA 摘要并接入 beam search，提升生成完成率和结构质量，而不是仅依赖
  prompt 或局部 token mask。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LLM 生成代码、JSON、SQL 等结构化对象时，现有 grammar-constrained decoding 主要做局部 prefix feasibility——每个 token 只要让当前前缀仍可扩展为某个合法完成即可。但在 tokenizer 与 grammar 不匹配以及 token 预算有限时，局部可行的前缀仍可能最终无法到达接受状态，导致生成中途失败或输出非法。

方法关键点：提出基于 pushdown automata 的 lookahead-guided decoding 框架。离线阶段计算 bounded pushdown summaries，带上 reachability labels 和到接受状态的上界距离估计；在线阶段利用这些距离估计做 horizon-aware pruning 和 beam search。这样解码器不仅保证每一步前缀可扩展，更能引导搜索朝最终可接受的方向前进，并证明输出在目标 CFG 上 syntactically sound，即每个输出一定被 grammar 接受。

关键结果：在 JSON、SQL、Linear Temporal Logic (LTL) 三个任务上，方法持续实现语法有效性，并在 completion quality 上优于现有 baseline，解决了局部可行但全局不可达的问题。
