---
title: 'StudentBench: AI and human tutoring yield equivalent GRE learning gains'
title_zh: AI辅导与人类专家在GRE学习增益上等效
authors:
- Curtis Northcutt
- Inaara Hasmani
- Kevin Feng
- Trevor Khangi
- Andreas Plesner
- Jonas Mueller
arxiv_id: '2609.28470'
url: https://arxiv.org/abs/2609.28470
pdf_url: https://arxiv.org/pdf/2609.28470
published: '2026-09-22'
collected: '2026-09-27'
category: Eval
direction: 对话式AI教学效果评估与基准
tags:
- LLM
- AI Tutoring
- Evaluation
- Learning Gains
- Cost Efficiency
- StudentBench
one_liner: StudentBench平台证明AI辅导在GRE学习增益上等效于人类专家，成本低918倍
practical_value: '- 在电商/搜索推荐系统的对话式Agent评估中，借鉴统计等效性检验（而非单纯显著性差异）来验证AI方案与人工方案的效果对等，可降低上线风险。

  - 将成本效率作为核心指标：计算单位用户行为增益（如点击率提升、转化增量）的AI调用成本，对标人工运营成本，为技术选型提供量化依据。

  - 响应速度与用户互动深度正相关（论文中速度→消息数→正确练习→学习增益），推荐系统Agent应优先优化首响延迟和流式生成速度，可能直接提升用户参与度和转化。

  - 构建公开评测平台收集大规模真实用户-Agent交互数据，用于横向对比不同模型/策略，加速迭代；电商场景可搭建类似Benchmark，统一评估多Agent的推荐对话质量。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有AI研究偏重模型能力提升，缺乏对AI教学效果的系统评估，无法回答“AI能否像人类专家一样提升学习成果”这一关键问题。

**方法关键点**：提出StudentBench评测套件和公开平台，收集175,000+条学生-AI消息。在2,383名参与者中随机分组接受AI辅导、人类专家辅导或无辅导，针对GRE Quantitative和Verbal七个子领域测量学习增益；第二项研究由专家对LLM生成的教案和练习题进行2,028次两两打分，从教案规划、习题创建、对话教学法、成本和参与度五个维度区分不同AI导师。

**关键结果**：AI辅导与人类专家辅导在学习增益上统计等效（p=.015），且在七个GRE领域中有五个最佳AI导师平均超过人类导师；一个AI导师达到等效学习增益时成本仅为人类辅导的1/918（每百分点增益$0.0052 vs $4.81）；Quantitative部分中，AI回复更快→学生消息更多→正确练习更多→学习增益更大（均p<.002）。
