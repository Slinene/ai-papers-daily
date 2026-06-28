---
title: 'NuclearQAv2: A Structured Benchmark for Evaluating Domain-Science Competence
  in Large Language Models'
title_zh: NuclearQAv2：面向核工程领域的大语言模型结构化评估基准
authors:
- Henry Shaowu Yuchi
- Michal Kucer
- Benjamin H. Sims
- Selma Peterson
- Emily Taylor
affiliations:
- Los Alamos National Laboratory
arxiv_id: '2606.27047'
url: https://arxiv.org/abs/2606.27047
pdf_url: https://arxiv.org/pdf/2606.27047
published: '2026-06-25'
collected: '2026-06-28'
category: Eval
direction: 领域科学评估基准
tags:
- benchmark
- domain-specific QA
- LLM evaluation
- quantitative reasoning
- hybrid pipeline
- nuclear engineering
one_liner: 提出混合流水线构建核工程QA基准，揭示大模型在定量推理与概念理解上的短板
practical_value: '- **领域评估集构建方法可复用**：采用专家出题+已有数据集+LLM辅助生成的混合流水线，成本可控且可扩展，可直接迁移到电商商品知识、广告政策合规等垂直领域评估集的构建。

  - **多类题型设计揭示模型盲区**：将题目分为布尔、数值、口头三类，分别考察事实记忆、定量计算和概念理解，借鉴此设计可定位Agent在推荐解释、金额计算等场景下的薄弱环节。

  - **结构化提示用于自动出题与判分**：通过精心设计的提示模板实现题目生成与答案校验，减少人工干预，适合需要快速迭代评估的推荐/搜索线上评测场景。

  - **评估结果强调定量推理是短板**：在各领域LLM应用中（如动态定价、效果预估）应重点监控数值型任务表现，辅助针对性微调或引入外部计算工具。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：大语言模型在医疗、金融等高技术领域的可靠性备受关注，核工程不仅需要事实知识，更依赖定量推理和概念理解，但缺乏系统评估基准。  
**方法**：提出NuclearQAv2，包含约1240道问答对，覆盖布尔、数值、口头三类题型。构建流水线混合专家编写、已有数据集与LLM辅助生成，利用结构化提示实现可扩展的问题生成与回答自动评估。  
**关键结果**：评测多种主流LLM后发现，模型在事实性问题上表现良好，但数值推理和概念理解题仍有明显差距，多维度评估框架能更全面暴露模型在专业领域的脆弱性，基准本身可低成本扩展至其他技术领域。
