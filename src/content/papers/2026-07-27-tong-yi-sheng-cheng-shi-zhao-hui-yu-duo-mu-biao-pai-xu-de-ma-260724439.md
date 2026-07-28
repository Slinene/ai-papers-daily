---
title: Unifying Generative Recall and Multi-Objective Ranking in a Single Decoder-Only
  Sequence
title_zh: 统一生成式召回与多目标排序的单解码器序列模型
authors:
- Ruochen Yang
- Shuang Wen
- Pengbo Xu
- Yusheng Huang
- Jiangxia Cao
- Shuang Yang
- Zhaojie Liu
- Jiawei Sheng
- Tingwen Liu
affiliations:
- Institute of Information Engineering, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Kuaishou Technology
arxiv_id: '2607.24439'
url: https://arxiv.org/abs/2607.24439
pdf_url: https://arxiv.org/pdf/2607.24439
published: '2026-07-27'
collected: '2026-07-28'
category: GenRec
direction: 生成式推荐 · 统一召回排序
tags:
- Generative Recommendation
- Multi-Objective Ranking
- Decoder-Only Transformer
- LoRA
- Prefix-Causal Attention
- Unified Model
one_liner: 用单个解码器Transformer和双查询前缀因果注意力统一生成式召回与多目标排序，表示耦合而优化隔离
practical_value: '- **统一序列设计可迁移**：将用户上下文、SID 生成轨迹、商品特征拼接为一个异构序列，在电商/广告的生成式召回+排序场景中可直接借鉴，消除两段式冗余编码，并且让排序阶段能直接消费召回轨迹中的语义信息，而不是只拿离散候选列表。

  - **双查询前缀因果注意力 (DQ-PCA) 实现任务隔离**：为召回分支提供前缀因果可见性，为排序分支提供双向注意力但仅关注用户画像和生成轨迹，同时共享基础注意力权重。这种设计能有效防止排序梯度干扰自回归生成，适合电商多任务联合训练。

  - **LoRA 作为优化隔离的低成本适配手段**：在基础 Transformer 上冻结生成主路径，仅通过 Low-Rank 适配器为排序侧提供任务专用表示学习，既保护了生成式召回的质量，又恢复了排序侧的深层特征交互能力，对电商的稀疏目标（如赠礼、收藏）提升显著。

  - **推理缓存复用与并行化部署**：生成召回阶段计算的用户上下文和 SID 轨迹 KV 缓存可直接传给排序阶段复用，与外部策略过滤并行执行，大幅减少推理延迟（实验中减少
  54% 推理时间），适合大规模电商/直播推荐系统的在线服务降本增效。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

### 动机
工业推荐系统通常将召回与排序分成两级独立模型，但这会导致目标不一致、候选传递中的信息损失以及用户侧上下文的重复编码。生成式召回（基于语义 ID 的自回归生成）与 Transformer 排序模型在架构上日益趋同，为统一建模提供了机会。然而直接共享参数会因两个任务所需的信息可见性与优化方式不同而产生优化冲突。

### 方法关键点
- **统一异构序列**：将用户行为序列与画像（用户段）、SID 生成轨迹（生成段）、商品特征（排序段）拼接为一个序列，喂入同一个 Decoder-Only Transformer。
- **双查询前缀因果注意力 (DQ-PCA)**：召回查询对用户段和自身历史可见（前缀因果），排序查询仅关注用户画像和生成轨迹（部分双向），共享注意力权重但保持任务可见性分离。
- **优化隔离与 LoRA 适配**：生成路径与排序路径的 FFN 独立，排序侧在 Q/K/V 投影中注入 Low-Rank 适配器，既冻结生成主参数（防止排序梯度干扰），又赋予排序自适应特征融合能力。
- **两阶段训练**：先仅用 NTP 损失训练生成召回，获得稳定的 SID 分布拟合能力，再加入多目标 BCE 损失联合训练，避免排序噪声早期破坏生成语义。
- **推理部署**：召回阶段产生的用户前缀和 SID 轨迹 KV 缓存直接被排序复用，排序仅需计算新增的商品特征 token 和 LoRA 路径，同时与策略过滤服务并行，隐藏排序延迟。

### 关键结果
在快手直播真实数据集（4 亿用户、30 万主播）上离线评估：
- 召回指标（Show Click）：UniR2 对比最强生成式基线 PROMISE，HR@64 提升 4.54%，MRR@64 提升 3.39%。
- 排序指标（CTR/LVTR/GTR AUC）：对比在线 MMoE 排序模型，AUC 分别提升 0.75%、1.13%、0.16%，UAUC 提升 1.45%、0.42%、0.18%。
- 在线 A/B 测试（5% 流量）：快手 App 播放量 +1.177%，关注率 +0.655%，点赞率 +2.560%；快手极速版赠礼人数 +0.717%，赠礼意图 +1.567%，赠礼总额 +2.569%。
- 推理效率：端到端推理时间减少 54.29%。
