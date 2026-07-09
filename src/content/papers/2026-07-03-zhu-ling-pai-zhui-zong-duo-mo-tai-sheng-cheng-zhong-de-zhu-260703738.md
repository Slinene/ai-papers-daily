---
title: Attending to Multimodal Generation One Token at a Time
title_zh: 逐令牌追踪多模态生成中的注意力动态
authors:
- Varun Gupta
- Vineet Gandhi
- Makarand Tapaswi
affiliations:
- CVIT, IIIT Hyderabad
arxiv_id: '2607.03738'
url: https://arxiv.org/abs/2607.03738
pdf_url: https://arxiv.org/pdf/2607.03738
published: '2026-07-03'
collected: '2026-07-09'
category: Multimodal
direction: 多模态LLM注意力机制的可解释性分析
tags:
- Multimodal LLM
- Attention Dynamics
- Interpretability
- Token-level Analysis
- Cross-modal Interaction
- Test-time Intervention
one_liner: 系统揭示多模态LLM生成过程中注意力随语义角色切换的逐令牌动态，并提出测试时干预提升多模态任务性能
practical_value: '- 在多模态推荐（如图文推荐理由生成）中，可借鉴注意力动态模式，在需要图像信息的生成阶段显式增强视觉注意力，提升描述准确性。

  - 测试时注意力干预方法简单有效，无需重新训练，可集成到现有多模态LLM推理流程中，用于电商详情页的多模态内容生成或广告文案优化。

  - 分析发现的跨模态泄漏和语言先验问题，提示在多模态Agent设计时需平衡视觉与文本信息，避免忽略图像或过度依赖语言模板。

  - 对于查询生成（如基于图片的搜索词生成），可参考指令令牌重访模式，在任务切换时重新引入指令线索，确保生成相关性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有多模态LLM可解释性主要关注静态层或电路（where），忽略了生成过程中逐令牌的注意力动态（when）。本文旨在填补这一空白，系统研究注意力如何随着语义角色在图像、文本、指令和已生成令牌之间转移。

**方法**：设计需要显式切换视觉与文本上下文的多模态任务，在四个开源多模态LLM上分析注意力分布。追踪每一步生成时模型对各类信息的关注程度，使用因果注意力阻断实验验证其功能作用。基于发现的动态模式，提出一种简单的测试时干预：在适当时刻增强对目标模态的注意力。

**关键结果**：
- 需图像信息的令牌处，图像注意力显著升高；任务转换时指令令牌被重新关注；生成后期对已生成令牌的注意力持续增加。
- 阻断实验证实这些注意力转移对生成至关重要，扰乱后会出现语言先验坠落、跨模态泄漏、拒绝回答或恢复等现象。
- 测试时干预在多个多模态任务上显著提升性能，验证了基于注意力动态的可控生成可行性。
