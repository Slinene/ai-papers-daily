---
title: X-Rec Technical Report
title_zh: X-Rec 技术报告：基于流匹配的连续嵌入生成式召回
authors:
- Chenglei Shen
- Chenzhe Huang
- Dong Jiang
- Hongjie Gao
- Jue Zhang
- Kun Xú
- Lincan Cai
- Nan Zhuang
- Pan Zhang
- Shi Chen
affiliations:
- ByteDance
- TikTok
arxiv_id: '2609.29180'
url: https://arxiv.org/abs/2609.29180
pdf_url: https://arxiv.org/pdf/2609.29180
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · 连续嵌入 Flow Matching
tags:
- Flow Matching
- Generative Retrieval
- Riemannian Flow Matching
- Late Interaction DiT
- Semantic ID
- Recommender Systems
one_liner: 用 Riemannian Flow Matching 在连续 item embedding 空间直接建模推荐分布，兼得 SID-AR 表达力与
  3.46 倍推理吞吐
practical_value: '- **借鉴连续嵌入生成式召回替代 SID-AR**：如果你的 item 已有归一化 embedding（如双塔/对比学习），可以直接用
  Flow Matching 在连续空间建模 p(x|c)，避免量化误差和自回归解码，吞吐提升 3.46×，召回与 SID-AR 持平。\n- **Anchor
  Conditioning 实现粗到细生成与多样性控制**：先预测目标 item 的粗粒度簇 anchor，再基于 anchor 生成 fine embedding；该设计在
  TikTok 上提升 Recall@20 2.05pp，且通过调节 anchor 采样温度可直接控制召回多样性，电商场景可对应类目/品牌/价格带等粗粒度约束。\n-
  **Late-Interaction DiT 大幅提升推理效率**：只在最后一层 Transformer 做 velocity 估计，复用前缀 KV cache，1
  层相比 14 层仅掉 1.05pp 召回，但吞吐提升 8.28×；适合对 QPS 敏感的在线召回系统。\n- **两阶段训练：先序列预训练，再检索事件 SFT**：用因果
  attention mask 和前缀 mask 并行计算多步损失；预训练带来 5.27pp 召回提升，建议落地时先在大规模用户序列上预训练，再在具体业务场景 SFT。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
传统 U2I 把用户上下文编码成 1 个或少量固定 embedding，本质是 delta 分布，难以刻画多峰兴趣；SID-AR 虽有更强表达力，但 item 量化成 Semantic ID 会引入量化误差且自回归解码吞吐低。X-Rec 希望直接在连续 item embedding 空间建模推荐分布，同时兼顾表达力和效率。

**方法关键点**  
- 用 **Flow Matching** 学习从噪声到目标 item embedding 的 velocity field，推理时生成多个 embedding trigger 做 ANN 召回。  
- **Anchor Conditioning**：先预测目标 item 的粗粒度 cluster index，再基于 anchor 条件生成 embedding，实现 coarse-to-fine 生成，降低难度并支持多样性控制。  
- **Riemannian Flow Matching**：在单位超球面上沿 geodesic 插值，与 ℓ2 归一化的 item embedding 几何对齐，避免欧氏空间 off-manifold 问题。  
- **Late-Interaction DiT**：只在最后一层 Transformer 计算 velocity，复用历史序列的 KV cache，极大降低重复计算。  
- **两阶段训练**：先在大规模用户序列上做自回归预训练，再用特定 retrieval events 做 SFT，带特殊 attention mask 实现并行计算。

**关键实验**  
在 TikTok 流式 benchmark（47 个连续分区）上，X-Rec 平均 Recall@20 达 10.76%，显著优于 U2I 基线（SASRec 1.03%、LRURec 1.19%、DreamRec 4.30%），与 SID-AR 方法（X-Rec-AR 10.23%）持平；1 层 late-interaction 生成吞吐 575.7 QPS，是 X-Rec-AR 的 3.46 倍。消融显示：去掉 anchor 掉 2.05pp，去掉 RFM 掉 1.78pp，去掉预训练掉 5.27pp。线上部署在 TikTok 特定垂直内容，连续两次上线分别带来垂直 engagement +4.1484% 和总 engagement +0.0111%。

**最值得记住的一句话**  
在连续 item embedding 空间用 Flow Matching + anchor conditioning + late-interaction DiT 做生成式召回，可以在大模型表达力和工业级吞吐之间取得目前最优的折中。
