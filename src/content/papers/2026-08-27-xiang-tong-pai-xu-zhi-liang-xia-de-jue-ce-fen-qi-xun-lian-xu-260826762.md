---
title: 'Equal Ranking Quality, Different Decisions: Training Order-Consistent LLM
  Scorers'
title_zh: 相同排序质量下的决策分歧：训练顺序一致的 LLM 打分器
authors:
- Markus Frohmann
- Mahdiyar Alavi
- Elizabeth Lingg
- Navid Rekabsaz
affiliations:
- Thomson Reuters Labs
- University of Toronto
- Vector Institute
arxiv_id: '2608.26762'
url: https://arxiv.org/abs/2608.26762
pdf_url: https://arxiv.org/pdf/2608.26762
published: '2026-08-27'
collected: '2026-08-28'
category: Training
direction: LLM 打分器顺序一致性训练
tags:
- order consistency
- LLM scorer
- reranking
- decision stability
- SFT
- presentation dependence
one_liner: 提出 OC-SFT 顺序一致性训练，在不损失排序质量下显著提升 LLM 打分器在重排、QA、偏好选择中的决策稳定性
practical_value: '- 线上使用 batched pointwise scoring 时，候选顺序会显著影响分数及下游决策（阈值截断、top-k 阅读、偏好对选择），不要只看
  nDCG。推荐在训练阶段加入 OC-SFT 式一致性惩罚：对同一窗口做两次 shuffle，一个 view 做 relevance anchor，另一个 view
  拉向 view-mean，MSE 惩罚学生自身 order variance。N=2 足够，推理时仍只需一次 permutation。

  - 该方法可将 passage reranking 的 retained-set overlap 从单顺序蒸馏的 0.656 提升到 0.835，同时 nDCG@10
  基本不变（0.459 vs 0.449）；在 multi-doc QA 上 answer flip 从 0.177 降至 0.125；在 response ranking
  上 pair flip 从 0.869 降至 0.661。一个 OC-SFT permutation 的稳定性即可超过 10 次离线平均 permutation
  的 batched self-consistency。

  - 训练标签无需 order-averaged distillation 的 10 倍 teacher 计算，只需单个 teacher 顺序，节省离线成本。更强的
  teacher 只提升质量不提升稳定性，说明稳定性收益来自 penalty 而非监督信号，可放心复用现有 teacher。

  - 如果打分器服务决策场景（如广告过滤、商品精选、prompt 选择），应报告决策稳定性指标：保留集 Jaccard、答案翻转率、偏好对翻转率，而不只是 ranking
  quality。round-robin partition 可提升 nDCG@10（+0.052）但不能改善决策稳定性，logit calibration 也无效，所以需要从训练目标入手。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM scorer 在一个 prompt 中为多个候选文档或响应打分，每个候选的分数依赖于同 prompt 中其他候选及其排列顺序，即 presentation dependence。这类 scorer 通常按排序质量（nDCG）选择，但下游消费者是基于分数做决策：阈值截断保留文档、reader 阅读 top-k、偏好模型选择 response pair。实验发现即便 nDCG@10 差距 <0.010，不同 scorer 在这些决策上的可复现性差异巨大：retained-set overlap 跨度 0.656–0.835。推理时多次排列平均（batched self-consistency）虽有效但成本随排列数倍增，因此需要训练时消除顺序依赖。

**方法关键点**
- 将 scorer 输出分解为 order-marginal μ_B 和 order residual δ_B，提出 τ-PSI 度量排名不稳定性。
- 读分方式固定：每个候选分配一个 grade token，一次前向得到 B 个候选的期望分数，连续且可直接用于阈值，不生成文本。
- OC-SFT 在单顺序蒸馏损失基础上，对同一窗口做 N=2 次 shuffle，每个 view 拉向 view-mean，用 λ 惩罚学生自身 order variance。仅一个 view 携带 relevance anchor，无需多个 teacher 顺序。
- 对比目标包括：单顺序蒸馏、order-averaged distillation（T=10 teacher 排列预计算）、DebiasFirst、permutation augmentation、以及推理时 BSC（K=10）。
- 训练数据：MS MARCO passage reranking 约 30K queries（B=20）；HotpotQA 多文档 QA 30K 问题（B=10）；UltraFeedback 响应排序约 30.7K prompts（B=4）。

**关键结果**
- 五个训练 scorer 在 18 个 passage reranking 集合上 nDCG@10 差距 <0.010，但 retained-set overlap 从 0.656 到 0.835；OC-SFT 达到 0.835 且 nDCG@10 0.459，与最优排序质量基本持平。
- OC-SFT 在 multi-doc QA 上 answer flip 为 0.125，对比其他顺序相关目标 0.149–0.164；在 response ranking 上 pair flip 为 0.661，其他目标 0.707–0.869。
- 在 12 个 base models（含 MoE）上，OC-SFT 稳定性均优于 order-averaged distillation。
- 一个 OC-SFT permutation 的 retained-set overlap 高于十次 averaged off-the-shelf permutations。
- 强 teacher 只提升质量不提升稳定性，证明收益来自一致性 penalty 而非监督信号。

**最值得记住的一句话**
排序质量指标无法区分 LLM 打分器在下游决策上的稳定性；用 OC-SFT 在训练时惩罚自身跨排列的 score variance，可在单次推理下达到甚至超过多次排列平均的决策一致性，且不损失排序质量。
