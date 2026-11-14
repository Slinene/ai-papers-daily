---
title: 'AgentSSL: Can MLE Agents Leverage Unlabeled Data?'
title_zh: AgentSSL：MLE Agent 能否利用无标签数据？
authors:
- Ethan Lin
- Akanksha Sarkar
- Ziang Liu
- Kristin Branson
- Jennifer J. Sun
affiliations:
- Cornell University
- Howard Hughes Medical Institute
arxiv_id: '2611.17323'
url: https://arxiv.org/abs/2611.17323
pdf_url: https://arxiv.org/pdf/2611.17323
published: '2026-11-12'
collected: '2026-11-14'
category: Agent
direction: Agent 驱动半监督学习程序搜索
tags:
- AgentSSL
- Semi-Supervised Learning
- MLE Agents
- Program Search
- Unlabeled Data
- AutoML
one_liner: 把半监督学习建模为程序搜索，MLE agent 在弱反馈下合成 SSL 代码，12 个设置中 8 个超越人类基线最高 21.8%，并揭示选择瓶颈。
practical_value: '- 在拥有大量未标注日志/行为数据的电商推荐场景，可让 LLM agent 自动搜索与组合 SSL 技术（伪标签、一致性正则、弱增强等），降低人工设计训练
  pipeline 的成本；关键是定义清晰的程序搜索空间和少量验证反馈。

  - 不要直接依赖 agent 自评指标做模型/程序选择：该研究发现性能可因此下降 47%。建议引入独立的无监督或主动选择策略，例如基于验证集小样本、模型不确定性或程序复杂度筛选。

  - ProgramSelectBench 的思路可复用到推荐模型调优：构建由 agent 生成和人工设计的训练策略池，在线下小规模评估选择后再上线，避免真实流量风险。

  - agent 发现的策略在受控 benchmark 和真实域之间存在迁移 gap，电商场景需要结合业务数据做二次验证，不能直接照搬。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：在电商/广告等新域落地 ML 常面临标注数据贵、人工 pipeline 工程贵。MLE agent 能自动设计 pipeline，但以往研究几乎都在完全监督设定下，未覆盖标注稀缺、无标注数据丰富的现实情况。

**方法关键点**：该工作提出 AgentSSL，把半监督学习（SSL）建模为程序搜索问题。LLM agent 在弱反馈和匹配算力下，自动合成代码来组合、适配已有 SSL 技术（如一致性正则、伪标签、数据增强）。为研究选择瓶颈，构建 ProgramSelectBench，包含 16,977 个 agent 生成与人工设计的 SSL 程序，评估无监督和主动选择方法。

**关键结果**：AgentSSL 在 12 个设置中 8 个超越最强人类基线，最高提升 +21.8%。但程序选择是关键瓶颈：仅用 agent 自身反馈指标选程序，性能最多下降 47%。在真实生态检测任务上验证了迁移的机会与挑战。
