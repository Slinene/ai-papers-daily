---
title: LLM-Based Re-Ranking for Real Estate Search
title_zh: 基于 LLM 的对话式房屋搜索重排序
authors:
- Nkateko Ntimane
- Rafel Guedes
- Tiago Cunha
- Pedro Nogueira
affiliations:
- QuintoAndar
- Growthloop
arxiv_id: '2607.14835'
url: https://arxiv.org/abs/2607.14835
pdf_url: https://arxiv.org/pdf/2607.14835
published: '2026-07-16'
collected: '2026-07-17'
category: RecSys
direction: 对话推荐 · LLM 重排
tags:
- LLM Re-Ranker
- Conversational Search
- Real Estate
- A-B Test
- LLM-as-a-Judge
one_liner: 用 LLM 融合多轮对话上下文重排房屋候选，线上 CTR +5.3%, 预约看房 +4.8%
practical_value: '- 在对话式推荐流程中插入 LLM 重排模块，将多轮对话总结后与物品描述拼接，让 LLM 产出 relevance score，能有效捕捉非结构化意图。

  - 构建离线评估数据时，可用 LLM-as-a-Judge 自动标注 query-item 对，再辅以人工验证，低成本获得大规模训练/评测样本。

  - 线上部署需权衡延迟与成本：文中在召回后仅对 Top-K 重排，且使用缓存与批量推理策略，适合对延迟敏感的业务。

  - 重排 prompt 工程是核心：需将对话历史压缩为结构化摘要（如预算、位置偏好），并限定输出格式（如 JSON 分数），确保稳定性和可解析性。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：房屋搜索意图多维度、强依赖上下文，传统结构化过滤难以捕捉对话中的细微需求；对话助手普及后，用户期望用自然语言持续表达偏好，推荐系统必须整合对话历史。

**方法**：提出基于 LLM 的重排器，嵌入现有检索-精排流程。首先从多轮对话中提取关键约束总结成结构化概要；将概要与候选房源描述（标题、属性）拼接送入 LLM，输出 0-1 的 relevance 分数；按分数重排检索结果。为支持训练与评估，构建了含 96 万 query-item 对的数据集，使用 GPT-4 作为 judge 自动标注，并通过人工抽样验证一致性。

**结果**：离线实验中，LLM 重排器在 NDCG@10 等指标上优于纯检索和特征排序基线。线上 A/B 测试（随机分组，样本量充足）显示统计显著提升：点击率 +5.3%，预约看房次数 +4.8%，证实对话上下文融合有效改善推荐质量。
