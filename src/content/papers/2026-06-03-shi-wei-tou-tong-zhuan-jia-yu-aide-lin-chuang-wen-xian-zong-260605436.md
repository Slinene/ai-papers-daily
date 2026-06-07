---
title: 'Ten Headache Specialists versus Artificial Intelligence for Clinical Literature
  Summarization: A Critical Evaluation and Comparison'
title_zh: 十位头痛专家与AI的临床文献总结评估与比较
authors:
- Alejandro Lozano
- Keiko Ihara
- Ping-Hao Yang
- Carrie E. Robertson
- Jennifer Stern
- Allan Purdy
- Hsiangkuo Yuan
- Pengfei Zhang
- Yulia Orlova
- Olga Fermo
affiliations:
- Stanford University
- Mayo Clinic
- Harvard Medical School
- Thomas Jefferson University
- Dalhousie University
arxiv_id: '2606.05436'
url: https://arxiv.org/abs/2606.05436
pdf_url: https://arxiv.org/pdf/2606.05436
published: '2026-06-03'
collected: '2026-06-07'
category: RAG
direction: 临床RAG Agent与人类总结的盲评对比
tags:
- RAG
- Agentic AI
- Clinical Summarization
- Expert Evaluation
- LLM
- Blinded Study
one_liner: 专家盲评对比RAG Agent与人类专家撰写的临床总结，发现专家总结仍占优但人机区分困难。
practical_value: '- **Agentic RAG pipeline 可复用**：论文构建的 RAG agentic 框架（检索+生成+工具调用）可直接迁移到电商场景，用于自动化生成商品优缺点总结、用户评论摘要、竞品分析报告，降低人工撰写成本。

  - **多维专家评估方法**：采用正确性、完整性、简洁性和临床实用性四维评分+偏好排序+人机辨别实验，这套评估体系可移植到推荐系统生成的推荐理由、搜索摘要、营销文案的质量评测上，尤其适合需专业领域知识的场景。

  - **人类与AI生成内容的区分度洞察**：专家难以可靠识别人机来源，提示在部署AI生成的用户界面文本时，可无需刻意标注机器生成；但必要时应加入可解释性信号（如引用来源）以增强信任。

  - **专家偏好的特征提炼**：研究识别出专家看重的关键特征（如证据权重、语境适配），可指导提示工程和微调目标，优化电商推荐中的自然语言生成，使其更贴近人工撰写的高质量内容。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：临床医生需快速总结医学文献指导决策，但文献量激增、时间不足。RAG增强LLM虽显示潜力，却缺乏与人类专家在广泛文献合成任务上的直接对比与严谨盲评。  
**方法**：构建一个RAG-based agentic AI框架，采用Sonnet、GPT-4o、Llama 3.1三种LLM。一位头痛专家设计13个临床问题（3个用于提示优化，10个正式评估）。10位头痛专家各自撰写一份总结，与三种LLM生成的总结混合，得到每道题四份总结。专家们盲评（排除自己撰写的题目），在1-10分标度上对正确性、完整性、简洁性和临床实用性打分，并给出偏好排名，同时判断该总结来自专家还是AI。  
**关键结果**：专家撰写的总结在四个维度上总体得分略高于AI，但在统计上优势并不压倒性；偏好排名中专家总结多数领先，但AI紧随其后。人机辨别准确率接近随机水平，专家常无法可靠区分来源。研究表明，当前RAG Agent接近人类总结水平，但在少数关键特征（如证据引用精准性）上仍有差距。
