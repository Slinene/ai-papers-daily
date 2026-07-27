---
title: Why Large Language Models and Humans Converge and Diverge in Evaluating Creativity
title_zh: 为何大语言模型与人类在创造力评价上既趋同又分歧
authors:
- Pengzhao Lyu
- Yeun Joon Kim
- Hanlin Xiao
- Yingyue Luna Luan
affiliations:
- University of Cambridge
- University of Manchester
- University of Queensland
arxiv_id: '2607.22218'
url: https://arxiv.org/abs/2607.22218
pdf_url: https://arxiv.org/pdf/2607.22218
published: '2026-07-24'
collected: '2026-07-27'
category: Eval
direction: LLM 评估标准与人类对齐研究
tags:
- LLM evaluation
- creativity
- human alignment
- novelty
- contextual insensitivity
- model-specific standards
one_liner: 揭示LLM创造力评估依赖更窄的新颖性标准且忽视上下文信息，模型选择显著影响对创意的识别
practical_value: '- 若用 LLM 评估广告文案或推荐理由的创意，须警惕其对市场趋势、品牌声誉等上下文信息不敏感，建议结合人工或上下文特征补充判断。

  - 选择 LLM 评估器时需考察其评估标准的广度：标准越宽泛的模型越能区分人类眼中的高/低创意，可预先在试点任务上校准。

  - 对于侧重新颖性的场景（如生成吸引点击的推荐语摘要），LLM 评估与人类一致性较高，可直接用作粗筛；而涉及语境契合度的任务则不宜单独依赖 LLM。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 被越来越多地用作创造力评估工具，但与人类评分的一致性证据混杂，缺乏对何时及为何对齐的深入理解。

**方法关键点**：通过三项研究、六种主流 LLM，系统识别 LLM 评估创造力的内在标准及其影响。研究 1 提炼人类与 LLM 的评估标准维度；研究 2 收集 1103 个真实想法，对比人机评分的相关性及模型标准广度对区分度的影响；研究 3 操纵上下文信息（1195 个样本）检验其对两类评估者的影响差异。

**关键结果**：
- LLM 整体依赖更窄的标准子集，与人类在新颖性（novelty）维度高度对齐，但在捕捉社会、市场、声誉等上下文（contextual）维度上显著偏离。
- 每个 LLM 表现出独特的评估标准轮廓，广度差异明显；标准更广的模型在区分人类高/低创意上表现更好（中等相关）。
- 注入上下文信息会显著改变人类评分，但 LLM 评分几乎不变，证明其对语境不敏感。
- 结论：对齐程度取决于任务所需证据类型——强调新颖性时 LLM 可近似人类，需情境判断时则不可靠；选择不同的 LLM 评估器会认定不同的‘创意’，因而该决策至关重要。
