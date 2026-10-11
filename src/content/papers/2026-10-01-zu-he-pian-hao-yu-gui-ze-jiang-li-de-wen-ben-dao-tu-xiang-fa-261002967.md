---
title: Post-Training Frontier Text-to-Image Models by Composing Preference and Rubric
  Rewards
title_zh: 组合偏好与规则奖励的文本到图像后训练方法
authors:
- Yuanhao Ban
- I-Hung Hsu
- Anastasios Angelopoulos
- Wei-Lin Chiang
- Ion Stoica
- Cho-Jui Hsieh
affiliations:
- Arena Intelligence Inc
- UCLA
arxiv_id: '2610.02967'
url: https://arxiv.org/abs/2610.02967
pdf_url: https://arxiv.org/pdf/2610.02967
published: '2026-10-01'
collected: '2026-10-11'
category: Training
direction: T2I 后训练奖励组合
tags:
- RLHF
- Reward Composition
- Text-to-Image
- Preference Reward
- Rubric Reward
- Post-Training
one_liner: 提出组合偏好奖励与规则奖励的 T2I 后训练策略，Flux2dev Elo 提升 69 分，Ideogram-4 达 1223.5 超开源模型
practical_value: '- **奖励组合策略可迁移到推荐/Agent 的 RL 后训练**：避免多目标简单加权平均，借鉴其组合策略（如分阶段、约束优化或优先级调度），平衡用户偏好（点击、停留）与业务规则（合规、真实性），降低单一指标被
  hack 的风险。

  - **偏好 + 规则双奖励结构**：在生成式推荐、query 改写或 Agent 输出中，可训练偏好奖励模型（基于大规模用户反馈）配合 rubric 奖励（显式检查忠实度、格式、安全），后者作为防
  reward hacking 护栏。

  - **小规模高质量奖励数据即可验证 RL 流程**：论文公开的 1K 子集能恢复部分全量训练收益，说明业务上可以先构建小规模标注奖励集跑通后训练、快速迭代，再扩展数据和模型规模。

  - **用 Elo / 在线评测追踪生成质量**：参考 Arena 的 pairwise 偏好评估，在内部对 search suggestion、文案生成等场景建立
  Elo 榜单，持续监控后训练收益与退化。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 text-to-image 模型视觉质量已很高，但后训练仍难，因为单一奖励信号无法覆盖完整人类偏好，且容易被优化利用。

**方法关键点**：奖励系统由两部分组成——偏好奖励在大规模人类偏好数据上使用 Bradley-Terry 目标训练，捕捉整体审美与感知偏好；rubric 奖励显式评估 prompt 忠实度等属性，提供防 reward hacking 的保障。针对异质奖励组合，发现 naive 加权平均会导致次优优化行为，因此提出一种简单的奖励组合策略，更有效平衡偏好优化与规则满足。

**关键结果**：在 Arena text-to-image leaderboard 上，RL 训练后的 Flux2dev Elo 比 base 模型高 69 分（1132.8 → 1202）；post-trained Ideogram-4 达到 1223.5（base 为 1204），超过所有开源模型（2026-09-04 快照）。同时发布 Arena-T2I-Training 1K 子集，可恢复部分全量训练收益。
