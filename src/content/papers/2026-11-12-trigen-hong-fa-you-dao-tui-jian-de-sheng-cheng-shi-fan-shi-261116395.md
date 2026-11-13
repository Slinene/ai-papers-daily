---
title: 'TriGen: A Generative Paradigm for Trigger-Induced Recommendation'
title_zh: TriGen：触发诱导推荐的生成式范式
authors:
- Muyu Zou
- Haibo Xing
- Shunye Tang
- Liyan Tie
- Lingyu Mu
- Yandong Wang
- Jinxin Hu
affiliations:
- Alibaba International Digital Commerce Group
- Nankai University
- Independent Researcher
arxiv_id: '2611.16395'
url: https://arxiv.org/abs/2611.16395
pdf_url: https://arxiv.org/pdf/2611.16395
published: '2026-11-12'
collected: '2026-11-13'
category: GenRec
direction: 生成式推荐 · 触发感知 SID 生成
tags:
- Generative Recommendation
- Semantic ID
- Trigger-Induced Recommendation
- Encoder-Decoder
- Adaptive Fusion
- Online A-B
one_liner: 面向触发诱导推荐提出 TriGen，通过尾部重复注入、双路径动态融合与位置特定 PFFN 平衡历史偏好与即时意图，线上收入 +3.27%
practical_value: '- 若业务存在“详情页点击进入相似/搭配/相关推荐 feed”的 TIR 场景，可直接借鉴 TriGen 的生成式 SID 方案；相比加
  trigger 特征后排序，生成式能在 token 级控制推荐，且东南亚 6 国线上收入 +3.27%、GMV +0.90% 证实生产可用。

  - Calibrated Tail Injection 最容易落地：把 trigger 的 Semantic ID 重复 N 次拼接在历史尾部，配合 RoPE，N
  作为超参（文中 1–5 之间）调节 trigger 强度；解决长序列中单一 trigger 被历史稀释的问题，工程成本极低。

  - Adaptive Dual-Path Fusion 的“trigger path + history path + 轻量门控”可复用到任何需要平衡即时意图与长期画像的任务，如搜索
  query 推荐、Agent 对话上下文化；两条路径均值池化拼接后 sigmoid 输出逐层权重，开销小且能 per-request 自适应。

  - 若使用分层 Semantic ID 生成，不要只在 BOS 处注入条件或用共享投影；为每个解码位置独立 MLP 并加到每步输入，能维持粗到细的粒度引导。TriGen
  线上延迟仅 10.5ms，组件对服务影响可忽略，适合增量替换。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
生成式推荐多在 User-Induced Recommendation (UIR) 设定下，从长期历史自回归生成 Semantic ID；但电商详情页点入后续 feed 是典型 Trigger-Induced Recommendation (TIR)，点击物品作为显式 trigger 代表即时意图，必须动态平衡“历史偏好连续性”与“触发驱动的意图转移”。现有生成式模型缺 trigger 机制，判别式 TIR 方法只能打分无法控制 token 生成，简单把 trigger 拼进序列或作为条件会被长历史稀释或过度窄化。

**方法关键点**  
- **Calibrated Tail Injection**：将 trigger 表示重复 N 次追加到编码器输入尾部，丢弃最旧 N 个行为保持窗口；尾部位置 + RoPE 让 trigger 与最近行为直接交互，N 调节 trigger 在 self-attention 中占用的容量。
- **Adaptive Dual-Path Fusion**：从原始历史分别用 trigger 作为 query 和 learnable default queries 做 attention，得到 trigger path 与 history path；二者均值池化拼接后经 sigmoid 产生每个 SID 层级的融合权重，逐层凸组合得到条件序列。
- **Position-Specific Trigger-PFFN**：每个解码位置用独立 MLP 投影对应条件向量，加到 decoder 输入 token embedding（BOS/上一 token），使 trigger 引导按 SID 从粗到细持续作用于自回归解码。

**关键结果**  
工业数据集（49.3M 用户、1.49B 样本）和 Amazon Industrial_and_Scientific 上对比 DIHN/DIAN/DEI2N、GRU4Rec/SASRec、TIGER/HSTU/LC-Rec 及三个简单 TIR-GR 变体。工业上 TriGen R@5 5.58、R@10 15.50，显著超过最佳简单变体（4.46/12.15）和生成式基线；Amazon 上 TriGen R@5 10.83、N@10 9.21，也优于强基线。消融证明三组件都有效；触发重复次数呈倒 U 曲线。线上 A/B 在 6 国市场全量部署，流量加权收入 +3.27%、GMV +0.90%，推理延迟约 10.5ms。

**最值得记住的一句话**：TIR 生成式推荐中 trigger 不能只作为普通特征，需要在编码、表示、解码三个层级分别校准：尾部重复注入控制影响力、双路径门控动态平衡历史与即时意图、按 SID 位置注入条件维持从粗到细的引导。
