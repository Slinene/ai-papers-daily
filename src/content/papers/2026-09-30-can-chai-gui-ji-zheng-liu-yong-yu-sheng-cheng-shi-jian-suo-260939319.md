---
title: Residual Trajectory Distillation for Generative Retrieval
title_zh: 残差轨迹蒸馏用于生成式检索
authors:
- Weihao Shen
- Wei Chen
- Fuwei Zhang
- Guojun Liu
- Qingsong Hua
- Wei Lin
- Fuzhen Zhuang
affiliations:
- Beihang University
- Meituan
arxiv_id: '2609.39319'
url: https://arxiv.org/abs/2609.39319
pdf_url: https://arxiv.org/pdf/2609.39319
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式检索 · Semantic ID · 残差蒸馏
tags:
- Generative Retrieval
- Semantic ID
- Residual Quantization
- Knowledge Distillation
- E-commerce Search
- Generative Recommendation
one_liner: 把冻结RQ索引器的残差码本偏好蒸馏进SID解码状态，保留检索索引与推理不变
practical_value: '- 如果已经在用 RQ Semantic ID 做生成式召回/推荐，可以把冻结的 RQ indexer 当成现成 teacher：沿存储
  SID 重建残差，用残差到码本的距离构造 soft target，KL 对齐 SID 解码状态；训练只加几个投影头，推理时全部移除，beam search 和索引完全不变。

  - 多 horizon future 监督值得复用：让早期解码状态同时预测后续几层码本偏好，类似 multi-token prediction，但目标是码本分布而非
  hard token；这能提前注入后续结构，缓解 beam search 早期剪掉正确 item 的情况，电商商品检索里尤其适合互补/长尾商品。

  - 必须做 collision-aware 修正：线上 SID 通常经过去重/冲突解决，直接拿原始 RQ 残差会与最终索引不一致。实现时沿最终存储 SID 重建残差路径，并对
  soft target 做最小 margin 插值，保证存储 code 仍是最高概率；这是工程能否落地的关键细节。

  - 控制实验显示 shuffled teacher、非目标对应或全局 codebook-only 都会掉点，说明 teacher 必须保留 item 级对应关系，不能只做通用码本统计蒸馏；在生成式推荐里
  TIGER 类骨干同样可接入，B-Shop/Yelp 上提升更明显。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式检索把商品/文档表示为离散 Semantic ID，通过自回归生成 token 完成召回。RQ 构建 SID 时，标准训练只监督最终 hard code，丢弃了残差轨迹。问题是：同一 hard code 可以由不同残差产生，残差到竞争码本的距离、margin 以及后续量化输入信息都不同，而这些差异无法被 hard SID 表达。索引阶段已经算出的残差几何，在检索训练中完全浪费。

**方法关键点**
- 把冻结的 RQ indexer 当作 process teacher：用残差 r_{t-1} 到码本 C_t 的距离构造 soft teacher 分布 Q_t(j|d)，保留所选 code 之外的竞争码字偏好。
- 在 SID 解码状态 h_t 上学习投影 g_s 到码本空间，得到 student 分布 P_t,s，用 KL 对齐；梯度等价于拉近 teacher/student 在码本空间中的期望向量。
- 多 horizon 蒸馏：不只对齐当前层，还让早期解码状态预测后续若干层的码本偏好，H=4，未来权重按 ρ^s 衰减；这相当于用码本分布做 future supervision，早状态提前编码后续 SID 结构。
- collision-aware teacher：沿最终存储的 SID 路径重建残差，并用最小插值修正 soft target，使存储 code 保持 margin，避免与检索地址冲突。
- 训练目标 L = L_GR + λ(u)L_RT，λ 线性 warmup，上限 0.1；推理时去掉所有辅助投影，保持原 SID 生成和 trie-constrained beam search。

**关键实验与数字**
在 ESCI-US/ES/JP 多语言电商检索上做控制实验：相比最强 baseline CaLIR，ResTD 的 R@10 分别提升 13.00%、12.21%、19.04%，N@10 提升 16.82%、14.40%、20.48%；R@100 和 NDCG@100 也全部提升。匹配训练预算下，H=4 优于当前层 RBD、future hard SID、shuffled teacher、codebook-only 等控制组。生成推荐扩展中，TIGER 骨干接入 ResTD 后，B-Shop/Yelp R@10 分别提升 8.33%、14.32%，NDCG@10 提升 9.89%、15.15%。表示探针显示，早解码状态对后续码本偏好的恢复 KL 降低 5.3–13.8%，未来信息确实被提前编码。

**最值得记住的一句话**：不要只让模型背 hard SID，把 RQ indexer 在量化过程中的残差几何作为过程监督，可以让早解码状态提前携带后续码本偏好，且不用改索引和推理。
