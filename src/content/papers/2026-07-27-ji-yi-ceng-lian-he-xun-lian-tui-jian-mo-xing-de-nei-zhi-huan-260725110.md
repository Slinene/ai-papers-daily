---
title: 'Memory Layer: Train the In-Model Cache for Recommendation Models'
title_zh: 记忆层：联合训练推荐模型的内置缓存
authors:
- Liangyuan Na
- Gufan Yin
- Yixin Bao
- Xianjie Chen
- Justin Lin
- Ziheng huang
- Xinyuan Zhang
- Wen Zhang
- Hao Lin
- Xiaoheng Mao
affiliations:
- Meta
arxiv_id: '2607.25110'
url: https://arxiv.org/abs/2607.25110
pdf_url: https://arxiv.org/pdf/2607.25110
published: '2026-07-27'
collected: '2026-07-29'
category: RecSys
direction: 训练-服务一致性 · 嵌入式缓存联合训练
tags:
- Training-Serving Consistency
- Embedding Cache
- Cold Start
- Online Training
- Memory Layer
- MPZCH
one_liner: 将物品嵌入缓存变为训练-服务共享的可写组件，消除表示不一致，冷启动提升5-6%，NE gap降低86%
practical_value: '- **将离线批量评估替换为可训练的嵌入缓存**：在粗排/精排中，可将物品塔输出写入共享嵌入表，训练时直接读取该表计算损失，推理时也读取同一表，消除特征源和新鲜度差异，大幅缩小训练-服务
  NE gap。

  - **Writeback 精确赋值技巧**：用学习率 η=1 的 SGD 优化器，通过构造梯度 g_wb = cached − target 实现 exact
  assignment，将物品塔输出写入缓存，无需额外优化器状态或自定义 CUDA 内核，工程实现简单。

  - **多表训练（Multi-Table Training）覆盖全候选池**：同时将从训练流和候选池流读取数据，合并特征后通过一次物品塔前向写入缓存，训练损失仅用训练样本，确保缓存包含全量候选物品，不再依赖单独的每小时批量评估服务，降低维护复杂度。

  - **Raw Embedding Streaming 实时更新缓存**：在训练 TBE 预取时捕获更新后的嵌入，通过异步流水线每秒推送到预测器，达到约 20
  秒延迟，比分钟级批量流式更新显著提升新鲜度，冷启动物品召回提升超 2×。

  - **Always-on 兜底消除硬 fallback**：用少量通用特征（如作者 ID）生成 always-on 嵌入，缓存命中时与缓存嵌入融合，缺失时只用
  always-on 嵌入，模型通过学习自动调节依赖权重，使冷启动物品和缺失物品仍能获得合理分数，避免固定负分或随机降级导致的体验和指标损失。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
推荐系统早期排序阶段（ESR）受延迟限制，常采用预计算物品嵌入并缓存的架构，但缓存仅在推理时存在，与训练解耦，导致训练-服务表示不一致：物品塔新鲜度滞后、特征源差异、缓存缺失处理不佳。这些问题造成训练 NE 与线上 NE 之间存在 5-12% 的差距，且新鲜内容覆盖率仅约 96%，冷启动物品被固定负分跳过或降级。

**方法关键点**
1. **Memory Layer**：将物品嵌入缓存作为模型的一部分（MPZCH 稀疏嵌入表），训练时物品塔写入，推理时模型读取，建立单一表示源。
2. **Writeback 机制**：利用精确 SGD（η=1）将物品塔输出 a 直接赋值给缓存行，不通过梯度下降逐步收敛，实现每次迭代精确更新，无需额外优化器。
3. **Always-on Embeddings**：引入少量通用特征（如作者 ID）作为兜底，训练时混合缓存与 always-on 嵌入，推理时缓存缺失则仅用 always-on，使每个物品都可评分，冷启动物品获得合理初始分数。
4. **Multi-Table Training**：训练时同时读取交互数据和候选池数据，合并物品特征送入物品塔，仅交互样本计算损失，但全部物品嵌入写入缓存，保证缓存覆盖全候选集，消除离线批量评估。
5. **Raw Embedding Streaming (RES)**：在 TBE 预取时捕获更新嵌入，异步流水线每 15 秒推送至预测器，新鲜度从 O(5 min) 提升至 O(20 s)。
6. **MPZCH 存储后端**：零冲突多探头哈希、LRU 驱逐、GPU/CPU 分布式推理，支持百亿级物品表。

**关键结果**
- 部署在 Instagram Reels 粗排阶段，预测覆盖率从 96% 提升到 100%，缓存命中率 99.5%。
- 嵌入新鲜度提升至 P99 约 21 秒，冷启动物品视频观看量在 5 分钟内提升超 2×。
- 冷启动参与度（reshare、时长）提升 5-6%，topline 冷启动 breakout 率 +5-6%，P25 创作到首曝时间缩短 40-45%。
- 训练-服务 NE gap：pselect 从 12.11% 降至 1.64%（86% 降幅），reshare 从 5.24% 降至 3.42%（35% 降幅）。
- 整体训练+发布计算成本降低 30%，推理成本持平，可靠性提升。

**核心 insight**
将独立的推理缓存变为与模型联合训练的状态，可以根本性解决表示不一致，同时通过 always-on 兜底和实时流式更新，将冷启动和召回覆盖率问题一并解耦，而不需要额外的特殊组件。
