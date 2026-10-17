---
title: 'LeanPRM: Lean-Grounded Process Supervision for Natural Language Proof Verification'
title_zh: LeanPRM：基于 Lean 的自然语言证明过程监督
authors:
- Rodney Lafuente-Mercado
- Salman Rahman
- Jingyan Shen
- James Shiffer
- Saadia Gabriel
- Pavel Izmailov
affiliations:
- University of Texas at Austin
- University of California, Los Angeles
- New York University
arxiv_id: '2610.17697'
url: https://arxiv.org/abs/2610.17697
pdf_url: https://arxiv.org/pdf/2610.17697
published: '2026-10-12'
collected: '2026-10-17'
category: Training
direction: 过程监督 · Lean 自动标注
tags:
- Process Supervision
- Lean
- Proof Verification
- Synthetic Data
- Reward Model
one_liner: 利用 Lean 形式化证明自动生成自然语言证明的逐步正确性标签，训练过程监督验证器，步级准确率从 48.2 提升至 74.7
practical_value: '- 对 Agent/多步决策轨迹，可借鉴「可执行环境自动打标签」：用沙盒、规则引擎或领域知识库对中间步骤做形式化校验，替代人工标注，低成本构建过程监督数据。

  - 「分离形式错误与语义错误」的过滤模型思路值得迁移：先自动生成大量轨迹标签，再训练一个二分类器剔除仅因语法/格式失败但推理正确的负样本，避免污染奖励模型。

  - 训练过程奖励模型时，可以混合少量人工标注与大量自动标注；本工作证明在没有人类标注的情况下，自动标签也能显著优于 PRM800K 人工标注，适合快速迭代线上推理链路。

  - 对于电商推荐理由生成、搜索 query 改写等有可执行校验（如转化、点击、库存）的场景，可尝试用业务指标为中间步骤提供弱监督，再微调 LLM 做步骤级打分。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：AI 生成的数学证明越来越长，逐步验证成为瓶颈；训练验证器需要每一步的正确性标签，但人类标注昂贵，最终答案又无法用于开放式证明，而形式化 Lean 证明需要专家投入。

方法关键点：
- 让一个模型同时写自然语言证明和配对的形式化证明（无 Lean 反馈）；
- Lean 对形式化证明逐步验证，自动为对应自然语言步骤产生标签；
- 训练第二个模型剔除仅因形式语法失败、但数学步骤正确的负样本，保留真实数学错误标签；
- 构建 LeanPRM 数据集：10,634 个证明、152K 标注步骤，全程无人类标注。

关键结果：
- 在 LeanPRM-Bench 200 个证明上，Qwen3-4B 验证器的 exact step-label accuracy 从 48.2 提升到 74.7，而 PRM800K 训练的同基座模型仅 60.3；
- 在 IMO 级别问题 best-of-N 选择中表现更好；
- 在四个外部验证基准中三项超过 PRM800K 训练模型；
- 从 0.6B 到 8B 参数，训练于 LeanPRM 均改善验证器性能。
