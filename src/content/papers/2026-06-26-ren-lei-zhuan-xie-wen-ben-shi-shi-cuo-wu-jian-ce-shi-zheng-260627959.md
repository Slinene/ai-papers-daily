---
title: An Empirical Analysis of Factual Errors in Human-Written Text and its Application
title_zh: 人类撰写文本事实错误检测实证分析与应用
authors:
- Kazuma Iwamoto
- Kazumasa Omura
- Shotaro Ishihara
affiliations:
- Nikkei Inc.
arxiv_id: '2606.27959'
url: https://arxiv.org/abs/2606.27959
pdf_url: https://arxiv.org/pdf/2606.27959
published: '2026-06-26'
collected: '2026-06-29'
category: Eval
direction: 事实错误检测分类与 LLM 评估
tags:
- Factual Error Detection
- LLM Evaluation
- Hallucination
- Human-Written Text
- Taxonomy
one_liner: 提炼人类文本事实错误分类法，评估 LLM 检测能力，GPT-5.4 仅 52% F1
practical_value: '- 在生成商品描述、推荐理由等文本时，可借鉴分类法（如数量词错误、实体误转换）设计事实性校验模块，提高内容可信度。

  - 评估场景中可复现类似的合成测试方法，针对自身业务常见错误类型（如价格单位、商品属性）构造测试集，检验 LLM 的事实一致性。

  - 观察到 LLM 对人类文本事实错误检测效果有限（F1 52%），提示在自动选品文案等场景中，不能完全依赖 LLM 自查，需加入后置规则或人工审核。

  - 对于 Agent 系统，在调用 LLM 生成对外内容时，可针对分类法中特定错误类型设计提示模板，引导模型避免常见事实性错误。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有事实错误检测（FED）研究集中于 LLM 幻觉，忽视了人类撰写文本。为填补此空白，通过分析报纸文章更正记录，系统归纳人类文本中典型的事实错误类型。

**方法关键点**：1) 从报纸更正数据中提炼错误分类法，识别出汉字误转换、数量词错误、专名错误等独特类别，不同于常见幻觉基准；2) 基于该分类法合成真实感测试用例，并结合真实更正数据；3) 在合成数据和真实数据上评估基础 LLM（包括 GPT-5.4）的单词级 FED 性能，并分析错误检测难度分布。

**关键结果**：GPT-5.4 在合成数据上仅达到 52% 的单词级 F1 分数，表明任务难度高；不同错误类型的可检测性差异明显，部分类别（如数量词错误）更难被 LLM 发现。论文揭示了当前 LLM 在人类文本事实核查上的能力短板。
