---
title: 'Quantizing Intent: Cross-Domain Semantic IDs from Organic Activity for Industrial
  Ranking'
title_zh: 量化意图：基于有机活动的跨域语义ID用于工业广告排序
authors:
- Julie Choi
- Haoran Ye
- Zhiwei Ding
- Bo Long
- Benjamin Zelditch
- Arpita Vats
affiliations:
- LinkedIn
arxiv_id: '2606.01396'
url: https://arxiv.org/abs/2606.01396
pdf_url: https://arxiv.org/pdf/2606.01396
published: '2026-05-31'
collected: '2026-06-02'
category: RecSys
direction: 跨域语义ID · 行为活动丰富度
tags:
- Semantic IDs
- Cross-Domain
- Ads CTR
- Residual Quantization
- Cold Start
- RQ-FSQ
one_liner: 提出跨域用户语义ID和行为活动丰富度原则，利用有机Feed信号提升广告冷启动CTR达+1.522%，同时RQ-FSQ匹配密集AUC且存储缩小30～280倍
practical_value: '- **行为活动丰富度选源原则**：跨域特征优先选择编码近期行为信号（如浏览、互动序列）的源，而非静态画像文本。实验显示 Feed
  Activity 直接聚合行为比纯文本嵌入多 +0.177% AUC，可作为电商/广告系统选择外部特征源的直接指导。

  - **RQ-FSQ 离散化通用方案**：将预训练用户/商品嵌入离散化时，可结合残差 VQ 保留全局结构与单维标量量化保留细节，匹配甚至超过原始密集嵌入 AUC。这一方法适用于压缩
  LLM 编码器输出，在存储受限的推荐服务中能直接复用，实现 30～280 倍压缩而不掉点。

  - **HDE 模块即插即用**：使用前缀 n-gram 哈希表对任意 K 级离散 ID 序列编码，支持多源独立查表与求和，插入现有 CTR 特征层无需修改骨干网络。该设计可直接迁移到电商排序模型的特征工程环节，降低多源离散特征集成成本。

  - **冷启动行为桥接**：将非广告域（如内容浏览、社交互动）的丰富行为量化为语义 ID，作为排序模型的用户侧特征，可有效缓解新用户/稀疏用户信号不足，冷启动段
  CTR 提升达 +1.522%，对电商 Push、新客推荐场景有直接借鉴意义。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
广告点击率预测面临用户交互极度稀疏，大多数用户几乎不点击广告，导致冷启动用户仅靠画像属性预测效果差。而用户有机 Feed 活动包含大量行为信号，却因领域差异、维度高和工程复杂难以直接迁移到广告排序模型。

### 方法关键点
- **跨域用户语义ID**：从有机 Feed 行为中构建离散的 K 级语义 ID 序列，作为广告模型输入特征，实现跨域信号迁移。
- **行为活动丰富度原则**：实验证明下游 AUC 增益与源嵌入编码的行为活动量单调相关：纯画像文本仅 +0.036%，经活动微调的 LLM 嵌入 +0.107%，直接行为聚合嵌入 +0.213%。
- **RQ-FSQ 量化方法**：融合残差 VQ（保留全局几何）与有限标量量化（保留逐维细粒度结构），在 Feed Activity 和 Activity-Tuned LLaMA 两个异构源上匹配密集嵌入 AUC，存储分别减少约 30 倍和 280 倍。
- **HDE 模块**：通过前缀 n-gram 哈希表将 K 级 SID 编码为稠密用户嵌入，支持多源独立编码后求和，内存可控，可直接插入现有 Transformer 排序模型。
- **多源 SID 与缺失值填补**：采用 Activity-Tuned LLaMA 作为主干，通过训练的 VAE 量化器填补缺失的 Profile Qwen 或 Feed Activity 编码，最大化用户覆盖。

### 关键结果
在大型生产广告系统上，相比无 SID 基线，Feed Activity SID 整体 AUC 提升 +0.213%，多源 SID 提升 +0.296%；冷启动用户段收益最大，达 +1.522%。RQ-FSQ 在两个源上匹配密集嵌入 AUC 的同时大幅压缩存储。MovieLens-100K 公开数据集验证了 RQ-FSQ > RQ-KMeans 的顺序。
