---
title: Understanding Data Temporality Impact on Large Language Models Pre-training
title_zh: 探究数据时序性对大语言模型预训练的影响
authors:
- Pilchen Hippolyte
- Fabre Romain
- Signe Talla Franck
- Perez Patrick
- Grave Edouard
affiliations:
- Kyutai, Paris
arxiv_id: '2605.22769'
url: https://arxiv.org/abs/2605.22769
pdf_url: https://arxiv.org/pdf/2605.22769
published: '2026-05-21'
collected: '2026-05-24'
category: Training
direction: 时序数据预训练优化
tags:
- Data Ordering
- Temporal Knowledge
- Pre-training
- Benchmark
- Factual Freshness
- Continual Learning
one_liner: 通过预训练6B模型发现，按时序排列数据训练能显著提升模型的时间知识准确性，且不影响通用能力。
practical_value: '- **时序数据组织**：在电商搜索或推荐模型的持续预训练中，可将商品语料按发布时间排序，使模型隐式学习时间对齐的知识，提升对新品、季节性趋势的捕获能力，避免依赖频繁的增量微调。

  - **评价协议设计**：可借鉴提出时间敏感问答基准的思路，构建电商领域的时间相关评测集（例如“2023年夏季流行款式”对应正确季节），用于检测推荐系统或Agent的时间感知准确性。

  - **训练效率权衡**：实验表明按时序训练与普通打乱训练相比，在通用理解任务上表现相当，但知识保鲜度更高。对于需要低成本保持知识新鲜的业务，可直接采用时序预训练，无需额外的中期继续训练阶段。

  - **负面发现启示**：打乱顺序训练会让模型更擅长记忆旧数据，可能因为重复事实更多；在构建电商语料时，若希望模型更关注近期数据，应避免过度打乱，或结合时间加权采样。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：标准LLM预训练对语料进行无序打乱，导致模型的知识停留在训练时刻，时间对齐能力差。本研究希望探究数据时序排序如何影响模型获取时间敏感的事实知识。

**方法关键点**：
- 构建了包含7,000+时间锚定问题的**KairosQA**基准，用于评测模型能否将事实与对应时间段正确关联。
- 使用按时间排序的Common Crawl快照预训练6B参数模型，与标准打乱训练的基线对比。
- 评估通用语言理解、常识知识和时间知识准确性。

**关键结果**：
- 按时序训练的模型在通用任务上与打乱基线持平，但时间知识**新鲜度更高、精度更优**。
- 在2023–2024时段问题上，时序模型相对F1提升16%，而其他开源模型（Llama3.1、Gemma3等）同期知识均出现衰退（-39%到-12%不等）。
- 打乱预训练使模型在旧数据上表现峰值更高，可能源于事实重复增多。
- 开放代码、检查点和数据集，为LLM持续学习研究提供基础。
