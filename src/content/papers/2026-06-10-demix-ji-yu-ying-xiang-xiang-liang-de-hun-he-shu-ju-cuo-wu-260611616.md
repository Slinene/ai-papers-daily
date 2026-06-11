---
title: 'DeMix: Debugging Training Data with Mixed Data Error Types by Investigating
  Influence Vectors'
title_zh: DeMix：基于影响向量的混合数据错误类型调试框架
authors:
- Jiale Deng
- Yanyan Shen
- Xiaogang Shi
- Chai Junjun
affiliations:
- Shanghai Jiao Tong University
- ByteDance Inc.
- Tiktok
arxiv_id: '2606.11616'
url: https://arxiv.org/abs/2606.11616
pdf_url: https://arxiv.org/pdf/2606.11616
published: '2026-06-10'
collected: '2026-06-11'
category: Training
direction: 基于影响向量的训练数据调试
tags:
- Data Debugging
- Influence Function
- Multi-Label Classification
- Invariant Learning
- Set Transformer
one_liner: 利用完整的影响向量代替标量分数，通过多标签分类同步检测训练数据中的标签错误、特征错误和虚假相关三类问题。
practical_value: '- **影响向量替代标量影响分数**：在推荐或电商数据中直接对标量影响力（如留一法影响值）聚合会掩盖错误类型特异性。保留完整验证样本上的影响分布，再用
  Set Transformer 编码，能更好捕获标签噪声、特征异常和虚假相关等细粒度错误模式。

  - **无需完全干净的验证集**：DeMix 通过干预不同的验证子集和模型架构，强制学到对验证集噪声、模型选择鲁棒的错误表征，适合推荐系统等验证集本身可能受系统性偏差污染的场景。

  - **部署时采用验证集采样与模型集成**：大规模推荐数据上计算完整影响向量开销大，可参照文中仅用 10% 验证子集和轻量模型集成（如 2~3 个不同架构），在保持调试
  F1 几乎不降的情况下将运行时和显存大幅降低。

  - **错误类型驱动的定向修复**：识别出的标签错误、特征错误、虚假相关可分别应用重标注、Z-score 特征补全、少数群体重加权等修复策略，直接作用于召回/排序数据，提升后续模型
  AUC。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
实际训练数据常同时混有标签错误（LE）、特征错误（FE）和虚假相关（SC），不同错误类型对模型预测的影响机制不同，但现有数据清洗和归因方法只能检测错误样本，无法区分错误类型，导致修复盲目。  

**方法**  
- **影响向量**：对每个训练样本，计算其对全验证集每个样本的影响函数，形成高维影响向量（而非仅用一个标量值），不同错误类型在向量上呈现可分离的分布模式。  
- **多标签分类器**：用 Set Transformer 编码影响向量（保持置换不变性，捕获元素间交互），再接 MLP 头预测每个样本的 LE / FE / SC 标签。训练样本通过可控错误注入（翻转标签、破坏特征、操控群体比例）合成，并允许错误共现。  
- **干预式不变表示学习**：为提升泛化，随机采样不同验证子集和构造不同架构的模型集成，分别用对比损失和 L2 对齐损失约束编码器，迫使所学表征对验证集选择和模型架构不敏感，聚焦于错误类型本质模式。  

**实验与结果**  
在 6 个表格预测、3 个推荐系统（Amazon, MovieLens, Yelp）和 2 个 LLM 对齐（UltraFeedback, Capybara）共 11 个任务上，与 Cleanlab 数据清洗流水线（DDC）、基于标量影响的 DDA-repair 等基线相比：  
- 调试 F1 平均提升 **22.61%**，在自定义的混合错误数据上尤为稳定，对错误比例变化不敏感。  
- 经类型定向修复后重训的模型性能平均提升 **9.32%**，在推荐任务中 AUC 明显回升。  
- 消融实验表明，移除验证集或模型干预正则项会引发约 3.5%~3.0% 的 F1 下降，且在跨验证集、跨模型架构的泛化测试中退化明显。  
- 在 MovieLens 上，仅用 10% 验证样本即可将调试时间从 35.4 分钟降至 6.6 分钟，F1 仅下降 0.2%。  

**核心结论**  
保留完整影响向量并对其建模，辅以跨配置不变性训练，能够在混合错误场景下实现精准且鲁棒的错误类型识别，结合针对性修复可有效恢复模型性能。
