---
title: Which Language Should a Skeleton Speak? Language Choices in Multilingual Reasoning
title_zh: 骨架应该说什么语言？多语言推理中的语言选择
authors:
- HyeonSeok Lim
- SeungWoo Song
- Inho Won
- Hoyun Song
- Jihyo Kim
- KyungTae Lim
affiliations:
- ETRI
- KAIST
- Dankook University
arxiv_id: '2610.09607'
url: https://arxiv.org/abs/2610.09607
pdf_url: https://arxiv.org/pdf/2610.09607
published: '2026-10-06'
collected: '2026-10-13'
category: Reasoning
direction: LLM 多语言推理 · 提示骨架语言选择
tags:
- Skeleton-based Prompting
- Multilingual Reasoning
- LLM
- Training-free
- Math Reasoning
- Language Selection
one_liner: 系统研究多语言数学推理中骨架提示语言选择，发现英语骨架平均微小正向但非普遍最优，效应依赖语境
practical_value: '- 多语言业务中若用结构化推理骨架（如多步 agent 的思考模板），默认英语骨架可作为 baseline，但必须按语言分桶评估；平均收益可能由低资源语言/小模型驱动，不能直接全量推广。

  - 将语言选择纳入 prompt 实验矩阵：不同骨架语言的效果存在方向一致、评估/基准依赖、不对称负效应，因此需要 multi-rollout + translation
  ablation 隔离语言变量，避免单次 greedy 结果误判。

  - 对低资源语言，如果训练额外的多语言推理模型成本高，可优先用英语骨架做训练免推理引导；但要警惕对某些语言产生负效应，发布前做显著性校正。

  - 工程上可复用其开源 LASEF 框架，构建多语言骨架版本管理、评估流水线，尤其适合跨境电商搜索/推荐场景的多语言 query 理解与 agent 推理。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：骨架推理提示（skeleton-based reasoning prompting）通过显式给出推理流程引导 LLM 解题，具有训练免优势，适合低资源语言；但此前研究默认英语中心，多语言场景中骨架语言如何选择未系统探索。

**方法**：LASEF 框架在多个数学基准、模型规模、语言维度上开展实验，组合 greedy decoding、multi-rollout evaluation、translation ablation、cross-benchmark validation，比较不同骨架语言效果，并进行显著性校正。

**结果**：英语骨架平均有小正向趋势，小模型和低资源语言中更明显；校正后少数语言级增益显著，英语并非普遍最优。发现三种骨架语言效应模式：方向一致、依赖评估/基准、不对称负效应；这些不能被生成质量单独解释，提示骨架语言是与上下文相关的设计变量。
