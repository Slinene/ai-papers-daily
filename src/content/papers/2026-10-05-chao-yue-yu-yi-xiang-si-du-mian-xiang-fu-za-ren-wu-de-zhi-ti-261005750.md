---
title: 'Beyond Semantic Similarity: Performance and Costs of Agentic Retrieval for
  Complex Tasks'
title_zh: 超越语义相似度：面向复杂任务的智能体检索性能与成本
authors:
- Reza Esfandiarpoor
- Radek Osmulski
- Yauhen Babakhin
- Gabriel de Souza P. Moreira
- Oliver Holworthy
- Jie He
- Ronay Ak
- Jiarui Cai
- Ryan Chesler
- Bo Liu
affiliations:
- NVIDIA
- University of Edinburgh
arxiv_id: '2610.05750'
url: https://arxiv.org/abs/2610.05750
pdf_url: https://arxiv.org/pdf/2610.05750
published: '2026-10-05'
collected: '2026-10-06'
category: Agent
direction: Agent 检索 · ReAct 循环
tags:
- agentic retrieval
- ReAct
- dense retrieval
- LLM
- query reformulation
- cost
one_liner: 用 ReAct 智能体循环结合 LLM 推理与稠密检索，复杂检索 nDCG@10 平均提升 8.7 点，但成本大幅上升
practical_value: '- 复杂 query 场景（多跳、数值推理、跨语言企业文档）可以尝试用 ReAct 检索 Agent 替代一次性 dense retrieval：把原始
  query 和初始召回结果一起喂给 LLM，提供 Retrieve/Think/Final_Results 三个工具，让 LLM 动态改写 query、分解子问题并迭代探索，能显著提升
  nDCG@10。

  - 工程上不要用 MCP 包装高频检索工具：MCP 每次拉起 server、加载 embedding、网络往返开销大；改成线程安全单例 retriever，模型和索引常驻进程内，能消除一类部署错误并大幅提升吞吐。

  - 可靠性设计可借鉴 RRF fallback：当 Agent 因 context 超限或安全错误中断时，收集已执行的所有检索结果，用 Reciprocal Rank
  Fusion 合并排序作为最终结果，避免整条链路失败。

  - 成本控制是落地关键：agentic retrieval 单 query 平均 107 秒、764K input tokens，不适合在线高 QPS 场景；电商/搜索推荐中应优先用于低流量高价值的复杂
  query，或通过小模型蒸馏、并行多路检索、最大步数限制来压低 token 与延迟。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
标准 dense retrieval 依赖 query 与 document 之间的表层语义相似度，面对数学定理检索、多跳企业文档查询、需要推理与迭代探索的复杂任务时效果不足。RAG 与 DeepResearch 等新兴应用正在推动检索任务从明确的 term matching 走向 high-level 任务描述，因此需要一种能结合 LLM 推理能力和大规模语料探索能力的检索方式。

## 方法关键点
- 构建基于 ReAct 循环的 NeMo Retriever Agent：LLM 可调用 Retrieve、Think、Final_Results 三个工具，动态决定何时检索、用什么 query 检索、检索多少文档。
- 初始 user message 中包含原始 query 的 dense retrieval top-k 结果，帮助 Agent 理解语料类型并补召缺失文档。
- 优化基础设施：放弃 MCP server，改为进程内线程安全单例 retriever，模型与 corpus embeddings 常驻 GPU，避免重复加载和网络往返。
- 可靠性兜底：当 Agent 因 context 超限或内容安全错误失败时，回退到 Reciprocal Rank Fusion (RRF) 合并已有的多轮检索排序。

## 关键结果数字
- 在 ViDoRe v3 和 BRIGHT 两个 benchmark 上，相同 embedding 模型下 agentic retrieval 平均提升 8.7 个点 nDCG@10。
- 最佳配置（Opus 4.5 + colembed-vl-8b-v2）在 ViDoRe v3 达到 69.22 nDCG@10，排名 #1；同一 pipeline 在 BRIGHT 达到 50.90，排名 #2，无需任何领域适配。
- 相反，BRIGHT 专用方法 INF-X-Retriever 迁移到 ViDoRe v3 后性能大幅下降，说明 agentic retrieval 具有跨领域泛化优势。
- 成本显著：每 query 平均 107.4 秒（标准检索 0.67 秒），消耗 764.1K input tokens 和 5.8K output tokens。
- Agent 部分弥补了弱 embedding 模型的缺陷：不同 embedding 模型间的性能差距在 agentic 设置下缩小约 57%。

## 最值得记住的一句话
Agentic retrieval 用 LLM 的推理与迭代探索把检索从“语义匹配”升级为“动态信息发现”，但单 query 百秒级延迟和 76 万级 token 成本使其当前只适合高价值复杂查询或离线场景，距离大规模在线部署仍有明显效率鸿沟。
