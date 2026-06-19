---
title: 'VCG: A Multimodal Retrieval Framework for E-Commerce Video Feeds under Extreme
  Cold-Start Conditions'
title_zh: 面向电商视频流极端冷启动的多模态检索框架 VCG
authors:
- Katya Mirylenka
- Egor Malykh
- Mahdyar Ravanbakhsh
- Michael Gygli
- Marco-Andrea Buchmann
- Andrew Dzhoha
- Svitlana Borzenko
- Francesca Catino
- Mohamed Gaafar
- Maarten Versteegh
affiliations:
- TU Wien
- Zalando SE
- Zalando Switzerland AG
arxiv_id: '2606.19627'
url: https://arxiv.org/abs/2606.19627
pdf_url: https://arxiv.org/pdf/2606.19627
published: '2026-06-17'
collected: '2026-06-19'
category: RecSys
direction: 多模态向量检索 · 极端冷启动
tags:
- Multimodal
- Cold-Start
- Two-Tower
- CLIP
- LLM-as-Judge
- E-commerce Video
one_liner: 用域适应 CLIP 构建双塔向量检索，绕过交互历史，在线视频深度观看提升 50%
practical_value: '- **视觉语义向量替代行为信号做冷启动**：新品 / 新视频无交互时，直接用像素级 CLIP 嵌入做相似度检索，适合电商直播、短视频
  feed 的极端冷启。

  - **用户动态表示技巧**：用近期交互商品的 CLIP 嵌入按时间衰减加权平均构建用户向量，无需训 User Tower，可快速嫁接已有商品多模态表征，适合推荐系统快速上线视频流场景。

  - **离线评测用 LLM-as-a-Judge 替代有偏指标**：当历史日志存在曝光偏差时，用 Qwen-VL 按 5 级量表评估视觉匹配度，能提前验证语义相关性，可作为业务中替代
  NDCG 的离线 proxy。

  - **检索场景优先选判别式嵌入（CLIP 而非 LLM）**：论文验证了 Qwen 等生成式模型虽有更强属性预测能力，但嵌入空间各向异性严重，k-NN 检索效果差，业务中若做向量搜索应优先选择对比学习训练的多模态表征。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
电商从搜索式目录转向沉浸式视频 feed 会引入极端冷启动：新视频毫无交互，协同过滤失效；且完播率指标受视频长度和位置偏差污染。必须找到一种不依赖点击图的语义优先检索方案。

**方法关键点**
- **双塔架构与零样本检索**：视频用域适应 CLIP 提取 10 帧画面的嵌入后取平均；用户嵌入则用近期交互商品的 CLIP 嵌入按时间衰减加权平均得到，因子 \(w_k = \exp(-\lambda(t_{now} - t_k))\)，新用户直接用热门商品全局嵌入。两者共享视觉语义空间，点积即可打分，完全解耦交互历史。
- **域适应 CLIP**：内部在约 2 亿图文对上微调时尚 CLIP，让商品与视频帧落在同一流形上，支持跨模态检索（商品 ↔ 视频、文本 ↔ 视频）。
- **离线评测创新：LLM-as-a-Judge**：Qwen2.5-VL 基于用户最近 12 个交互商品与推荐视频的视觉一致性进行 5 级评分，解决传统 NDCG/AUC 受曝光偏差影响的问题。
- **生成式 vs 判别式嵌入的对比分析**：Qwen2.5-Omni 在属性预测 F1 上比 CLIP 高 6-10%，但嵌入空间高度各向异性，向量搜结果拥挤；CLIP 的对比损失提供更均匀的超球面分布，成为检索引擎的选择。

**关键结果**
- 离线：LLM-as-Judge 分数 Top-10 从 2.43 → 3.09 (+27%)，视觉相似度指标 fDNA 提升 37%，CLIP 相似度提升 22%。
- 在线 A/B 测试（4 周）：视频播放进度 @50% 提升 +50.10%，@25% 提升 +40.97%，而视频开始率仅 +8%，说明推荐的相关性大幅提升深度消费，有效避免“标题党”。核心收入与留存指标持平，视频 feed 未蚕食交易。
- 推理延迟：P50 17.5ms，P99 30ms。

**最值得记住的一句话**：在生成式 AI 时代，推荐相关性应由语义连贯性而非历史点击来衡量——离线用 LLM-as-Judge 评测，线上用多模态双塔零样本检索，能有效突破冷启动与曝光偏差的困境。
