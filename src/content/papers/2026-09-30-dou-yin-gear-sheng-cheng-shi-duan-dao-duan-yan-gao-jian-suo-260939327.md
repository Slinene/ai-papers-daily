---
title: Generative End-to-end Ad Retrieval at Douyin
title_zh: 抖音 GEAR：生成式端到端广告检索框架
authors:
- Shaowen Zeng
- Yanhua Huang
- Jiacheng Sun
- Jiarui Liu
- Qian Dai
- Zhikai Yang
- Hancheng Li
- Boya Wu
- Tuoyu Zhang
- Yekui Chen
affiliations:
- ByteDance
arxiv_id: '2609.39327'
url: https://arxiv.org/abs/2609.39327
pdf_url: https://arxiv.org/pdf/2609.39327
published: '2026-09-30'
collected: '2026-10-01'
category: GenRec
direction: 生成式推荐 · VQ/Semantic ID
tags:
- Generative Retrieval
- Vector Quantization
- Representation Collapse
- Item Collision
- Industrial Ads
- End-to-end
one_liner: GEAR 用正交基 BasisRQ 稳定码本更新，并用轻量重排头消解 item 碰撞，在抖音广告上线取得显著收益
practical_value: '- **BasisRQ 可迁移到动态分布下的生成式召回码本**：用可学习正交基重参数化 codebook，训练时全局共享梯度、避免死码，推理时码本可预计算缓存、零额外延迟；若业务中生成式
  item tokenizer 因流式数据分布漂移而码本利用率低，可替代 EMA 或冻结码本。

  - **prefix-aware 快速距离计算值得直接复用**：在 RQ 每层按前序量化结果对 codebook 做逐元素 affine 变换，再通过代数重排把距离矩阵计算保持为
  O(bNd)，避免 3D tensor 内存爆炸；适合电商/广告巨量 item 的 tokenization。

  - **轻量生成式重排头可低成本解决 token 碰撞**：复用 decoder autoregressive hidden states 生成用户向量，与 item
  tower embedding 做 dot product，只多一步 decoding + INT4 低精度打分；当 item token 序列碰撞严重时，不必依赖唯一
  token 或缩小码本容量。

  - **工程化训练与索引策略可借鉴**：渐进 warm-up 先训两塔、再开 RQ、最后开生成与重排；生成损失按 secpm 重加权强化高价值样本；近线索引分钟级更新
  item 序列与 embedding，CSR-like 目录 + per-sequence 截断保证候选多样性。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式检索把推荐重构为逐 token 生成 item ID，但在真实广告系统规模化时面临两个耦合瓶颈：一是表示坍缩——连续分布漂移下码本训练不稳定，大量 code 死亡；二是 item 碰撞——海量候选下不同 item 共享 token 序列，损害检索精度。扩大码本容量能缓解碰撞，却又加剧坍缩，因此需要统一框架同时解决。

**方法关键点**  
- **BasisVQ/BasisRQ**：用可学习正交基重参数化 codebook，通过 Newton-Schulz 迭代保证正交性；几何上等价于对整个坐标系统做刚性旋转，激活的 code 更新会带动 inactive code 一起移动，从而在流式训练中恢复码本利用率。 
- **prefix-aware BasisRQ**：基于前序量化结果对当前层 codebook 做逐元素 affine 变换，提升表达力；通过代数重排保持距离计算复杂度与 vanilla VQ 相同，避免高内存开销。  
- **Generator**：轻量 encoder 将用户特征投影为 KV 表示，2 层 decoder 用 cross-attention + gated FFN 自回归生成 item token 序列。
- **Reranker**：生成结束后额外做一步 decoding，产生候选序列特定的用户 embedding，与 item tower embedding 做 dot product 打分，用 LambdaLoss 训练，以极小计算代价消解碰撞项。
- **联合训练**：两塔 LambdaLoss + RQ codebook/commitment loss + secpm 加权交叉熵生成 loss + 重排 LambdaLoss；渐进 warm-up 分阶段激活。

**关键实验**  
在抖音广告平台做 7 天在线 A/B，GEAR 作为新增生成式检索通路对比生产 baseline：ADSS +0.563%，ADVV +0.658%；冷启动激活率相对提升 +1.46%。消融显示替换 prefix-aware BasisRQ 掉点最多，移除 rerank 和 secpm 加权也有明显损失。Tokenizer 对比中，progressive 码本大小 (2048,512,128) 取得最高的 codebook 利用率 8.83%、最低碰撞率 52.3%、最低量化误差 1.82e-3，优于 uniform 分配和 vanilla RQ。

**最值得记住的一句话**  
生成式检索的码本坍缩与 item 碰撞必须联合治理：用正交基保持码本容量与梯度稳定，再用轻量 context-conditioned 重排消解碰撞，才能在工业级广告系统中稳定上线。
