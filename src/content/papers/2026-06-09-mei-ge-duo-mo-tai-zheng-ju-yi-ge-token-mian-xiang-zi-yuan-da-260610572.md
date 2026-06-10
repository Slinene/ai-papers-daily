---
title: 'One Token per Multimodal Evidence: Latent Memory for Resource-Constrained
  QA'
title_zh: 每个多模态证据一个Token：面向资源受限问答的潜在记忆
authors:
- Zhi Zheng
- Ziqiao Meng
- Hao Luan
- Wei Liu
- Wee Sun Lee
affiliations:
- National University of Singapore
arxiv_id: '2606.10572'
url: https://arxiv.org/abs/2606.10572
pdf_url: https://arxiv.org/pdf/2606.10572
published: '2026-06-09'
collected: '2026-06-10'
category: RAG
direction: 潜在记忆表示 · 多模态RAG效率优化
tags:
- Latent Memory
- Multimodal QA
- RAG
- Evidence Compression
- Latent Space Retrieval
- Token Efficiency
one_liner: 提出 Latent Memory，将多模态证据压缩为单潜在Token进行检索与生成，以3-10倍更少生成Token达到竞争性能。
practical_value: '- **多模态商品/内容压缩**：在电商搜索或推荐中，将商品图文、详情页等证据压缩为单个潜在Token，存储和生成成本大幅降低，同时通过联合训练保留检索和生成所需的信息。

  - **Agent记忆管理**：借鉴 Latent Memory 将Agent交互历史、工具返回等多模态证据压缩为潜在Token库，支持高速相似性检索和直接注入生成，适合资源敏感的端侧Agent。

  - **三目标训练范式**：重建（保持内容）+ 对比（对齐查询与证据）+ 蒸馏（适配冻结生成器）的联合优化，可迁移至其他需要连续表示与检索的场景，如对话状态压缩、用户行为建模。

  - **跨域泛化**：在 HotpotQA 训练的压缩器直接用于多领域QA，表明压缩出的潜在Token具有良好迁移性，可借鉴以降低电商跨品类/跨场景的重复训练成本。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有RAG将检索到的原始文本或图像直接拼入生成器的提示，导致极高的token消耗和存储压力，难以在资源受限的端侧或边缘设备部署。为此，需要一种能高效压缩多模态证据、同时保持检索和生成能力的记忆机制。

**方法**：提出 **Latent Memory**，用一个小型压缩模型（LLM/VLM + LoRA）将每项证据（文本段落或图像）压缩为**单个高维潜在Token**，构成潜在记忆库。查询时，将问题也嵌入同一潜在空间，通过内积检索Top-k潜在Token，经一个可训练的投影层直接注入冻结的大模型（LLM/VLM）进行生成。训练阶段联合三个目标优化压缩器：
- **重建损失**：强制潜在Token能自回归重建原始文本（或预测图像CLIP嵌入），防止退化为纯检索标识。
- **对比损失**：让查询表示与正证据的潜在Token靠近，与负证据远离，构造统一的检索空间。
- **蒸馏损失**：让生成器在潜在Token条件化下的输出尽量模仿其基于原始证据的输出，对齐生成行为。

**关键结果**：在 HotpotQA、2WikiMultihopQA、MuSiQue 三个文本QA数据集上，用 LLaMA-8B 生成器，Latent Memory 仅用71个生成Token（k=5）达到与使用209-219 Token的BM25/稠密检索相似的F1，且跨域平均Recall@k显著更高。在WebQA多模态基准上，LLaVA-13B + Latent Memory 在图像子集上F1达69.4，仅需82 Token，而对比方案需1885 Token；平均F1可与最佳基线持平，但Token消耗仅为其1/10。消融显示重建损失对质量和检索均有意义，增加Token数可进一步提升但成本仍远低于原始证据。
