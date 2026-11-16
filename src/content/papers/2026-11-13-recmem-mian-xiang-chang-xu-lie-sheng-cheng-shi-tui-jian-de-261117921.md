---
title: 'RecMem: Recurrent Memory Compression for Long-Sequence Generative Recommendation'
title_zh: RecMem：面向长序列生成式推荐的循环记忆压缩
authors:
- Haoyi Hu
- Gaoyang Guo
- Yunjia Xi
- Wen Chen
- Weiwen Liu
- Jian Wu
- Yuning Jiang
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Taobao & Tmall Group of Alibaba
arxiv_id: '2611.17921'
url: https://arxiv.org/abs/2611.17921
pdf_url: https://arxiv.org/pdf/2611.17921
published: '2026-11-13'
collected: '2026-11-16'
category: GenRec
direction: 生成式推荐 · 循环记忆压缩
tags:
- Generative Recommendation
- Recurrent Memory
- Memory Compression
- Long Sequence
- Stream Consistency
- HSTU
one_liner: 固定16个记忆槽压缩归档历史，配合流一致性训练，在216 token上下文下保持HSTU-1200约97% R@200
practical_value: '- 在电商长序列生成式推荐/LLM4Rec 中，可将交互历史分成 archived prefix 与 recent suffix，用固定数量
  memory slots（如 16）通过 slot-wise forget gate 增量压缩早期历史；decoder 只消费 memory + recent
  window，避免 context 随历史线性增长。推理时持久缓存 memory state，新 segment 只做一次 O(1) 更新，单用户 state
  仅 8 KiB（对比 PHSTU 432 KiB），适合高并发线上服务。

  - 架构上采用 bifurcated encoder-decoder：底层 HSTU 共享、上层分开做 memory encoding 和 next-item
  decoding。实验显示在相近参数下比复用同一 backbone（SharedStack-16）和浅分支（SplitTop-6/5/5）更好；工程上可以作为轻量但有效的多任务分支设计参考。

  - 训练时引入 stream-consistency：从同一前序 memory 出发，比较「顺序处理最后两段」与「打包成一段处理」的预测分布 KL，作为局部代理约束处理顺序稳定性。该方法成本低，能带来稳定的小幅提升（两个种子
  R@10 +0.089/+0.813），适合流式更新与离线训练不一致的场景。

  - 使用 rollout curriculum + burn-in 稳定循环状态梯度，先从无梯度 burn-in 段构造真实 memory，再逐步增加 rollout
  段数；这可以迁移到任何需要长程循环 rollout 的序列模型训练中，减少梯度爆炸/不稳定。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

生成式推荐能从更长交互历史中获得更丰富的用户偏好，但直接送入 Transformer 会带来上下文、GPU 显存和推理延迟的线性增长。在电商场景中用户历史可达数千条，完全保留不现实。

**方法关键点**
- 将历史分为 archived prefix 和 recent suffix（默认各 200），archived prefix 按 200 一段切成 K 段，用固定 M=16 个 memory slots 循环压缩；decoder 只接收 memory slots + recent items，共 216 token，与历史长度无关。
- 每步更新采用 slot-wise forget gate：g_t = sigmoid(W_g mean_s + b_g)，M_t = G_t ⊙ M_{t-1} + (1-G_t) ⊙ candidate_M；每个 slot 独立做 norm 投影防爆炸，且 padding-only segment 自动跳过更新。
- 使用 bifurcated encoder-decoder：底层 8 个 HSTU block 共享，上层 8 个 encoder block 负责 memory encoding，8 个 decoder block 负责 next-item decoding；encoder 输入为 [M_{t-1}; E(S_t); Q]，在 query token 位置读取候选 memory。
- 训练目标：NCE loss 作用于 recent suffix 的 shift 预测；stream-consistency loss 对齐「顺序处理最后两段」与「打包成一段处理」的预测分布 KL（stop-gradient 在 packed 分支），λ=0.05。Rollout curriculum 先 burn-in 构造真实状态，逐步增加梯度回传段数。
- 理论：在 contraction（ρ<1）和 approximate semigroup consistency（ε）假设下，顺序与打包处理的状态差异上界为 ε/(1-ρ)，与历史长度无关。

**关键结果**
在 MerRec 上，RecMem-Stream 仅用 216 decoder token（HSTU-1200 的 1/5.6），保留 HSTU-1200 的 87.9% R@10 和 97.0% R@200；比 PHSTU 高 9.622/11.096 个百分点（R@10/R@200），也比 recent-only 和 retrieval baseline 更好。相同 checkpoint 在 6,442 用户固定 cohort 上评估到 10,000 交互，R@10/R@200 在 40.519–40.689 / 69.867–70.379 之间稳定。模型计算上，每用户 state 8 KiB、warm latency 7.653 ms，对比 PHSTU 432 KiB/9.245 ms、HSTU-1200 106.613 ms。

**最值得记住的一句话**：固定数量 memory slots + slot-wise forget gate 将长历史压缩成 O(1) 状态，stream-consistency 约束顺序/打包一致性，在生成式推荐中以极小上下文代价逼近全历史效果。
