---
title: Optimal Sequential Annotations for Off-Policy Evaluation
title_zh: 离线策略评估中序列标注预算的最优分配方法
authors:
- Woojin Chae
- Ezinne Nwankwo
- Haitong Qin
- Angela Zhou
affiliations:
- University of Southern California
- University of California, Berkeley
- University of Washington, Seattle
arxiv_id: '2609.26707'
url: https://arxiv.org/abs/2609.26707
pdf_url: https://arxiv.org/pdf/2609.26707
published: '2026-09-22'
collected: '2026-09-23'
category: Eval
direction: 离线策略评估 · 标注预算优化
tags:
- Off-Policy Evaluation
- Doubly Robust
- Annotation Budget
- Active Learning
- Sequential Decision Making
- Variance Reduction
one_liner: 在离线评估中，用有限标注预算优化序列标注概率以最小化方差，结合双重稳健处理缺失标签
practical_value: '- 在电商搜索推荐场景中，构建离线评估集时往往需要人工标注或付费获取真实点击/转化数据。该方法提供了一种方差最优的标注采样策略：根据样本对评估方差的影响程度分配标注预算，而不是随机采样，可以在相同预算下显著降低策略价值估计的
  RMSE（论文中降低 34-68%）。

  - 面对 LLM-as-a-judge 存在的未知偏差，可采用论文中的双重稳健 OPE 框架：将 LLM 标注作为缺失奖励的插补模型，结合少量专家标注进行校正，既降低成本又控制偏差。

  - 序列推荐/会话评估中，论文提出的前向单调标注协议很有借鉴意义：只标注序列中当前及之后的关键状态点，避免回溯标注成本过高，适合在线动态标注场景。

  - 批量自适应实现思路可迁移：在推荐系统 A/B 测试模拟中，先基于历史数据估计每个 context 的潜在方差，再动态调整后续批次的标注概率，逐步逼近最优分配，工程上容易落地。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**
离线强化学习与策略评估依赖历史数据中的状态和奖励信息。在 AI 应用中，状态/奖励常以复杂文本或图像形式存在，LLM-as-a-judge 可以低成本标注但存在未知偏差，而专家标注昂贵。如何在有限标注预算下获得可靠的策略价值估计成为关键问题。

**方法关键点**
将标注预算分配问题形式化为方差最优的序列标注概率设计。采用双重稳健 (doubly-robust) OPE 处理缺失奖励，结合插补模型和倾向权重，保证在模型误设时仍有一致性。针对序列前向单调标注协议（即只能按时间顺序标注，不能回溯）推导出最优标注概率的解析特征，并给出可行的批量自适应实现：根据历史数据估计方差相关量，动态更新后续批次的标注概率。

**关键结果数字**
在仿真和两个真实数据集上验证：无家可归者服务案例笔记数据中，住房安置 RMSE 降低 34-65%，住房申请进展 RMSE 降低 17-68%；在 LMArena 人类偏好投票数据上，所有预算水平 RMSE 降低 55-62%。
