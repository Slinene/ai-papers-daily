---
title: 'AutoRubric-T2I: Robust Rule-Based Reward Model for Text-to-Image Alignment'
title_zh: AutoRubric-T2I：基于自动规则学习的可解释 T2I 奖励模型
authors:
- Kuei-Chun Kao
- Daixuan Huo
- Yuanhao Ban
- Cho-Jui Hsieh
affiliations:
- University of California, Los Angeles
- Arena
arxiv_id: '2605.17602'
url: https://arxiv.org/abs/2605.17602
pdf_url: https://arxiv.org/pdf/2605.17602
published: '2026-05-19'
collected: '2026-05-23'
category: Multimodal
direction: 自动规则学习构建可解释 VLM 奖励模型
tags:
- Reward Model
- VLM Judge
- Rule Learning
- Preference Alignment
- Interpretability
- RLHF
one_liner: 自动从少量偏好对合成判别规则构建 VLM 法官，仅用 0.01% 标注数据超越强基线
practical_value: '- 用极少偏好对（<0.01% 标注数据）自动合成评估规则，结合 L1 正则化逻辑回归筛选 Top 判别规则，大幅降低奖励模型训练成本，可用于电商多模态评估（如商品图与描述的对齐检测）。

  - VLM 法官通过显式 rubrics 打分，提供细粒度、可解释的奖励信号，适合需审计和调试的生成式推荐场景（例如解释为什么某张生成商品图更符合描述）。

  - 框架可泛化：用 LLM 从用户反馈中自动提取评估维度，再通过特征选择保留关键维度，在推荐系统中构建可解释的用户偏好奖励模型。

  - ℓ1-Regularized Logistic Regression Refiner 作为通用的特征选择 trick，可迁移到任何需要从大量候选指标中筛选最有区分力维度的任务（例如从评论关键词中提取影响点击/转化的核心因子）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 T2I 奖励模型多基于 Bradley-Terry 对大规模人类偏好数据训练，成本高、难适应且不透明；VLM 法官虽可用文本规则提供细粒度评估，但手工设计的规则难以可靠反映人类偏好。  
**方法**：提出 AutoRubric-T2I，首个自动规则学习框架。流程分三步：(1) 从少量偏好对中由 VLM 生成推理轨迹并提炼候选规则；(2) 用同一 VLM 法官在每条规则下对成对图像打分，得到规则级分数差作为特征；(3) 用 ℓ1 正则化逻辑回归筛选出 Top-N 最具判别力的规则，构成最终可解释奖励信号。  
**结果**：仅使用不到 0.01% 的标注偏好数据，在 MMRB2 图像奖励基准上超越强基线；将奖励用于 Flow-GRPO 强化学习时，在 TIIF 和 UniGenBench++ 上提升扩散模型生成质量，优于标量奖励模型。
