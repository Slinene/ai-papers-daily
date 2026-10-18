---
title: Training Reasoning Models to Generate Diverse Scientific Ideas
title_zh: 训练推理模型生成多样化科学创意
authors:
- Manya Wadhwa
- Pranav Narayanan Venkit
- Hiroaki Hayashi
- Yu Li
- Tuhin Chakrabarty
- Chien-Sheng Wu
affiliations:
- New York University
- Stony Brook University
- Salesforce AI Research
arxiv_id: '2610.22324'
url: https://arxiv.org/abs/2610.22324
pdf_url: https://arxiv.org/pdf/2610.22324
published: '2026-10-15'
collected: '2026-10-18'
category: Training
direction: LLM 创意生成 · 集合级 RL 多样性
tags:
- Set-level RL
- Diverse Generation
- Idea Generation
- LLM Training
- Grounding
one_liner: 用集合级强化学习奖励多样性，训练 8B 模型一次生成 K 张高质量且互异的科学创意卡
practical_value: '- **生成多个候选时用距离加权奖励**：在推荐理由、广告文案、搜索 query 建议等场景，要求模型一次生成 K 个候选，并在强化学习/偏好优化中把每个候选的质量分数乘以其与已生成候选的语义距离（如
  embedding 相似度的倒数），可显著减少重复、提升集内多样性。

  - **结构化卡片输出**：让模型输出类似 idea card 的结构化 JSON（标题、卖点、理由、证据），便于后续用规则或模型做联合评分、去重与排序；电商可生成“商品卖点卡”或“用户兴趣标签卡”。

  - **集合级联合评分替代逐条采样**：在 RL/GRPO 中直接对一组 K 个候选做 group-level reward，而不是逐条独立采样打分，能更好平衡质量与覆盖，工程上可用一个
  LLM judge 或业务指标作为奖励。

  - **执行反馈作为最终验证**：借鉴用 coding agent 跑实验验证想法可执行性，在业务中可让生成内容进入仿真或小流量评测，用真实业务指标（CTR、转化）作为
  success 信号，避免只靠 LLM 自评。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**  
科研流程第一步是生成想法。现有 LLM 创意生成多关注单条质量，忽视集合多样性；而实际研究者需要在一批想法中权衡比较，单一最优想法通常不够。  

**方法关键点**  
研究文档 grounded ideation：给定多篇论文，模型一次性写 K 张结构化 idea cards，每张卡片带标题、描述、证据等。训练采用 set-level RL：不再逐条打质量分，而是对整组 K 张卡联合评分——每张卡的质量分乘以其与之前所有卡的距离权重（距离越大权重越高），使模型在生成后续想法时主动避开已有内容。这样模型学会在一个序列内保持多样性，而无需后处理去重。  

**结果**  
在 contamination-free benchmark 上，训练后的 8B 模型 creative utility（质量+多样性）超过 Claude Opus 4.8 和 GPT-6 Astra。四名专家的人类试点研究认为其集合与 Claude Opus 4.8 同样有前景，且包含略多的独特想法。用 coding agent 对想法做概念验证实验时，success@k 与 Claude Opus 4.8 相当，说明提升多样性并未牺牲可执行性。
