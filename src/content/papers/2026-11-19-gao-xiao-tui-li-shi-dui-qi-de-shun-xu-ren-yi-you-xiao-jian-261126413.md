---
title: Sequential Anytime Valid Tests for Efficient Inference-Time Alignment
title_zh: 高效推理时对齐的顺序任意有效检验
authors:
- Vishesh Kumar Singh
- Sayak Ray Chowdhury
affiliations:
- Indian Institute of Technology Kanpur
arxiv_id: '2611.26413'
url: https://arxiv.org/abs/2611.26413
pdf_url: https://arxiv.org/pdf/2611.26413
published: '2026-11-19'
collected: '2026-11-20'
category: LLM
direction: LLM 推理时对齐 · 自适应停止
tags:
- Inference-Time Alignment
- Anytime-Valid Test
- Best-of-N
- Reward-Weighted Self-Consistency
- Sequential Testing
- e-Process
one_liner: 提出e-RWSC自适应停止规则，为LLM推理时对齐提供统计错误保证并降低token成本
practical_value: '- 在LLM推理时对齐场景（产品文案生成、对话回复、Agent决策候选筛选），可用e-RWSC替代固定Best-of-N，让简单prompt提前停止，复杂prompt动态增加采样，平均节省token成本。

  - e-RWSC对认证错误提供概率保证，适合生产环境中的可靠性要求，避免启发式阈值带来的不可控风险。

  - 奖励加权自一致性(RWSC)思想可借鉴：对候选答案按最终内容聚类，用奖励模型加权投票，能更有效地利用奖励信号，可迁移到生成式推荐中对候选item的评估与筛选。

  - 工程实现上需为每个答案维护e-process统计量，计算开销低，易于集成到现有推理管线；但要求答案空间可聚类且奖励模型准确，否则可能影响认证效率。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：推理时对齐方法如Best-of-N为每个prompt固定生成N个候选并用奖励模型筛选，但不同prompt所需计算量差异大，统一预算造成浪费。现有自适应停止方法基于启发式阈值，无统计错误控制。

**方法关键点**：
- 将候选按最终答案聚类，用奖励加权自一致性(RWSC)分数衡量各答案的支持强度。
- 将停止决策视为对簇的顺序检验。直接应用Wald的SPRT（SPRT-RWSC）虽有效，但保证失效，因为领先答案会随采样漂移且测试被持续监控。
- 主要贡献e-RWSC：为策略产生的每个答案维护一个betting supermartingale（e-process），保证任何时候认证非主导答案的概率≤α，且在持续监控下统一有效。RWSC分数驱动下注，只影响主导答案a*被认证的速度，不影响有效性。
- 理论复杂度：认证所需样本数 O(log(1/α)/d_KL(θ_a* || 1/2))。

**关键结果**：在多个语言模型、数据集和奖励模型上验证了成本随1/d_KL伸缩，准确率优于基线，且token成本大幅降低。
