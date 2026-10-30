---
title: 'GistRank: Gist-Compressed Listwise Ranking with Large Language Models'
title_zh: GistRank：基于 Gist 压缩的大模型列表级排序
authors:
- Guo Chen
- Wenhan Liu
- Reed Li
- Qianwen Ma
- Yu Lu
- Haibo Shi
- Bingbing Xu
- Junjie Huang
affiliations:
- Southwest University
- Renmin University of China
- Yuanbao Team, Tencent
- Institute of Computing Technology, Chinese Academy of Sciences
arxiv_id: '2610.39610'
url: https://arxiv.org/abs/2610.39610
pdf_url: https://arxiv.org/pdf/2610.39610
published: '2026-10-29'
collected: '2026-10-30'
category: RecSys
direction: LLM listwise 重排 · Gist 压缩
tags:
- Gist Ranking
- Listwise Ranking
- LLM
- Context Compression
- Reranking
- KV Cache
one_liner: 用三阶段训练将每个候选段落压成4个gist token，在TREC/BEIR上以约14倍加速逼近全文本重排效果
practical_value: '- 把商品标题/详情/卖点用 Stage 1 的 query 预测目标预训练成 4 个 gist token，线上重排只拼接 gist，可将
  100 个候选的 prompt 从 8k+ token 降到约 1.25k，延迟和 KV cache 占用大幅下降

  - 借鉴 Stage 2 的 citation/click 偏好：在电商搜索中可用点击 vs 曝光、成交 vs 点击构造成对数据，训练 gist 或 item
  表示具备判别性，无需昂贵人工标注；再用少量人工/LLM 标注做 Stage 3 listwise 微调

  - 用 rank-slot + ListMLE 非自回归打分替代 LLM 自回归生成排序，可以把排序阶段从生成式 token 序列变成一个固定大小的打分矩阵，吞吐更稳定，适合在线
  serving

  - 注意成本结构：候选压缩占 90%+ 延迟，优先考虑对全量商品库离线预计算 query-independent gist 或做近似缓存，只在线对当前 query
  做轻量融合/重排序'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

动机：LLM 列表级排序（listwise ranking）需要对所有候选联合比较，但把每条候选全文串进 prompt，输入长度随候选数与长度线性增长，线上排序延迟与成本难以承受。滑动窗口重复编码重叠块，硬压缩又丢判别细节。soft gist 压缩虽然能缩短上下文，但普通 gist 训练目标是重构或生成条件，不会保留“相对偏好”这类排序关键信号，直接用于排序效果有缺口。

方法：
- Stage 1 Query-predictive gist learning：用约30B token 的搜索 query-doc 数据，把 [passage; gist tokens; query] 放在一起，通过半双向注意力 mask 让 gist token 能充分看到整段 passage，但 query 只能看到 gist，从而强制 passage 信息经过 gist 完成 query 预测。
- Stage 2 Pairwise preference training：利用约1536万 query 的搜索结果 citation 行为，cited 结果当作正样本、uncited 当负样本，输入 [passage; gist; query prompt; CLS]，用 pairwise hinge loss 让 gist 学会区分同一 query 下相近候选。
- Stage 3 Listwise ranking adaptation：在 GPT-4o 标注的 MS MARCO 排序数据上微调，query 先于 gist，给 gist 加 learned document-position embedding；压缩阶段保留 gist 的 layer-wise KV cache，rank 阶段把 KV 注入 rank slots，用 ListMLE 非自回归一次输出排序。

结果：
骨干 Qwen3-4B。在 TREC DL19/20 与 5 个 BEIR 子集上，平均 nDCG@10 为 59.17，排名第二，仅比最强全文本基线 FullRank100 低 0.89；比同骨干全文本 SFT 高 1.37–2.00 点。K=4 gist token 是效率-效果拐点。端到端 P50 延迟 DL19 为 1,625ms、DL20 为 1,634ms，相对 one-shot 全文本排序快约 14 倍；候选压缩占约 93% 延迟，rank 阶段仅占约 7%。

最值得记住：gist 压缩用于排序的关键不是把 prompt 变短，而是通过 pairwise/ranking-aware 训练让压缩表示显式保留相对偏好信号；推理端主要瓶颈转移到候选压缩阶段。
