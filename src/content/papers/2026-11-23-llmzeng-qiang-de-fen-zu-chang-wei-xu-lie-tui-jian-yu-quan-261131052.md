---
title: 'From Head to Tail: LLM-Augmented Sequential Recommendation and Trade-off Optimization'
title_zh: LLM增强的分组长尾序列推荐与权衡优化
authors:
- Adeep Hande
- Shaghayegh Agah
- Neeraj Sharma
- Karina Halevy
- Sardar Hamidian
affiliations:
- Comcast Applied AI Research
- Carnegie Mellon University
arxiv_id: '2611.31052'
url: https://arxiv.org/abs/2611.31052
pdf_url: https://arxiv.org/pdf/2611.31052
published: '2026-11-23'
collected: '2026-11-24'
category: RecSys
direction: 序列推荐 · LLM数据增强 · 长尾优化
tags:
- LLM
- Data Augmentation
- Long-tail Recommendation
- Sequential Recommendation
- Popularity Bias
- SASRec
one_liner: 按交互频率分组，用LLM从候选池生成单条合成交互插入序列，显著提升长尾/冷启动NDCG与覆盖，并刻画整体降解约束下的权衡。
practical_value: '- 用 log-space 交互频次分位数动态划分 G0/G1/G2/G3，替代固定阈值；电商可直接按商品销量/曝光分桶，并在各桶上分别评估
  NDCG@20，避免把长尾当整体。

  - LLM 增强采用 embedding 候选召回 + closed candidate pool：先用文本 embedding 算用户历史均值与商品描述 embedding
  的 cosine 相似度筛选 top-10，再让 LLM 从候选池 listwise 选择；这比随机候选稳定得多，适合有标题/类目元数据的场景。

  - 每个用户只插入一条合成交互，位置放在验证/测试项之前（Sn-2）。SASRec 对近期项敏感，插入位置很关键；早期插入 Sn/2 会稀释信号，工业落地应把位置作为超参。

  - 把整体 NDCG@20 下降 ≤5% 作为 guardrail，逐组做 Pareto 分析选 operating point；跨组同时增强不是简单叠加，单组最优组合总比例过大会导致整体大幅下降，需要联合校准。生产上默认用
  70B LLM + 元数据少提示成本最低，要更多提升再上 metadata enrichment 或小模型微调。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：推荐系统的 popularity bias 造成长尾/冷启动物品交互稀疏，SASRec 在头部和尾部之间 NDCG@20 差 92-95%，冷启动零曝光。传统 contrastive/negative sampling 只在既有交互分布内操作，未带来新曝光；LLM 生成合成交互有潜力，但现有方法把长尾当单一体或未刻画整体与分组指标的 trade-off。

方法关键点：
- 用 log-space 75th/95th 分位数把物品分为 G0（冷启动，交互=0）、G1（极端长尾，0-75th）、G2（常规长尾，75th-95th）、G3（热门），而非固定阈值。
- 增强 pipeline：对目标组抽 p 比例用户，每用户生成一条合成交互。先由 Linq-Embed-Mistral 计算用户平均 embedding 与物品 embedding 余弦相似度，从组内取 top 10 候选（ML-32M 元数据不足则随机）；Llama-3.3-70B-Instruct 用 listwise prompt 从封闭候选池选一个物品，插入到用户序列的 Sn-2 位置；SASRec 在增强后数据上从头重训。
- 优化形式：约束最大化组级 NDCG@20 与组级 coverage GCov@100，整体 NDCG@20 下降 ≤5% 作为 guardrail；用坐标下降逐一优化候选选择、增强比例、跨组分配、LLM 配置。

关键实验：
- PRD 工业数据上，G2 在 p=5% 时 GN@20 +48.28%，整体 N@20 -2.09%；极端长尾 G1 最终提升超过 100%，常规长尾 G2 提升 60%+，覆盖增加。ML-32M 上 G1/G2 分别约 +40%/+25%。
- 跨组增强：把单组最优比例直接合并（总 23%）使整体 N@20 下降 24.49%，说明单组最优不可简单加和，需要联合多目标校准。
- LLM ablation：默认 Mistral-7B + Llama-70B 成本-质量最优；加入完整元数据使 GN@20 达 +60.39% 但 token 成本 5.12x；LLM-as-a-judge 提升整体但组增益下降；插入位置早期 Sn/2 效果差于 Sn-2。

最值得记住：长尾增强必须分位数分组，并在整体 NDCG 约束下逐组做 Pareto 选择；单组最优策略不能直接叠加。
