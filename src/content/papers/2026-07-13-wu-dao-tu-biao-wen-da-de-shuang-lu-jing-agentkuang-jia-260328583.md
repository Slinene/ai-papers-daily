---
title: 'Navigating the Mirage: A Dual-Path Agentic Framework for Robust Misleading
  Chart Question Answering'
title_zh: 误导图表问答的双路径Agent框架
authors:
- Yanjie Zhang
- Yafei Li
- Rui Sheng
- Zixin Chen
- Yanna Lin
- Huamin Qu
- Lei Chen
- Yushi Sun
affiliations:
- HKUST
- HKUST(GZ)
arxiv_id: '2603.28583'
url: https://arxiv.org/abs/2603.28583
pdf_url: https://arxiv.org/pdf/2603.28583
published: '2026-07-13'
collected: '2026-07-16'
category: Agent
direction: Agent 双路径图表问答框架
tags:
- Agent
- MisleadingChartQA
- VLM
- GRPO
- SFT
- Cross-modalVerification
one_liner: 提出ChartCynics双路径Agent框架，通过视觉诊断与OCR数据验证解耦，大幅提升小模型对误导图表的鲁棒QA性能
practical_value: '- **双路径解耦验证范式可迁移至电商多模态审核**：商品图文一致性检查、广告素材合规判定等任务中，可构建类似“视觉异常检测路径
  + OCR文本抽取路径”，由Agent Summarizer进行冲突裁决，提高对欺骗性描述的鲁棒性。

  - **Oracle蒸馏 + 对抗对齐训练方法**：在推荐系统对抗恶意行为（如虚假评论、刷单）时，可用Oracle-Informed SFT蒸馏出批判性推理链，再通过Deception-Aware
  GRPO进行对抗式强化学习，让模型学会识别操纵模式。

  - **小模型 + Agent工作流超越闭源大模型**：电商搜索推荐场景资源受限时，可将大模型能力拆解为多个专家子路径，通过Agent编排让开源小模型在多模态推理任务上达到甚至超过GPT-4V等专有模型，性价比更高。

  - **可借鉴的ROI策略与多证据整合**：推荐系统中处理商品主图、详情图等多图像信息时，可引入战略性的ROI裁剪聚焦关键区域，结合文本证据进行最终判断，避免全局视觉偏见。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有VLM在误导图表问答上表现脆弱，容易被篡改的坐标轴、失真比例等视觉陷阱欺骗。传统端到端模型未解耦感知与数值验证，缺乏对图文矛盾的显式审查。

**方法关键点**：
- **双路径架构**：Diagnostic Vision Path通过策略性ROI裁剪捕获结构异常（如倒置轴）；OCR-Driven Data Path提取并对齐数值事实，实现视觉与数据的解耦感知。
- **Agentic Summarizer**：接收双路径信号，先由Oracle-Informed SFT从强推理过程蒸馏出初始批判性策略，再经Deception-Aware GRPO进行对抗对齐，牺牲视觉捷径，强制逻辑一致。
- 训练中使用Oracle推理链（来自GPT-4o等）作为监督信号，GRPO阶段通过奖励惩罚模型依赖视觉假象，鼓励基于数据的理性回答。

**关键结果**：
- 在两个误导图表QA基准上分别达到74.43%和64.55%准确率。
- 以Qwen3-VL-8B为基座，绝对提升约29个百分点，显著超越GPT-4V等专有闭源模型。
- 消融实验证实双路径与两阶段对齐训练的关键作用。
