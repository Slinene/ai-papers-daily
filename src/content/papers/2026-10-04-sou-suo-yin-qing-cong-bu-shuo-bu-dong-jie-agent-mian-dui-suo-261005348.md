---
title: 'Search Engines Never Say No: How Frozen Agents React When the Retrieval Tool
  Refuses'
title_zh: 搜索引擎从不说“不”：冻结 Agent 面对检索工具拒答时的反应
authors:
- Ramraj Chandradevan
- Sayontan Ghosh
- Vinoth Selvendran
arxiv_id: '2610.05348'
url: https://arxiv.org/abs/2610.05348
pdf_url: https://arxiv.org/pdf/2610.05348
published: '2026-10-04'
collected: '2026-10-06'
category: Agent
direction: 搜索 Agent · 工具侧拒答机制
tags:
- Search Agent
- Tool Refusal
- Abstention
- RAG
- Hallucination
- Query Performance Prediction
one_liner: 工具侧返回 NULL 拒答信号，让顺从 Agent 弃答率提升 243%，并给出按 recall 定价的收益曲线
practical_value: '- 在电商搜索/导购 Agent 的检索出口加“拒答门”，不改模型和检索栈：对 Qwen3-8B/32B、Haiku 这类顺从模型，一句
  NULL_RESULT + 解释就能把不可答问题的弃答率从 24% 拉到 84%、幻觉率从 65% 降到 10%，且可答准确率不降。

  - 拒答 wording 必须放进 observation，不是 system prompt；效果排序 directive > explanation > bare
  token，soft warning 几乎无效。线上无货/无匹配结果适合写成“没有可靠结果，可能索引没有该信息；请换 query 或回答 unknown”。

  - 对闭源强模型（Sonnet/Opus 5.5）工具侧拒答失效，它们更吃 system-prompt 指令（+16 点 vs 工具侧 +2 点）。多模型混合部署时建议按模型家族分别配置拒答策略。

  - 真实收益受 miss-detector 的 recall 上限约束：在固定 false-refusal budget 下，弃答收益几乎由触发器 recall
  决定。可先用轻量 QPP/交叉编码器，再按 recall-收益曲线判断是否值得上 LLM judge；detector 不行时改 agent 也白搭。

  - 用删除黄金段落/答案串构造 index-hole 测试集，比人工标注便宜且边界干净；适合复用到商品知识库 RAG 的不可答样本评估。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
检索工具总是返回 top-k，即使索引里没有答案，agent 会把不相关段落当证据并产生幻觉。训练 agent 弃答需要动权重，闭源模型不可行；重训检索栈成本又高。于是把控制点放在工具出口：做一个二元 gate，miss 时返回 NULL observation，保持 agent 和检索栈 frozen。

**方法关键点**
- 构造 index-hole 测试集：NQ 257 + HotpotQA 300，基于 wiki-18 21M BM25；ANS 保留黄金段落，HOLE 删除 gold articles 和答案别名，不可答性由构造保证。
- 7 个 frozen agents：Qwen3-8B/32B、Claude Haiku 4.5/Sonnet 5.5/Opus 5.5、Sonnet 4.6、Search-R1。
- 5 种拒答 wording：bare token、empty list、explain、directive、soft warning，另有 system-prompt directive 对照。
- Oracle/ORACLE-Q/噪声 oracle 控制触发器 recall；现实触发器包括 BM25-QPP、dense QPP、cross-encoder 和 LLM grounding judge。
- 指标：HOLE 弃答率、错误率、记忆正确率、平均调用数；ANS cover-EM。

**关键结果**
- 对 Qwen3-8B/32B + Haiku，N-EXPLAIN/ORACLE 将 HOLE 弃答率从 24.4% 提升到 83.7%（相对 +243%），错误率从 64.5% 降到 10.5%（-84%），ANS 准确率不降；比 system-prompt 高 51 点。
- wording 排序：directive 92.5% > explain 83.7% > bare 79.5% ≈ empty 79.4%；soft warning 仅 29.2%，几乎无效。
- Search-R1 不服从拒绝，72% 的推理虚构检索结果；Sonnet/Opus 5.5 工具侧拒答只使弃答 +2 点，但会凭记忆答对 39%。
- Benefit-vs-signal-quality 曲线：对顺从 agent，弃答收益与触发器 recall 近似线性；QPP 召回 16%/37%，LLM judge 61%/71% 但 false refusal 28%/36%，所有现实触发器都落在曲线上。

**最值得记住的一句话**
做一个会拒绝的检索工具，把 miss 显式写进 observation，对顺从模型可提升弃答 243% 且不损伤可答准确；但真实收益被 miss-detector 的 recall 锁死。
