---
title: 'Glance: The Generator Is Its Own Reranker'
title_zh: Glance：生成器即重排序器
authors:
- Adilet Metinov
- Chingiz Arziev
affiliations:
- Airun Intelligence Labs
arxiv_id: '2610.40454'
url: https://arxiv.org/abs/2610.40454
pdf_url: https://arxiv.org/pdf/2610.40454
published: '2026-10-28'
collected: '2026-10-30'
category: RAG
direction: 生成器内置重排序，共享 prefill
tags:
- RAG
- Reranking
- LLM
- Adapter
- Shared Prefill
one_liner: 提出 Glance，给生成器加轻量决策适配器和指针头，共享一次 prefill 对候选段落打分，免去独立重排模型
practical_value: '- 若业务中已部署 LLM 作为生成式排序或回答模型，可借鉴 Glance 思路：在同一个 LLM 上挂轻量决策头同时完成相关性打分与生成，避免单独服务
  cross-encoder，节省显存和部署成本。

  - “共享 prefill + 轻量 probe”技巧：对候选商品/内容批量编码一次，从缓存中分支不同 probe 产生分数，比逐对 prefill 更高效，适合候选量较大的重排场景。

  - 激活适配器变体允许生成继续使用原始缓存，可将重排与生成解耦为不同 adapter，按需激活，主干权重不变，便于多技能扩展。

  - 注意：论文仅在通用 RAG 数据集上验证，迁移到电商/推荐需自行评估，但“单骨干多技能”的架构思想值得复用。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：RAG 通常分开部署 reranker 和 generator，导致模型重复驻留、候选 passage 被反复处理。生成器本来就要读 passage，能否让它自己完成打分？

**方法关键点**：Glance 给生成器加一个轻量决策适配器和 256 维指针头。先对候选 passages 做一次共享 prefill，然后从缓存中分支短 relevance probes，每个 passage 产生一个分数，无需单独 prefill 每个 query-passage 对。同一个 9B 骨干模型支持生成、通用决策和重排，每个决策技能仅增加约 0.1 GiB 内存。激活适配器变体让生成阶段直接复用原始 passage cache。

**关键结果**：在 MS MARCO 上微调 39 分钟后，Glance 在 SciFact 上 nDCG@10 达到 0.741（bge-reranker-v2-m3 为 0.721），NFCorpus 上 0.345（对比 0.326）。在 300 个 HotpotQA 问题上，Glance 选出的上下文使答案 F1 比 cross-encoder 选出的上下文高 0.045（paired bootstrap 95% CI [0.014, 0.076]）。缩放实验中，共享一次 prefill 可评分多达 200 个候选（43k tokens），重排质量仍超过 cross-encoder 0.058 nDCG@10。
