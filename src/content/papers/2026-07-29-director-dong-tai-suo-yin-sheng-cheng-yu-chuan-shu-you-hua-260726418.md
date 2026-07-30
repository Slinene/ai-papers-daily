---
title: 'DIRECTOR: Dynamic Index-based Recommendation with Transport-Optimized Retrieval'
title_zh: DIRECTOR：动态索引生成与传输优化检索的平行重排框架
authors:
- Yuanhao Pu
- Chenghao Zhang
- Chao Feng
- Xiang Li
- Defu Lian
affiliations:
- University of Science & Technology of China
- Kuaishou Technology
arxiv_id: '2607.26418'
url: https://arxiv.org/abs/2607.26418
pdf_url: https://arxiv.org/pdf/2607.26418
published: '2026-07-29'
collected: '2026-07-30'
category: RecSys
direction: 生成式重排 · 最优传输
tags:
- Non-Autoregressive
- Reranking
- Optimal Transport
- Generator-Evaluator
- Prefix-Anchored Credit
- Slate Recommendation
one_liner: 用连续动态索引替代逐位自回归，通过最优传输耦合实现无重复、全局协调的平行重排。
practical_value: '- 将候选物品与输出位置映射到同一隐空间，生成连续检索索引（dynamic retrieval indices），再通过全局硬匹配（矩形指派）直接输出无重复
  slate，可避开自回归解码的串行依赖与 prefix 剪枝风险，工程部署中可将 proposal 生成并行化。

  - 训练时采用熵正则化最优传输（capacity-constrained soft transport）作为可微代理，联合所有位置的分配进行冲突感知监督，推导时使用
  Bregman-Dykstra 算法快速求解；推理时仅需一次相似度矩阵计算并执行标准指派，兼顾效果与低延迟。

  - 针对只有整 slate 标量反馈的黑盒 Evaluator，提出“prefix-anchored pathwise credit”：沿一条保留有效性的交换路径逐步替换位置，把全局奖励差分解为每个位置的特异优势，提供细粒度训练信号，适合工业场景中无法获取梯度或内部评分的
  listwise 评估器。

  - 在快手短视 feed 线上真实流量对比中，DIRECTOR 相比自回归 + Beam Search 基线在同等延迟约束下降低 66.7% 的 CPU 消耗，且
  vv 提升 0.519%，证明平行重排在大规模服务中的效率与效果优势。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：重排需要从请求相关的候选集中选择一个有序且无重复的 slate，搜索空间巨大且受位置间依赖影响。现有自回归（AR）生成器因逐位解码导致前缀剪枝和串行延迟，非自回归（NAR）方法虽可并行，但独立的位置预测易产生重复或冲突。如何在保持并行效率的同时实现全局位置协调，并能利用仅返回标量奖励的 listwise 评估器进行优化，成为关键挑战。

**方法关键点**：
- **动态索引生成**：对每个输出位置，联合用户上下文和候选集生成连续检索向量，所有位置并行产生，避免 AR 顺序。支持 CVAE 或条件扩散两种实现。
- **传输导向的检索**：计算位置–候选相似度矩阵，训练时使用熵正则化容量约束最优传输作为可微监督，显式展平位置间竞争；推理时直接解矩形指派问题得到无重复 slate，无需额外冲突解决。
- **前缀锚定的信用分配**：基于基线 slate 和生成 slate 构建一条保留有效性的替换路径，每一步替换一个位置，将全局奖励差分解为每个位置的优势，用于 REINFORCE 式策略梯度，强化或抑制相应分配。
- **理论分析**：证明硬匹配与软传输的等价性及无间隙；给出熵正则化的近似误差界；分析有限提案覆盖率和并行推理复杂度，显示其在线计算复杂度远低于 AR beam search。

**关键结果**：
- 离线：在 ML-1M、Amazon-Books、RecFlow 三个数据集上，DIRECTOR（CVAE/Diff 变体）NDCG@6 分别提升 3.69%、2.80%、3.61%，一致优于 Seq2Slate、PIER、NAR4Rec、OMGRec 等强基线。
- 在线 A/B：快手短视频生产环境，用户观看 VV 提升 0.519%（显著），互动指标同步提升。
- 压力测试：同等延时与可用性下，CPU 资源消耗降低 66.7%。
