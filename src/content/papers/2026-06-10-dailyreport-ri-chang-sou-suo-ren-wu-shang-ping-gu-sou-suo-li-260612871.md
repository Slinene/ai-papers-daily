---
title: 'DailyReport: An Open-ended Benchmark for Evaluating Search Agents on Daily
  Search Tasks'
title_zh: DailyReport：日常搜索任务上评估搜索代理的开放式基准
authors:
- Jingxuan Han
- Wei Liu
- Mingyang Zhu
- Youpeng Wang
- Ziwen Wang
- Lin Qiu
- Xuezhi Cao
- Xunliang Cai
- Zheren Fu
- Licheng Zhang
affiliations:
- University of Science and Technology of China
- Meituan
arxiv_id: '2606.12871'
url: https://arxiv.org/abs/2606.12871
pdf_url: https://arxiv.org/pdf/2606.12871
published: '2026-06-10'
collected: '2026-06-23'
category: Agent
direction: Agent 评估基准 · 细粒度与可解释评估
tags:
- Search Agents
- Benchmark
- Evaluation
- Rubrics
- LLM
- Daily Tasks
one_liner: 构造包含150个日常搜索任务与3546条细粒度评分标准的基准，提供可解释的多维评估，揭示现有搜索代理普遍未达用户预期
practical_value: '- 任务分解与级联评分标准：借鉴其子任务分解和级联 rubric 设计，可在电商搜索/推荐代理评估中实现细粒度能力诊断（如商品推荐的准确性、解释质量、多源信息融合能力）。

  - 用户中心聚合分数：提出的用户偏好分数可作为离线代理指标，近似真实用户满意度，用于 Agent 的迭代优化或线上 A/B 测试前的快速筛选。

  - 17 个系统对比揭示的短板：时效性、多源合成等维度的普遍缺陷表明，在构建电商搜索代理时需特别强化实时信息的抓取与融合机制。

  - 数据集与任务构造思路：可从真实用户讨论中挖掘任务，构建贴合电商场景（如比价、商品咨询）的评估集，复现其评估管线。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有搜索代理基准主要针对专业任务，脱离真实用户场景，且评估粒度粗糙、可解释性差。

**方法**：提出 DailyReport，包含 150 个源自真实用户讨论的日常搜索任务，每个任务被分解为若干子任务，共配备 3,546 条细粒度评分标准（rubric），覆盖多个可解耦的评估维度（如完整性、准确性、时效性等）。通过级联归因和用户中心聚合，得到各维度高度可解释的分数以及一个综合的用户偏好分数。在 17 个代表性代理系统上进行了评测。

**结果**：当前系统普遍未能满足用户期望，尤其在需要综合多源信息和保持内容时效性的任务上表现不足。分析表明，细粒度 rubric 能有效定位系统短板，用户偏好分数与人工判断高度一致。
