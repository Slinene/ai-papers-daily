---
title: 'AVTR: Adaptive Multimodal Reasoning with Visual Imagination'
title_zh: AVTR：带视觉想象的自适应多模态推理
authors:
- Xiaoqian Shen
- Yunyang Xiong
- Changsheng Zhao
- Saksham Suri
- Chong Zhou
- Zechun Liu
- Zhipeng Cai
- Zhuang Liu
- Qi Qian
- Wei Wen
affiliations:
- Meta AI
- King Abdullah University of Science and Technology (KAUST)
- Princeton University
arxiv_id: '2611.24161'
url: https://arxiv.org/abs/2611.24161
pdf_url: https://arxiv.org/pdf/2611.24161
published: '2026-11-18'
collected: '2026-11-20'
category: Multimodal
direction: 多模态自适应推理 · 视觉想象力
tags:
- Multimodal Reasoning
- Visual Imagination
- Routing
- VLM
- Adaptive Inference
one_liner: 引入视觉想象力作为文本推理的补充模态，并学习路由选择推理模态，提升多模态推理准确率并降低延迟
practical_value: '- 自适应推理深度控制：借鉴路由思路，对用户 query 或商品上下文做复杂度判断，简单请求直接走轻量生成，复杂请求才触发深度推理，可显著降低线上推理延迟。

  - 多模态商品理解的视觉反思：在电商场景中，对商品图片生成关键视觉描述（如材质、细节、风格）作为辅助文本证据，再与文本推理结合，提升推荐理由或商品匹配质量。

  - 可学习路由替代固定模式：不预先指定走文本或视觉，而是用轻量策略模块动态分配，适合将 Agent 的推理步骤与工具调用解耦，按需调用视觉检索或生成模块。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：VLMs 感知是多模态的，但推理几乎只在文本 token 上进行。这带来两个问题：纯文本推理会限制视觉中心问题的感知能力；对所有输入统一进行文本推理会导致冗余、低效，忽视问题所需的推理模态与深度差异。

方法关键点：提出 AVTR，将视觉想象力作为文本推理的补充模态。模型通过生成式视觉反思重新审视视觉观察，提取显著视觉证据。同时，将推理模态选择形式化为可学习路由问题，单一策略根据输入的感知与推理需求，在视觉反思和文本推理之间自适应选择，避免无谓的推理痕迹。

关键结果：在 16 个基准上，AVTR 平均得分比 Qwen3.5 基线提升 4.5 分，推理延迟降低 33%；在小规模 backbone 上同样有效，超过评测的 2B 级基线。
