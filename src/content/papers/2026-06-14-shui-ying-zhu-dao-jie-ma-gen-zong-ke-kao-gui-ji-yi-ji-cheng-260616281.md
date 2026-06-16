---
title: Who Should Lead Decoding Now? Tracking Reliable Trajectories for Ensembling
  Masked Diffusion Language Models
title_zh: 谁应主导解码？跟踪可靠轨迹以集成掩码扩散语言模型
authors:
- Heecheol Yun
- Joonhyung Park
- Joowon Kim
- Eunho Yang
affiliations:
- KAIST
- AITRICS
arxiv_id: '2606.16281'
url: https://arxiv.org/abs/2606.16281
pdf_url: https://arxiv.org/pdf/2606.16281
published: '2026-06-14'
collected: '2026-06-16'
category: LLM
direction: 掩码扩散语言模型集成与解码动态
tags:
- Masked Diffusion
- Ensembling
- Decoding Dynamics
- Knowledge Fusion
- Iterative Decoding
- Reasoning
one_liner: 提出TIE框架，通过跟踪解码轨迹置信度动态，实现MDLM的迭代知识融合，提升推理性能
practical_value: '- 多Agent协作推理可借鉴：跟踪各Agent中间解码状态的置信度，动态选择轨迹更可靠的Agent主导生成，提升复杂推理准确性，适用于搜索推荐中的多步推理场景。

  - 生成式推荐（如Semantic ID生成）可采用类似融合策略：集成多个生成模型，在每一步去噪或解码时评估中间状态质量，由当前最优模型接管，纠正其他模型的不可靠方向。

  - 搜索查询改写或广告文案生成中，可交替利用不同LLM的互补优势：当某个模型生成过程中出现低置信度区域，注入其他模型的中间状态以稳定生成轨迹。

  - 该方法强调在生成过程而非结果层面融合，为电商场景中多模型协同（如多路召回融合、多生成器投票）提供新思路：关注中间表示的置信度动态而非最终输出概率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：掩码扩散语言模型（MDLMs）多样性强但缺乏有效的集成手段。观察发现，成功生成中答案相关位置的置信度轨迹稳定，不可靠轨迹可通过注入其他模型中间状态纠正。

**方法**：提出TIE（Trajectory-based Iterative Ensembling），一种迭代式知识融合框架。在联合去噪过程中，TIE实时监控各模型在答案相关位置的置信度动态，判断哪一模型当前轨迹更可靠，然后将该模型的部分去噪序列（即中间状态）传递给其他模型作为起点。这种“接力”机制允许在解码不同阶段由最具优势的模型主导，充分发挥互补性。

**结果**：在多个推理任务上，TIE一致地优于单模型和常规集成基线，验证了轨迹跟踪与动态切换的有效性。分析表明，不同模型在去噪步中贡献度变化显著，TIE能自适应捕捉这些变化。
