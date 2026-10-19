---
title: 'Code Skill Server: A Large-Scale Search Engine for Code Generation Skills'
title_zh: 代码技能服务器：面向代码生成技能的大规模搜索引擎
authors:
- Xiaoyong Li
- Haolong Li
- Dongliang Xu
- Haoyu Li
- Yifan Wang
- Jingyuan Shi
- Yanghua Wang
- Yanbin Sun
- Shidong Pan
- Yue Yao
affiliations:
- Shandong University
- Guangzhou University
arxiv_id: '2610.23186'
url: https://arxiv.org/abs/2610.23186
pdf_url: https://arxiv.org/pdf/2610.23186
published: '2026-10-16'
collected: '2026-10-19'
category: Agent
direction: Agent 技能检索与代码生成增强
tags:
- Agent Skills
- Code Generation
- Skill Retrieval
- Search Engine
- RAG
- Pass@1
one_liner: 构建包含 993 个代码生成技能的检索服务器，检索注入可提升 Pass@1 最高 13.91%
practical_value: '- 将可复用能力沉淀为技能库：把营销文案模板、API 调用代码、平台规则等封装成统一 schema 的技能，用 embedding
  建立增量索引，Agent 根据 target task 检索注入上下文

  - 检索即增强，不依赖微调：实验显示跨模型稳定提升至少 4.21%，可直接将技能检索作为外挂模块，接入现有多模型 pipeline

  - 异构来源技能标准化是关键：统一技能描述、触发条件、示例等字段，能提高检索命中率与可复用性

  - 评估上关注 Pass@1 提升和跨模型泛化，可作为生成式推荐/Agent 工具检索旁路增强的验证指标'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：Agent 技能能提升代码生成等任务表现，但现有方法依赖人工从异构来源发现和整理技能，难以规模化。

方法：提出 Code Skill Server（CSS），一个大规模代码生成技能搜索引擎。CSS 增量收集并索引公开可用的代码生成技能，语料库含 993 个技能。检索流程采用多种检索方法（如 embedding 检索、重排等），将检索到的相关技能注入代码生成模型上下文，辅助生成。

结果：在不同检索方法和代码生成基准上测试，最佳 CSS 配置 Pass@1 最高提升 13.91%；跨模型评估中所有模型至少提升 4.21%，说明技能检索能稳定增强多种模型的代码生成能力。
