---
title: 'Dialogue to Detection: A Multimodal Hybrid NLP Pipeline for Insurance Fraud
  Detection'
title_zh: 对话到检测：面向保险欺诈检测的多模态混合NLP流水线
authors:
- Muhammad Shakeel Akram
- Amal Htait
- Abdul Hamid Sadka
- Emma Meisingseth
- Karishma Jaitly
affiliations:
- Aston University
- Domestic & General
arxiv_id: '2606.28002'
url: https://arxiv.org/abs/2606.28002
pdf_url: https://arxiv.org/pdf/2606.28002
published: '2026-06-26'
collected: '2026-06-29'
category: Other
direction: 多模态融合 · 规则基评分
tags:
- synthetic data
- multimodal fraud detection
- LLM-RAG
- voice clustering
- rule-based scoring
one_liner: 合成多模态框架融合语音与文本，用规则风险评分检测叙事复用与声音重复以增强可解释欺诈检测
practical_value: '- 借鉴LLM-RAG检索重复叙事和相似案例的方法，可用于客服质检、反欺诈或用户投诉分析中的异常话术识别。

  - 规则基风险评分可解释性强，适合风控场景，可将NLP特征、声纹相似度等异构信号通过业务规则融合打分，降低误报。

  - 合成数据生成思路（模拟双人对话生成文本+音频）可用于构造训练数据，解决隐私和样本不均衡问题，支持冷启动。

  - 多模态特征（文本NER、正则特征 + 声纹聚类）的工程化组合可迁移到智能质检、投诉处理等场景，实现跨模态一致性校验。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：保险欺诈年损失超3000亿美元，从首次损失通知（FNOL）的对话中早期检测至关重要，但现有研究多限于私有文本数据集，忽略语音、行为等模态。本文旨在提供一个可复现的多模态基线，结合话语、结构和说话人声纹线索。

**方法**：设计合成多模态框架，首先生成代理-客户对话文本及双人音频，然后应用ASR和说话人分离。下游检测流水线集成：①基于NER和正则的特征提取（如时间、金额、地点的一致性）；②LLM-RAG以检索历史案例，检测跨案例的叙事复用；③说话人嵌入向量聚类，识别同一声音在不同案例中的出现。最终通过一个可解释的规则基风险评分引擎，融合上述信号输出欺诈风险分数，平衡敏感性和误报率。

**结果**：数据集验证及组件级评估表明，各模块（ASR、NER、RAG检索、声纹聚类）在合成数据上表现稳定，提供超越纯文本方法的可迁移基线，展示了多模态辅助欺诈检测的可行性。
