---
title: 'How Reward Gain Imbalance Shapes Ranking: Rethinking Rubric-Based Reward Aggregation'
title_zh: 奖励增益不平衡如何影响排序：重思评分标准型奖励聚合
authors:
- Zhengyuan Fan
- Zhonghua Wu
- Tianyu Cheng
- Qun Chen
affiliations:
- School of Computer Science, Northwestern Polytechnical University
arxiv_id: '2611.24005'
url: https://arxiv.org/abs/2611.24005
pdf_url: https://arxiv.org/pdf/2611.24005
published: '2026-11-18'
collected: '2026-11-19'
category: Training
direction: LLM RL 奖励聚合优化
tags:
- reward aggregation
- rubric-based RL
- GRPO
- ranking
- LLM alignment
- reward gain imbalance
one_liner: 提出自适应 Dual-Center Clipping 聚合，约束每个准则对奖励差的上界，缓解奖励增益不平衡，提升排序与 GRPO 训练效果
practical_value: '- 业务中用 LLM 做多维度 rubric 打分（如相关性、多样性、商业价值、文案质量）并线性加和时，先计算各维度的 reward
  gain（满足/不满足样本期望分差），识别增益极度失衡的维度；不要简单移除或标准化，否则可能丢失有用信号，可采用 DCC 式裁剪：基于当前候选集动态设置各维度分差贡献上限。

  - DCC 仅依赖当前 batch/rollout 组分数分布，无额外权重学习，适合在线策略优化（如 GRPO）；若业务有生成-排序-反馈闭环，可直接在每个 rollout
  组内重估裁剪区间，降低工程复杂度。

  - 对推荐/搜索中 LLM judge 打分排序场景，多个评估准则得分分布不一致会扭曲 item/candidate 排名；可借鉴其排序分解思路诊断错排样本：把两候选
  reward 差拆成基础信号 + 不平衡项 + 残差，定位是哪一项导致误判，再决定是否对某些准则做裁切或重标定。

  - DCC 的裁剪上界针对候选组内分差而非原始分，保留连续评分信息、避免简单截断导致的排序收缩；在实现业务 judge 聚合时，可把“限制分差贡献”作为比“截断绝对值”更温和的正则。'
score: 7
source: arxiv-stat.ML
depth: abstract
---

**动机**：在基于评分标准的强化学习中，常将多个准则得分等权聚合，但不同准则评分分布差异（奖励增益不平衡）会扭曲候选排序。以往工作改进评判器、学习权重或聚合方式，但对不平衡与排序的交互缺乏理解。

**方法关键点**：将评分异质性形式化为奖励增益不平衡，即每个准则满足与不满足响应期望得分之差。实验发现即使使用真实标签，消除不平衡反而降低排序准确率。推导任意两候选奖励差的精确分解：基础满意度信号、奖励增益不平衡项、残差项，不平衡可减弱或放大基础信号，错排常集中在减弱处。据此提出自适应 Dual-Center Clipping 聚合（DCC）：仅用当前候选组得分确定裁剪区间，对所有准则间候选得分差施加共同上界，限制极端分数影响同时保留连续判断信息；此区间对每个 rollout 组在线重估，适合 GRPO 训练。

**关键结果**：在多个基准上，DCC 在全部排序指标中优于对比方法，并在作为 GRPO 奖励时取得最佳 WritingBench 分。
