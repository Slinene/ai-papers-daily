---
title: 'Beyond Entropy: Correctness-Aware Advantage Shaping via Contrastive Policy
  Optimization'
title_zh: 超越熵：对比策略优化实现正确性感知优势塑造
authors:
- Weiwen Xu
- Jia Liu
- Hou Pong Chan
- Long Li
- Deng Cai
- Min Chen
- Hao Zhang
affiliations:
- The Chinese University of Hong Kong
- South China University of Technology
- Nanyang Technological University
arxiv_id: '2607.14614'
url: https://arxiv.org/abs/2607.14614
pdf_url: https://arxiv.org/pdf/2607.14614
published: '2026-07-15'
collected: '2026-07-21'
category: Training
direction: RLVR中的正确性感知优势塑造
tags:
- RLVR
- Contrastive Policy Optimization
- Advantage Shaping
- Token-level Correctness
- Entropy Alternative
- Reasoning
one_liner: 用对比分歧替代熵作为优势信号，实现RLVR中更细粒度的token级正确性感知和策略优化。
practical_value: '- 在对话推荐或搜索Agent的RLHF/RLVR训练中，使用参考策略（如预训练LLM）与当前策略的token级分布对比分歧，替代熵来构造优势，可更精细地区分哪些token导致错误，从而提升训练效率。

  - 处理推荐或问答任务中常见的“全对/全错”组（zero-advantage组）时，对比分歧可提供内部差异信号，避免训练数据浪费，尤其适用于二元成功反馈的场景。

  - 利用正确与错误响应自然引导利用与探索的思想，可设计在线学习策略：对高奖励样本偏向利用（低温度），对失败样本增加探索（高温度或对比分歧驱动的扰动），平衡推荐Agent的短期准确率和长期多样性。

  - On-policy蒸馏的视角为生成式推荐模型的知识蒸馏提供新思路：可将外部教师（如精排模型）的输出作为后验分布，用对比分歧对齐学生策略，提升列表生成任务的逐token优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统RLVR（如GRPO）使用熵进行优势塑造，但熵无法区分“有用不确定性”与“有害困惑”，导致无法准确识别token级正确性，且在全正确/全错误的组中产生零优势问题，浪费训练数据。

**方法**：提出对比策略优化（CPO），通过对比参考引导分布与普通生成分布之间的token级分歧，构建正确性感知的优势信号。理论证明该分歧是token级正确性的可靠指标。CPO将On-policy蒸馏统一为特例（此时后验分布由外部教师提供），并自然解决零优势问题。

**结果**：在数学推理和编程等域内/域外基准上，CPO显著优于基于熵的方法，同时保持强泛化性。分析显示，正确响应天然支持利用，错误响应支持探索，平衡两者可达到最优性能。
