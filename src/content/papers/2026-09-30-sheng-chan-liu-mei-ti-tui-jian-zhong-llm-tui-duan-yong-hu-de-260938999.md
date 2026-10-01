---
title: When LLM-Inferred User Context Adds Value in Production Streaming Recommendation
title_zh: 生产流媒体推荐中 LLM 推断用户上下文的增益条件
authors:
- Milad Sabouri
- Neeraj Sharma
- Sardar Hamidian
- Shaghayegh Agah
affiliations:
- DePaul University
- Comcast Technology AI
arxiv_id: '2609.38999'
url: https://arxiv.org/abs/2609.38999
pdf_url: https://arxiv.org/pdf/2609.38999
published: '2026-09-30'
collected: '2026-10-01'
category: RecSys
direction: LLM 用户画像 · 上下文自适应推荐
tags:
- LLM user profiling
- context-aware recommendation
- semantic representation
- popularity bias
- streaming recommendation
- consumption regime
one_liner: LLM 生成的语义用户画像只在探索型用户上优于聚合画像，且会显著放大热门偏差
practical_value: '- **按消费模式分层选画像策略**：线上可用训练期特征（历史长度、历史内容多样性）预估用户是习惯型还是探索型，对探索型才启用
  LLM 画像，习惯型默认 centroid。论文给出 history size r=-0.30、历史 embedding 多样性 r=+0.11 两个弱但显著的相关特征，可直接作为
  serving 端策略信号。

  - **默认 aggregate 更稳，LLM 画像需配 fallback**：在约 82% 的习惯型用户上，LLM 画像 Recall@10 比 centroid
  低 21-31 个百分点；若拿不准用户 regime，保守选择 aggregate embedding，避免大范围掉点。

  - **警惕 LLM 画像的 popularity attractor**：LLM 生成式画像把推荐集中到更小、更热门目录，Coverage 下降约 80%，Novelty
  下降 18-22%。电商/广告场景若重视长尾曝光，需要对 LLM profile 做 debias、温度/多样性控制，或只在探索型用户上启用，否则会系统性压制长尾商品。

  - **时间 split + attention 对 LLM 画像才有明显作用**：TemporalNarrative 在习惯型用户上比单段 Narrative
  回升约 9 个点 Recall@10，但仍追不上 centroid；对 aggregate 几乎无影响。因此若用 LLM 画像，短/长期 split 值得做；若用
  embedding centroid，不必增加时间切分复杂度。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
传统 context-awareness 依赖预定义变量，可覆盖的因素有限。LLM 能把非结构化行为历史概括成自然语言摘要，编码后替代聚合用户画像，但 LLM 画像相比聚合 embedding 究竟在什么条件下更优，此前只在 domain 粒度讨论过，缺少生产环境、全量 catalog、用户粒度的证据。

### 方法关键点
- 2×2 设计：representation type（aggregate vs LLM-generated）× contextual scope（holistic vs short/long attention-fused），得到 Centroid(C)、TemporalCentroid(TC)、Narrative(N)、TemporalNarrative(TN) 四种策略。
- 固定 SBERT item encoder、两层 ReLU MLP 打分头、训练协议和负采样，唯一变量是用户 profile vector，干净隔离画像设计。
- 用户按 test 中 item 是否出现在训练历史划分为 Explorer（约 18%）和 Non-Explorer（约 82%）两种消费 regime。
- 生产流媒体平台随机 10,000 用户，过滤后 catalog 约 2.4×10⁵ items，80/10/10 时序切分；在完整 catalog 上 ranking。
- 指标：Recall、NDCG、HitRate @10/100，加 Diversity、Coverage、Novelty 三个 beyond-accuracy 指标。

### 关键实验
- 全量用户上，LLM 画像显著弱于 centroid：Narrative Recall@10 -30.7%，TemporalNarrative -21.6%；Non-Explorer 上同样大幅落后。
- Explorer 上排序反转：Narrative Recall@10 +18.7%，TemporalNarrative +14.3%，而 TemporalCentroid -7.4%。
- LLM 画像呈现 popularity attractor：Diversity 约 +4%，Coverage 约 -80%，Novelty -18~22%，且所有 regime 一致。
- Temporal split 对 aggregate profile 基本无效，对 LLM profile 有方向性影响：在习惯型用户上 TemporalNarrative 比 Narrative 回升约 9 点 Recall@10，但仍不追平 centroid；在探索型用户 top-K 上 Narrative 反而更优。
- 训练期特征与 Explorer 标签相关：history size r=-0.30，历史内容多样性 r=+0.11，说明 regime 可被部分预判。

### 最值得记住的一句话
LLM 语义画像的增益不是普适的，而是高度依赖消费 regime：习惯型用户用 aggregate centroid 更稳，探索型用户才值得换 LLM 画像，且必须处理 LLM 画像带来的 popularity bias。
