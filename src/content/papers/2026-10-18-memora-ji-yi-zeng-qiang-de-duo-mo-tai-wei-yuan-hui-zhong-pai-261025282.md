---
title: 'MEMORA: A Memory-Enhanced Multimodal Committee Reranking Agent for Reasoning-Intensive
  Retrieval'
title_zh: MEMORA：记忆增强的多模态委员会重排 Agent 用于推理密集检索
authors:
- Mohamed Mahmoud
- Mostafa Farouk Senussi
- Mahmoud Abdalla
- Mahmoud SalahEldin Kasem
- Abdelrahman Abdallah
- Hyun Soo Kang
affiliations:
- Chungbuk National University
- University of Innsbruck
arxiv_id: '2610.25282'
url: https://arxiv.org/abs/2610.25282
pdf_url: https://arxiv.org/pdf/2610.25282
published: '2026-10-18'
collected: '2026-10-20'
category: Agent
direction: Agent 记忆增强多模态检索重排
tags:
- multimodal retrieval
- agentic reranking
- episodic memory
- reasoning-intensive IR
- LLM judge
- hard negative mining
one_liner: 提出记忆增强多模态委员会重排 Agent，将查询分解为意图因子并用 episodic memory 调整优先级，在 MM-BRIGHT 上 nDCG@10
  达 41.5/38.9
practical_value: '- 把 query 拆成意图因子，对每个因子单独召回和提取 evidence，再交给 LLM judge 重排。电商搜索常见多意图
  query（如“轻薄 防晒 户外 外套”），可按材质/功能/场景拆因子，避免单一 reranker 忽略部分需求。

  - 训练电商检索向量模型时，给训练 query 拼接 GPT-4o 等生成的 CoT 意图描述，并挖 hard negatives 做 InfoNCE 微调；推理时不拼接，能显著提升语义召回，尤其适合标题和
  query 表面词重叠低的商品。

  - 用 domain episodic memory 记录历史 query 各因子是否帮助命中相关商品，在线调整因子优先级和召回权重。注意论文结论：memory
  需 >50 条/类目才有效，低频类目可考虑跨类目迁移或用规则兜底；不要单独用 document prior，会引入频率偏差。

  - 自适应 controller 采用线性状态机，根据 ranking margin 和 evidence support 决定是否继续 LLM 精排或停止，能平衡
  nDCG 收益和 API 成本；电商在线系统可把该逻辑作为开关，简单可解释，便于 A/B 测试。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：MM-BRIGHT 显示多模态查询加入图像反而拉低检索效果——最好多模态编码器 nDCG@10 仅 27.6，低于纯文本 32.2。现有系统存在单一重排器、无状态检索、弱多模态 grounding 三个未被联合解决的失败。

方法关键点：
- Reasoning-Aware Dense Retriever：基于 Qwen-Embedding 双塔，用 20k+ Stack Exchange 问答对微调，query 训练时拼接 GPT-4o 的 CoT 意图标注，hard negatives 来自 BM25 挖掘；推理时只用原始 query。
- Episodic Memory：按 domain 存储历史 query 的因子图、evidence、因子得分与成败信号；新 query 检索相似 episode，得到 document prior 和 factor helpfulness/failure prior，调整因子优先级。
- Collaborative Factor Committee：将 query 分解为意图因子，生成因子子查询扩展召回，对每个候选提取因子级 evidence 和分数，构建 bipartite factor-document graph，meta-verdict judge 基于结构化证据排序。
- Adaptive Controller：线性策略根据 ranking margin、memory hit ratio、evidence support、retriever/factor 排名 Spearman、图像标志决定 expand/judge/stop。

关键实验：在 MM-BRIGHT 29 域、2.5M 文档上，standalone MEMORA-R 达 34.1(T1)/33.4(T2)，完整系统 41.5/38.9，超过最强 agentic 基线 8.3/7.9 点。消融显示所有组件有效，episodic memory 和 meta-judge 最关键；document prior 单独使用有害；memory 深度需 >50 episodes/domain 才显著；因子数量 N=3 在 44% 成本下取得 87.2% 的 N=5 收益。

最值得记住的一句话：把 query 拆成意图因子并保留因子级成败记忆，比用单一 LLM reranker 更能处理推理密集检索。
