---
title: Sona Technical Report
title_zh: SONA：Yandex Music的单一生成式推荐模型
authors:
- Sona Team
- Alexandr Udeneev
- Aleksei Krasilnikov
- Alexey Nadtochiy
- Andrey Semenov
- Andrey Tsyrkunov
- Anna Krivonos
- Anna Lipkina
- Artem Matveev
- Daniil Burlakov
affiliations:
- Yandex
arxiv_id: '2608.11015'
url: https://arxiv.org/abs/2608.11015
pdf_url: https://arxiv.org/pdf/2608.11015
published: '2026-08-11'
collected: '2026-08-12'
category: GenRec
direction: 生成式推荐 · Semantic ID · 单模型统一排序
tags:
- Generative Recommendation
- Semantic ID
- Teacher Distillation
- Unified Ranking
- Music Recommendation
- Online A-B Test
one_liner: 用一个生成式模型统一召回与排序，通过教师蒸馏和Semantic ID在音乐推荐中实现显著在线收益。
practical_value: '- **单模型统一生成与排序**：借鉴共享编码器 + 自回归解码 + 交叉注意力打分模块的架构，可简化电商/广告的多阶段级联系统，减少维护成本。

  - **Semantic ID 与 trie 约束 beam search**：用多模态 LLM + 协同信息精炼 + 残差量化的方式构建物品语义码，适应大动态物品库，适合迁移到有内容特征的商品推荐。

  - **无手工特征排序教师蒸馏**：Teacher Ranker 仅用日志事件预训练（NIP）+ 多目标微调，可替代依赖大量特征的排序模型；通过稠密蒸馏将长期历史知识注入轻量学生，对特征工程受限的场景有参考价值。

  - **低延迟在线训练循环**：会话聚合、推断日志对齐、10分钟级模型推送，实现从事件到模型更新的 45 分钟中位延迟，可作为实时推荐系统在线学习的工程范本。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：音乐推荐需平衡熟悉曲目与发现新歌，现有级联式多阶段系统复杂、迭代慢。探索单一生成式模型能否端到端替代整个推荐链，并在大型音乐流媒体场景取得指标提升。

**方法关键点**：
- **Semantic Tokenizer**：用冻结的多模态 LLM（Qwen2.5-Omni）提取音频+元数据特征，经协同过滤对（InfoNCE）精炼 transformer 后，残差 K-means 量化成 3 级 ×32k 码本的 Semantic ID。
- **无手工特征用户建模**：仅使用播放、跳过、喜欢等日志事件，通过项目 / 上下文 / 反馈三个嵌入器求和构成事件 token。
- **历史压缩编码器**：将用户序列分为远期块 O 和近期块 R，仅在 R 上应用深层堆叠，同时通过交叉注意力保留全局信息，降低注意力平方开销。
- **生成 + 排序一体化**：解码器自回归产生 Semantic ID 候选，Ranking Module 通过交叉注意力对同一编码器状态打分，训练时联合 NTP 损失和教师蒸馏（MAE）。
- **教师排序器**：顺序 Transformer 预训练下一事件预测（NIP），再用 pairwise 与 pointwise 多目标微调，提供稠密排序信号。
- **在线训练**：会话聚合、流量过滤、历史对齐后连续训练，模型 10 分钟更新一次，端到端延迟中位 45 分钟。

**关键实验**：
- **离线消融**：3 级 32k 码书 + 协同精炼的 tokenizer 取得最高 Recall@1000（0.8524）；教师预训练使 WPA 从 0.6153 提高到 0.6215；联合训练时使用 rollouts+impressions 蒸馏，Teacher Recall@100 达 0.7344；历史压缩 8k 长度下 Recall@1000 仅微降至 0.8709（完整注意力 0.8722）。
- **在线 A/B 测试**：在智能音箱 My Vibe 场景，相比生产级联，**Active Users +4.53%，总收听时长 +6.30%，喜欢 +11.42%**，且 Active Users 提升是此前最佳模型 Argus 的 2.35 倍。
