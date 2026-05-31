---
title: 'Mind Your Tone: Does Tone Alter LLM Performance?'
title_zh: 注意你的语气：语气会改变LLM的表现吗？
authors:
- Om Dobariya
- Akhil Kumar
affiliations:
- Pennsylvania State University
arxiv_id: '2605.29027'
url: https://arxiv.org/abs/2605.29027
pdf_url: https://arxiv.org/pdf/2605.29027
published: '2026-05-27'
collected: '2026-05-31'
category: LLM
direction: 提示工程 · 语气敏感性
tags:
- Prompt Engineering
- Tone Sensitivity
- LLM Evaluation
- Model Robustness
- Human-AI Interaction
one_liner: 量化提示语气变化对多个LLM客观题准确率的影响，发现语气效应高度依赖模型，且在不同学科间存在差异。
practical_value: '- 在电商搜索推荐中，用户 query 的改写或推荐理由生成若采用固定语气模板，可能因语气敏感性导致模型表现波动，需针对所用 LLM
  进行语气鲁棒性测试。

  - 多 Agent 协作场景下，Agent 间交互提示的语气一致性设计可能影响整体决策质量，可借鉴本研究的语气扰动实验，评估不同语气对任务完成率的影响。

  - 生成式推荐中，控制生成物品描述的提示语气（如专业、随意、紧迫）可能引起推荐准确率的系统性偏移，建议对核心推荐链路做语气消融实验，选择最稳定的语气风格。

  - 构建 LLM 评测集时，应纳入语气变体，避免仅使用单一中性提示导致对模型真实能力的过高估计。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

**动机**：LLM 在实际应用中常因提示的细微语气差异而表现波动，但缺乏系统量化。本文旨在探索客观多选题场景下，语气变化是否以及如何影响 LLM 准确率。

**方法**：构建两个数据集：一个含 50 道基础题和 5 种语气变体（如中性、正式、鼓励性等），另一个从 MMLU 抽取 570 道题覆盖 57 个学科，施以 7 种语气变体。在 ChatGPT-4o、ChatGPT-5-nano、Gemini 2.5 Flash 和 Gemini 2.5 Flash Lite 四个成本友好的 LLM 上评测。通过统计检验和学科级分析，并引入一种“路由框架”解释语气如何调整内部推理模式。

**关键结果**：语气对准确率的影响显著但高度依赖模型。部分模型仅出现小幅统计显著偏移，而另一些模型在不同语气间准确率波动高达 20 个百分点以上。不同学科的语气敏感性差异明显，说明语气效应与任务性质相关。路由框架表明，语气可能通过触发模型不同的内部推理路径而产生影响。该发现警示用户不应假设 LLM 在任何语气下都表现稳定。
