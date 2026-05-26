---
title: Can LLMs Time Travel? Enhancing Temporal Consistency in Legal Agentic Search
  through Reinforcement Learning
title_zh: 法律大模型能否穿越时间？基于强化学习增强法律智能体搜索的时序一致性
authors:
- Wei Fan
- Yining Zhou
- Mufan Zhang
- Yanbing Weng
- Yiran HU
- Tianshi Zheng
- Baixuan Xu
- Chunyang Li
- Jianhui Yang
- Haoran Li
affiliations:
- HKUST
- Tsinghua University
- University of Waterloo
arxiv_id: '2605.25920'
url: https://arxiv.org/abs/2605.25920
pdf_url: https://arxiv.org/pdf/2605.25920
published: '2026-05-25'
collected: '2026-05-26'
category: Agent
direction: 时序感知的Agent法律检索RL训练
tags:
- Temporal Consistency
- Legal Agent
- Reinforcement Learning
- Hybrid RAG+Search
- GRPO
- Time-Aware Retrieval
one_liner: 提出 LegalSearch-R1，通过时序索引训练与混合检索增强的强化学习框架，大幅提升法律智能体的时序一致性与检索精度。
practical_value: '- 时序感知的双工具架构：本地 RAG（精确检索版本化法规条文）搭配在线 web_search（获取司法解释和评论）。电商场景可类比：本地
  RAG 存商品规格、价格等结构化信息，web_search 补充社媒评测与市场动态；RL 训练让 Agent 学会根据问题时间上下文自动路由。

  - RL 训练使 Agent 主动在查询中嵌入时间约束：无需显式标注，通过 GRPO 与 entropy-based advantage shaping 即可学会在高熵决策点（如规划期）加入时间短语。推荐智能体可借鉴，处理季节性商品、时变用户偏好时自主注入时间信号。

  - 时间索引 RAG 管道：对知识库条目标注生效时间窗口，检索时按查询时间过滤候选，确保只返回当时有效的条目。适用于政策规则、促销规则、商品生命周期等具有版本更迭的业务知识。

  - 奖励函数设计：针对异构任务（背诵条文、罪名预测、咨询评价）设计不同评分（ROUGE-L 阈值、无序匹配、LLM judge），兼顾格式合规。多任务 RL 训练时可按任务难度分配不同
  reward shaping，防止简单任务主导。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
法律推理必须在正确的时态下适用法条，但现有法律 LLM 严重受训练截止时间影响，检索智能体也几乎不加入时间约束，导致"法不溯及既往"原则被破坏。如图 1 所示，同一犯罪事实在 2009 与 2023 年修正案下得出相反结论。观察发现，所有模型在训练截止年份附近表现最好，前后版本迅速衰退（图 2），且搜索查询中极少包含时间参考（图 3）。此外，仅靠网页搜索无法提供条文级别的精确法律文本。

## 方法关键点
1. **时序索引基准构建**：从 LawBench、LexEval 等数据集中筛选含明确时间上下文的 7 项域内任务，并新增 LAR（条文背诵）任务，标注 13 个修正版本、2000–2025 年的条文，每条条文含生效时间窗口。
2. **混合工具集**：Agent 配备 `web_search`、`browse_webpage` 与 `rag_retrieve` 三工具；后者构成时序增强型本地 RAG——先由 LLM 提取查询中的时间、法规条款与关键词，再按有效性窗口过滤候选，最后通过关键字匹配、稠密向量与 BM25 三路召回经 RRF 融合排序。
3. **端到端 RL 训练**：以 Qwen2.5-7B 为基座，采用 token 级 GRPO，在时序索引数据上训练 112 步。引入 entropy-based advantage shaping（EAS）放大规划阶段 token 的优势信号，促使 Agent 学会在查询中自动添加年份等时间约束。奖励函数按任务分别设计：LAR 用 ROUGE-L≥0.95，CCP 用无序匹配，LCS 用 LLM judge 等，均为二值奖励。
4. **系统提示与路由规则**：通过 domain-specific 系统提示强制 Agent 将法条查询路由至 RAG，法律理论与案例查询路由至 web_search，并规范 think-plan 或 think-tool_call 输出格式。

## 关键实验
在 7 个域内任务（896 样本）和 6 个域外考试任务（768 样本）上评测。主要基线包括法律 LLM（DISC-LawLLM、LegalDelta）、大推理模型（DeepSeek-V3.2、o4-mini）、深度研究智能体（Search-R1、DeepPlanner 等）。
- 域内平均分 55.90，超出最强深度研究基线 DeepPlanner 42.7%，超出 DeepSeek-V3.2 10.6%。
- LAR 任务达 96.73 ROUGE-L，远超所有基线（最高 63.30）。
- 域外泛化平均 63.67，与 30B 模型相当。
- 时序查询数量：域内 502、域外 537，基线仅 97–227，增幅 121–454%。
- 消融：去掉 RAG 模块后训练奖励从 0.561 降至 0.469，LAR 降幅尤为显著。

> 最值得记住的一句话：**智能体通过 RL 主动学会在查询中注入时间约束，而非依赖显式编程，是让系统天然遵守"法不溯及既往"的核心机制。**
