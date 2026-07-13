---
title: Parallelized Autoregressive Decoding for Omni-Modal Dense Video Captioning
title_zh: 全模态密集视频描述并行自回归解码
authors:
- Wenzheng Zeng
- Siyi Jiao
- Chen Gao
- Hwee Tou Ng
- Mike Zheng Shou
affiliations:
- National University of Singapore
arxiv_id: '2607.02963'
url: https://arxiv.org/abs/2607.02963
pdf_url: https://arxiv.org/pdf/2607.02963
published: '2026-07-03'
collected: '2026-07-13'
category: Multimodal
direction: 多模态事件描述 · 并行解码
tags:
- Dense Video Captioning
- Parallel Decoding
- Autoregressive Model
- Event-Factorized
- Latent Planning
one_liner: 利用事件间弱局部依赖重构解码依赖图，实现无损并行生成，大幅提升密集视频描述效率与性能
practical_value: '- 推荐系统生成序列化推荐理由或事件描述时，可将文本分解为相对独立的语义块（如商品卖点、活动节点），利用块间弱依赖并行解码，降低端到端生成延迟。

  - 借鉴潜在全局规划模块的设计，在Agent多步推理中预先规划步骤间的因果依赖，对无依赖的推理步骤并行执行，提升复杂任务的处理效率。

  - 事件因子化解码机制平衡局部连贯与全局感知的思路，可用于电商直播合辑、广告创意序列等需同时保持单条内容紧凑性和整体叙事流的场景。

  - 依赖图动态重构方案可迁移到搜索建议生成、会话式推荐中，根据输入意图的独立性自动分组，实现部分并行以加速响应。'
score: 6
source: arxiv-cs.MM
depth: abstract
---

**动机**：现有密集视频描述模型采用逐令牌自回归解码，随着视频长度和事件密度增加，推理效率低下，可扩展性受限。

**方法关键点**：
- 洞察：不同时间事件间存在弱局部依赖，可借此重构因果依赖图，将强耦合的事件内令牌保留顺序解码，而弱依赖的跨事件令牌并行生成，实现无损并行。
- 设计两个核心组件：(1) 潜在全局规划机制自动学习事件级结构，生成紧凑的全局令牌以编码事件间因果关系，同时自适应聚合事件级音视频语义，指导依赖重构；(2) 事件因子化并行解码机制，在保持事件内局部语义连贯的同时融入全局事件间感知。

**结果**：在多个基准（如ActivityNet Captions、YouCook2）上，该方法在事件定位与描述性能上优于现有方案，同时解码速度显著提升，实现了效率与性能的双赢。
