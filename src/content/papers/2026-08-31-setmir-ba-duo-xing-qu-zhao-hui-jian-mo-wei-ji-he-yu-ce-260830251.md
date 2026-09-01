---
title: 'SetMIR: Multi-Interest Retrieval as Set Prediction'
title_zh: SetMIR：把多兴趣召回建模为集合预测
authors:
- Xiaodong Liu
- Congfei Zhang
- Hsiang-wei Chao
- Siman Wang
- Xiao Bai
- Tong Zhao
- Jingxiao Ma
- Wen Zhang
- Zhe Liu
- Shantanu Aggarwal
affiliations:
- Snap Inc.
arxiv_id: '2608.30251'
url: https://arxiv.org/abs/2608.30251
pdf_url: https://arxiv.org/pdf/2608.30251
published: '2026-08-31'
collected: '2026-09-01'
category: RecSys
direction: 多兴趣向量召回 · Set Prediction
tags:
- Multi-Interest Retrieval
- Set Prediction
- Hungarian Matching
- Presence Gating
- ANN Query Reduction
- Interest Collapse
one_liner: 用 Hungarian 一对一匹配 + presence 门控解决多兴趣召回的兴趣坍缩与固定 ANN 预算问题
practical_value: '- 如果现有多兴趣召回存在 interest collapse，可以直接把 argmax 目标分配换成 Hungarian 一对一匹配，并给未匹配
  query 明确的 absence 标签；训练成本低，只增加一个小型匹配步骤。

  - 在 ANN 召回侧做动态 query 调度：presence head 先过滤低置信兴趣，再做 query-level NMS 去冗余，平均 ANN 调用可减少
  33% 而召回几乎不降；线上可先离线扫描 τ、δ 找安全阈值。

  - 已有统一 item embedding 和 ANN 索引时，可以在 user 侧加 learnable queries，item 侧保持单向量，避免改造索引；event-type
  的 α-gated embedding 初始化 α=0，能平滑引入行为信号。

  - K 不一定要很大：实验里 K=7 已接近 K=10 的 99.8% R@10，生产可先用较小 query bank 控制 decoder 成本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
单 user embedding 常把用户多兴趣压缩成主导类别，丢失窄而短期的意图。现有多兴趣召回主要存在两个问题：一是 interest collapse，argmax 分配会让多个 target 撞到同一个 query，未匹配 query 收不到梯度；二是 static dispatch，固定发满 K 路 ANN，部分 query 冗余仍占用预算。

**方法关键点**
- 将多兴趣召回建模为 set prediction：K 个 learnable queries 经 transformer decoder 输出 K 个兴趣 embedding 和 presence score。
- 训练时用 Hungarian matching 做 target-query 一对一匹配，cost 同时考虑 embedding 相似度和 presence logit；匹配上的 query 走 InfoNCE，未匹配 query 只接收 absence 监督。
- 额外加 margin diversity loss，仅惩罚高 presence 且余弦相似度超过 0.3 的活跃 query 对。
- 输入侧用 frozen 预训练 item embedding，事件类型 embedding 通过 α-gated 加法引入，α 初始化 0，逐步学到行为信号。
- 推理时 presence threshold τ=0.3 先 gate，再做 query-level NMS δ=0.9 去冗余，幸存 query 各发一路 ANN，top-M_q = ⌈N/˜K⌉ 保持总召回深度，最后 max-merge。

**关键实验**
在 Snap DPA 数据上与 MIND、ComiRec-SA、DCM、KuaiFormer 对比，共享同一 frozen item embedding 和召回预算，SetMIR 在所有指标上最优，同时每请求平均只发 6.70 路 ANN，比 baseline 的 10 路少 33%。在线 A/B 叠加到生产检索后整体 CVR +3.11%；在相同 item embedding、ANN 索引和 quota 下，相比 item-to-item 源 CTR +44%、CVR +51%。

**最值得记住的一句话**
Hungarian 一对一匹配 + presence 门控，把固定 K 路 ANN 变成按请求动态调度，既缓解兴趣坍缩又省 33% 召回预算。
