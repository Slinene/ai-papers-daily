---
title: 'When LLMs Read Tables Carelessly: Measuring and Reducing Data Referencing
  Errors'
title_zh: 当LLM粗心读表：数据引用错误的衡量与减少
authors:
- Yuqing Yang
- Qi Zhu
- Zhen Han
- Boran Han
- Zhengyuan Shen
- Shuai Wang
- Vassilis N. Ioannidis
- Huzefa Rangwala
affiliations:
- University of Southern California
- AWS AI Labs
arxiv_id: '2606.32029'
url: https://arxiv.org/abs/2606.32029
pdf_url: https://arxiv.org/pdf/2606.32029
published: '2026-06-29'
collected: '2026-07-02'
category: LLM
direction: 表格数据引用错误检测与校正
tags:
- Data Referencing Errors
- Table Reasoning
- Critic Model
- Rejection Sampling
- Factuality
- LLM Evaluation
one_liner: 首次系统评估LLM表格推理中的数据引用错误，通过critic模型检测并过滤错误，答案准确率提升最高12.0%
practical_value: '- 在Agent工作流中引入轻量级critic模型（4B参数）检测LLM生成中的数据引用错误，尤其适用于需要精确数值的广告预算计算、商品属性提取等场景。

  - 使用critic-based过滤或拒绝采样，对候选回答进行后验验证，无需重训主模型即可提升最终答案可靠性，类似推荐系统中的多阶段过滤。

  - 对于表格类输入（如用户画像、商品参数表），可训练专用的引用错误检测模型，作为安全校验层，降低因数值错漏导致的决策风险。

  - 该方法展示了小模型（4B）辅助大模型推理的有效性，可参考用于电商搜索中的查询改写、结果解释等需要精准数据引用的环节。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM在表格任务中虽能理解结构，却频繁出现数据引用错误（DRE），如错误引用或遗漏数值，直接影响中间推理的可靠性。以往研究仅做了小规模分析，缺乏系统性评估。

**方法**：首先对1.7B至20B参数的多种LLM在不同表格任务上进行DRE的系统评估。然后提出将数据引用作为critic信号：利用critic模型判断生成回答中数值引用的正确性，并基于critic分数进行过滤或拒绝采样，筛选出更可靠的回答。最后训练了一个仅4B参数的轻量级critic模型，能检测分布内和分布外的DRE，并用于辅助更大模型的推理。

**关键结果**：DRE在所有测试模型中普遍存在；引入critic后，答案准确率最高提升12.0%；4B critic模型检测DRE的平均F1达78.2%，在分布外数据上也表现稳健，有效辅助大模型提升最终输出质量。
