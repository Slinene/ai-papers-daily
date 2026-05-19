---
title: 'Towards Sustainable Growth: A Multi-Value-Aware Retrieval Framework for E-Commerce
  Search'
title_zh: 面向可持续增长：电商搜索的多价值感知检索框架
authors:
- Yifan Wang
- Yixuan Wang
- YiDan Liang
- Qiang Liu
- Fei Xiao
affiliations:
- Taobao & Tmall Group of Alibaba
arxiv_id: '2605.17994'
url: https://arxiv.org/abs/2605.17994
pdf_url: https://arxiv.org/pdf/2605.17994
published: '2026-05-18'
collected: '2026-05-19'
category: RecSys
direction: 生成式推荐 · 冷启动与长期生态价值
tags:
- Generative Retrieval
- E-commerce Search
- Cold-Start
- Causal Inference
- Policy Optimization
- New Item Growth
one_liner: 提出兼顾即时转化与新商品长期增长潜力的多价值感知生成式检索框架，在淘宝实现新商品GMV提升5.3%
practical_value: '- **长短期价值解耦的奖励设计**：通过 ItemLTV 反事实预测新商品的“增量交易价值”，将长期潜力量化为可优化信号，可直接迁移到电商推荐/检索的重排或混排阶段，作为长期收益的辅助目标。

  - **多价值对齐训练范式 (MoPO)**：将搜索漏斗（曝光→点击→购买）与 ItemLTV 分数统一为加权奖励，并用 clipped importance
  weight 缓解头部偏差，可复用到多目标召回模型，自动探索高潜力长尾商品。

  - **生成式检索 + Semantic ID 的冷启动方案**：利用 RQ-VAE 生成三层语义ID，并在解码时使用 trie 约束保证合法性，可借鉴到品类多、新品频出的电商场景，避免
  ID 冷启动问题。

  - **线上 A/B 测试设计**：结合用户侧（即时效率）和物品侧（长期增长）分桶实验，提供了一套评估长期生态价值的方法论，对业务中衡量新商品扶持策略的真实效果很有借鉴价值。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：电商搜索系统普遍面临“马太效应”——传统模型依赖历史点击转化数据，导致新商品因缺乏反馈而难以获得曝光，损害平台长期生态。现有冷启动方法缺乏对单次交互长期价值的量化，也无法有效平衡短期效率和长期增长。

**方法关键点**
- **ItemLTV 模块**：用反事实因果推断量化一次点击对新商品未来7天交易额的 uplift。采用双塔结构，底座塔预测基础增长，uplift 塔建模用户交互带来的增量，训练时取对数空间并联合优化。
- **MultiGR 生成式检索**：将召回建模为从语义ID生成序列的任务。先用电商多模态基础模型得到商品表征，再用 RQ-VAE 量化为三层语义ID；以 Decoder-only Transformer 自回归生成候选商品，推理时采用 trie 约束解码保证层级合法。
- **多价值偏好对齐 (MoPO)**：在监督预训练后，引入组内相对优化：奖励由搜索漏斗标签（曝光、点击、购买）与 ItemLTV 高潜力标签加权组合，并用裁剪的重要性权重（-log概率）纠正流行度偏差，鼓励发现长尾高价值商品。

**关键结果**
- 离线对比生产 Dense Retrieval 和 TIGER，GrowthGR 在所有 long-term 指标上最优（Recall@1000 达 0.8991）; 两阶段组合 GrowthGR+DR 在所有指标上均大幅提升。
- 线上 A/B 测试：新商品 GMV 提升 5.39%，整体搜索 GMV +0.31%，新商品曝光占比 (PVR) +1.54%。
- 物品侧长期实验：新商品在第30天后的交易额（TI@30）提升 20.0%，证明模型不仅注入短期流量，而是真正培育出持续转化能力。

**一句话**：通过将长期增长潜力反事实量化并融入生成式检索的奖励对齐，GrowthGR 在不牺牲大盘效率的前提下显著改善了新商品冷启动的生态健康度。
