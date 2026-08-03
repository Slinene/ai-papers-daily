---
title: 'GALA: Generative Aligned Learning for Adaptive Multimodal Representation in
  the Taobao Shangou Recommender System'
title_zh: GALA：淘宝上购推荐的自适应多模态生成式对齐学习
authors:
- Jiping Liu
- Zhongmin Zhang
- Zisen Sang
- Zhijia Fang
- Tao Ouyang
- Ma Jiang
- Shaopeng Liang
- Zeyang Hou
- Guodong Cao
- Jia Jia
affiliations:
- Rajax Network Technology (Taobao Shangou of Alibaba)
- Central South University
arxiv_id: '2607.29213'
url: https://arxiv.org/abs/2607.29213
pdf_url: https://arxiv.org/pdf/2607.29213
published: '2026-07-31'
collected: '2026-08-03'
category: RecSys
direction: 多模态推荐 · 生成式RL对齐 · 自适应融合
tags:
- multimodal representation
- reinforcement learning
- recommendation system
- food delivery
- adaptive fusion
- industrial deployment
one_liner: 三阶段流程：行为感知预训练、GRPO行为对齐、自适应门控融合，使多模态嵌入动态匹配用户意图，提升排序效果
practical_value: '- 利用搜索日志构造查询-图像-文本三元组进行对比预训练，可迁移至电商搜索推荐场景，提升多模态表示的用户意图感知能力。

  - 中间阶段用 GRPO 基于转化奖励优化多模态嵌入，使其与行为目标对齐；该方法可抽象为“用 RL 微调内容表征适应排序目标”，适合有交互序列的场景。

  - 自适应门控融合层根据 ID 特征动态加权多模态与 ID 贡献，配合辅助损失防止门控偏向 ID 分支；这种结构可直接用于有强 ID 特征的推荐模型，提升内容特征的实际利用率。

  - 离线计算嵌入、在线 KV 查表的部署范式，兼顾效果与毫秒级延迟要求，对大规模推荐系统有直接工程参考价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
多模态特征在外卖推荐中至关重要，但当前主流两阶段方案（先预训练图文对齐、再冻结嵌入喂入排序模型）导致内容语义与用户行为目标错位，且 ID 特征主导的排序模型易抑制多模态贡献。为弥合预训练与微调之间的 Gap，引入生成式行为对齐成为关键。

**方法关键点**
- **阶段 1：域自适应交叉模态对齐**。从搜索日志挖掘查询→购买的店铺，构造（查询，图像，文本）三元组，用对比损失同时对齐文本-图像、查询-文本、查询-图像和查询-融合表示，使多模态嵌入直接捕捉用户意图。
- **阶段 2：生成式行为对齐 (GRPO)**。用 LLM（Qwen2.5-7B）接收融合 prompt（上下文+历史店铺+候选店铺，嵌入替换为阶段1输出），预测下一购买店铺的索引。先用大模型蒸馏生成推理文本 SFT 预热，再通过 GRPO 以转化奖励（购买正确=1）优化模型参数和店铺嵌入，使嵌入动态对齐行为序列和互补模式。
- **阶段 3：自适应融合**。在排序模型中，对用户序列和目标店铺分别做 ID 和模态交互，输出拼接后经门控网络（sigmoid）加权融合，门控输入来自 ID 表示，实现头/尾店铺的差异化模态权重。同时添加辅助损失直接监督模态分支，缓解门控向 ID 倒塌。

**实验结果**
- 召回任务：GALA（T5+GRPO）平均 Recall@K 达 0.877，比 GME（1536d）高 3.4 %，且只有 128 维。
- 排序：CTR AUC 0.7263（对比 MMREC 0.7242），CVR AUC 0.8193（0.8158），PCOC 更接近 1。
- 分 shop 层分析显示长尾店提升更显著，且门控权重确实随尾部增加而向多模态倾斜。
- 在线 A/B 测试：总订单量 +0.55 %。
