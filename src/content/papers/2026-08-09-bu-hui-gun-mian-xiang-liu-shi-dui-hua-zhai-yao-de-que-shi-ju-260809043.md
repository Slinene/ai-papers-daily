---
title: 'Don''t Scroll Back: Missing-Evidence Memory for Streaming Dialogue Summarization'
title_zh: 不回滚：面向流式对话摘要的缺失证据记忆
authors:
- Hyangsuk Min
- Hwanjun Song
affiliations:
- KAIST
arxiv_id: '2608.09043'
url: https://arxiv.org/abs/2608.09043
pdf_url: https://arxiv.org/pdf/2608.09043
published: '2026-08-09'
collected: '2026-08-13'
category: Other
direction: 流式对话摘要 · 缺失证据记忆
tags:
- Streaming Summarization
- Memory Retrieval
- Dialogue Summarization
- Missing Evidence
- RAG
one_liner: 提出缺失证据记忆框架 ReMEMBER，在固定预算下针对当前窗口未解决依赖检索并提炼证据，提升流式对话摘要的缺口补全
practical_value: '- 在电商客服/导购 Agent 中，多轮对话当前轮常含指代或隐含前提，直接总结或回答会丢失 grounding。可借鉴 ReMEMBER：先识别当前窗口的未解决依赖，再按依赖检索证据，而非按语义相似度盲目取
  top-k；检索到的片段做证据密度提炼，在固定 token 预算下提升回答/摘要的事实一致性。

  - 对推荐系统长序列用户行为建模，类似流式窗口总结：每次只处理最近一段 session，但长期偏好需从历史检索。可将当前目标视为带依赖的 query，先抽取缺失证据（早期点击、属性变化）再生成紧凑记忆；这比简单截断历史或普通
  RAG top-k 更有效。

  - 工程上，评估 RAG/记忆模块不要只看生成文本质量，应拆分 memory recall 和 gap-resolution completeness 等诊断指标，便于定位是检索没召回还是生成没利用，直接用于调试检索
  Augmented 流水线。

  - 若要用 LLM 记忆服务在线低延迟场景，固定预算下先检索后压缩的 evidence-dense memory 思路，适合做 prompt 压缩或 KV cache
  精简，减少无效历史对注意力的干扰。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现代平台中用户需要反复对近期对话片段做摘要，但当前窗口往往不自洽：代词无先行词、实体无属性、决策无依据。传统对话摘要假设完整对话可用，做一次性全局摘要，难以应对无界历史流式场景。

**方法关键点**：论文将流式对话摘要形式化为“当前窗口 + 固定预算下的选择性记忆”，并指出核心挑战不是访问多少历史，而是记忆是否找到当前窗口预设的缺口证据。提出 ReMEMBER 框架：先用未解决窗口依赖（unresolved dependencies）引导检索，再把检索到的 chunk 提炼成证据密集记忆，在固定预算内喂给摘要模型。同时构建基准，分别评估记忆是否包含缺口化解证据，以及生成摘要是否真正反映该证据。

**关键结果**：在历史长达 160K tokens 的对话上，相同预算下 ReMEMBER 相比记忆构建 baseline 提升了记忆召回率和缺口补全完整度，验证了按依赖检索比单纯扩大上下文窗口更有效。
