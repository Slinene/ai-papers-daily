---
title: 'Enhancing Generative Information Extraction with Two-step Validation: A Product
  Attribute Use Case'
title_zh: 两阶段验证增强生成式信息抽取：产品属性用例
authors:
- Yi-Sheng Hsu
- Nermeen Abou Baker
- Uwe Handmann
affiliations:
- Computer Science Institute, Ruhr West University of Applied Sciences
arxiv_id: '2607.26780'
url: https://arxiv.org/abs/2607.26780
pdf_url: https://arxiv.org/pdf/2607.26780
published: '2026-07-29'
collected: '2026-07-30'
category: LLM
direction: 生成式信息抽取 · 两阶段验证
tags:
- generative IE
- product attribute extraction
- PLM correction
- LLM validation
- low-resource
- privacy-preserving
one_liner: 将小型PLM预测结果作为LLM的校验输入，提升低显著性实体的抽取效果，减少对大型模型的依赖
practical_value: '- 在商品信息抽取（如电商详情、DPP数据）场景，可用小模型先抽属性，再让中等LLM校验修正，平衡效果与成本。

  - 两阶段流水线可本地部署小LLM，避免调用外部API，保护数据隐私，适合商品描述等敏感文本。

  - 对于低频、表述模糊的实体（如‘可回收包装’），PLM易漏召，LLM校验可显著提升召回，可针对性地用于这类属性。

  - 中等模型（7B-13B）在校验任务上可逼近大模型性能，延迟和成本更低，推荐在搜索推荐系统的离线信息抽取模块中尝试。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：数字产品护照（DPP）等场景需要从有限标注数据中抽取产品属性，大型语言模型（LLM）虽泛化强，但直接抽取开销大且易泄露隐私。本文探索生成式信息抽取的效率与隐私平衡方案。

**方法**：提出两阶段验证流水线。第一步用小型预训练语言模型（PLM，如BERT）对文本做初步属性抽取；第二步将PLM输出与原始文本一起交给LLM，要求LLM校验并修正结果，而非从零抽取。本质上将IE转化为校验任务，利用LLM的语义理解纠错。

**结果**：在多个产品属性实体上，两阶段法显著优于仅用LLM直接生成，尤其对低频、隐式表达的实体提升明显。中等规模LLM（如Qwen-2.5-7B）在校验任务上可达到接近大模型（如70B）的性能，但对最小模型（3B）改善有限。此外，第一步PLM预测质量直接影响最终输出，表明PLM与LLM可协同增效。
