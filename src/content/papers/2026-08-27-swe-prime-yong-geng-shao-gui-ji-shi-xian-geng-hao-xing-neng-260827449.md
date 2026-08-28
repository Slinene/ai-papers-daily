---
title: 'SWE-Prime: Fewer Trajectories, Better Performance'
title_zh: SWE-Prime：用更少轨迹实现更好性能
authors:
- Dewu Zheng
- Ruizhe Ye
- Yanlin Wang
- Yang Ye
- Hongyu Zhang
- Ensheng Shi
- Xilin Liu
- Yuchi Ma
- Jianxing Yu
- Zibin Zheng
affiliations:
- Sun Yat-sen University
- Huawei Cloud Computing Technologies Co., Ltd.
- Chongqing University
arxiv_id: '2608.27449'
url: https://arxiv.org/abs/2608.27449
pdf_url: https://arxiv.org/pdf/2608.27449
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: 轨迹数据筛选与分段SFT
tags:
- SFT
- data selection
- trajectory filtering
- coding agent
- SWE-Bench
- segment-level loss
one_liner: 提出多粒度两阶段SFT数据筛选，轨迹级选10%高质量子集并片段级屏蔽损失，训练效果超全量数据
practical_value: '- 在电商导购/售后 Agent 的轨迹 SFT 中，可直接借鉴“成功轨迹 ≠ 优质监督”的假设：先按结果质量、过程质量、代表性筛掉含无效操作或高风险步骤的样本，再用小比例高质数据做
  SFT，实验显示 10% 数据可超越全量；适合业务上语料噪声大、训练成本敏感的场景。

  - 分段级 loss masking 很实用：保留完整轨迹作为上下文，但只让“对最终成交/解决方案有正向贡献、可学习且低风险”的 segment 参与梯度回传，能避免模型模仿冗余点击、重复搜索或危险操作。

  - 三段评估指标可迁移：贡献度（是否影响最终结果）、可学习性（Agent 能否从该步骤归纳出策略）、风险（是否会放大幻觉/违规动作）可作为构建推荐/搜索 Agent
  轨迹语料的自动过滤信号。

  - 若是多步商品推荐/搜索召回 Agent，可按语义将轨迹切分为意图识别、query改写、候选筛选、解释推荐等片段，复用其片段级数据选择框架，只优化关键决策段。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM 解决真实软件问题常依赖大规模 Agent 轨迹 SFT，但任务成功不等于监督质量高：成功轨迹仍可能包含无效、冗余或有风险的步骤。直接使用这些轨迹做 SFT 会引入噪声监督，让模型模仿不良的问题解决行为。

**方法关键点**：SWE-Prime 提出多粒度、两阶段数据筛选。第一阶段在轨迹级基于过程质量、结果质量、数据代表性进行筛选，从成功轨迹中选出高质量且有代表性的约 10% 子集。第二阶段在片段级选择：将连续步骤分组为语义片段，评估每个片段对最终方案的贡献、可学习性和潜在风险；SFT 时保留所有片段以维持上下文，但只对选中片段计算 loss。

**关键结果数字**：在 SWE-Bench Pro 和 SWE-Bench Verified 上，仅用 SWE-Prime 选择的 10% 轨迹子集训练，就超过全量 resolved 数据集训练效果，相对性能增益最高分别达 12.2% 和 24.2%。
