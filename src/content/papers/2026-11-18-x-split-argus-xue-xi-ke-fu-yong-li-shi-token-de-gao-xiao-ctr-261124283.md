---
title: 'X-split Argus: Learning Reusable History Tokens for Efficient CTR Prediction'
title_zh: X-split Argus：学习可复用历史 Token 的高效 CTR 预测
authors:
- Alexander Ploshkin
- Nikita Stepanov
- Alexey Pismenny
- Viacheslav Ovchinnikov
- Nikolay Savushkin
arxiv_id: '2611.24283'
url: https://arxiv.org/abs/2611.24283
pdf_url: https://arxiv.org/pdf/2611.24283
published: '2026-11-18'
collected: '2026-11-19'
category: RecSys
direction: 高效长历史CTR预测与历史压缩
tags:
- CTR Prediction
- History Compression
- Knowledge Distillation
- Sequential Modeling
- Ad Ranking
one_liner: 离线压缩用户长历史为可复用 token，在线跨注意力结合近期行为，蒸馏保留 71.6% 教师增益并提升线上 ACV 4.65%
practical_value: '- **历史 compression 与 candidate scoring 解耦**：把长期历史离线压成 K 个不依赖 candidate
  的 token，在线只对 candidate 做 cross-attention；请求内近期行为编码和 memory self-attention 跨候选复用。适合电商广告长行为序列排序，能把长历史建模成本从候选数×历史长度降到候选数×(K+M)。

  - **用全历史 teacher 蒸馏指导压缩器**：teacher 保留未压缩历史，对每个 candidate 产出 click logit；student
  用单独 KD head 以 L1 拟合 teacher raw logit，梯度穿过 ranker 回到 compressor。与业务结合时，可以先训一个大 teacher
  离线，再让线上 student 用 KD loss 学习保留信息。

  - **负样本不对称 label smoothing 零成本提升**：对曝光未点击的负样本把 target 从 0 抬到 ε=0.01，点击仍为 1；离线 NE
  相对 binary 提升 0.179%，不增加训练和推理成本。CTR 训练中曝光未点击不一定是强负样本，值得尝试。

  - **模型新鲜度要按天评估和 fine-tune**：固定 checkpoint 相对优势每天约掉 0.05 pp，因此采用每日 fine-tune，数据/训练成本远小于在线推理；历史
  embeddings 用 BF16 存储，每日 batch 预计算。对长历史 online 服务是较实用的运维策略。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：CTR 预测需要同时建模长期偏好和近期意图，但线上 ranking 对每个请求处理完整用户行为历史，计算量和延迟成本不可接受；候选依赖的历史处理又难以跨候选复用。已有 ARGUS 等两塔模型支持预计算 user 表示，但历史与候选的交互有限。本文研究：能否把长期历史压缩成不依赖候选的可复用 token，并用未压缩历史的 teacher 蒸馏，使 online ranker 保留大部分预测收益。

**方法关键点**：
- X-split ARGUS 由 history compressor、runtime user encoder、candidate encoder 和 decoder with cross-attention 组成。
- Compressor 是 causal Transformer，对历史事件建模并输出 context states；对一个 prefix，取最后 K 个 state 作为压缩历史 tokens Z(b)，离线计算并缓存。
- Runtime encoder 用 sliding window causal attention 处理最近 M 个事件，得到 U；decoder 以 candidate token 作为 query，对 [Z(b); U] 做 cross-attention；可选 self-attention 只在历史 memory 上，因此仍不依赖候选，可跨候选复用。
- 训练用 observed click BCE + KD：大 teacher 处理未压缩历史，对每个 target item token 产出 click logit；student 的独立 KD head 用 L1 拟合 teacher raw logit，梯度穿过 decoder 同时更新 compressor 和 runtime encoder。
- 对曝光未点击负样本做 asymmetric label smoothing：负 target 从 0 抬到 ε=0.01，点击仍为 1。

**关键实验**：内部 RTB 数据，1 年历史，history cap 8192，约 10^9 training targets，3 天 test。对比 Context-aware ARGUS baseline 和未压缩 teacher。X-split ARGUS 相对 baseline NE 降低 0.814%，保留 teacher 71.6% 的提升。Ablation：K=8 最好，K=2 掉 0.193%，K=32 仅 +0.075%；M=256 最好，M=8 掉 0.342%；更深 encoder 继续提升；负样本 smoothing +0.179%。线上 A/B 七天，相对生产 baseline ACV +4.65%，clicks +2.96%，p<0.001；在相同 latency budget 下，需增加 15% 同类型在线 GPU。

**最值得记住的一句话**：把历史编码/压缩从在线候选打分路径中拆出来，离线生成不依赖候选的可复用 token，在线只做候选对 token 的 cross-attention，并用全历史 teacher 蒸馏保住压缩损失。
