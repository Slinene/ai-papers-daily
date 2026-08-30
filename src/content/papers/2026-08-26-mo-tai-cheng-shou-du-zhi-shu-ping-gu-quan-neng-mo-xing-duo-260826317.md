---
title: 'Modality Maturity Index: A benchmark for assessing multimodal capabilities
  of omni models'
title_zh: 模态成熟度指数：评估全能模型多模态能力的基准
authors:
- Rohit Patel
- Dieuwke Hupkes
- Sloan Strader
affiliations:
- Meta Superintelligence Labs
arxiv_id: '2608.26317'
url: https://arxiv.org/abs/2608.26317
pdf_url: https://arxiv.org/pdf/2608.26317
published: '2026-08-26'
collected: '2026-08-30'
category: Eval
direction: 多模态 LLM 评估基准
tags:
- multimodal
- evaluation
- benchmark
- LLM judge
- rubric
- omni models
one_liner: 提出 MMI 基准和模态存在性得分 MPS，发现前沿多模态模型输出模态存在率仅 15.6-34.9
practical_value: '- 在多模态 Agent 评估中引入「模态存在性得分」：先测量模型是否生成所需输出模态（图片/表格/音频等），再评估内容质量，可在工程链路早期暴露模态缺失问题，避免在不存在的内容上浪费人工评分。

  - 对多模态生成任务，采用人工撰写每个输出模态的 rubric，再由 LLM judge 打分；论文显示与 rubric-blind 人类标注一致性约 70.8%，可作为电商导购/客服多模态输出评估的自动化基线，但需留意
  Scott''s π 仅 0.41，不能完全替代人工。

  - 设计评测集时要求 prompt 自包含、明确期望的输出模态组合，可用于构建电商场景下多模态商品推荐、广告创意生成、客服回复的 benchmark；尤其适合评估模型是否按指令返回「商品图+文字说明」等组合。

  - 当前前沿模型多模态输出模态存在性低，提示实际部署 RAG/Agent 系统时，不应依赖模型自主决定输出模态，而应在 prompt 或后处理中显式约束输出格式，例如强制返回图片、表格或语音。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有评估几乎只覆盖 text + 单模态的双模态理解，无法检验模型作为「全能系统」在多模态输入输出组合上的能力。

**方法**：MMI 包含 893 道题，覆盖文本、图像、音频、视频、文档五种模态，输入与输出最多三模态组合。每道题自包含，并附有人类撰写的每个输出模态 rubric。MMI Value 取每 prompt 各模态得分平均。由于低分可能是模态缺失或内容错误，引入 Modality Presence Score (MPS)，计算预期输出模态的 per-prompt F1。

**结果**：五个前沿多模态模型中，MPS 仅 15.6（Claude Opus 4.6）到 34.9（GPT-5.4），大量预期输出模态压根没有生成。在给模型提供图像/音频/视频生成工具后，LLM judge 按 rubric 打分与 rubric-blind 人类标注一致性为 70.8%（Scott's π 0.41），图像 66.5%，视频 74.4%。结论：当前模型距离 omni 多模态输出成熟度仍很远。
