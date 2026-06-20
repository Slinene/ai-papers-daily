---
title: Thinking with Visual Grounding
title_zh: 视觉锚定思维：VLMs推理步骤与图像区域显式关联
authors:
- Junkai Zhang
- Yihe Deng
- Kai-Wei Chang
- Wei Wang
affiliations:
- University of California, Los Angeles
arxiv_id: '2606.16122'
url: https://arxiv.org/abs/2606.16122
pdf_url: https://arxiv.org/pdf/2606.16122
published: '2026-06-14'
collected: '2026-06-20'
category: Multimodal
direction: 多模态推理 · 视觉定位强化学习
tags:
- Visual Grounding
- VLM Reasoning
- Reinforcement Learning
- Synthetic Data Pipeline
- Point-Box Grounding
- Gemma
one_liner: 通过在文本思维中插入点/框级视觉定位，显著提升VLM计数和空间推理性能
practical_value: '- 电商多模态Agent可借鉴该方法，对商品图片进行属性验证时，在推理链中显式锚定图像区域（如领口、logo位置），提升判别可解释性与准确率。

  - 合成数据管线利用SAM3自动提取掩码并生成点/框监督，可低成本构建商品图像问答或合规审核的接地推理数据，减少人工标注。

  - 接地感知RL（答案正确+密集接地奖励）的多奖励框架，可迁移到微调多模态推荐模型，使其输出推荐理由时精准指向图片关键证据。

  - 点定位适合计数、框定位从空间奖励中获益更多的结论，可指导电商图文推荐中不同任务（如数量统计 vs. 布局合规）的接地策略选择。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前VLM的推理链往往隐式依赖图像证据，缺乏可验证的视觉定位，难以监督与纠正。该工作提出“视觉锚定思维”，要求模型在文本思维步骤中显式输出点或边界框定位，指明推理所依据的图像区域。

**方法**：1) 构建可扩展的合成数据管线：利用SAM3 Agent为正确推理链中涉及的视觉对象自动生成掩码，并导出点/框监督信号，蒸馏出带接地标注的推理数据；2) 设计接地感知RL：在RL微调中同时奖励答案正确性和接地准确性（密集奖励），提升视觉思维与图像证据的一致性。模型基于Gemma3-4B-IT。

**关键结果**：在两个计数基准和四个空间推理基准上，添加视觉锚定思维的模型显著优于原始模型和无定位的思维基线。在空间推理任务上，4B定位模型性能匹配甚至超越同系列27B模型。分析表明：点定位特别适合计数任务，框定位在空间任务上从显式接地奖励中获益最大。
