---
title: 'Embedding Surgery: Localized Updates for Adaptive Ranking Correction in Dense
  Retrieval'
title_zh: 嵌入手术：稠密检索中自适应排序纠正的局部化更新
authors:
- Maddalena Amendola
- Antonio Mallia
- Raffaele Perego
affiliations:
- IIT-CNR
- Seltz
- ISTI-CNR
arxiv_id: '2609.05110'
url: https://arxiv.org/abs/2609.05110
pdf_url: https://arxiv.org/pdf/2609.05110
published: '2026-09-04'
collected: '2026-09-07'
category: RecSys
direction: 稠密检索 · 排序纠正 · 向量索引更新
tags:
- Dense Retrieval
- Ranking Correction
- Relevance Feedback
- Convex Optimization
- ANN Index
one_liner: 提出嵌入手术，在查询时对文档嵌入做最小凸优化更新，以满足排序偏好约束，无需重训或重建索引
practical_value: '- 在推荐/广告向量召回中，针对 badcase、编辑干预（提权、打压、合规）无需重训或重建索引：对召回 top-k 的 item
  embedding 解一个小规模 QP，约束可来自人工规则、点击/转化信号或 LLM 评估；更新仅限参与 pair 的 item，保持全局空间不变。

  - 利用反事实点击偏好作为约束：第 i 位点击 > 第 i-1 位未点，立即触发局部更新；即使点击有噪声也稳定，近随机点击不导致显著退化，适合在线反馈闭环。

  - ANN 工程：小幅度 embedding 更新可直接原地覆盖 HNSW/IVF，无需改图边或重建索引；实验显示 185k 向量覆盖后 DL 指标无显著变化，IVF
  仅 0.38% 向量跨簇，可支撑实时修正层。

  - 与 query 侧自适应（如 CoRocchio）组合用；文档侧对噪声更鲁棒且能传播到语义相关 query，query 侧在可靠反馈下更强，组合在良好反馈下最高。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

静态文档嵌入与离线索引使稠密检索难以响应编辑规则、用户反馈和意图漂移；微调再重建代价过高，且无法做查询级纠错。embedding surgery 把排序纠正建模为一个凸二次规划：对 top-k 检索到的文档嵌入施加最小 L2 扰动，同时满足成对排序约束 ⟨q,d_r+Δd_r⟩≥⟨q,d_n+Δd_n⟩+ε。约束来自编辑标注、LLM reranker（BGE/Qwen）或反事实点击模型；从目标排序与当前排序的 Kendall Tau 距离构造相邻交换，保证约束无环、问题可行。优化仅修改参与 pair 的文档向量，不重新归一化，解用 CVXPY，单约束约 7.9×10⁻³ 秒，批量编辑约束约 3.6×10⁻³ 秒/约束。实验中验证对称更新优于 promotion/demotion；在 TREC DL 19/20/Hard、Robust 04、CAsT、MS MARCO 上，Contriever/TAS-B/E5/Snowflake 四个模型均稳定提升。编辑反馈下最大相对提升 +60.64% nDCG@10（TAS-B, DL-Hard）；Contriever 在 DL'19 从 0.674 到 0.845、DL'20 从 0.672 到 0.878、Robust'04 从 0.466 到 0.687。点击反馈在 perfect user 下接近编辑，noisy 下依旧稳定，near-random 不显著退化；LLM 反馈增益受 reranker 质量限制但在多数设置为正。大规模 56k MS MARCO 查询的原地更新使 judged Dev MRR 从 0.348 提升到 0.714/0.709（HNSW/IVF），DL 基准无显著变化；185,006 个 HNSW 向量原地覆盖而未改图边，IVF 仅 0.38% 向量改变聚类。与 CoRocchio 联动时，perfect/noisy 反馈下 nDCG@10 达 0.809/0.720，均优于单用；near-random 下 surgery 更鲁棒。最值得记住：局部最小扰动求解排序约束，把静态向量索引变成可交互、可反馈的排序修正层。
