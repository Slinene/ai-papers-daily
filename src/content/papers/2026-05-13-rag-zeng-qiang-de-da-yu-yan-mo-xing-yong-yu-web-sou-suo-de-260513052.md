---
title: RAG-Enhanced Large Language Models for Dynamic Content Expiration Prediction
  in Web Search
title_zh: RAG 增强的大语言模型用于 Web 搜索中的动态内容过期预测
authors:
- Tingyu Chen
- Wenkai Zhang
- Li Gao
- Lixin Su
- Ge Chen
- Dawei Yin
- Daiting Shi
affiliations:
- Baidu Inc.
arxiv_id: '2605.13052'
url: https://arxiv.org/abs/2605.13052
pdf_url: https://arxiv.org/pdf/2605.13052
published: '2026-05-13'
collected: '2026-05-16'
category: Reasoning
tags:
- Temporal Reasoning
- RAG
- LLM
- Web Search
- Content Freshness
- Expiration Prediction
one_liner: 利用 LLM 对查询意图和文档时间上下文进行语义推理，动态判定内容有效期，取代静态时间窗口规则
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：商业搜索引擎中，传统“一刀切”的时效性排序策略（例如固定 30 天的新鲜度提升）无法捕捉不同查询意图下信息有效期的巨大差异。一篇关于“香港火灾”的新闻可能两天后已过期，而“交通法规”文档多年后仍有效。这种粒度错配导致搜索结果要么错误地推广已失效内容，要么过早压制仍具价值的权威信息。为此，百度提出将时效性重新定义为查询感知的动态语义有效期推理任务，用大语言模型判断内容在语义层面何时过时。

**方法关键点**：
- **时间信息提取模块**：从检索到的文档中定位时间锚点，基于查询关键词和时间实体进行上下文分块评分，提取聚焦的时间语义块集 \(S_{focus}\)，抑制噪声。
- **结构化提示与时间推理**：设计结合查询意图、\(S_{focus}\)、搜索时间的提示模板，通过少量样本示范和负约束引导 LLM 进行链式思维推理，预测查询特定的过期阈值 \(t^*_{exp}\)。同时定义时间对齐联合优化目标，包含时间距离、粒度偏差和逻辑一致性惩罚。
- **时间一致性验证模块**：采用对比前向‐后向链式思维（Forward-Backward CoT）对初始候选时间戳进行反向压力测试，计算一致性惩罚与粒度惩罚；并融合文档权威度与相关性权重，通过证据投票选取最优 \(t^*_{exp}\)，压制幻觉。
- **在线特征转换与集成**：将 \(t^*_{exp}\) 与文档时间因子比较，生成 0/1 过期信号，注入百度 Aurora 排序模型的新鲜度子网络，进行多阶特征交叉，实现软约束。系统设有失效保护，在缓存缺失或超时时退化为基线。

**关键实验**：在百度搜索真实流量上进行离线评估和 14 天在线 A/B 测试，基线为无过期信号的 Aurora 模型。离线结果显示，全局满意度分数提升 0.52%，高新鲜度查询的正导航率（PNR）在 ≤1 周和 ≤1 月区间分别提升 7.36% 和 5.21%，同时 top-4 和 top-10 结果的中位文档年龄（day_away）分别下降 2.44% 和 3.19%。在线 A/B 测试中，高新鲜度查询的 day_away 中位数降幅达 12.81%，满意度消费提升 0.78%，点击率提升 0.41%，搜索回访率也正向增长。人工评估显示，长尾/冷需求场景的好/坏比高达 12:2，时间敏感场景为 6:1，随机查询场景仍保持 5:2 的正向优势。
