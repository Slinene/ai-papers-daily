---
title: 'It Takes Two: Complementary Self-Distillation for Contextual Integrity in
  LLMs'
title_zh: 互补自蒸馏：让 LLM 兼顾任务效用与上下文隐私完整性
authors:
- Sangwoo Park
- Woongyeong Yeo
- Seanie Lee
- Yumin Choi
- Hyomin Lee
- Kangsan Kim
- Jinheon Baek
- Seong Joon Oh
- Sung Ju Hwang
affiliations:
- KAIST
- DeepAuto.ai
arxiv_id: '2605.20258'
url: https://arxiv.org/abs/2605.20258
pdf_url: https://arxiv.org/pdf/2605.20258
published: '2026-05-17'
collected: '2026-05-21'
category: Agent
direction: LLM Agent 隐私对齐 · 互补自蒸馏
tags:
- Contextual Integrity
- Self-Distillation
- Product-of-Experts
- Privacy Alignment
- LLM Agents
- Reverse KL Divergence
one_liner: 提出 SELFCI 互补自蒸馏框架，用双教师乘积专家目标解耦隐私保护与任务效用，无需外部监督。
practical_value: '- **解耦多目标优化**：将隐私和效用分为两个独立教师信号，各自用逆 KL 散度逼近，最后通过乘积专家（PoE）组合目标，避免单一奖励信号冲突，可直接用于电商推荐中同时优化准确性、多样性、隐私等多目标。

  - **无需外部标注的自蒸馏**：完全基于模型自身反馈生成教师分布，省去昂贵人工标注，适合快速迭代；在隐私合规检查场景（如智能客服处理用户敏感信息）可快速部署尝试。

  - **乘积专家集成方式**：将两个甚至多个专家分布相乘得到对齐目标，提供了一种灵活的多目标集成方法，可推广到生成式推荐中组合协同过滤与内容过滤需求。

  - **验证了 Agent 工作流泛化性**：在涉及多步交互和累积隐私上下文的 Agent 场景中效果稳定，表明该方法可迁移到电商对话代理的长期隐私管理，如用户多轮对话中分层次披露地址、购买记录等。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM 作为个人代理处理敏感信息时，需遵循上下文完整性（CI）决定信息是否公开。现有模型隐私决策不可靠，且现有缓解方法常损害任务性能，面临隐私-效用权衡困境。

**方法**：提出 SELFCI，一种互补自蒸馏框架。核心是将任务效用与隐私披露解耦为两个独立的教师分布——效用教师鼓励保留任务相关信息，隐私教师强制最小化不必要披露。通过让训练策略同时最小化与这两个教师分布的逆 KL 散度，等价于匹配两个教师分布的乘积专家（PoE）目标，从而对齐隐私规范与能力需求。整个框架仅依赖模型自身反馈，无需外部昂贵监督。

**关键结果**：在上下文隐私基准上，SELFCI 在隐私合规率与任务性能上均显著优于在线强化学习（如 GRPO）等基线，打破了隐私-效用权衡。在涉及 Agent 工作流和累积隐私上下文的分布外场景中同样表现良好，表明方法具有实用泛化性。
