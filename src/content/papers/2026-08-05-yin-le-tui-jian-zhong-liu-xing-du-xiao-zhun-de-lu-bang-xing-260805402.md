---
title: 'Robustness and User-Perceived Value of Popularity Calibration in Music Recommendation:
  A User Study'
title_zh: 音乐推荐中流行度校准的鲁棒性与用户感知价值：用户研究
authors:
- Oleg Lesota
- Gustavo Escobedo
- Bruce Ferwerda
- Simone Kopeinik
- Dominik Kowald
- Elisabeth Lex
- Markus Schedl
affiliations:
- Johannes Kepler University Linz
- Jönköping University
- Know-Center GmbH
- University of Graz
- Graz University of Technology
arxiv_id: '2608.05402'
url: https://arxiv.org/abs/2608.05402
pdf_url: https://arxiv.org/pdf/2608.05402
published: '2026-08-05'
collected: '2026-08-09'
category: RecSys
direction: 流行度校准的用户感知与鲁棒性
tags:
- popularity calibration
- user study
- music recommendation
- JSD
- robustness
- item familiarity
one_liner: 用户能感知推荐列表的流行度差异，但并不明显偏好校准列表，离线流行度校准指标与用户感知弱相关
practical_value: '- **电商推荐中慎用流行度校准**：用户并不能明确感知或偏好流行度分布匹配其历史消费的列表，单纯优化离线校准指标（如JSD）可能无法提升体验，反而浪费资源。

  - **评估离线指标的鲁棒性边界**：研究发现JSD与用户感知流行的关联受物品熟悉度、列表组成和历史长度影响，业务中若依赖此类指标，需验证其在用户历史稀疏、新老客差异等场景下的稳定性。

  - **熟悉度是调节变量**：用户对热门/冷门物品的感知受自身熟悉度制约，推荐系统可考虑在流行度调控中引入用户熟悉度信号，避免“冷门”推荐被误判为低质。

  - **计算流行度 ≠ 用户眼中的流行度**：平台计算的流行度标签与用户的主观判断存在弱对齐，在需要用户感知流行的场景（如解释、打标）中，应结合用户研究校准流行度定义。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：现有研究多通过离线指标评估流行度校准，假设用户偏好与其历史消费分布一致的推荐。但相关的用户研究有限，且校准与用户体验的关系并不明确，尤其在不同物品熟悉度和用户历史完整性下，校准指标的鲁棒性未知。

**方法**：基于用户近期听歌记录构造个性化曲目列表，利用受控朴素推荐器生成三种流行度组成：高流行度为主、低流行度为主和校准列表。通过用户实验，考察用户能否感知列表流行度差异、是否偏好校准列表，并分析JSD流行度校准指标与用户感知关系在不同熟悉度和历史可用性下的鲁棒性，以及计算流行度标签与用户主观判断的一致性。

**关键结果**：用户能感知列表间的流行度差异，但并未明确偏好校准列表。JSD与感知流行度的关联受物品熟悉度、列表组成和历史长度显著影响；计算流行度标签与用户判断仅呈弱相关。这表明离线校准指标与用户实际感知存在脱节，流行度校准作为一种用户中心个性化的假设需要更审慎的审视。
