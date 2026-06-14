---
title: Building Social World Models with Large Language Models
title_zh: 基于大语言模型的社会世界模型构建
authors:
- Haofei Yu
- Yining Zhao
- Guanyu Lin
- Jiaxuan You
affiliations:
- University of Illinois Urbana-Champaign
- Carnegie Mellon University
arxiv_id: '2606.11482'
url: https://arxiv.org/abs/2606.11482
pdf_url: https://arxiv.org/pdf/2606.11482
published: '2026-06-09'
collected: '2026-06-14'
category: Other
direction: 社会信念动态建模 · 预测市场
tags:
- Social World Model
- LLM
- belief dynamics
- prediction markets
- state transition
one_liner: 提出社会世界模型（SWM），利用LLM从预测市场数据学习社会信念的状态转移规律
practical_value: '- **群体趋势预测的思路**：电商场景中可将商品/话题的集体兴趣视为“社会信念”，借鉴SWM框架，用搜索量、点击量等时序数据作为信念强度代理，结合事件（如大促、热点）训练状态转移模型，提前预判需求变化。

  - **低成本监督信号**：使用预测市场概率（如Polymarket）或内部平台上的“用户期望投票”作为信念标签，替代昂贵的用户调研，动态捕捉用户对商品/功能的偏好强度。

  - **LLM作为可解释时序引擎**：用LLM编码事件并学习时序上的ELBO，得到可解释的状态转移，这可以迁移到推荐系统的多步序列建模中，提供“用户状态→行为”的可视化解释。

  - **事件驱动的多智能体模拟**：Agent系统可借鉴SWM，用LLM预测其他Agent或用户的信念变化，辅助协作决策（如谈判、动态定价），但领域差异较大，需谨慎适配。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：社会信念如何随事件演变是社会科学核心难题，缺乏显式标注的信念转移数据，且大规模人口调研成本高昂。LLM具备常识与社会智能，能否模拟社会信念动态？

**方法**：提出社会世界模型（SWM），将社会信念定义为人群对某命题的集体概率估计。SWM用LLM编码事件与当前信念，学习状态转移函数，通过ELBO优化时间序列证据下界，从社会数据（如预测市场价格）中自动挖掘信念变迁模式，无需人工标注事件-信念映射。

**基准与结果**：构建SWM-Bench基准，源自真实预测市场Kalshi与Polymarket，包含政治、金融、加密货币等领域的12k+数据点。实验表明SWM显著优于TimesFM等时间序列基础模型，在Kalshi数据上达到SOTA，在Polymarket上获得竞争性能，且能提供信念转移的可解释机制。
