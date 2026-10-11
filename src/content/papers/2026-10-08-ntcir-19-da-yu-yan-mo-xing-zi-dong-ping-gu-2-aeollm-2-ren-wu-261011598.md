---
title: Overview of the NTCIR-19 Automatic Evaluation of LLMs 2 (AEOLLM-2) Task
title_zh: NTCIR-19 大语言模型自动评估 2（AEOLLM-2）任务综述
authors:
- Junjie Chen
- Yuxi Dong
- Haitao Li
- Yiqun Liu
- Qingyao Ai
affiliations:
- Tsinghua University
- Quan Cheng Laboratory
- University of Science and Technology Beijing
arxiv_id: '2610.11598'
url: https://arxiv.org/abs/2610.11598
pdf_url: https://arxiv.org/pdf/2610.11598
published: '2026-10-08'
collected: '2026-10-11'
category: Eval
direction: LLM 自动评测 · 长文本深度研究报告
tags:
- LLM evaluation
- long-form generation
- NTCIR-19
- deep research
- meta-evaluation
one_liner: 推出 Deep Research Evaluation 子任务，聚焦 LLM 生成深度研究报告的自动评估，收到 10 队 91 个提交
practical_value: '- 评估 LLM 生成的商品文案、推荐理由、广告创意等长文本时，先建立人类标注的质量基准，再开发自动评估器并关注与人类打分的一致性（如相关性、事实性、可读性）。

  - 长文本生成评估需要细分维度，不要只给整体分；可参考任务将 deep research 报告质量拆解为多个标注维度，便于定位模型问题。

  - 自动评估器本身要作为系统组件持续迭代：用 human-annotated ground truth 定期回归，关注自动化指标与人类评估的秩相关（Kendall/Spearman），而不是只盯绝对分数。

  - 任务中参赛方法常见 LLM-as-judge 或集成指标，可迁移到业务中做离线文案质量门禁，但需注意长文本事实性错误的检测仍是难点。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

动机：NTCIR-18 的 AEOLLM 已开始探索 LLM 自动评估，NTCIR-19 在此基础上进一步聚焦长文本生成场景。LLM 生成的深度研究报告篇幅长、信息密集，人工评估成本高且难以规模化，需要自动评估方法。

方法关键点：AEOLLM-2 推出 Deep Research Evaluation 子任务，参与者针对 LLM 生成的深度研究报告开发自动评估方法，以人类标注的质量标签作为 ground truth，用自动打分与人工打分的一致性衡量方法性能。任务提供数据集和评估指标，今年收到 10 个团队共 91 次提交。论文描述任务设置、数据构建、评价指标、参与者方法及最终结果。

关键结果：共有 10 支队伍提交 91 份运行，具体指标与排名以论文报告为准；该任务为长文本 LLM 评估建立了比较基准，系统汇总了当前自动评估方法的性能差异。
