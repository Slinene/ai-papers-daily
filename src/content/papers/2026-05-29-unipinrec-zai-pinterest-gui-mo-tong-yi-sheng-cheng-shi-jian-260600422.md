---
title: 'UniPinRec: Unifying Generative Retrieval and Ranking at Pinterest Scale'
title_zh: UniPinRec：在 Pinterest 规模统一生成式检索与排序
authors:
- Hanyu Li
- Yi-Ping Hsu
- Aditya Mantha
- Prabhat Agarwal
- Laksh Bhasin
- Jialu Wang
- Hongtao Lin
- Bella Huang
- Yaxin Li
- Xinyi Li
affiliations:
- Pinterest
arxiv_id: '2606.00422'
url: https://arxiv.org/abs/2606.00422
pdf_url: https://arxiv.org/pdf/2606.00422
published: '2026-05-29'
collected: '2026-06-02'
category: RecSys
direction: 统一检索与排序的全栈推荐
tags:
- Unified Retrieval and Ranking
- Generative Retrieval
- Masked Action Modeling
- KV Cache Sharing
- Production Recommendation
- Transformer
one_liner: 通过掩码动作建模、联合训练与跨进程 KV 缓存共享，实现检索和排序的全栈统一，线上提升互动并降低延迟。
practical_value: '- **掩码动作建模（MAM）**：将排序监督直接融入检索的序列输入，随机掩码历史动作避免序列长度膨胀，实现检索与排序共享同一主干，可快速复用到多任务推荐场景。

  - **跨阶段 KV 缓存共享**：通过 GPU 内存池 + CUDA IPC 实现进程间零拷贝传输，排序阶段复用检索生成的用户历史 KV，将排序的计算量从 O(n²)
  降至 O(nk)，显著降低在线延迟。

  - **统一训练数据构造**：采用 feedview（展示集）作为排序监督，构建“过去行为序列 + 未来展示列表”的统一样本，结合 Ray 在线桶连接避免数据膨胀，为级联模型的联合训练提供了可落地的数据管线范式。

  - **增量上线策略**：先替换检索+轻量排序（L0+L1），再逐步扩展到精排，保持与现有系统兼容，支持分阶段 A/B 测试和回滚，降低统一模型部署风险。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
现代推荐系统检索和排序两个阶段使用相同的用户行为数据，却独立训练和部署，导致参数、训练和推理成本严重重复。统一这两个阶段成为降本增效的核心目标，但面临输入格式不兼容、训练目标分歧和跨阶段计算冗余三大挑战。

**方法关键点**
- **掩码动作建模（MAM）**：在非交织的用户行为序列中，将动作多热向量与物品嵌入拼接，随机掩码部分历史动作，使得同一序列可同时用于检索（下一物品预测）和排序（动作预测），避免序列长度翻倍，实现参数完全共享。
- **联合训练**：损失函数由检索的采样 softmax 损失和排序的分动作二分类交叉熵损失加权求和构成，两种任务梯度同时更新共享主干，排序监督信号反哺检索表示。
- **统一数据构造**：以 feedview 为中心，将用户历史行为序列与后续展示集（含曝光未点击负样本）拼接，通过 Ray 在线桶连接避免数据冗余，正负采样比可训练时动态调整。
- **跨阶段 KV 缓存共享**：检索编码用户历史后，将 KV 状态写入 GPU 内存池，排序进程通过 CUDA IPC 直接映射访问，无需 CPU 中转；排序仅计算候选与历史的交叉注意力，成本降为 O(nk)。

**关键结果**
- 离线评估：UniPinRec 在召回 Recall@10 与专用检索模型持平（0.7766 vs 0.7749），排序 Hit@3 比生产排序模型提升 +14.8%（0.1010 vs 0.0880），且超越仅排序变体和微调方案。
- 在线 A/B：在 Pinterest 的 Board More Ideas 上 saves 提升 +0.95%，通知推送打开率提升 +0.91%，端到端延迟降低 -11.1%，QPS 提升 +63.6%。

**核心takeaway**
掩码动作建模实现了检索和排序在同一个非交织序列上的联合训练，跨进程 KV 缓存共享则让排序几乎以零额外计算代价融入检索链路，为工业级级联推荐系统的全栈统一提供了可复制范式。
