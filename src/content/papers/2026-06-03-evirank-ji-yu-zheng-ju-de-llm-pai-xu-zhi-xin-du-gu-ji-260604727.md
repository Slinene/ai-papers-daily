---
title: 'EviRank: Evidence-Based Confidence Estimation for LLM-Based Ranking'
title_zh: EviRank：基于证据的 LLM 排序置信度估计
authors:
- Meng Yan
- Cai Xv
- Xujing Wang
- Ziyu Guan
- Wei Zhao
affiliations:
- Xidian University
arxiv_id: '2606.04727'
url: https://arxiv.org/abs/2606.04727
pdf_url: https://arxiv.org/pdf/2606.04727
published: '2026-06-03'
collected: '2026-06-04'
category: RecSys
direction: LLM 重排序 · 置信度估计
tags:
- LLM Ranking
- Confidence Estimation
- Evidence Aggregation
- Position-aware Calibration
one_liner: 通过单次前向传播提取三种证据并融合，实现位置级置信度估计与重排序，同时提升推荐质量和不确定性建模。
practical_value: '- 可直接复用单次前向传播提取置信度的思路：从 LLM 的 hidden state 计算语义差距、注意力熵、输出概率差，无需多轮采样，推理零额外开销，适合在线重排场景。

  - 位置感知校准的 NDCG 折扣目标可迁移至电商推荐：将置信度校准为与位置重要性一致，用 (confidence * NDCG weight) 进行 sigmoid
  映射，缓解 LLM 输出概率普遍偏低的扁平分布问题。

  - 可靠意见聚合中的可靠性系数值得借鉴：按各证据源自身的不确定性动态加权融合，比简单平均或 Dempster 组合更鲁棒，可应用于多信号融合的 Agent 决策或排序融合。

  - 置信度加权重排公式简洁有效：用置信度缩放 logits 再 softmax，结合 BPR 损失端到端训练，可直接嵌入现有 LLM4Rerank 管道，适合电商场景中候选集重排。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 在推荐排序中存在领域覆盖不足和随机性问题，现有不确定性量化方法（全局置信度、内部概率）无法揭示排序列表中哪些位置不可靠；内部概率呈现严重欠置信且分布平坦，难以过滤低质推荐。亟需位置级置信度估计来指导可靠重排。

**方法关键点**
1. **三源证据提取**：从 LLM 单次前向传播中提取语义证据（相邻位 hidden state 与用户偏好向量的余弦差距）、注意力证据（注意力熵的反向归一化）和输出证据（相邻位最大生成概率差），均为位置级信号。
2. **可靠意见聚合**：用主观逻辑将各证据转化为 Dirichlet 信念质量，再通过可靠性系数加权融合（Reliable Opinion Aggregation），自动根据各源不确定性调整权重，得到联合信念质量。
3. **位置感知校准**：将信念质量乘以 NDCG 位置折扣因子后经可学习参数 sigmoid 映射，用与 NDCG 折扣值匹配的 MSE 损失训练，纠正欠置信并恢复位置区分度。
4. **置信度引导重排**：用校准置信度缩放 LLM 输出 logits 的 softmax 值，结合 BPR 损失与校准损失联合优化，端到端学习重排分数。

**关键实验结果**
在 Movielens 1M、Amazon Grocery、Steam 三个数据集上，使用 Mistral、Llama3、Qwen2.5 三种骨干：
- 推荐指标：EviRank 在 R@5/N@5 上较 LLM4Rerank 平均提高约 5‑10 个百分点（如 Qwen2.5 在 MovieLens 上 R@5 0.570 vs 0.517，N@5 0.424 vs 0.401）。
- 不确定性指标：Kendall’s τ 和 C-index 均明显优于 Label Prob.、Semantic Unc.、Verb. 1S 等基线，且消融实验证实三源证据、可靠聚合和位置校准均带来增益。
- 校准效果：校准后置信度分布与 NDCG 曲线高度吻合，成功消除欠置信和扁平问题。
