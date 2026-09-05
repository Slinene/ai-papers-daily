---
title: 'Beyond Retrieval: Progressive Latent Memory Evolution for Streaming Video
  Understanding'
title_zh: 超越检索：面向流式视频理解的渐进潜在记忆演化
authors:
- Hongyu Qu
- Guangming Yao
- Ling Xing
- Xiaobin Hu
- Rongxing Ding
- Guibin Zhang
- Fan Zhang
- Yi Yuan
- Xiangbo Shu
- Shuicheng Yan
affiliations:
- Nanjing University of Science and Technology
- Ant Group
- National University of Singapore
- The Chinese University of Hong Kong
arxiv_id: '2609.04131'
url: https://arxiv.org/abs/2609.04131
pdf_url: https://arxiv.org/pdf/2609.04131
published: '2026-09-02'
collected: '2026-09-05'
category: Multimodal
direction: 流式视频 MLLM 的渐进潜在记忆
tags:
- Streaming Video
- MLLM
- Latent Memory
- Retrieval
- Memory Evolution
- Progressive Optimization
one_liner: 提出 LatentStream，将流式视频记忆从 store-and-retrieve 转为 retrieve-and-internalize，通过层级记忆与渐进置信度优化取得
  SOTA
practical_value: '- 借鉴“查询无关层级压缩 + 查询相关检索内化”两段式记忆架构：电商用户行为序列建模可先用无查询的自适应聚类（如 Jenks
  natural breaks）压缩长短期兴趣，收到请求后再用 query 检索相关证据并内部化为固定长度 latent 表示，平衡内存与推理精度。

  - 固定内存预算下的短/中/长期分层组织可迁移到 Agent 或在线推荐系统的会话记忆管理，避免历史状态无限增长，适合延迟敏感的长序列处理。

  - Progressive confidence-guided optimization 用分组预测熵构建层级奖励，可应用于多步推理或交互式推荐，对中间状态逐层优化置信度，提升最终输出稳定性。

  - retrieve-and-internalize 方式比将检索证据直接拼接到上下文更节省 KV cache，适合长视频/直播理解、多轮对话 Agent 等需持续累积历史的在线场景。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机
流式视频理解要求多模态大模型在严格因果和有限内存下处理连续视觉输入并实时回答用户查询。现有 store-and-retrieve 范式把历史压缩到外部记忆库，检索查询相关证据作为额外视觉上下文。但历史证据始终停留在外部，未被内部化为紧凑演化的潜在记忆，难以持续引导流式推理。

## 方法关键点
提出 LatentStream，将流式记忆从 store-and-retrieve 转向 retrieve-and-internalize，包含三个协同组件：

- **Query-Agnostic Hierarchical Streaming Memory**：用 Jenks-guided adaptive consolidation 在固定内存预算下，把视觉历史组织为短/中/长期三个层级。
- **Hierarchical Latent Memory Evolution**：查询到达后，分组潜在记忆 token 逐步扩大记忆感受野，从对应范围迭代检索历史证据并内部化到固定长度的潜在记忆中。
- **Progressive Confidence-guided Latent Memory Optimization**：基于分组预测熵构建层级 progression reward，联合优化潜在记忆 token 与检索证据，促使流式推理逐步提升置信度。

## 关键结果
在多个在线和离线视频基准上取得新的 state-of-the-art 表现，验证了 retrieve-and-internalize 记忆机制相比传统外部检索的优越性。
