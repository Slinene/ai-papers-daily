---
title: 'PrivacyAlign: Contextual Privacy Alignment for LLM Agents'
title_zh: PrivacyAlign：LLM Agent 的情境化隐私对齐
authors:
- Manveer Singh Tamber
- Abhay Puri
- Marc-Etienne Brunet
- Perouz Taslakian
- Jimmy Lin
- Spandana Gella
affiliations:
- University of Waterloo
- ServiceNow AI Research
- McGill University
- Mila – Quebec AI Institute
arxiv_id: '2606.21710'
url: https://arxiv.org/abs/2606.21710
pdf_url: https://arxiv.org/pdf/2606.21710
published: '2026-06-19'
collected: '2026-06-23'
category: Agent
direction: Agent 情境隐私对齐与人类规范对齐
tags:
- Privacy
- LLM Agents
- Human Alignment
- Reward Modeling
- Contextual Privacy
- Annotation-Conditioned
one_liner: 引入PrivacyAlign数据集和注释条件奖励建模，训练的小型开源Agent更符合人类隐私规范
practical_value: '- 在电商Agent中防止泄露用户订单、地址等私密信息，可复刻该数据集的构建方法：收集实际泄露场景，进行多轮人工标注（包含解释），用于对齐训练与评测。

  - 注释条件奖励建模：利用人类标注（标签+解释）为响应生成细粒度奖励，用于强化学习训练，可迁移到生成式推荐等任务中，避免模型输出敏感用户偏好。

  - 用LLM裁判评估隐私行为时，通过条件化人类标注和解释作参考，能提高裁判的可靠性，这一技巧可直接嵌入业务自建的隐私评估流水线。

  - 小模型（如Llama-3-8B）经过隐私对齐训练后，能在不牺牲通用能力下大幅提升隐私保护，证明业务场景可用较小自有模型微调实现合规。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**
AI Agent 在代表用户行动时，可能因访问邮件、日历、记忆等数据而泄露隐私，现有隐私对齐依赖规则等不可靠代理，缺乏基于人类判断的训练与评测。该工作直接以人类标注为中心构建隐私对齐。

**方法**
首先构建PrivacyAlign数据集：1,350个样本、3,516条详细标注，来自599名标注者，覆盖LLM真实泄露场景。标注包含二元隐私判断、严重性评分及解释。在此基础上，提出两种利用标注的方法：(1) 在评议时，将同一提示的人工标注和解释作为LLM裁判的条件，提升其判断可靠性；(2) 注释条件奖励建模：利用人工标注为Agent响应生成奖励信号，在强化学习（RL）中训练Agent，使响应与人类隐私规范对齐。

**结果**
用该奖励训练的小型开源Agent（如Llama-3-8B）在PrivacyAlign测试集上显著优于未对齐模型，并在现有Agent隐私基准TrustVQA、DPA-PQA等取得强增益，同时通用能力保持稳定。
