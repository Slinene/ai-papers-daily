---
title: Calibrating Semantic Uncertainty from Observable Language-Model Probabilities
title_zh: 从可观测语言模型概率校准语义不确定性
authors:
- Matthew F. Dixon
affiliations:
- Artificial Intelligence Finance Institute
- Quiota LLC
arxiv_id: '2607.17447'
url: https://arxiv.org/abs/2607.17447
pdf_url: https://arxiv.org/pdf/2607.17447
published: '2026-07-20'
collected: '2026-07-21'
category: Eval
direction: 语言模型概率校准与语义稳健性
tags:
- semantic uncertainty
- calibration
- language models
- posterior inference
- stability under paraphrasing
- auditability
one_liner: 提出语义映射框架，将语言模型词汇概率校准为可验证的语义后验，在改写下保持稳定
practical_value: '- **评估LLM输出的可靠概率**：在电商推荐中，若用LLM生成推荐理由或解释，可通过语义映射把 token 概率转化为推荐置信度，避免直接使用模型打印的数值概率。

  - **保证改写稳定性**：提示词工程中，不同措辞的同义提示可能导致概率漂移。该方法通过标定后验确保语义级输出对改写稳定，可用于构建鲁棒的对话式推荐或Agent决策。

  - **审计推荐系统语义一致性**：对生成式推荐或Agent的响应进行校准审计，检测是否存在语义不稳定，提升系统可解释性与可信度。

  - **小样本后验估计**：利用少量标定数据连接语言模型输出与目标后验，适用于缺乏大量标注的电商场景，如用户意图分类或商品属性判别。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：语言模型为词元输出概率，但实际决策需要的是语义状态（如诊断、假设）上的可靠不确定性度量。模型打印的数值置信度并不可信，且概率会随提示措辞变化，而真实后验应不随等价改写改变。

**方法**：提出“语义映射”——一种半参数推断框架，将语言模型的词汇响应分布映射到有限潜在语义状态的后验。通过参考模型定义目标后验，语言模型提供无限制的条件分布，再用标定样本桥接二者。理论推导了后验误差界，并给出了映射存在、唯一、稳定和序列贝叶斯更新的条件。

**关键结果**：在美联储经济文本仿真和精确后验模拟中，两个语言模型上，语义映射得到的概率优于直接数值概率，能以有效的不确定性覆盖还原后验分布，并在同义改写下基本稳定，对证据变化反应恰当。方法将提示工程的措辞依赖性转化为可测试的统计问题，为审计分类、推荐等流畅响应中的语义不稳定性提供了模板。
