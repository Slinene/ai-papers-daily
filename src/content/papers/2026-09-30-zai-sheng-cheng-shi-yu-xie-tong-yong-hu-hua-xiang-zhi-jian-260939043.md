---
title: 'Routing Between Generative and Collaborative User Profiles: A Serving-Time
  Gate for Controllable Novelty'
title_zh: 在生成式与协同用户画像之间路由：一种用于可控新颖性的服务时门控
authors:
- Milad Sabouri
- Neeraj Sharma
- Sardar Hamidian
- Shaghayegh Agah
affiliations:
- DePaul University
- Comcast Technology AI
arxiv_id: '2609.39043'
url: https://arxiv.org/abs/2609.39043
pdf_url: https://arxiv.org/pdf/2609.39043
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: 生成式用户画像 · 服务时路由
tags:
- LLM
- User Profiling
- Routing
- Novelty
- Recommender Systems
- Serving-time Gate
one_liner: 提出服务时路由门控，在协同过滤与LLM生成画像推荐模型间按用户选择性切换，以可控新颖性-相关性权衡提升Novelty@10
practical_value: '- 借鉴 serving-time gate 思路：当有多个候选模型（如协同过滤 vs LLM画像）时，不要全局切换，而是训练轻量分类器根据用户特征动态路由，用
  NDCG 损失预算控制流量分配。

  - 特征设计简单有效：使用历史长度、消费物品流行度均值/中位数、niche ratio 等行为统计特征，无需复杂模型或画像生成过程，即可预测路由收益；其中协同表示范数是最重要特征。

  - 用 pairwise 差值定义训练标签：对每个用户计算切换前后的 ΔNovelty 和 ΔNDCG，设定双条件（ΔNovelty>0 且 ΔNDCG>=0）作为正样本，可以训练门控直接预测“有益路由”概率。

  - 评估时采用 OOF 和覆盖排名扫描，在固定相关性预算下选择最大化新颖性的阈值，避免过拟合，并得到可解释的 operating point。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM 生成的用户画像能捕捉高层偏好并提高推荐新颖性，但统一部署会大幅降低排序相关性（如 Narrative 画像 NDCG 损失高达 94.7%），且生成和刷新成本高。因此需要选择性使用，只在能带来正收益的用户上切换到生成式画像模型。

**方法关键点**：
- 将问题建模为服务时路由：默认协同过滤模型 C，候选画像模型 G（包括 LLM 生成的 Narrative、TemporalNarrative 和非生成式 Centroid）。
- 路由门控使用 Gradient Boosting 分类器，输入 serving-safe 特征：历史长度及其对数、消费物品流行度均值/中位数、niche ratio（低于全局中位流行度的比例）、C 和 G 用户表示的范数。
- 训练标签定义为：若从 C 切换到 G 后 ΔNovelty>0 且 ΔNDCG≥0，则为正样本。使用五折 OOF 评估避免标签泄漏。
- 推理时输出路由概率，通过调整阈值 τ 控制路由比例，实现可控的 novelty-relevance trade-off。

**关键实验**：在 10,000 用户真实流媒体数据集（电影/电视/体育）上评估，所有模型使用相同物品编码器。统一部署时所有画像均大幅提升 Novelty 但 NDCG 损失严重。学习到的门控在 5% NDCG 损失预算下，路由约 12.5% 用户，Novelty@10 提升 6.5%；同样预算下，学习门控优于 niche 启发式（+4.7%）、随机（+4.1%）和短历史（+2.7%）。Centroid 和 TemporalNarrative 也呈现类似模式，表明收益来自选择性路由而非 LLM 生成本身。

**值得记住**：生成式用户画像的价值不仅在于表示本身，更在于何时使用它；服务时门控提供了一种轻量且可控的部署方式。
