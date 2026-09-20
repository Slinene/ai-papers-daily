---
title: 'DocAttriBench: Benchmarking Answer Grounding in Document Visual Question Answering'
title_zh: DocAttriBench：文档视觉问答的答案证据定位基准
authors:
- Luca De Grandis
- Silvia Cappelletti
- William Raccagni
- Marcella Cornia
- Lorenzo Baraldi
- Rita Cucchiara
affiliations:
- University of Modena and Reggio Emilia
- University of Pisa
arxiv_id: '2609.20574'
url: https://arxiv.org/abs/2609.20574
pdf_url: https://arxiv.org/pdf/2609.20574
published: '2026-09-17'
collected: '2026-09-20'
category: Eval
direction: 多模态文档VQA评估基准
tags:
- Document VQA
- Answer Grounding
- Benchmark
- Multimodal LLM
- Attribution
one_liner: 提出 DocAttriBench 基准与 MAPPET 自动归因方法，评估多模态 LLM 在文档 VQA 中的答案证据定位能力
practical_value: '- MAPPET 的 mask-perplexity 归因可迁移到电商商品详情页/广告素材问答：通过对输入区域做掩码扰动，用 perplexity
  上升幅度自动定位支撑答案的关键元素，低成本生产“答案-证据”对齐数据，减少人工框选成本。

  - 在客服问答、商品资质审核、广告文案合规等场景，不要只评测答案正确率：要求 MLLM 返回 supporting element 并计算 attribution
  accuracy，可暴露“答对但证据定位错”的可信度问题，适合作为 RLHF/DPO 奖励项或上线前评测门禁。

  - 若要生成推荐理由、商品卖点或搜索摘要，建议显式加入布局感知与证据约束，因为该基准显示大模型答案准确率高但 grounding 差；后处理可校验归因区域与生成内容一致，提升可解释性。

  - 可利用 DAB 开源的自动标注流程，对业务中已有文档 VQA 数据快速扩展 grounding 标签，支撑可验证推荐/问答模型的训练与回归测试。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：文档 VQA 的 answer grounding 长期缺少高质量标注，人工构建 grounded 数据集成本高，导致模型可验证性不足。

方法关键点：构建 DocAttriBench (DAB) 大规模基准，引入 MAPPET（Mask-based Perplexity-Derived Attribution）。MAPPET 结合文档布局与语言模型：对候选元素（文本块、表格、图片）做掩码，测量 perplexity 的上升幅度，将答案归因到使模型置信度下降最大的元素。将 MAPPET 应用到多个现有 Document VQA 数据集，自动获得 element-level grounding，最终 DAB 包含 237k 文档、296k 问答对。

关键结果：在 DAB 上评估具备 grounding 能力的多模态 LLM，同时考虑 answer accuracy、attribution accuracy 与整体答案质量。结果表明，更大的模型通常 answer accuracy 更高，但即使最强模型也经常无法准确定位支撑答案的视觉元素。DAB 为开发可验证、可信的文档 VQA 模型提供了可扩展的评测基准。
