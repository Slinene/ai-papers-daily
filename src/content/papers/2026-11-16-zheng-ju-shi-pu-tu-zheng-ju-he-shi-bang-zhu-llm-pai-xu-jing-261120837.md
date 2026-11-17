---
title: 'Evidence Diet: When Graph Evidence Helps LLMs Rank Competing Candidates'
title_zh: 证据食谱：图证据何时帮助 LLM 排序竞争候选
authors:
- Yuchong Hu
- Zhao Zhang
- Ziyao Zhao
- Haoyu Wang
- Jing Xiao
affiliations:
- University of Science and Technology of China
- Ping An Technology (Shenzhen) Co., Ltd.
arxiv_id: '2611.20837'
url: https://arxiv.org/abs/2611.20837
pdf_url: https://arxiv.org/pdf/2611.20837
published: '2026-11-16'
collected: '2026-11-17'
category: RecSys
direction: LLM 图证据协同排序 · evidence diet
tags:
- LLM recommendation
- graph evidence
- collaborative filtering
- ranking
- evidence attribution
- LoRA
one_liner: 通过控制支持度与计数多集，揭示 LLM ranker 需要正确归因的图证据，而非原始路径
practical_value: '- 证据编译优于原始路径：把协同证据编译成每个候选的 (support b, distinct users c, distinct
  paths p) 统计，比打印原始两跳路径更省 token 且 NDCG@5 更高（Books +0.94, MovieTV +0.78）；电商/广告 rerank
  可离线算好，注入 prompt 或数值特征。

  - 证据归因必须精确：交换用户级证据导致 H@1 下降 2.17 点，而语义/流行度匹配替换几乎无影响；在推荐 Agent 生成解释或 RAG 检索证据时，务必保证证据与候选一一对应，避免串味。

  - 支持计数数值注入优于文本：当 target 和 rival 都有支持时，数值 counts 相比文本 Z 的 NDCG@5 提升 Books +5.38 /
  MovieTV +3.88；可将支持数、distinct users、paths 作为额外 logit 加成（αb+γlog(1+c)+δlog(1+p)）融合，工程简单。

  - 零支持查询是互补信号主战场：历史 LLM 分数与图特征融合在无支持查询上增益最大（Books zero-support H@1 +4.45），可选择性只对零支持查询调用
  LLM，节省成本且几乎不掉点。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM reranker 常结合用户历史与协同证据，但哪些证据真正有用、多个候选共享图支持时如何排序仍不清楚。该工作通过控制支持度和计数多集，系统诊断 LLM 如何消费图证据。

**方法关键点**
- 数据集：Amazon Books 和 MovieTV（InstructRec）。Suite I 用 Qwen3 0.6B/1.7B/4B + LoRA 在 1000 用户、13 种输入配置训练；Suite II 用固定 Qwen3-4B 对 10 候选打 logits，对比 prompt 变体：N（仅历史）、R（原始两跳路径）、Z（编译每候选统计 b/c/p）、RZ、Z_mis（错误重分配）、Bonus（N+3.125b）。
- 控制变量：在保持支持度和计数 multiset 不变下交换支持/计数，分离“识别有支持候选”与“在候选间排序”。
- 构造度匹配 rival 支持、BM25 负样本，并在 274 名新 Books 用户上做冻结评估。

**关键结果**
- 源分解：用户摘要最好 H@1 45.0，混合所有信号最差 31.6；固定 checkpoint 加无关文本 H@1 从 44.77 降到 38.70，但 99.9% 排名仍有效。
- 证据绑定：长度匹配跨用户交换降低 H@1 2.17 点，语义/流行度/双匹配替换变化 <0.43 点；目标提示替换 oracle +5.77。
- 主对比：uniform pool 下 Z vs N 的 NDCG@5：Books 69.12 vs 66.52，MovieTV 70.60 vs 66.65；Z vs R +0.94/+0.78；Z_mis 降 4.38/5.95。
- 度匹配：Z 比 N 提升 NDCG@5 2.28（Books）/ 2.54（MovieTV）。
- 支持计数归因：正确分配比错误分配提升 supported-pair accuracy +6.07 pp（新 Books 用户，95% CI [4.18,8.00]）；数值 counts 优于文本，supported target+rival NDCG@5 +5.38/+3.88。
- 融合：LLM 历史分数与图特征 LR/HGB 融合提升 H@1/NDCG@5，零支持查询贡献大部分增益。

**最值得记住的一句话**
当多个候选共享图支持时，正确绑定证据到候选并保留支持计数，比提供更多原始路径更重要。
