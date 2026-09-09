---
title: 'SequenceO1: End-to-End Ultra-Long (100K) Sequence Modeling in Recommendation
  with Low-Rank Caching'
title_zh: SequenceO1：基于低秩缓存的推荐系统端到端 100K 序列建模
authors:
- Lin Guan
- Jia-Qi Yang
- Zhishan Zhao
- Jiaqi Huang
- Hangyu Wang
- Longbin Li
- Beichuan Zhang
- Haonan Jiang
- Jinan Ni
- Xiangyu Fan
affiliations:
- ByteDance
arxiv_id: '2609.08443'
url: https://arxiv.org/abs/2609.08443
pdf_url: https://arxiv.org/pdf/2609.08443
published: '2026-09-08'
collected: '2026-09-09'
category: RecSys
direction: 超长序列推荐 · 低秩缓存
tags:
- Long-sequence Modeling
- Sketch Attention
- Low-Rank Caching
- STCA
- System Co-design
one_liner: 用 Sketch Attention 将 100K 用户历史压缩为固定大小可缓存 sketch，结合两时间尺度 STCA 与缓存复用，实现端到端超长序列推荐
practical_value: '- **超长历史压缩为可缓存 sketch**：用 learnable prototypes + prototype-wise
  softmax 把 100K 行为序列压缩成固定大小（如 1K×128）的 user-only sketch。相比 token-wise softmax，prototype-wise
  归一化避免早期 token 选择、保证全局覆盖，适合作为跨目标/请求复用的长期兴趣表征。电商/广告场景可直接替换 TWIN V2 这类两阶段 lifelong
  模块，减少离线聚类+检索的系统复杂度。

  - **训练/推理缓存复用**：训练侧 local KVCache 以 userID + model version + history timestamp 为
  key，TTL 失效 + 容量淘汰；同用户多请求用 MRLB 分组，只算一次 sketch。推理侧同样缓存，命中时无需再读取/传输 100K 原始特征，路径成本
  O(1)。这是把长序列建模从学术可行变成生产可用的关键。

  - **两时间尺度推理**：近期 10K 后缀走 STCA 捕捉 recency，超长 sketch 走 STCA 捕捉长期偏好，再轻量 fusion。这个结构比单一路径更贴合真实用户行为，且近期分支成本可控。

  - **FlashSA 工程实现**：融合 kernel 流式计算 prototype-token affinities，不物化 k×n 中间矩阵，降低显存和内存带宽。对任何需要把长序列压缩成固定表示的模块都适用。

  - **对 Agent/LLM 长期记忆启发**：固定大小、用户侧、可缓存的 sketch 可作为用户长期记忆压缩层，Agent 或 LLM 检索增强推荐时，可以缓存该
  sketch 避免重复处理长上下文，与 pipeline lift 结合可进一步隐藏延迟。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
短视频推荐需要利用超长用户历史（可达 10 万甚至百万级），但精排阶段有严格延迟和吞吐约束。截断、多阶段检索（如 TWIN V2）或长度外推（如 STCA 训练短推理长）要么牺牲端到端优化，要么仍保留随序列长度增长的系统成本。100K 规模的瓶颈不只是单层计算，而是特征存储、通信、训练/推理计算的系统性成本。

## 方法关键点
- **Sketch Attention (SA)**：把 100K 历史压缩为固定大小 sketch。学习 k 个全局 prototype，计算 prototype–token affinity 后做 prototype-wise softmax（每个 token 分配到多个 prototype），再聚合得到 k×d 的 user-only sketch。该表示目标无关、长度无关、可差分、可缓存。
- **两时间尺度 STCA**：近期 10K 后缀走 STCA 捕捉 recency；sketch 走 STCA 捕捉超长信号，最后轻量 fusion。sketch 侧 STCA 成本固定，与原始长度无关。
- **缓存优先系统**：训练侧 local KVCache 缓存同用户 sketch，MRLB 将同用户多个请求/目标分组一次计算；推理侧复用同一缓存，命中时跳过原始 100K 特征读取、传输和 sketch 计算。Pipeline lift 将 user-only sketch 计算提前到请求入口与召回并行。
- **FlashSA**：融合 kernel 流式计算 affinity，不物化 k×n 矩阵，降低显存和内存带宽。

## 关键实验
在 Douyin 全量部署。离线对比生产 STCA 10K + TWIN V2，SequenceO1 移除 TWIN V2 后 Finish AUC +0.29%、Finish UAUC +0.40%，多目标全面提升；在线 A/B 中 Douyin Finish +2.33%、Dislike -6.98%，Douyin Lite Finish +3.49%。轻量消融下 SA 相比 STCA(512) 提升 +1.07% Finish AUC，保留直接扩展 STCA 增益的 83%。训练 FLOPs 降低 49.9×，推理 FLOPs 降低 63.9×。

最值得记住的一句话：**超长用户历史应先压缩成固定大小、可缓存的用户侧 sketch，再在 sketch 上做目标条件推理，从而把缓存命中路径的成本降到 O(1)。**
