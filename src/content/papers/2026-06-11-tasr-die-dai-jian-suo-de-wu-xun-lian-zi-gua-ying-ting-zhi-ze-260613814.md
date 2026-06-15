---
title: 'TASR: Training-Free Adaptive Stopping for Iterative Retrieval'
title_zh: TASR：迭代检索的无训练自适应停止规则
authors:
- Adrian Kieback
- Uyiosa Philip Amadasun
- Aman Chadha
- Aaron Elkins
affiliations:
- San Diego State University
- James Silberrad Brown Center for AI
- Stanford University
- Google DeepMind
arxiv_id: '2606.13814'
url: https://arxiv.org/abs/2606.13814
pdf_url: https://arxiv.org/pdf/2606.13814
published: '2026-06-11'
collected: '2026-06-15'
category: RAG
direction: 迭代RAG · 无训练停止策略
tags:
- RAG
- adaptive stopping
- training-free
- calibration
- iterative retrieval
- multi-hop QA
one_liner: 提出一个固定的停止谓词，通过重复答案和校准后的logit margin阈值，无需训练就能减少RAG中不必要的检索轮次
practical_value: '- 可直接在现有RAG管线中插入一行代码作为停止条件：重复前轮归一化答案且 isotonically calibrated logit
  margin > 0.25。对电商问答、多跳商品查询等场景，能在不损失太多精度的情况下大幅降低检索调用次数。

  - 发现RLHF调优模型的verbalized置信度极度塌缩（96.5%输出最高分），而logit margin具有44倍的类条件分离度，这提示在依赖LLM自信度进行决策（如Agent中断、推荐解释可信度）时，应避免使用提示词直接索取的置信度分数，转向logit-level信号。

  - 通过固定阈值实现跨模型、检索器、语料库的零次迁移，无需针对每个新模型或任务重新训练停止策略，降低了维护成本。对于多智体框架中调用外部工具的轮次控制，可以借鉴这种简单启发式规则作为默认基线。

  - 论文从381个候选规则中筛选出Pareto最优规则，这种穷举评估再选择的范式，可以用来为其他agent决策点（如何时触发重排序、何时退出对话）设计低成本、可解释的启发式策略。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：迭代检索增强生成（RAG）Agent常在答案已收敛后继续检索，浪费算力且不改变输出。现有停止策略需训练专用模型，不具备跨任务迁移性。

方法：提出TASR，一行代码的停止谓词——当模型重复上一轮归一化后的答案，且等保校准（isotonic calibration）后的logit margin超过0.25时终止检索。无需学习任何分类器或价值头，阈值固定，适用于所有24种（模型×检索器×语料库）配置。

结果：在3模型×2数据集的干扰测试中，TASR保留了固定k=5的94.8%宏F1，仅使用62.6%的调用量，比固定k=3高出3.42 F1。在9个BM25开放域和9个稠密检索扩展中，均无显著退化，且通用阈值跨配置直接有效。信号分析揭示：RLHF调优模型的verbalized置信度（1-5分）几乎坍缩到5（96.5%），熵仅0.182 nats；而logit margin的类条件分离度是前者的44倍，为规则设计提供了可测量的病理依据。TASR成为一个可审计、无训练的Pareto基线，供学习的停止控制器对比。
