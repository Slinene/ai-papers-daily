---
title: System One models Are Not Better Rerankers
title_zh: System One 模型并非更好的重排序器
authors:
- Michael Dinzinger
- Kanishka Ghosh Dastidar
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria (IT:U)
arxiv_id: '2610.32318'
url: https://arxiv.org/abs/2610.32318
pdf_url: https://arxiv.org/pdf/2610.32318
published: '2026-10-23'
collected: '2026-10-26'
category: RecSys
direction: LLM reranker 微调策略对比
tags:
- reranking
- decision models
- fine-tuning
- calibration
- IR
- LLM
one_liner: 在 0.6B–27B 六个 Qwen 骨干上，决策微调从未超过重排微调，9B 以下重排微调领先 5–29 nDCG@10
practical_value: '- 实际搜索/推荐重排中，若目标是 nDCG，优先选择专门 reranker 微调模型（如 Qwen3-Reranker），不要拿
  System One/决策模型按“是/否”概率直接排序；0.6B–9B 差距为 5–29 nDCG@10，27B 才打平。

  - 9B 以下 decision fine-tuning 相比 untuned zero-shot 没有排序增益，如果已有 untuned LLM，可先做零样本问法
  baseline，不必额外引入决策微调。

  - 决策模型的校准优势对问题措辞敏感，换一种问法可能消失；在线上系统评估校准或做阈值策略时，必须用实际 prompt 验证，不能直接沿用论文结论。

  - 若关心固定阈值下保留优质结果，reranker fine-tune 的概率比 decision model 概率更可靠；做准入/截断时应基于 reranker
  fine-tune 输出。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：System One（决策）模型以校准概率回答输入问题，发布后很快被用作 reranker，但缺乏在同一骨干上与专门重排微调的对比。

方法：在 0.6B 到 27B 的六个 Qwen 骨干上，对 TREC DL 2019–2023 和五个 BEIR 集合，比较三类模型在 BM25 top-100 候选上的重排效果：untuned model 零样本提问、decision fine-tunes、reranker fine-tunes（含 Qwen3-Reranker、Prism 及自训两个）。指标为 nDCG@10 和校准。

关键结果：从 0.6B 到 9B，reranker fine-tuning 在每个骨干上领先 5–29 nDCG@10，包括零样本集合；到 27B 两者打平。9B 以下 decision fine-tuning 相比直接询问 untuned model 没有任何排序增益。校准方面，决策模型在“passage 是否回答 query”的问法下，从 4B 起比公开 reranker fine-tunes 更校准；但换一个稍有不同的问法后，优势消失。此外，校准不能弥补排序差：9B 以下 reranker fine-tune 在固定阈值下能保留更好的 passage。结论：需要 reranker 就应 fine-tune reranker，而非依赖决策微调。
