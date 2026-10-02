---
title: 'RPTune: Learned Context Curation for LLM Catalog Search'
title_zh: RPTune：LLM 目录搜索的学习式上下文筛选与后训练
authors:
- Chuxuan Hu
- Hejie Cui
- Norman Huang
- Shubham Kumar Bharti
- Wang-Chiew Tan
- Sercan Ö. Arık
affiliations:
- Google
- University of Illinois Urbana-Champaign
arxiv_id: '2610.00964'
url: https://arxiv.org/abs/2610.00964
pdf_url: https://arxiv.org/pdf/2610.00964
published: '2026-09-30'
collected: '2026-10-02'
category: RecSys
direction: 长上下文 LLM 商品搜索 · 上下文筛选
tags:
- LLM4Rec
- Context Curation
- Catalog Search
- RLHF
- Post-training
- SMB
one_liner: 提出 RPTune，用可学习 curator 对全量商品目录做剪枝重排，并配合 LLM 后训练，在 7 个小商家上显著提升商品搜索准确率
practical_value: '- 对中小商户/长尾目录，若 catalog 可放入 LLM context，直接全量 prompt 比多阶段 RAG 更优；可先用
  RPTune 类 curator 做 25% 剪枝，精度不降反升，同时降低延迟。

  - 用 encoder+MLP 重排器，让 reorganizer 以冻结 LLM 反馈为信号做 RL，优化目标对齐下游选择准确率，而非单纯语义相似度；ascending
  排列把高分商品放在 prompt 末尾（靠近生成位置）效果最好。

  - 无行为数据冷启动时，用 frontier LLM 为每个商品生成合成 query，并对全 catalog 做 graded relevance scoring，训练和评估都无需商户日志；这种数据管线可复用到新品/小目录场景。

  - LLM 后训练采用 context-relative reward：只要求在 curated 目录内选最高相关商品，并对幻觉（输出 catalog 外商品）给
  -1 惩罚，能充分利用剪枝后的候选集，比全局 top-1 或连续分奖励更稳定。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：小商家 SMB 的目录通常只有几十到几百个商品，可直接放入长上下文 LLM，但 LLM 对长上下文的利用不均匀，简单全量 prompt 仍有较大改进空间；同时 SMB 缺少行为数据和 ML 团队，无法使用传统多阶段检索。论文研究如何为 LLM 整理和呈现目录，以及如何针对整理后的上下文做后训练。

**方法关键点**：
- RPTune 由 catalog curator 和 LLM post-training 组成。curator 包含 encoder 和 reorganizer：encoder 用双塔生成 query/product 嵌入；reorganizer 计算 priority score = τ·相似度 + MLP([query_emb; item_emb])，据此剪枝并 ascending 排序（高分商品放最后，靠近生成位置）。
- reorganizer 用 LLM-in-the-loop RL 训练：冻结的 LLM 从 curated context 采样商品，用预计算的 relevance 分数做组内标准化得到 advantage，更新重排器，使其直接优化 LLM 选择准确率。
- 训练数据全部由 frontier LLM 合成：对每个商品生成 10 个 query，再对每个 query 对全 catalog 打分得到 graded relevance；无需商户行为日志。
- LLM 后训练采用 GRPO，reward 为 context-relative：选中 curated 目录内最高分商品 +1，幻觉（输出目录外商品） -1，其余 0。

**关键结果**：在 7 个真实 Shopify 商家（覆盖美妆、食品、宠物等）的 100 个复杂对话 query 上，RPTune 在 9 个 LLM backbone 上平均提升 EM 13.5 pp、FR 10.1 pp，延迟降低 28%；全 pipeline 将 gemma-4-E4B-it 的 EM 从 10.7% 提升到 31.0%（+20.3 pp）；全 catalog 直接 prompt 已比 RAG 类基线高至少 9 EM 点；curation 最高带来 31.4 pp 的提升。

**最值得记住**：对于能塞进 LLM 上下文的目录，先用小型可学习 curator 剪枝重排，再用 context-relative reward 后训练 LLM，可以在无行为数据下大幅超过全目录 prompt 和多阶段 RAG。
