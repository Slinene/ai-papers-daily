---
title: Traditional statistical representations outperform generative AI in identifying
  expert peer reviewers
title_zh: 传统统计表示在识别同行评审专家方面优于生成式AI
authors:
- Vicente Amado Olivo
- Tereza Jerabkova
- Jakub Klencki
- John Carpenter
- Mario Malički
- Ferdinando Patat
- Louis-Gregory Strolger
- Wolfgang Kerzendorf
affiliations:
- Michigan State University
- Masaryk University
- Max Planck Institute for Astrophysics
- Joint ALMA Observatory
- Stanford University
arxiv_id: '2605.18752'
url: https://arxiv.org/abs/2605.18752
pdf_url: https://arxiv.org/pdf/2605.18752
published: '2026-05-18'
collected: '2026-05-24'
category: RecSys
direction: 专家推荐 · 信息检索评估
tags:
- Expert Review
- TF-IDF
- GPT-4
- Information Retrieval
- Benchmark
- LLM Evaluation
one_liner: 在细粒度领域专家匹配任务上，TF-IDF明显优于GPT-4o mini，揭示了生成式语义平滑的局限
practical_value: " - 构建专家匹配或领域内容推荐系统时，不要盲目引入 LLM；TF-IDF 等稀疏词汇匹配在需要区分近似子领域的场景下可能更可靠。\n\
  \ - 评估框架可复用：以项目提案作者作为领域专家的 ground truth，用召回率等 IR 指标严格对比方法，这种设计在电商的商家-类目匹配、达人-品类对齐等场景中也可应用。\n\
  \ - 生成式嵌入的语义平滑会丢失细粒度词汇信息，可考虑混合稀疏/稠密表示（如结合 TF-IDF 与 LLM embedding）来提升长尾或冷启动物品的推荐精度。\n\
  \ - 在 Agent 的工具调用或知识检索模块中，若任务需要精确匹配专有名词或小领域术语，传统检索方式可能比基于 LLM 的 RAG 更有效，可作为基线。"
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：学术投稿爆炸增长，传统人工寻找审稿专家已不可行，许多机构转向大语言模型（LLM）进行自动化专家推荐，但其可靠性缺乏严格评估。本文旨在构建严谨的基准，比较统计与传统方法在真实评审场景中的表现。

**方法**：将专家识别定义为信息检索问题，使用某大型国际天文台的分步式同行评审系统数据，以项目提案的作者身份作为领域专长的代理标签（ground truth）。系统评估了 6 种检索方法，包括经典的 TF-IDF 及 GPT-4o mini 等生成式 AI 方案，并采用 top-k 召回率作为主要指标。

**关键结果**：TF-IDF 在 top25 推荐中成功命中标签专家的概率达 79.5%，而 GPT-4o mini 仅为 51.5%。生成式模型因语义平滑丢失了区分相似子领域所需的细粒度词汇信息，导致性能显著落后。该结论表明，即使在大模型时代，透明、可复现的统计表示在专业化科学任务中依然具有竞争力。
