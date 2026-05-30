---
title: Reflective Prompt Tuning through Language Model Function-Calling
title_zh: 通过语言模型函数调用的反思式提示调优
authors:
- Farima Fatahi Bayat
- Moin Aminnaseri
- Pouya Pezeshkpour
- Estevam Hruschka
affiliations:
- Megagon Labs
arxiv_id: '2605.21781'
url: https://arxiv.org/abs/2605.21781
pdf_url: https://arxiv.org/pdf/2605.21781
published: '2026-05-19'
collected: '2026-05-30'
category: LLM
direction: 提示优化 · 反思式优化 · 函数调用
tags:
- prompt optimization
- function calling
- reflective tuning
- memory
- confidence calibration
one_liner: 用LLM函数调用模拟人类提示工程师的迭代诊断-修订流程，结合结构化反馈与记忆机制提升提示性能与校准
practical_value: '- **诊断-聚类-修订的迭代提示优化**：可迁移到电商推荐/Agent系统中的LLM提示词优化，通过函数调用自动收集失败样本、聚类失败模式并生成针对性修订，实现Prompt的自我演进。

  - **置信度校准融入优化目标**：将Brier Score等校准指标纳入优化反馈与最终提示选择，有助于在电商风险评估、Agent主动退避（abstention）等场景中提升模型自报置信度的可靠性。

  - **利用LLM函数调用能力解耦评估与修改**：将“跑prompt→收集行为→聚类错误→生成报告”封装为可调用的诊断函数，让优化器专注决策，工程上可实现模块化、可追溯的自动提示调优流程。

  - **历史记忆机制避免无效反复**：积累历史诊断报告与修订记录，帮助优化器识别顽固错误、避免重复编辑，适用于长周期、多轮次的提示优化任务，如推荐系统召回策略的指令迭代。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
提示工程依赖大量人工试错，LLM对措辞、格式、指令顺序高度敏感。现有自动优化方法多基于单样本或小批量反馈，缺乏对系统性错误模式的诊断，且无历史记忆，难以进行长期、可解释的修订。  

**方法关键点**  
- **反思式框架（RPT）**：用LLM作为优化器，通过函数调用模拟人类提示工程师的迭代流程——评估当前提示、诊断失败、修订提示。  
- **诊断函数**：在完整优化集上评估目标模型，记录推理链、答案、置信度；对错误样本进行Critique，生成1-3条失败诊断；通过ClusterFusion将这些诊断聚类为K个重复失败主题，压缩为结构化报告，包含性能指标与失败模式总结。  
- **记忆与修订**：优化器接收当前报告和历史报告（外部记忆），据此进行针对性的提示修订，避免重复错误，同时支持停止条件判断。  
- **置信度感知优化**：在诊断反馈和最终提示选择中纳入校准误差（Brier Score），使优化兼顾任务性能与置信度可靠度。  

**关键结果**  
- 在HotPotQA（多跳推理）、LiveBench-Math（数学推理）、Formula（财务推理）三个数据集上，以GPT-4.1为目标模型，优化器使用GPT-5等。  
- RPT相比初始提示最高提升**+12.9**（HotPotQA）、**+12.4**（LiveBench-Math）、**+11.7**（Formula），整体竞争SOTA（ACE、GEPA、MIPRO）。  
- 置信度感知优化同时降低Brier Score，改善校准。  
- 分析显示RPT的修订与诊断出的失败模式高度对齐，验证性Patch（如验证步骤、单位处理）带来明显性能增益。  

**核心启示**：函数调用LLM能有效模拟人类提示工程师，通过结构化诊断与记忆，实现可解释、可扩展的提示自动迭代。
