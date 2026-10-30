---
title: 'PFA: Attention Can Be Progressively Focused in Long-Sequence Generative Recommendation'
title_zh: PFA：长序列生成式推荐中注意力可渐进聚焦
authors:
- Pengjie Zhou
- Weiqin Yang
- Haibo Xing
- Hao Deng
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Zhejiang University
arxiv_id: '2610.39273'
url: https://arxiv.org/abs/2610.39273
pdf_url: https://arxiv.org/pdf/2610.39273
published: '2026-10-29'
collected: '2026-10-30'
category: GenRec
direction: 生成式推荐 · 稀疏注意力加速
tags:
- Generative Recommendation
- Sparse Attention
- Long-Sequence Modeling
- Beam Search
- KV Cache
- E-commerce
one_liner: 利用 GR 解码中注意力渐进聚焦与跨步排名一致性，PFA 通过共享重要性排名和几何预算缩减，加速长序列生成式推荐
practical_value: '- 对长序列生成式推荐，可借鉴"早期构造共享重要性排名 + 后续几何缩减预算"，替代每步每 beam 独立 top-k，消除重复选择和
  KV gather 开销，尤其适合 beam width 大、序列长的电商召回/广告候选生成。

  - 工程实现上，用 beam 生成概率加权聚合注意力分布来挑选关键历史 token，比每个 beam 独立选更稳定且能共享连续 KV cache；可先 reorder
  KV cache，后续直接前缀截断，降低非连续内存访问。

  - Step-aware KV projection：为不同解码步分配独立 KV 投影参数，成本低但能显著缓解复用 token 带来的表示退化，适合层级 SID
  生成。

  - 若业务采用生成式推荐，可保留 Step 0 全注意力做全局探索，不用过早压缩历史，对长序列效果稳定。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
长用户行为序列能提升生成式推荐（GR）效果，但 beam search 解码每一步都对全历史做 full attention，延迟随历史长度线性增大。静态压缩可能丢关键语义；动态 top-k 稀疏注意力又因每步每 beam 重复选择和非连续 KV cache 访问，实际加速有限。论文发现 GR 解码中注意力会渐进聚焦到少数关键 token，且这些 token 的重要性排名跨步较稳定。

## 方法关键点
- PFA 分三阶段：Step 0 全注意力做全局偏好探索；Step 1 做 cross-beam importance-based token selection，用 beam 生成概率加权聚合注意力分布，得到共享重要性排名，选出 top-k token 并 reorder 成连续 KV cache；Step ≥2 复用该排名并几何递减 token 预算 k_t = max(1, ceil(k*r^(t-1)))。
- 加入 step-aware KV projection：每个解码步独立 KV 投影参数，预计算 KV cache，避免复用 token 导致表示坍缩。
- 支持跨 beam 和跨 step 共享 KV cache 子集，减少非连续内存访问。

## 关键结果
在 Kindle Store、Tmall、Industry 三个数据集上，PFA 相比最强 baseline 平均 Recall@10 提升 5.75%、NDCG@10 提升 7.18%；Industry 上比 Full Attention 推理加速约 1.45×（延迟 62ms vs 90ms），Recall@10 提升 3.16%；在线 A/B 中广告收入 +3.76%、GMV +2.56%，RT 11ms。
