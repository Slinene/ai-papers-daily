---
title: 'Better Supervision Is Nearby: Neighborhood On-Policy Self-Distillation'
title_zh: 更好的监督在邻近：邻域在线策略自蒸馏
authors:
- Xincheng Wei
- Yifan Ding
- Yoshua Li
- Yuquan Lu
- Ziheng Li
- Yi Lu
- Dongsheng Ma
- Rongxiang Weng
- Xunliang Cai
affiliations:
- The Chinese University of Hong Kong, Shenzhen
- Meituan, LongCat Team
- Peking University
- University of Toronto
arxiv_id: '2609.39687'
url: https://arxiv.org/abs/2609.39687
pdf_url: https://arxiv.org/pdf/2609.39687
published: '2026-09-29'
collected: '2026-10-03'
category: Training
direction: LLM 推理训练 · 自蒸馏
tags:
- On-Policy Self-Distillation
- Neighborhood OPSD
- Expert Pool
- LLM Reasoning
- Knowledge Distillation
one_liner: 用局部参数扰动构建专家池并按状态路由，为在线自蒸馏提供更优监督，平均提升 1.67~2.75 点
practical_value: '- 训练电商/Agent 场景下的 LLM 推理型任务（query 改写、推荐解释、工具调用规划）时，可借鉴 N-OPSD：保留多个邻近参数的冻结专家，按状态路由提供多样但参考对齐的监督，避免单一
  teacher 覆盖不足。

  - 离线专家池构建的贪心选择准则（filtered reference-token gains 超过池当前最佳）可作为通用监督选择指标：只保留能在不同前缀位置提供增量校正的专家，压缩池规模、降低训练成本。

  - 路由时分离 anchor direction 与 support level（MaxPeak 选 token，quantile 选专家）值得借鉴到多策略/多专家生成式推荐：不要只选置信度最高（highest
  peak）的策略，而要选 top token 一致且分布支撑更稳的专家作为训练目标。

  - 用 clipped forward-KL 从专家完整 next-token 分布学习，比只学 hard label 更平滑，适合生成式推荐中 Semantic
  ID 或多 token 决策序列的蒸馏；推理只部署学生，不增加线上成本。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：标准 OPSD 在数学推理训练中固定使用单一参数设置的特权教师，忽略邻近参数可能带来的额外监督。本文发现局部参数扰动能在同一参考上下文中产生互补的、与参考对齐的校正，不同专家在不同参考位置提供校正，池化后覆盖更广。

方法关键点：N-OPSD 离线阶段用贪心选择构建紧凑的冻结专家池，奖励过滤后的参考 token 增益超过池当前最佳的位置；在线路由把 anchor 方向与支撑程度解耦——MaxPeak 选 anchor token，quantile 选择从 top token 匹配的专家中挑一个；学生用 clipped forward-KL 学习该专家完整 next-token 分布。

结果：在 AIME 2024、AIME 2025、HMMT Feb 2025 上，三个 benchmark Average@12 比 OPSD 提升 2.75/1.67/1.94 点，分别对应 Qwen3-1.7B/4B/8B；student-prefix continuations 验证池可泛化到选择时未见的参考轨迹外；推理仅用学生。
