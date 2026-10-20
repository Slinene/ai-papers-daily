---
title: 'OpenSaC: A Python Library for Search as Code in Deep Research Agents'
title_zh: OpenSaC：面向深度研究智能体的 Search as Code Python 库
authors:
- Qi Liu
- Jiaxin Mao
- Fengbin Zhu
- Tat-Seng Chua
- Ji-Rong Wen
affiliations:
- Renmin University of China
- National University of Singapore
arxiv_id: '2610.25779'
url: https://arxiv.org/abs/2610.25779
pdf_url: https://arxiv.org/pdf/2610.25779
published: '2026-10-19'
collected: '2026-10-20'
category: Agent
direction: 深度研究 Agent · Search as Code
tags:
- Search as Code
- Deep Research Agents
- Python Library
- Agentic Search
- Codex
one_liner: 开源 Python 库 OpenSaC 将搜索、抓取、重排、LLM 调用组合为可执行程序，使 Codex 类智能体做深度研究时显著节省 token
  与时间
practical_value: '- 在电商/广告深度研究型任务（竞品调研、商品参数多源比对、落地页批量解析）中，可将“搜索→抓取→重排→LLM 字段抽取”封装为可组合
  SDK，由 coding agent 一次写成批量程序执行，避免 ReAct 逐条交互，显著降低 token 与 wall-clock 时间。

  - 统一返回结果并保留 URL/来源标识，天然适合需要可追溯证据的选品、价格监控和广告素材合规审查；把中间文件落盘到 workspace 可复用，避免重复抓取。

  - provider 可替换和批处理容错设计（batch 保持顺序、返回 per-input errors、部分成功）值得直接借鉴到推荐/搜索的离线数据生产：批量
  query 生成、召回通道调用、rerank 评估都可以做成可配置后端和可重试代码单元。

  - 若业务已有编码 agent（如 Codex/Claude Code），可模仿其 skill 机制增加内部“检索/数据获取”技能卡，显式教授 agent 何时
  batch、何时保留 full source、何时只返回高置信片段；这种方式比硬编码 pipeline 更灵活且可调整。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
深度研究 agent 需分解复杂问题、查找来源、检查定义、对齐证据；传统 ReAct 循环每次搜索/阅读都返回中间结果，增加交互与上下文，但许多已知输入的操作（批量检索、融合候选、解析记录）无需模型决策。Search as Code 把可执行程序作为交互单元，批量组合搜索、抓取、重排、模型调用和本地处理，仅把选定的证据返回给模型，从而减少 token 和延迟。

### 方法关键点
- OpenSaC 提供类型化 SDK：search.many、content.fetch_many、rerank、llm.complete/extract、fuse、dedup 等，支持独立配置 provider。
- 统一结果类型保留 URL、标题、snippet、domain 等来源信息，便于保留证据和审查。
- 批量方法保持输入顺序，返回 per-input 错误，可部分成功和重试。
- 异步 runtime 管理并发上限、超时、校验、日志；本地 helpers 提供加权 RRF 融合和去重。
- provider dispatch 通过 adapters 注册，可替换 Serper、Jina Reader、OpenAI 兼容 endpoint 等，无需改程序逻辑。
- 配套 skill 指导 Codex/Claude Code 如何写程序、何时批量、如何保留 sources 和选择 observations。

### 关键实验
在 BrowseComp（事实查找）和 WideSearch（宽泛信息收集）上对比标准 Codex 内置 web search。排除污染后 169/166 paired tasks。BrowseComp：准确率 82.25→85.21，时间 -30.3%，token -37.8%，成本 -36.4%。WideSearch：row F1 60.62→59.78，降 0.84pp，时间 -29.5%，token -13.8%，成本 -12.6%。

### 最值得记住的一句话
把多步信息获取编写为可检查、可复用的程序，能大幅降低深度研究的 token 和时间成本，但需注意在宽泛信息收集任务上可能牺牲部分召回/覆盖。
