---
title: 'Computational Humor with Multimodal LLMs: Methods, Datasets, Evaluation, and
  Challenges'
title_zh: 多模态大语言模型的计算幽默：方法、数据集、评估与挑战
authors:
- Tuo Liang
- Zhe Hu
- Disheng Liu
- Jing Li
- Yu Yin
affiliations:
- Case Western Reserve University
- The Hong Kong Polytechnic University
arxiv_id: '2607.19011'
url: https://arxiv.org/abs/2607.19011
pdf_url: https://arxiv.org/pdf/2607.19011
published: '2026-07-20'
collected: '2026-07-25'
category: Multimodal
direction: 多模态LLM与幽默计算
tags:
- Multimodal Humor
- MLLM
- Benchmark
- Humor Generation
- Reasoning
- Survey
one_liner: 全面综述多模态LLM在视觉幽默理解与生成上的能力层级、基准与建模范式，揭示评估捷径等核心挑战
practical_value: '- 电商广告创意中可借鉴多模态幽默识别能力，用于预筛选或评估营销素材是否包含不当或低效的幽默元素，降低品牌风险

  - 用户生成内容（UGC）审核时可结合证据推理模块，提升对梗图、讽刺内容的理解准确率，减少误判

  - 推送消息文案优化中可尝试可控幽默生成，但需注意安全性与文化适配，可先构建内部 benchmark 测试

  - 构建幽默相关的评测集时需避免捷径特征（如文字重叠），确保模型学到真正的图文推理而非表面模式'
score: 6
source: huggingface-daily
depth: abstract
---

动机：视觉幽默（梗图、漫画、卡通）的理解需要结合非字面机制、文化背景和交际意图，传统多模态模型对此表现不佳。本文从能力视角出发，系统梳理了多模态幽默理解与生成的最新进展。

方法关键点：以能力层级（recognition, interpretation and reasoning, generation）为框架，总结了基准设计、评估协议和建模范式。文献轨迹显示，领域正从任务特定的多模态融合模型转向基于多模态对齐、证据驱动推理和可控生成的 MLLM 方法。重点关注了大规模多模态模型 (如 GPT-4V) 在幽默任务中的表现与局限性。

关键结果与挑战：尽管已有专门评测基准（如 MEMES、MAMI），但多数存在捷径主导的现象，模型常通过文本线索或表面特征作弊，而非真正推理。文化多样性、叙事连贯性和证据基础薄弱是主要瓶颈。此外，安全与版权问题在幽默生成中尤为突出。
