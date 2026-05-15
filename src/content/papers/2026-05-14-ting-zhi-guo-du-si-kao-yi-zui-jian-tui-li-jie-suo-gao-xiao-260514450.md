---
title: 'Stop Overthinking: Unlocking Efficient Listwise Reranking with Minimal Reasoning'
title_zh: 停止过度思考：以最简推理解锁高效列表重排序
authors:
- Danyang Liu
- Kan Li
affiliations:
- Beijing Institute of Technology
arxiv_id: '2605.14450'
url: https://arxiv.org/abs/2605.14450
pdf_url: https://arxiv.org/pdf/2605.14450
published: '2026-05-14'
collected: '2026-05-15'
category: RAG
tags:
- RAG
- Listwise Reranking
- Chain-of-Thought
- Self-Distillation
- Efficiency
- Overthinking
one_liner: 提出长度正则化自蒸馏，剪枝冗余推理，在保持排序效果的同时减少 34–37% 的推理 token
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推理增强的列表重排序（如 Rank-K）通过生成长链推理（CoT）提升检索效果，但往往产生数千 token 的推理过程，导致高延迟，无法满足实际应用。实验发现“过度思考”现象：增加推理长度对排序质量回报递减，nDCG@10 几乎停滞。因此，如何在保持排序精度的同时大幅压缩推理长度成为关键挑战。

**方法关键点**：
- 提出**长度正则化自蒸馏框架**，让模型从自身生成的简洁高效推理轨迹中学习。
- **采样**：用 Rank-K 教师模型对每个查询采样 16 条推理轨迹（温度 0.7，top-p=0.95）。
- **双标准过滤**：只保留 nDCG 不低于该查询平均值、且长度短于平均值的轨迹，排除“思考不足”与“思考过度”的样本。
- **构建蒸馏语料**：从每查询高效集合中取最短轨迹，最终获得约 1.1 万条高质量短推理样本（种子 5 万查询，保留约 22%）。
- **微调**：用长度归一化的负对数似然对原模型做全参数微调，使其内化简洁推理模式。

**关键实验**：
- 数据集：TREC DL 2019/2020，TREC NeuCLIR（波斯语、俄语、中文），第一阶段分别用 BM25 和 SPLADE-v3 检索。
- 对比：RankZephyr（非推理）、原始 Rank-K（32B 推理模型）。
- 核心结果：Rank-KDistill 在 nDCG@10 上持平甚至略优 Rank-K（如 DL 2019 BM25：0.668 vs 0.662），同时推理 token 数在 BM25 设置下减少 37%，SPLADE 下减少 34%。跨域泛化良好，避免了 RankZephyr 在 NeuCLIR 上的严重退化。
- 冗余分析：蒸馏模型将尾重复比（TRR）从 0.210 降至 0.126，多出现比（MOR）从 0.293 降至 0.185，证实其减少了无意义的自循环与反复推敲。

**最值得记住的一句话**：自蒸馏让模型学会在排序决策稳定后果断停止生成，用更短的推理路径达到同等甚至更好的排序质量。
