---
title: 'Orthogonal Norm Growth in Two-Tower Retrieval: A Popularity Mechanism for
  Unified Discovery'
title_zh: 双塔检索中的正交范数增长：统一发现中的流行度机制
authors:
- Andrei Atamaniuk
affiliations:
- Wildberries and Russ, Russia
arxiv_id: '2611.09294'
url: https://arxiv.org/abs/2611.09294
pdf_url: https://arxiv.org/pdf/2611.09294
published: '2026-11-06'
collected: '2026-11-09'
category: RecSys
direction: 双塔检索 · 向量范数增长机制
tags:
- two-tower retrieval
- embedding norm
- popularity bias
- unified search
- InfoNCE
- shared item tower
one_liner: 推导并验证了共享 item tower 在 cosine-only loss 下更新满足特定条件时 item 向量范数单调增长，并经 raw-dot
  检索放大头部曝光
practical_value: '- 在统一搜索/推荐共享 item tower 的场景，若使用 cosine InfoNCE + 纯 ID embedding
  table + SGD/Exact RowWise Adagrad，每个 item 的范数会随更新次数近似单调增加。上线前应审计 realized motion
  而非只看输出梯度：记录 q_i^T Δq_i / (||q_i|| ||Δq_i||) 的分布，按 task 分开统计更新次数 N^S_i, N^R_i 和累计
  tangent energy D^S_i, D^R_i，定位范数累积来源。

  - raw inner product 检索会放大高范数 item 的曝光，可以通过 unit-item serving 快速消解 magnitude 通道；但论文实验显示抑制
  norm 增长同时导致 raw-dot Recall 和 NDCG 相对下降 17-22%，说明 popularity 信号可能部分有用，不能直接当 bias
  去掉，适合做诊断而非 blind debias。

  - 如果 item tower 是 ID row + shared content encoder 的混合结构，ID row 更新部分的范数贡献可精确分离（Exact
  RowWise Adagrad 保持方向），可以低成本做“retraction”干预实验，快速评估 norm 导致的曝光变化及 utility 影响。

  - 跨任务共享同一 item 索引时，搜索流的更新机会会对推荐候选排序产生间接影响（via norm），建议对两个任务的 item 更新数和能量分别打点，并在
  serving 层做 raw vs unit 的分解，以评估跨表面泄漏的规模。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
统一搜索/推荐系统常共享 item tower 以提升效率，但这也可能让一个任务的训练通过共享表示影响另一个任务的候选排序。已知 cosine-only loss 的输出梯度垂直于 item 向量（tangent），常被推测会导致 item 范数增长，但参数化编码器的实际位移不一定 tangent。论文研究在什么充分条件下实际位移 tangent、跨任务如何累积到同一范数，以及该范数何时影响 serving。

**方法关键点**  
- 定义 lookup-equivalent（不同 item ID 独立参数块且 Jacobian 乘积为 c_i I）、parameter-linear、direction-preserving row update。  
- 定理：当 item encoder 是 parameter-linear 且 lookup-equivalent，loss 仅通过 cosine 依赖输出，优化器对 item block 做正标量方向保持更新（如 SGD、Exact RowWise Adagrad），则每一步实际 item 位移满足 q_i^T Δq_i = 0，范数平方增加量等于位移平方。  
- 跨任务路径等式：若顺序更新满足以上条件，两个流的 tangent 能量可加性累积到同一 item 范数。  
- 混合 tower（ID row + shared content encoder）中，ID row 更新部分精确 tangent，shared content 更新为 residual，可测量总位移角度的偏离来源。

**关键实验与结果**  
在玩具实验验证条件后，MovieLens 32M 和 Amazon Books 上实验 8/9/10 显示 exact regime 下 tangent 路径成立，足够累积位移后 frequency-norm 相关显著（Exp8 r=.66/.63，Exp10 r=.57/.61）。raw-dot top-100 中 top-1% 频次物品占比显著高于 unit-item ranking（Exp8 .72/.60 vs .29/.06；Exp10 .63/.98 vs .32/.11）。Hybrid 实验 active item movement 接近 tangent（median |cos| .0034/.0003），ID update count 与频率正相关但每次能量不增；matched retraction 降低 norm lift（ML 1.62→-11.98 pp；Amazon 20.12→-.33 pp），但 raw-dot Recall 和 NDCG 相对下降 17-22%，说明 norm 通道包含有用信号而非纯粹 bias。

**最值得记住的一句话**  
cosine loss 的梯度正交性不能保证参数化 item 向量的实际移动 tangent，只有验证 lookup-equivalent + direction-preserving 条件成立后，共享 item tower 的更新次数才会可加地累积为范数，并通过 raw inner product 转化为频率相关曝光——这是一个可审计的跨表面通道，而非必然的偏见。
