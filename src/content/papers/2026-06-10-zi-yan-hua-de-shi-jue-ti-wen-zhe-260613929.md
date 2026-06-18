---
title: Self-Evolving Visual Questioner
title_zh: 自演化的视觉提问者
authors:
- Yijun Liang
- Hengguang Zhou
- Ming Li
- Lichen Li
- Cho-Jui Hsieh
- Tianyi Zhou
affiliations:
- University of Maryland, College Park
- University of California, Los Angeles
- Peking University
- Arena
- MBZUAI
arxiv_id: '2606.13929'
url: https://arxiv.org/abs/2606.13929
pdf_url: https://arxiv.org/pdf/2606.13929
published: '2026-06-10'
collected: '2026-06-18'
category: Other
direction: 自监督问题生成 · 视觉提问
tags:
- Self-Evolution
- Visual Question Generation
- VLM
- Active Learning
- Diversity
- Self-Training
one_liner: 让VLM通过自我生成与过滤，逐步产出更困难、更多样化的视觉问题，无需外部监督
practical_value: '- 搜索/推荐场景下，可用类似 self-evolving 范式自动产出更困难、更多样化的用户查询词或推荐理由，无需人工标注。

  - 对话式推荐 Agent 可利用自提问-过滤机制，主动向用户提出高信息量的澄清问题，提升交互效率。

  - 论文的 Agentic 评估协议（感知、推理、多样性）可直接迁移用于评估推荐系统生成的 query 或对话的质量。

  - 工程上可借鉴其双模式训练（提问者+回答者联合优化），保证生成能力不损害原有任务性能。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机：**
现有视觉-语言模型（VLM）多被训练为被动回答者，主动提出多样化、以视觉为中心问题的能力被忽视。高质量提问数据的稀缺和标注成本制约了模型在此方向上的表现。

**方法关键点：**
- 提出 Self-Evolving 框架：VLM 同时作为问题提议者（proposer）和过滤器（filter），从自身采样中筛选出更困难、信息量更大、更聚焦视觉内容的问题。
- 引入探索多样性约束，避免生成问题坍缩到狭窄模式，确保持续进化。
- 筛选后的问题用于同时训练 VLM 的提问者模式与回答者模式，形成闭环。
- 设计 Agentic 评估协议，从感知难度、推理深度、问题多样性三个维度自动化评估提问质量。

**关键结果数字：**
- 在多种 VLM 骨干上，问题质量与难度边界均大幅提升。
- 同等训练预算下，自监督方法效果优于使用静态源数据训练。
- 自演化的提问者在回答任务上仍保持竞争力甚至更优。
