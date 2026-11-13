---
title: 'ReSID: Rethinking Long-Tail Retrieval in Generative Recommendation through
  Item Reachability'
title_zh: ReSID：从物品可达性视角重新思考生成式推荐长尾检索
authors:
- Muyu Zou
- Shunye Tang
- Yi Xu
- Haibo Xing
- Yandong Wang
- Lingyu Mu
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Nankai University
arxiv_id: '2611.16404'
url: https://arxiv.org/abs/2611.16404
pdf_url: https://arxiv.org/pdf/2611.16404
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 长尾可达性优化
tags:
- Semantic ID
- Long-tail Retrieval
- Generative Recommendation
- Beam Search
- Partial Matching
- Parallel SID
one_liner: 提出 ReSID，用长平行 SID、去流行度/用户语义引导 beam search 与部分 SID 匹配，系统解决生成式推荐长尾可达性问题
practical_value: '- 生成式推荐中长尾损失不只在训练，更多在解码与匹配链路；线上可在窄 beam 下用 partial SID matching（容忍
  1–3 个 token mismatch）恢复大量尾部候选，直接提升长尾曝光与 recall。

  - 表示层优先选择 parallel SID：各 position 独立 codebook、无残差链，同码空间下比 sequential SID 尾部 recall/coverage
  更好，且位置间错误隔离，适合故障容错检索。

  - 解码端加两个低开销信号：从 logits 减去经验 token prior 做 popularity calibration；用用户向量与候选 item 向量的相似度作为
  beam 扩展打分，保留与用户相关的尾部 prefix。可提前缓存 prefix-level 语义分数，线上成本低。

  - 工程上不必扩大 beam：用 beam 20 相当于基线 beam 200 的效果，延迟为基线 1/2–1/8、吞吐提升 3.7–16.7 倍；在线 A/B
  广告收入 +1.3%、CTR +1.1%、GMV +0.8%、长尾曝光份额 +4.0%。预算受限时改进搜索策略比增加搜索宽度更划算。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：生成式推荐把 item 映射为 Semantic ID 序列，以生成方式做检索，但在交互偏斜与在线 beam 预算有限时，长尾 item 很难被生成和匹配。已有长尾工作集中在训练侧表示/目标，未系统审视 SID 构造、解码、匹配完整链路。ReSID 从“物品可达性”角度分析，发现 parallel SID 在等码长下尾部表现优于 sequential；即使全序列生成失败，局部 token 仍可通过 partial matching 恢复相关尾部；但该恢复被上游 beam search 的早期剪枝严格限制。

**方法关键点**：ReSID 三个组件。1) 长 parallel SID：将物品表示分成 L 个独立子空间，每个 position 独立 codebook 量化，避免残差链逐层累积头部偏置；2) Reachability-Aware guided beam search：在冻结 backbone 基础上加入 popularity calibration（从 logits 减 log prior）和 user-semantic alignment（用户向量与候选 item 向量相似度作为 beam 扩展打分），在窄 beam 下保留相关尾部 prefix；3) partial SID matching：用 mismatch tolerance r 做部分匹配，从保留的 beam 中恢复与候选码距 ≤r 的物品，并优先排序 mismatch 更少、beam 分数更高的候选。

**关键结果**：在 Amazon Industrial/Office 和大规模 In-house 电商广告数据集上，对比 RQ-VAE、TIGER、OneRec、CRAB、Ghost、SA2CRQ。ReSID 在所有长尾 Recall/NDCG/EffCov 上取得最优：Industrial tail R@200 达 21.22%（Ghost 16.11%），Office 20.54%（Ghost 13.50%），In-house tail R@200 36.62%（Ghost 18.94%）；整体指标保持竞争且 In-house 全面领先。效率上，ReSID 用 beam 20/100 对比 baseline beam 200/300，延迟为基线 1/2–1/8，吞吐提升 3.7–16.7 倍。在线 A/B：广告收入 +1.3%，CTR +1.1%，GMV +0.8%，长尾曝光份额 +4.0%。

**最值得记住的一句话**：生成式推荐的长尾问题需要 SID 构造、解码和匹配联合优化；parallel SID 的局部一致信号 + guided beam search 保留 prefix + partial matching 恢复，是有限 beam 预算下兼顾长尾与效率的有效路径。
