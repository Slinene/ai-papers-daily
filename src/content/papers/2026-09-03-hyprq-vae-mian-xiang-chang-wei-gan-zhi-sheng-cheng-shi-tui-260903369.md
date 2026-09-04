---
title: 'HypRQ-VAE: Hyperbolic Item Indexing for Long-Tail-Aware Generative Recommender
  Systems'
title_zh: HypRQ-VAE：面向长尾感知生成式推荐的双曲语义 ID 索引
authors:
- Longfeng Wu
- Tong Zeng
- Giovanni Seni
- Zhimin Peng
- Bhanu Pratap Singh Rawat
- Si Zhang
- Yao Zhou
- Lecheng Zheng
- Bo Ji
- Yujun Yan
affiliations:
- Virginia Tech
- Amazon
- Meta AI
- Google
- Dartmouth College
arxiv_id: '2609.03369'
url: https://arxiv.org/abs/2609.03369
pdf_url: https://arxiv.org/pdf/2609.03369
published: '2026-09-03'
collected: '2026-09-04'
category: GenRec
direction: 生成式推荐 · 语义ID · 双曲空间
tags:
- Generative Recommendation
- Semantic ID
- Hyperbolic Geometry
- Long-tail Recommendation
- RQ-VAE
- LLM4Rec
one_liner: 首次将双曲空间残差量化 VAE 用于生成式推荐语义 ID，显著提升长尾物品推荐
practical_value: '- 语义 ID 生成可把 RQ-VAE 从欧氏空间换成 Poincaré ball + Möbius 减法/加法，无需额外正则即可让
  codebook 使用更均衡，对尾部、新品 item 更友好。

  - 长尾收益明确：按 H20/T80 划分评估，Hit@10 在尾部提升 17.24%-52.71%，推荐列表尾部占比提升约 8-10 个百分点；建议上线前对尾部流量单独做指标拆分。

  - 碰撞处理可直接复用：对冲突 item 构建距离张量，从最后一层向上做 nearest-available token 分配，比额外 ID 或正则更干净，适合电商大目录
  item 压缩。

  - 工程配置可参照：Stage1 用 Adam lr=1e-3、L=4、K=256；Stage2 用 LLaMA2-7B + LoRA r=8/alpha=32/dropout=0.05，配合
  Trie 约束解码 beam=20。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 做生成式推荐必须把物品压缩成离散 token，现有 RQ-VAE 在欧氏空间学习语义 ID，对长尾分布建模不足：头部物品主导训练，尾部物品编码质量差、碰撞多，导致 LLM 推荐偏向头部。双曲空间指数体积增长天然匹配幂律分布和层级结构，更适合 item 语义与流行度的长尾特征。

**方法关键点**
- 将 RQ-VAE 量化过程搬进 Poincaré ball：编码器输出 ze，经指数映射到双曲空间作为初始残差 r0；逐层用 Möbius 减法找最近 codebook 向量并计算残差，最终用 Möbius 加法聚合码向量，再 log 映射回欧氏空间重构。
- 使用 L 层、每层 K=256 的 codebook，生成如 <a_1><b_3><c_2><d_9> 的语义 ID。
- 碰撞处理：对冲突 item 构建距离张量，从最后一层开始逐层向上做 nearest-available token 分配，不引入额外正则。
- 第二阶段：用 LLaMA2-7B + LoRA 在语义 ID 序列上做 next-item 自回归生成，配合 Trie 约束解码。

**关键实验**
在 MovieLens、Amazon Instruments、Arts 三个数据集上，对比 MF、Caser、SASRec、P5-TID、P5-CID、TIGER、LC-Rec、LETTER。HypRQ-VAE 全面超过最强 baseline：MovieLens Hit@10 +4.8%，Instruments NDCG@10 +14.0%。相比欧氏 TIGER，尾物品 Hit@10 提升 17.24%-52.71%。量化误差分析显示双曲空间头部/尾部 AQE 差距大幅缩小，MovieLens 上尾部 AQE 甚至低于头部。

**值得记住的一句话**
双曲空间给语义 ID 生成带来更均衡的长尾表征，让 LLM 生成推荐不再只推头部。
