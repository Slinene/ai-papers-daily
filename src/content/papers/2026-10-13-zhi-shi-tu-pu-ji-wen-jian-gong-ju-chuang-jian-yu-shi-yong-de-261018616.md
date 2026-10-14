---
title: 'Knowledge Graphs as Files: An Agent Harness Where Tool Creation and Tool Use
  Co-Evolve'
title_zh: 知识图谱即文件：工具创建与使用协同演化的 Agent Harness
authors:
- Yuyang Bai
- Yu Wang
- Yu Zhang
affiliations:
- Texas A&M University
- University of Oregon
arxiv_id: '2610.18616'
url: https://arxiv.org/abs/2610.18616
pdf_url: https://arxiv.org/pdf/2610.18616
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: Agent 知识图谱搜索与工具演化
tags:
- Knowledge Graph
- Agent
- Tool Creation
- Direct File Access
- Training-Free
- STaRK
one_liner: 让 LLM 直接读写完整节点/边文件并现场编写图访问代码，训练自由即在 STaRK 上超越最强基线
practical_value: '- 对文本富商品/内容知识图谱，不要只提供固定的 `neighbors/get_node/search` 工具（截断 top-k
  易漏掉关键证据）。可把完整节点记录和边表导出为 jsonl/tsv 文件，让 agent 直接用 shell/grep/Python 做任意图访问，避免预定义
  API 的证据瓶颈。

  - 大输出存文件：多跳遍历或全节点扫描常超出上下文，可把完整输出写入 scratch 文件，只给模型看 head/tail 和大小提示，后续代码再搜索/过滤完整输出。这个
  trick 对电商商品大量评论、论文摘要、知识图谱邻居列表等场景很实用。

  - 允许 agent 在一个任务内多轮编写并修订 Python 程序，而不是只允许单次代码生成或纯工具调用。消融显示多轮编程相比单次程序提升约 6.2 overall
  H@1，相比 shell-only 提升 6.9 点；单次程序只恢复约十分之一增益。

  - 让执行反馈驱动工具演化：保留历史代码和输出文件，复用前面程序出现的节点 ID，失败后优先修订上一程序。trajectory 中 48.4% 的程序包含前序输出里的
  ID，失败后 88.6% 的下一程序会修订上一程序；更强模型会更早编程、更多复用输出、更高修订率。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**

文本富知识图谱（如 Amazon 商品、MAG 论文、PrimeKG 药物）上的查询常同时包含关系约束和文本证据查找。现有方法依赖预定义图接口：`search/get_node/neighbors` 或 subgraph retriever，单次调用返回的证据有限，例如 `neighbors` 只返回 20 条邻居，导致 agent 可能完全错过 gold 节点。即使让 agent 写代码组合 API 调用，仍然受接口返回截断和可访问范围限制。

**方法关键点**

DKGI 把 KG 无损导出为普通文件：
- 每个节点一行 jsonl，含 `node_id, node_type, is_candidate, attributes`；每个关系一个边表 tsv，列为 `source_id, target_id`；另有 `schema.json` 和 `candidate_ids.txt`。
- Agent 在 Pi 或 Codex CLI 中用 ReAct 循环，自由组合 shell 工具（`cat/head/rg`）和 Python；代码直接读文件，实现全节点扫描、ID 查找、一跳/多跳遍历、集合交并差、打分排序等图操作。
- 大输出写入 scratch 文件，模型只接收 head/tail 和大小提示，后续代码可再处理完整输出，控制上下文。
- 工具创建与工具使用协同：执行反馈（候选 ID、空匹配、错误）引导代码修订，修订后的代码再决定后续证据采集；历史代码集 `T_t` 和输出文件集 `L_t` 支持复用。

**关键结果**

在 STaRK 三个数据集完整测试集上，training-free DKGI 用 GPT-6-Astra 达到最高 H@1/MRR，比最强已发布基线 GRASP 在 Amazon/MAG/Prime 分别高 8.2/9.0/6.7 H@1；即使 GPT-6-Luna 在 Pi 也超过最强 training-free 基线。消融固定模型和 harness：Full DKGI overall H@1 75.2，Graph tools 72.8，Shell only 68.3，One program 69.0；去掉边文件降到 44.2，说明关系遍历关键。Trajectory 分析显示平均每 query 写 4.0 个程序，75.0% 含全节点扫描，48.4% 复用早期输出 ID，36.5% 修订前序代码。

最值得记住的一句话：让 agent 把知识图谱当文件直接编程访问，并让工具创建与工具使用在执行反馈中协同演化，是提升文本富图谱上复杂查询能力的关键，而不是设计更复杂的预定义图 API。
