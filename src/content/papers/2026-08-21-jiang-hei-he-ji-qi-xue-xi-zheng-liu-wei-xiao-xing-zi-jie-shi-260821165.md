---
title: Distilling Black-Box Machine Learning into a Small, Self-Explaining Language
  Model for Learning Analytics
title_zh: 将黑盒机器学习蒸馏为小型自解释语言模型用于学习分析
authors:
- Chenguang Pan
- Airui Meng
- Youmi Suk
affiliations:
- Department of Human Development, Teachers College Columbia University
arxiv_id: '2608.21165'
url: https://arxiv.org/abs/2608.21165
pdf_url: https://arxiv.org/pdf/2608.21165
published: '2026-08-21'
collected: '2026-08-24'
category: RecSys
direction: 模型蒸馏 · 可解释 AI
tags:
- knowledge distillation
- explainable AI
- LLM fine-tuning
- decision support
- faithfulness evaluation
- learning analytics
one_liner: 提出两阶段微调管线，把黑盒估计器及其事后解释蒸馏进小型开源 LLM，实现离线个体级预测与自然语言解释
practical_value: '- **蒸馏+事后解释作为 mentor 的架构可迁移**：把现有黑盒排序/预测模型（如 GBDT、FM、DNN）及其 SHAP/LIME/注意力归因一起蒸馏到小型
  LLM，业务侧就能用自然语言给商家/运营解释推荐或广告出价原因，同时保留个体级预估。

  - **faithfulness-first 评估思路值得借鉴**：不只评测文本流畅度，而是校验叙述是否忠实于归因结果，是否引用虚假特征、编造数值。电商生成式推荐/解释场景可以照搬这种审计机制，当作文本质量门槛。

  - **离线小模型部署降低隐私与成本压力**：文中蒸馏后 2B LLM 可在笔记本离线运行，学生记录不出本机。对电商场景可类比：把用户行为序列、特征留在本地推理，避免调用云端大模型，既省成本又满足隐私合规。

  - **不平衡决策的警示**：严重类别不平衡下，文本解释虽然流畅但决策会塌缩到多数类。做推荐/广告中的解释型 Agent 时，需要单独监控决策分布，不能因为语言流畅就认为模型可靠。'
score: 7
source: arxiv-cs.HC
depth: abstract
---

动机：学习分析中常用黑盒 ML 模型，但模型不透明、部署负担重，难以进入教育实践。作者希望把黑盒估计器及其事后解释蒸馏成一个小型开源 LLM，既能返回个体级估计，又能用自然语言解释原因。

方法：提出两阶段微调管线。第一阶段用黑盒模型（mentor）的预测和事后归因生成训练信号，第二阶段微调一个 2B 参数开源 LLM（mentee），最后模型能同时输出数值估计和叙述性解释。评估上采用 faithfulness-first 框架，对每条叙述审计其是否忠于归因结果，是否编造特征或量值。通过仿真研究分离蒸馏损失与估计器损失：对比 oracle mentor 与真实 ML mentor。

结果：使用 oracle 信号时，蒸馏几乎无损失，效应面恢复 r > .90，重要变量排序完全正确，且未引用无关协变量；真实估计器下，残留误差主要来自上游黑盒模型。在国家级教育数据集上，模型复现了高数课程对最不可能上四年制大学的学生收益最大的发现，98.8% 叙述通过审计，无编造数值。结论：蒸馏后的小 LLM 可在笔记本离线推理，预测与解释一体化。
