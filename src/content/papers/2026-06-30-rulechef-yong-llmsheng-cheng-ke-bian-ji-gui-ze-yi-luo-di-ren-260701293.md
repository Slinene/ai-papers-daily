---
title: 'RuleChef: Grounding LLM Task Knowledge in Human-Editable Rules'
title_zh: RuleChef：用LLM生成可编辑规则以落地任务知识
authors:
- Ádám Kovács
- Nadia Verdha
- Gábor Recski
affiliations:
- KR Labs
- TU Wien
arxiv_id: '2607.01293'
url: https://arxiv.org/abs/2607.01293
pdf_url: https://arxiv.org/pdf/2607.01293
published: '2026-06-30'
collected: '2026-07-09'
category: LLM
direction: LLM 规则生成与可解释AI
tags:
- rule-based system
- LLM
- interpretability
- symbolic reasoning
- human-in-the-loop
- rule generation
one_liner: 利用LLM从标注数据自动生成、迭代修补可执行规则，得到快速、可解释的符号系统
practical_value: '- **离线LLM生成规则，在线轻量推理**：在电商搜索/推荐中，可将LLM用于离线规则合成（如意图分类、属性提取），线上部署为确定性规则引擎，避免高延迟与API成本，适合高QPS场景。

  - **规则迭代与人工反馈闭环**：借鉴RuleChef的patch机制，将人工审核或业务专家反馈直接转化为规则补丁，持续优化文本处理逻辑，如query改写规则、违禁词过滤。

  - **模型蒸馏为透明规则**：利用已有模型（如BERT分类器）的输入输出对bootstrap规则，把黑盒模型知识转化为可解释、可审计的规则集，满足风控、合规等场景对可解释性的要求。

  - **版本化与可调试的文本处理管道**：规则集易于版本管理与调试，可配合A/B测试快速迭代，提升推荐系统中query理解、内容审核等模块的灵活性与可控性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统规则系统透明、确定、高效，但人工编写与维护成本高；LLM强大但推理慢、黑盒且难以审计。RuleChef旨在结合两者优势：仅在学习阶段用LLM，将标注数据转化为人类可编辑的可执行规则，保留可解释性的同时降低规则构建成本。

**方法**：框架输入任务描述与少量标注样本，LLM合成初步规则；在留存集上探测错误，LLM生成规则补丁；支持人工介入编辑/修正规则。迭代直至性能收敛。另外，也可从任意现有模型的输入输出对bootstrap规则，实现模型知识提取。最终输出一套纯符号的规则系统，推理仅涉及规则匹配，快速且确定。

**结果**：在文本分类与NER任务上的初步评估显示，自动生成的规则集准确率超过GPT-3.5 zero-shot，接近GPT-4o，同时推理速度远快于LLM调用，且完全可解释。代码已开源。
