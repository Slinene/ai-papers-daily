---
title: Measuring and Mitigating Identity-Cue Preference Drift in LLM-based Recommender
  Systems
title_zh: 测量与缓解 LLM 推荐系统中的身份线索偏好漂移
authors:
- Zhuoxiong Gan
- Qiang Dong
affiliations:
- Institute of Intelligent Computing, University of Electronic Science and Technology
  of China
arxiv_id: '2609.34229'
url: https://arxiv.org/abs/2609.34229
pdf_url: https://arxiv.org/pdf/2609.34229
published: '2026-09-28'
collected: '2026-09-29'
category: RecSys
direction: LLM RecSys 身份线索漂移测量与缓解
tags:
- LLM4Rec
- Preference Drift
- Prompt Sensitivity
- Reranking
- Bias Mitigation
- Identity Cue
one_liner: 提出 PromptShift 训练-free 框架，量化并缓解 LLM 推荐中单条身份线索导致的群体偏好漂移，SliceShift 平均降低
  62.42%
practical_value: '- 在 LLM 排序/推荐中，prompt 注入用户性别、年龄等 profile 属性不是中性输入：即使行为历史不变，也会系统性把结果拉向该群体热门物品。工程上应把身份字段视为可干预变量，并对线上
  prompt 做受控对照测试（paraphrase controls）以区分普通措辞敏感性。

  - 可复用其 slice-popularity table：用近期正反馈构建 identity slice × item 频率表，小样本 shrink 向全局，再用
  Δφ=φ(item,g)-φ(item,⋆) 识别“群体过流行”物品，作为无参数偏差审计信号。

  - 后处理 reranking 适合合规/轻量去偏：对 LLM 生成候选池 (N>K) 用 score = α_u·rank_score + (1-α_u)·(1-φ(item,g))
  重排，α_u 由用户历史 mainstreamness 动态调节；保留 top K'' 不干预，能提升 HitRate/MRR 且几乎无额外模型调用。

  - 注意 trade-off：该方法可能降低 NDCG，因为会扰动多命中排序；如果业务更重 NDCG 需压 α 下限或只在前 K 外做调整。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM 推荐越来越依赖自然语言 prompt，输入通常包含用户 profile 里的 demographic 属性。已有研究发现 LLM 对 prompt 措辞高度敏感，但尚未隔离“单条事实性身份线索”是否会改变推荐列表，以及方向是否朝该群体消费模式靠拢。若成立，则身份字段不是中性输入，需要单独测量与缓解。

## 方法关键点
- **配对设计**：同一行为历史生成 history-only、identity-cued、三个 identity-free paraphrase 控制。所有解码参数固定，identity-cued 只多一句事实性身份陈述。
- **Slice 表**：用正反馈构建 identity-slice-by-item 表，小 slice 向 all-user 收缩；φ(i,g) 为 slice-conditioned popularity，Δφ(i,g)=φ(i,g)-φ(i,⋆) 表示 item 在该群体的超额流行度。
- **测量指标**：Drift = 1 - RBO_p(history-only list, cued list)，量化列表变化幅度；SliceShift = mean Δφ(cued list) - mean Δφ(history-only list)，量化方向是否朝 cued slice 偏移。
- **措辞基线**：用 paraphrase Drift 作为措辞敏感性基线，Cue Drift 减 paraphrase Drift 得到 Δd，从而隔离真实 cue 效应。
- **缓解**：无需训练的后处理重排。候选池 N=30，输出 K=20，保留前 K'=5 不动；对每个用户计算 within-slice history mainstreamness \bar φ_u；动态权重 α_u 由 \bar φ_u 相对场景均值决定；score = α_u r_i + (1-α_u)(1-φ(i,g_u))，r_i 是原始 rank 的几何保留分。主流用户更信原始排名，非主流用户更多提升 slice 内低流行度物品。

## 关键实验
MovieLens 1M 与 Last.fm 1K，GPT-5.6 Terra、Gemini 3.1 Pro、Qwen3-8B，性别、年龄、性别×年龄三种 cue。六个 dataset-model 设定中：Cue Drift 均超过 paraphrase Drift，Δd 0.0270-0.0759；SliceShift 全为正 0.0550-0.0680。PromptShift 将 macro-mean SliceShift 从 0.0612 降到 0.0230（-62.42%），Difficulty@20 从 21.22 升到 25.96，HitRate@20 从 0.8423 升到 0.8845，MRR@20 从 0.4775 升到 0.5032，NDCG@20 从 0.4957 略降到 0.4866。消融显示：all-user popularity 固定权重反而使 SliceShift 升高、HitRate 下降；slice-conditioned 固定权重次优；自适应 PromptShift 最佳。

## 最值得记住的一句话
身份线索不是中性输入，单条事实性 demographic 句会系统性把 LLM 推荐拉向群体热门，但用 slice-conditioned inverse popularity + 用户 mainstreamness 的无训练重排能显著抑制该漂移。
