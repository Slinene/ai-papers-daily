---
title: 'Beyond Borrowed Histories: Person-Aligned User Simulation for Interactive
  Role-Playing Evaluation'
title_zh: 超越借用历史：面向交互式角色扮演评估的个性化用户模拟
authors:
- Yuhang Zhu
- Mingxuan Du
- Benfeng Xu
- Jie Gao
- Lingyun Yu
- Hongtao Xie
affiliations:
- University of Science and Technology of China
- MetaStone Technology, Beijing, China
arxiv_id: '2607.27816'
url: https://arxiv.org/abs/2607.27816
pdf_url: https://arxiv.org/pdf/2607.27816
published: '2026-07-29'
collected: '2026-08-01'
category: Eval
direction: 角色扮演代理评估 · 用户模拟器
tags:
- role-playing agent
- user simulator
- personalized rubric
- multi-turn conversation
- evaluation
- LLM
one_liner: 提出基于用户模拟器的个性化评估框架，解决现有基准使用固定对话史和通用评分的问题
practical_value: '- 用户模拟器可复用到对话推荐或搜索系统的离线评估中，针对不同用户画像生成个性化交互会话，模拟真实用户行为。

  - 个性化评分标准的思想可迁移至推荐满意度预测，训练用户特定的评估模型，比单一评分更准确衡量个体体验。

  - 多轮会话级别的评估范式适用于对话式推荐、客服Agent等长交互场景，突破单轮评估局限，捕捉长期交互质量。

  - 生成可解释的用户-系统对级评估报告，帮助分析细分用户群的体验差异，指导业务进行针对性优化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有角色扮演代理(RPA)评估要求系统续写固定对话历史，并用脱离用户的通用评分标准评价。这种设计忽视了两点：(1) 输出受给定历史影响，无法科学反映真实多轮交互能力；(2) 用户满意度存在个体差异，通用标准与真实感受不一致。

**方法关键点**：提出PALATE，一个基于用户模拟器的可伸缩评估基准。首先收集300个角色画像，训练五个用户模拟器代表不同用户类型；然后让模拟器与候选RPA在固定角色集上进行自由形式多轮对话。评估时，除通用质量评分外，还为每个用户构建个性化评分标准（通过采集用户偏好数据训练）。在留出测试集上，个性化标准比通用标准更接近人类判断。主评估涵盖16个候选系统，从三个维度剖析：通用轮次质量、长期会话能力，以及每个用户的具体体验，最终输出可解释的用户-RPA对级评估，而非单一排名。

**关键结果**：个性化评分标准与人类判断的一致性显著高于通用标准；PALATE揭示了不同系统在不同用户群上的表现分化，提供了更细粒度的诊断信息。
