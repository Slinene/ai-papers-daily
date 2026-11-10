---
title: 'Beyond Ranking: Are Decision Models Calibrated Relevance Scorers?'
title_zh: 超越排序：决策模型是校准的相关性打分器吗？
authors:
- Shengyao Zhuang
- Xueguang Ma
- Matthias Petri
- Jimmy Lin
affiliations:
- Keenable
- University of Waterloo
arxiv_id: '2611.11480'
url: https://arxiv.org/abs/2611.11480
pdf_url: https://arxiv.org/pdf/2611.11480
published: '2026-11-08'
collected: '2026-11-10'
category: Eval
direction: LLM 相关性打分校准与评估
tags:
- calibration
- relevance scoring
- LLM
- decision models
- reranking
- Brier score
one_liner: 验证 Jev 等决策模型的直接相关性概率，发现原生概率过度自信，二参数校准后可跨数据集提升 Brier 分数并支持按 expected F1
  动态截断。
practical_value: '- 生产环境用 LLM 做相关性打分/重排时，不要直接采信模型给出的概率；可以用少量人工标注 pair（如 ~2k 条）拟合二参数校准（类似
  Platt scaling / temperature scaling），跨数据集迁移后 Brier 分数显著下降，阈值决策更可靠。

  - 在电商搜索/推荐中，需要把相关性分数用于截断或准入门控（决定曝光哪些商品/广告）时，校准后的概率支持按 expected F1 自动选择每个 query 的
  cut-off，避免固定 top-k，能适应头尾部 query 差异，减少人工阈值调参。

  - 决策模型的 typed score primitive 直接输出分等级概率，比从 token likelihood 派生分数更自然，可作为 reranker
  接入检索链；开源 27B pplx-decider 排序能力已超过 cross-encoder 和 FLAN-UL2，值得小规模 A/B 验证。

  - 评估这类模型建议同时看 Brier score 和 relevant/non-relevant 概率分离度，而不只看 ranking metric；如果只做排序，原生分数够用，但要做阈值策略必须先校准。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM 相关性打分通常只看 rank 或 label，忽略概率校准；决策模型 Jev 声称直接输出已校准的分级相关概率，但缺少对照人工标注的验证。

方法：复现 Beyond Yes and No 的 FLAN-UL2 zero-shot pointwise 设置在 8 个 BEIR 集合上的表现；在同一协议下评估 Jev 和两个开源决策模型；用 DL19/DL21 人工相关标签对比原生概率，并拟合二参数校准。

关键结果：Jev 与 27B pplx-decider 平均排序质量超过 FLAN-UL2 和三个 cross-encoder；Jev 原生概率过度自信——DL21 中评分 >0.9 的 pair 只有 66% 真正相关；用 DL19 的 2,257 对拟合二参数校准可迁移到 DL21，校准后 Brier 分数更低，主要因为其能更好分离 relevant/non-relevant；用校准概率按 expected F1 选择每个 query 的截断，无需单独参数，超过固定 top-10，并持平在 DL19 上调好的阈值。
