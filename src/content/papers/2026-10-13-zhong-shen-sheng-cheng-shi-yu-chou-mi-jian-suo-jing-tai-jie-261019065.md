---
title: 'Revisiting Generative vs. Dense Retrieval: A Static Value Prior Reverses the
  Gap'
title_zh: 重审生成式与稠密检索：静态价值先验逆转差距
authors:
- Renbo Tu
- Yang Liu
- Shuying Sun
affiliations:
- Shopify
- University of Toronto
arxiv_id: '2610.19065'
url: https://arxiv.org/abs/2610.19065
pdf_url: https://arxiv.org/pdf/2610.19065
published: '2026-10-13'
collected: '2026-10-15'
category: RecSys
direction: 生成式 vs 稠密检索的评估与价值先验
tags:
- generative retrieval
- dense retrieval
- semantic ID
- popularity bias
- sequential recommendation
- evaluation metrics
one_liner: 电商候选检索中，GR 的价值领先主要来自静态热门度，静态价值先验重排 DR 可反超且保持 recall 领先
practical_value: '- 在电商候选生成离线评测中，除了 Recall@k / NDCG@k 的 exact next-item，务必加入 best-item
  value (BV@k) 和 value-weighted NDCG (vNDCG@k)。精确命中指标有 substitute blindness，无法奖励“有用替代品”，可能导致
  GR 看起来很强；用类目/共现/LLM-judge 的部分得分更能反映真实业务价值。

  - 若团队正在对比 Semantic ID 生成式召回与双塔/稠密召回，先做一次价值分解：把生成式方法的价值领先拆成 popularity / rating /
  brand 等静态项。如果 popularity 贡献 50%+，说明领先很可能来自“背热门”，不是个性化理解；可以做 popularity-agnostic
  评估或对热门项降权。

  - 训练一个简单且强的 baseline：DR + static prior。把 DR 相似度归一化后与静态商品价值分按 0.5 权重融合，只对 top-200
  候选重排；不用重新训练、不用 decoder，线上可即时部署。论文中这一招把 DR 的 BV@50 从落后 GR 变成领先，Recall 还高于 GR，vNDCG
  最高。

  - 工业场景不要被参数规模唬住：14B 的 SID-LLM 生成式召回在 LLM-judged 分级相关性上低于约 300M 的稠密 encoder。升级到 GR
  前，建议用 LLM-judge 对候选做 graded relevance（可给替代品部分分数），并与 DR+静态价值先验做 A/B；如果 GR 没有显著价值增量，维持
  DR 成本更低。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式检索（GR）借助 Semantic ID 和 LLM 已经成为电商候选生成的强候选方案，但并非在所有指标上都一致强于稠密检索（DR）。现有 Recall@k / NDCG@k 只给精确命中目标记分，存在 substitute blindness，也不考虑商品商业价值，导致“谁更强”取决于评估口径。  

**方法关键点**  
- 在 Amazon Toys 2014 和 2023 两个数据集上做受控对比：GR 和 DR 共用同一个 T5 encoder-decoder，GR 用 prefix constrained beam search 解码 Semantic ID，DR 用历史 embedding 做 cosine 相似度召回。  
- 定义补充指标：类目相关性 qcat 给同叶子类目的替代商品记分；静态商品价值 vi = 0.25×log popularity 分位 + 0.25×Wilson rating + 0.50×brand footprint；BV@50 看 top-50 中最佳相关商品的价值，vNDCG@50 看整列表的 value-weighted NDCG。  
- 分解 GR 价值领先中 popularity / rating / brand 的贡献，并提出训练无关的 DR+prior：对 DR top-200 候选做相似度归一化，再与静态价值分按 0.5 权重融合重排。  

**关键结果**  
- 公开数据上 DR 领先 Recall@50（2014：0.228 vs 0.167；2023：0.084 vs 0.052）和 vNDCG@50（2014：0.222 vs 0.215；2023：0.168 vs 0.160），但 GR 在 BV@50 配对比较中赢面超过 DR 的两倍。  
- 在 GR 赢 BV 的用户中，popularity 贡献了 2014 年 49.8% 和 2023 年 65.4% 的价值领先。  
- DR+prior 逆转了 BV@50：2014 年 ΔBV 从 -0.020 到 +0.023，2023 年从 -0.016 到 +0.006；同时 Recall 仍高于 GR，vNDCG 达到最高的 0.240 / 0.175。  
- Cold items 和替代品信用测试没有显示 GR 的稳定优势；工业数据集上 14B SID-LLM 的 NDCG@50 为 0.453，低于约 300M 稠密 encoder 的 0.474，DR+prior 进一步提升至 0.530。  

> 最值得记住：GR 的价值领先主要来自静态热门度/价值属性，把同一静态先验接到 DR 的候选重排上，就能反超 GR 并保留 recall 优势。
