---
title: 'CRIM: Composable and Reusable Item Memory for Efficient Personalized Retrieval'
title_zh: 可组合可复用物品记忆的高效个性化检索
authors:
- Haolin Li
- Haipeng Zhang
- Mang Li
- Zhaohui Xia
- Xun Zhu
- Miao Li
- Yu Zhang
- Ji Wu
affiliations:
- Tsinghua University
- Alibaba International Digital Commerce Group
arxiv_id: '2610.35323'
url: https://arxiv.org/abs/2610.35323
pdf_url: https://arxiv.org/pdf/2610.35323
published: '2026-10-26'
collected: '2026-10-27'
category: RecSys
direction: LLM 高效个性化检索 · 物品记忆压缩
tags:
- item memory
- personalized retrieval
- LLM efficiency
- context compression
- caching
- dense retrieval
one_liner: 将物品语义编码与请求历史建模分离，用可学习摘要token压缩物品为连续记忆，结合缓存与采样重编码大幅降低LLM检索成本
practical_value: '- **物品级记忆缓存替代每次请求重复编码**：在电商搜索/推荐中，同一商品会在大量用户历史中反复出现。可以离线用可学习 summary
  tokens 把商品文本压缩成少量连续向量（如4个/dim 2560），在线只做请求级组合，推理输入长度可降80%以上，延迟降低4倍。

  - **用 REC tokens 引入段内预测监督**：在用户历史里每 b=4 个商品插入一个共享 readout token，预测下一段首商品。这个中间监督能让前缀表征学会“未来交互”信息，比只靠最终检索损失提升
  Recall@100 达3.7个百分点，适合迁移到长序列行为建模。

  - **联合训练采用“缓存+采样重编码”控制梯度成本**：训练时随机采样少量历史位置用当前 encoder 重算，其余位置直接读缓存并 stop-gradient。这样既让
  item encoder 能接收检索梯度更新，又避免全量历史重编码，训练成本与历史长度解耦。电商长历史场景可直接复用，每请求只重编码 κ=4~8 个商品。

  - **定期刷新缓存而非实时更新**：epoch 结束后重建 item memory 和 candidate cache，平衡表征新鲜度与计算开销。线上部署时可结合模型更新周期做异步刷新，避免每次推理都重算商品表征。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
LLM 用于个性化搜索/推荐时，长交互历史导致训练和推理成本随历史长度线性增长，且同一商品文本在不同用户、不同请求中被反复编码，造成大量重复计算。现有压缩方法（如 ICAE、Token Factory）缺乏对交互顺序的监督，而缓存方法难以协调编码器更新与梯度路径。本文要解决三个问题：复用商品语义的同时保留请求级上下文；压缩表示同时保留语义和交互模式；在缓存使可微计算减少的情况下联合优化商品与请求编码器。

**方法关键点**
- **双模块架构**：Item Memory Encoder (IME) 独立将每个商品文本和 ID 压缩为 K=4 个连续记忆向量，Request Encoder (RE) 按交互顺序组合记忆并融合可选 query，生成个性化检索表示。商品记忆与用户/查询无关，可全局缓存复用。
- **语义预训练**：在商品目录上，用可学习 summary tokens + 受限注意力做标题重建，并与全上下文冻结 LLM 的预测分布做 KL 蒸馏，仅更新 summary/ID embeddings，为记忆提供语义初始化。
- **序列监督**：将历史切分为每 b=4 个商品的段，每段后插入共享 REC tokens，用它们预测下一段首商品，提供中间前缀的交互监督。
- **联合训练机制**：训练时每请求采样 κ=8 个历史位置用当前 IME 重编码，其余位置读缓存并 stop-gradient，检索梯度经采样位置更新 IME；同时加入段预测损失和语义重建损失。epoch 结束刷新商品记忆和候选缓存。

**关键实验**
在三个数据集上验证：新构建的 LazSeq（约3万请求、历史最长500、目录 49,993 商品）、Qilin、MovieLens-1M。CRIM 以 Qwen3-Embedding-4B 为 backbone，对比 GRU4Rec、SASRec、TIGER、GTE-1.5B、Qwen3-Embedding-4B 等。结果：LazSeq 上 Recall@100 达 0.6969，相对同 backbone baseline 提升2.49%，且推理输入长度减少80.75%，单请求延迟从367.45ms降至90.76ms（4.05x加速）；ML1M 上 Recall@100 提升33.61%；Qilin 上 NDCG@100 相对提升5.64%。成本分析显示约31.5k请求后收回额外离线成本，100万请求累计节省51.05% GPU算力。

**最值得记住的一句话**：把稳定的商品语义压缩成可缓存、可组合的连续记忆，把动态请求上下文留给轻量级请求编码器，是 LLM 长历史检索降本增效的有效路径。
