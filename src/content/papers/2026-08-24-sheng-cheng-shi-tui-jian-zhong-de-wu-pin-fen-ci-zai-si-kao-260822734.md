---
title: 'Rethinking Item Tokenization in Generative Recommenders: From Fixed Atoms
  to Semantic Subwords'
title_zh: 生成式推荐中的物品分词再思考：从固定原子到语义子词
authors:
- Xinrui Miao
- Mingjia Yin
- Jiaqing Zhang
- Wei Guo
- Yong Liu
- Yuyang Ye
- Hao Wang
- Enhong Chen
affiliations:
- University of Science and Technology of China
- Huawei Technologies
arxiv_id: '2608.22734'
url: https://arxiv.org/abs/2608.22734
pdf_url: https://arxiv.org/pdf/2608.22734
published: '2026-08-24'
collected: '2026-08-25'
category: GenRec
direction: 生成式推荐 · Semantic ID
tags:
- Generative Recommendation
- Semantic ID
- Tokenization
- Subword
- Attention Overload
- Sequential Recommendation
one_liner: 提出 SST：历史侧用变长语义子词压缩 SID、目标侧保留定长解码，缓解 intra-item 注意力过载并稳定提升生成式推荐
practical_value: '- 在 SID-based 生成式推荐中，历史侧和目标侧使用不对称 tokenization：用户历史序列用子词合并压缩，降低
  encoder 的 intra-item attention 负担；候选 item 仍用固定长度 SID 生成，不破坏 beam search 解码语法。可直接作为现有
  RQ-KMeans/TIGER 类线上模型的输入层改造。

  - 子词合并规则可以优先尝试 CondEntropy：同时考虑 frequency、互预测性和上下文纯度，比 BPE/WordPiece 更适合推荐场景的语义耦合，尤其在稀疏或噪声较大的业务数据上更稳。

  - BCA 用行为序列中语义前缀对（如取 SID 前 2 个 token）滑窗统计高频共现，把原始交互子序列作为增强样本注入训练，开销低、无需额外标注，能改善长尾
  item 的曝光和 NDCG。

  - 上线前可做 token-level attention workload 分析：统计 encoder 中 same-item attention 占比和 atom
  reassembly load，验证压缩是否真正释放了模型容量；同时注意不要将目标侧改成变长子词，否则低频语义 token 在 beam search 中会被边缘化，性能可能大幅下降。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
固定长度 Semantic ID 在生成式推荐中作为候选侧的解码语法很便利，但历史 user sequence 也复用同一套原子 token 表示，会导致 encoder 花费大量注意力在 item 内部 token 重组上，形成 **intra-item attention overload**，干扰真正的 inter-item 行为转换建模。

## 方法关键点
- **非对称 tokenization**：历史侧使用变长 semantic subword 作为 encoder 输入，目标侧保留固定长度 SID 用于 autoregressive decoding。
- **IST**：从 item 内相邻原子对收集候选，按 BPE / WordPiece / CondEntropy 学习 merge 规则，将稳定的相邻原子合并为 semantic subword token（如 `<p_a7_b4>`），缩短历史 token 序列，减少 encoder 对低层原子耦合的重复拟合。
- **BCA**：取 item SID 前 P 个 token 作为语义前缀，滑窗统计用户行为序列中前缀对共现，选取 top-k 高价值对，将对应历史子序列作为 replay 样本注入训练，引导释放的注意力关注粗粒度 inter-item 转移信号。
- **目标侧保持固定长度**：变长目标会导致语义 subword token 成为长尾解码符号，在 beam search 中难以进入 top beams，造成性能坍塌。

## 关键实验
在 Beauty、Instruments、Yelp 三个公开数据集上，以 TIGER-KM、TIGER-VAE、LETTER 为 backbone，与 Fixed、SARQ、VSID 等 baseline 对比。
- TIGER-KM 上：Beauty HR@10 +5.8%、NDCG@10 +10.0%；Instruments NDCG@5 +5.5%；Yelp HR@10 +6.7%、NDCG@10 +8.3%。
- attention workload 分析显示：SST 显著降低 intra-item attention budget 和 atom reassembly load，验证了容量释放机制。
- 效率上：IST 缩短历史 token 长度，BCA 增加 replay 样本，两者抵消，且收敛 epoch 减少，无系统性时间增加。
- 消融与覆盖 bucket 分析表明，IST 和 BCA 互补，BCA 还能改善长尾曝光。

## 最值得记住的一句话
用于解码的固定长度 ID 不一定是好的上下文表示；历史侧做语义子词压缩、目标侧保留固定长度，才能更有效地分配注意力，稳定提升生成式推荐。
