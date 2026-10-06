---
title: 'KeyRec: Bounded Visual Memory for Streaming and Long-Video Understanding'
title_zh: KeyRec：面向流式与长视频理解的有界视觉记忆框架
authors:
- Zihan Chen
- Xuejian Rong
- Xiaojuan Wang
- Boqing Gong
- Adi Zicher
- Yael Pritch
- Nikhil Karnad
affiliations:
- University of Virginia
- Google
arxiv_id: '2609.32182'
url: https://arxiv.org/abs/2609.32182
pdf_url: https://arxiv.org/pdf/2609.32182
published: '2026-09-25'
collected: '2026-10-06'
category: Multimodal
direction: 多模态长视频流式推理视觉记忆压缩
tags:
- Visual Memory
- Streaming Video
- Long-video Understanding
- Token Compression
- VLM
- Training-free
one_liner: 训练免费的视觉记忆框架，用事件银行与近期缓存分离存储，在固定预算下高效压缩长视频视觉 token
practical_value: '- 借鉴“近期缓存 + 事件银行”的双层记忆结构：在电商用户行为序列或会话流建模中，可保留最近交互的细粒度 token（如点击、浏览），同时将较旧历史压缩为结构化事件表示（如会话摘要、关键行为节点），避免每次推理全量回放，降低长序列注意力成本。

  - 采用 query-agnostic writing + query-dependent readout 的两阶段设计：离线阶段持续更新记忆，查询到来时用轻量
  text-only router 自适应分配固定 readout 预算到近期与事件记忆，无需重处理历史帧。可在 Agent 记忆系统中应用，控制上下文窗口，降低
  LLM API 费用。

  - 事件合并与逐出策略（add-merge-evict）可用于用户兴趣画像维护：根据 novelty 决定是否新增事件，合并相似兴趣，淘汰过时兴趣，保持画像有界且信息密度高。

  - 对于直播电商、商品视频理解等场景，可复用 KeyRec 的视觉 token 压缩思路，仅保留 10% 的 visual token 预算即可保持接近密集处理的性能，显著降低推理成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：VLM 用于理解长视频和连续流时，视觉 token 随视频时长线性增长，长上下文推理代价高昂。现有训练免费视觉 token 选择方法虽能降低成本，但易丢失连贯事件证据，且无法区分近期详细观察与长程历史。

**方法关键点**：KeyRec 是一个训练免费框架，构建有界视觉记忆。在 query-agnostic 写入阶段，保留细粒度近期观察在视觉缓存中，并将历史证据组织为结构化事件银行。候选事件根据与已存储事件的 novelty 提出，通过在线 add–merge–evict 更新维护。当问题到达时，仅用文本路由器自适应地在近期记忆与事件记忆之间分配固定 readout 预算，无需重处理历史帧。KeyRec 直接操作 model-facing visual embeddings，兼容模块化 encoder–projector VLM 和 encoder- 与 projector-free 的 NEO-ov 架构。

**关键结果**：在 4 个流式与长视频基准、3 个 VLM 骨干上，仅使用 10% 的密集 decoder-facing visual-token 预算，在 15 个设置中的 13 个取得最佳压缩性能；在实时问题上比最强压缩基线高 2.21–18.37 分；在 6 个长视频设置中的 5 个取得最佳压缩结果；在 NEO-ov 2B 的每个设置中表现最佳。
