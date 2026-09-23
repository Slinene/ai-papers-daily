---
title: 'The Sirens'' Song: When Proximal Background Context Overshadows Distant Evidence'
title_zh: 塞壬之歌：当近端背景语境压过远端证据
authors:
- Xiaoyu Yang
- Jie Lu
- Wei Duan
- En Yu
affiliations:
- Australian Artificial Intelligence Institute (AAII), University of Technology Sydney
arxiv_id: '2609.26718'
url: https://arxiv.org/abs/2609.26718
pdf_url: https://arxiv.org/pdf/2609.26718
published: '2026-09-22'
collected: '2026-09-23'
category: LLM
direction: 长上下文注意力机制 · 重尾相关性对齐
tags:
- Long-context
- Attention
- Proximity Trap
- Heavy-tailed
- LYRA
- Benchmark
one_liner: 识别长上下文 LLM 的 Proximity Trap，并提出重尾相关性对齐机制 LYRA，把更多注意力导向任务相关证据
practical_value: '- 在电商搜索、RAG 或 Agent 长记忆场景中，不要把长上下文优化只等同于“扩大窗口”或“距离加权”；需要显式对抗近端无关内容的干扰，例如在
  memory / context 读取层增加相关性门控或对注意力分布做重尾变换。

  - 可以借鉴 LYRA 的 t-distributed heavy-tailed relevance alignment 思路：在检索增强、用户历史建模或商品详情拼接时，对
  token 级的 relevance score 做重尾映射，避免注意力被大量近端噪声 token 稀释，让远端关键信息获得更高概率质量。

  - 构建与 ProxBench 类似的评测：在 prompt 中注入大量近端但任务无关的背景文本，测试模型能否稳定利用远端证据；这比单纯 LongBench 更能暴露实际
  Agent / 搜索推荐场景下的上下文干扰问题。

  - 若自训长上下文排序或生成模型，可加入近端干扰样本，并设计 relevance-aware 的注意力匹配损失，帮助模型学习“位置近不等于任务相关”的归纳偏置。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有长上下文 LLM 研究多聚焦于解决“距离远”的问题，但论文发现远端证据被忽视通常不单是距离造成，而是大量近端、任务无关的背景文本累积竞争注意力，形成 Proximity Trap。

**方法关键点**：提出 LYRA，一种基于 t 分布的重尾相关性对齐机制。它通过方向性匹配重塑上下文检索分布，将更多注意力质量集中到任务相关证据上，同时保留原始相对位置信息，缓解 RoPE 等位置偏置带来的近端优先问题。此外，论文引入 ProxBench，一个多级细粒度基准，用于在近端背景干扰递增条件下评估远端证据利用能力。

**关键结果**：在 LongBench-v2、RULER 和 LongBench 上，LYRA 在不同上下文长度和任务类别上均取得一致提升。
