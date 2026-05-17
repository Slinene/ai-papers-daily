---
title: Small, Private Language Models as Teammates for Educational Assessment Design
title_zh: 小语言模型作为队友：教育评估设计中的私密部署比较研究
authors:
- Chris Davis Jaldi
- Anmol Saini
- Shan Zhang
- Noah Schroeder
- Cogan Shimizu
- Eleni Ilkou
arxiv_id: '2605.15015'
url: https://arxiv.org/abs/2605.15015
pdf_url: https://arxiv.org/pdf/2605.15015
published: '2026-05-14'
collected: '2026-05-17'
category: Eval
direction: 教育评估生成任务中的SLM vs LLM对比评估
tags:
- SLM
- LLM
- Educational Assessment
- Bloom's Taxonomy
- Model-based Evaluation
- Human-in-the-Loop
one_liner: SLM在教育题目生成任务中性能接近LLM，但模型自评不可靠，须有人工闭环
practical_value: '- 若业务场景（如私域商品评价问题生成）需低成本、隐私敏感部署，SLM 是可行选择，性能接近大模型，可优先实验。

  - 为生成式推荐或 Agent 的指令设计建立多维质量指标时，可借鉴 Bloom 分类法，对生成内容层次化打分，避免单维度评价。

  - 模型自评（用 LLM 评价 LLM 输出）存在系统性偏差，必须加入人工校验环节；在人机协同工作流中，可先让 SLM 粗筛，专家抽检校准。

  - 在 Agent 工具链中，对小范围、高并发的结构化内容生成（如提示词模板、回复候选），用 SLM 可实现质量与成本的平衡。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：教育评估设计（如出题）中，大语言模型（LLM）展现潜力，但现有研究大多依赖主观或有限评价，且主要关注闭源模型，较少系统考察生成、评估与部署约束。小型语言模型（SLM）虽具备本地化、隐私友好优势，但在评估题目生成任务上的有效性缺乏探索。

**方法关键点**：该工作系统对比 LLM 与 SLM，在 Bloom 认知层级上生成题目，采用可复现、教学法对齐的指标评估质量；同时分析模型评判（model-based judging）与专家评定在可靠性和一致性上的差异。

**关键结果**：SLM 在关键教学法质量维度上取得有竞争力的表现，且支持本地隐私保护部署；但模型自动评估相对于专家评分存在系统性不一致与偏差。
