---
title: 'MolE-RAG: Molecular Structure-Enhanced Retrieval-Augmented Generation for
  Chemistry'
title_zh: MolE-RAG：面向化学的分子结构增强检索增强生成
authors:
- Joey Chan
- Wonbin Kweon
- Ashley Shin
- Niharika Bhattacharjee
- Pengcheng Jiang
- Yue Guo
- Jiawei Han
affiliations:
- University of Illinois Urbana-Champaign
- University of California, San Diego
arxiv_id: '2606.05693'
url: https://arxiv.org/abs/2606.05693
pdf_url: https://arxiv.org/pdf/2606.05693
published: '2026-06-04'
collected: '2026-06-06'
category: RAG
direction: RAG · 化学分子性质预测
tags:
- RAG
- Molecular Property Prediction
- LLMs
- Chemistry
- Structure Retrieval
one_liner: 无训练的分子中心RAG框架，集成多种化学上下文，大幅提升LLM分子性质预测性能。
practical_value: '- 多源上下文注入思路可迁移：为每件商品提供属性、评论摘要、相似商品等多源信息，提升LLM推荐解释或预测。

  - 无需微调的推理时增强：直接检索注入知识，适合迭代快的电商业务场景，降低模型更新成本。

  - 结构相似性检索：利用商品结构化特征（类目、品牌、价格）计算相似度，检索相似商品信息作为prompt，增强模型理解。

  - 根据任务和模型选择上下文源：不同LLM偏好不同来源，可消融实验确定最优组合，避免信息冗余。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：LLM在分子性质预测上有潜力，但分子SMILES表示与自然语言差异大，造成知识鸿沟。为弥补此差距，提出MolE-RAG框架，无需训练，在推理时通过检索增强生成提升预测。

方法：MolE-RAG注入三类上下文：①检索的化学文献，提供领域知识；②分子特定信息，包括化合物同义词、标识符、官能团标注和理化描述符（如TPSA、LogP），将分子转化为LLM可理解的语言；③从训练集检索结构相似的分子及其标签，利用结构相似性传递信息。三类上下文组合后作为LLM的输入。

关键结果：在9个分子性质预测任务（涵盖分类和回归）上评测，使用通用、化学专用和开源LLM。通用LLM上，分类ROC-AUC最高提升28个百分点，回归RMSE相对SMILES-only基线最多降低67%。不同模型和任务从不同上下文源获益，体现了框架的灵活性和组合空间。
