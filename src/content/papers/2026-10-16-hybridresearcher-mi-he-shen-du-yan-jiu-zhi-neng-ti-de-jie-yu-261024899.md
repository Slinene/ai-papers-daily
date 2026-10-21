---
title: 'HybridResearcher: Bridging the Structured-Unstructured Boundary for Deep Research
  Agents'
title_zh: HybridResearcher：弥合深度研究智能体的结构化与非结构化边界
authors:
- Soyoung Yoon
- Peiran Xu
- Han Wang
- Ruofan Wu
- Xiaodong Yu
- Feng Yan
- Mohit Bansal
- Debiao Li
- Seung-Won Hwang
- Yuxiong He
affiliations:
- Seoul National University
- University of California, Los Angeles
- University of North Carolina at Chapel Hill
- University of Houston
- Snowflake AI Research
arxiv_id: '2610.24899'
url: https://arxiv.org/abs/2610.24899
pdf_url: https://arxiv.org/pdf/2610.24899
published: '2026-10-16'
collected: '2026-10-21'
category: Agent
direction: Agent 跨源推理训练与数据合成
tags:
- Deep Research Agent
- Cross-Source Reasoning
- SFT+RL
- Data Synthesis
- Small Model
one_liner: 4B深度研究Agent经跨源桥接轨迹合成训练，在混合基准上超397B大模型8.3分且无灾难遗忘
practical_value: '- 电商/广告分析型 Agent 常需同时查询内部数据库（订单、库存、用户行为）和外部网页（竞品价格、市场趋势、社媒评论），可借鉴本工作从单源种子任务（text-to-SQL
  或 web search）出发构造跨源训练轨迹，让 4B 小模型掌握跨源工具调用与证据综合能力。

  - 构造训练样本时引入严格 gate（验证单源不足以回答）能强制模型学习互补性而非走捷径，业务中自制跨源数据时可效仿该机制提升数据质量。

  - 小模型经精心编排的跨源轨迹 + SFT+RL 可超越大模型且不遗忘单源能力，对成本敏感的线上 Agent 部署有直接参考：无需依赖大模型，领域内单源数据可
  bootstrap 跨源推理。

  - 评估时同时监测单源基准（如 BrowseComp）和跨源基准，确保增强能力不损伤原有单源检索或 SQL 能力，可作为模型迭代的常规检查项。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：真实分析问题常需要同时利用结构化数据（数据库、表格）和非结构化数据（网页、文档），但现有 Agent 评测显示前沿模型在跨源证据结合上仍薄弱，且缺少显式教授跨源推理的方法。

方法关键点：
- 数据合成：从已验证的单源任务（text-to-SQL 或 web search）出发，围绕种子输出中的 bridge entity 构造缺失的另一侧数据源，形成跨源轨迹。
- 质量 gate：仅保留经严格构造性验证确认“单源不足以回答”的样本，确保数据要求真正的跨源相互依赖。
- 训练：在 4B 基座 Qwen3.5-4B 上用该数据集进行 SFT，随后做 RL。

结果：在 HybridDeepResearch 基准上，HybridResearcher-4B 比基座 Qwen3.5-4B 提升 30.0 分（pass@8），并超越大得多的 Qwen3.5-397B-A17B 8.3 分；同时在单源基准 BrowseComp 和 BrowseComp-Plus 上也有提升，表明没有灾难性遗忘。
