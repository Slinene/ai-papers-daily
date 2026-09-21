---
title: LLMs as Feature Engineers for Text-and-Tabular Prediction
title_zh: LLM 作为特征工程师用于文本与表格预测
authors:
- Merwan Barlier
- Blaz Skrlj
affiliations:
- Teads
arxiv_id: '2609.21894'
url: https://arxiv.org/abs/2609.21894
pdf_url: https://arxiv.org/pdf/2609.21894
published: '2026-09-18'
collected: '2026-09-21'
category: RecSys
direction: LLM 自动化特征工程
tags:
- LLM
- Feature Engineering
- Text-and-Tabular
- Interpretability
- CTR Prediction
- Automated Feature Discovery
one_liner: 迭代式 LLM 框架自动从文本提取可解释分类特征，并通过错误反馈将发现速度提升最高 3 倍
practical_value: '- 借鉴 generator-LLM 与 extractor-LLM 的职责分离：一个负责提出语义特征定义（如商品目标人群、文案情感、新颖度），另一个负责从原始文本中具体抽取类别值。这种解耦便于在电商商品描述、广告创意、用户评论中批量生成结构化特征。

  - 用下游模型显式错误（如 AUC 排序反转）作为自然语言反馈，指导 LLM 迭代修正特征。实际工程中可记录预测高置信但排序错误的样本对，转化为提示词让 LLM
  聚焦于解决特定失败模式，避免盲目搜索。

  - 生成的可解释类别特征与 TF-IDF、dense embeddings 存在强互补性，建议在线性/树模型中将三者同时作为输入，而非二选一。论文实验显示组合严格优于任何子集，可提升
  CTR 模型的预测能力。

  - SHAP 分析表明 LLM 提取的特征在重要性排名中占主导，适合需要审计和解释的广告投放、推荐排序场景，能为每个预测提供人可读的语义依据。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：表格预测模型（如 CTR、推荐）难以有效利用原始文本，传统 dense embeddings 不可解释，手工特征成本高且难迁移。

**方法**：提出迭代框架，包含三个组件：generator LLM 提出 schema-bound 的语义特征定义；extractor LLM 根据定义从文本中抽取具体类别值；下游表格模型评估特征贡献。关键创新是将模型的显式错误（如 AUC 排序反转）转化为自然语言反馈，回传给 generator LLM 迭代优化，使特征搜索聚焦于解决实际预测失败。

**结果**：在三个公开数据集上，错误驱动的循环相比无引导搜索将特征发现速度提升最高 3 倍。生成的特征与 TF-IDF 和 dense embeddings 结合时严格优于任何单一特征子集，表现出强多视图互补性。此外，这些特征在 SHAP 重要性排名中占主导地位，为每个预测提供透明的语义审计轨迹，实现实例级可解释性。
