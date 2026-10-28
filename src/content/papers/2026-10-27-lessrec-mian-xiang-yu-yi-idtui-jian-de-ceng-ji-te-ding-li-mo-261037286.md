---
title: 'LESSRec: Level-Specific History Modeling for Semantic ID-Based Recommendation'
title_zh: LESSRec：面向语义ID推荐的层级特定历史建模
authors:
- Shangxin Yang
- Zongwei Wang
- Jing Long
- Junliang Yu
- Min Gao
affiliations:
- Chongqing University
- Griffith University
arxiv_id: '2610.37286'
url: https://arxiv.org/abs/2610.37286
pdf_url: https://arxiv.org/pdf/2610.37286
published: '2026-10-27'
collected: '2026-10-28'
category: GenRec
direction: 生成式推荐 · Semantic ID 层级建模
tags:
- Semantic ID
- Generative Recommendation
- Level-Specific Attention
- Encoder Decoder
- Efficiency
one_liner: 发现并利用同层历史对语义ID预测更有效，提出层级隔离编码与层级对齐注意力
practical_value: '- 如果你的语义 ID 生成式推荐或商品 token 化采用多层语义码本，预测第 r 层 code 时，把用户行为序列按 code
  层级拆分，只让 decoder cross-attention 看到同一层历史 token。这可以用 attention mask 低成本实现，线上推理不增加候选大小，但能减少交叉层噪声。

  - 保留 item 级语义序列作为补充：对每个历史 item 的各层 token 做平均池化 + MLP 残差，得到行为序列里的 item summary。再通过独立的
  cross-attention 分支与层级分支做加权融合（alpha≈0.5）。类似 RAG/Agent 检索里同时提供细粒度 token 证据和 item 级摘要证据。

  - 工程部署：LESSRec 的 mask 方式仍会计算全量 attention 矩阵；要用 LESSRec+ 把 encoder 按层级分组、每组只处理对应层序列，序列长度从
  L*T 降到 T，attention 计算量下降 L^2，训练显存和每 epoch 时间显著降低（论文：峰值显存 -39.2%，每 epoch -33.7%），适合电商长行为序列。

  - 如果要做长历史 / 长序列生成式推荐，层级隔离 + 分组 encoder 可以缓解长序列带来的无关 token 稀释，长历史桶收益更明显（+46.7%/+53.3%），值得在用户行为长度较大的场景优先实验。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
语义 ID 生成式推荐中，每个 item 用 L 个从粗到细的语义 token 表示，历史序列拼接所有层 token，decoder 预测时可关注任意层历史。作者通过推理时 masking 实验发现：当 target token 处于某语义层时，历史同层 token 更有信息量，跨层可能引入干扰。在 level-isolated encoding 下，完全同层访问比完全不匹配访问 Recall@10 提升 49.46%，说明同层历史重要。

## 方法关键点
- **Level-Isolated Self-Attention (LIS)**：encoder self-attention 用 mask 限制每个 token 只 attend 同层 token，EOS 可看全部但历史 token 不能看 EOS；避免跨层混合。
- **Level-Aligned Cross-Attention (LAC)**：decoder cross-attention 预测第 r 层 token 只 attend 历史第 r 层 token + EOS。
- **Item-Level Semantic Sequence (ILS)**：对每个历史 item 的 L 个编码向量做平均池化，经 LN→MLP→残差得到 item-level 表示，按交互顺序组成 item 序列；通过第二个 cross-attention 分支，与 level-aligned 分支输出加权融合（alpha=0.5）。
- **LESSRec+**：将 encoder 层分成 L 组，每组只处理对应层序列，总层数不变，减少注意力矩阵计算和显存，层级 encoder 可并行。

## 关键实验
Games/Software/Beauty 三个数据集，RQ-VAE/RQ-Kmeans/LETTER 三种 tokenizer。对比 Caser/GRU4Rec/BERT4Rec/SASRec/RPG/CARE/DiscRec/TIGER。LESSRec 相对 TIGER 提升 6.2%-39.2%，LESSRec+ 提升 6.0%-54.3%，在 36 个比较中 LESSRec+ 31 个优于 LESSRec。参数 +0.4%，LESSRec+ 训练收敛时间 -65.2%，每 epoch 时间 -33.7%，峰值显存 -39.2%。历史长度越长收益越大，LESSRec+ 在 15-20 长度桶 Recall@5 相对 TIGER +53.3%。

## 最值得记住的一句话
生成式推荐中，预测语义 token 时应将历史访问对齐到目标 token 的语义层级，并通过独立层级编码 / 分组 encoder 降低跨层干扰和计算开销。
