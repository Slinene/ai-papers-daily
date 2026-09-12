---
title: 'Caption-once, Frames-on-Demand: Visual-Need Routing for Budget-Aware Agentic
  Long Video Understanding'
title_zh: 一次性字幕，按需取帧：预算感知的智能体长视频理解视觉需求路由
authors:
- Weitong Cai
- Hang Zhang
- Yukai Huang
- Yiqiao Xie
- Shan Gao
- Jiankang Deng
- Songcen Xu
- Jifei Song
- Zhensong Zhang
affiliations:
- Queen Mary University of London
- Independent Researcher
- Durham University
- Imperial College London
- Huawei
arxiv_id: '2609.11899'
url: https://arxiv.org/abs/2609.11899
pdf_url: https://arxiv.org/pdf/2609.11899
published: '2026-09-10'
collected: '2026-09-12'
category: Agent
direction: 预算感知的长视频理解 Agent 路由
tags:
- Long Video Understanding
- Budget-Aware
- Edge-Cloud Agent
- Visual-Need Router
- Multi-modal LLM
one_liner: 提出边云协同的 CFD 框架，用双轨叙事索引和视觉需求路由器按需取帧，显著降低长视频在线视觉处理成本
practical_value: '- 借鉴双轨索引思想：在电商直播/商品视频理解中，离线生成事件级叙事骨架 + 片段级细节日志，将长视频转化为可复用索引，后续 query
  只查索引不重跑 captioning，降低线上 token 与耗时。

  - 将 Visual-Need Router 改造成多模态 RAG/Agent 中的“证据门槛”：根据 query 是否涉及外观、OCR、属性判别，决定是否检索原图/帧；时序、流程类问题直接走文本
  memory，从而控制每 query 的多模态检索成本。

  - 边云预算分离：让边缘端承担一次性离线 captioning 与索引缓存，云端按 query 拉取有界关键帧，适合直播回放、素材审核、商品视频 QA 等预算敏感场景，避免逐
  query 全量视频重灌模型。

  - “按 query 封顶视觉证据数，与内容长度无关”可以迁移到搜索推荐 Agent 的工具调用：为商品主图、评论、卖点等证据源设置 budget，只有 router
  认为必要时才触发额外检索，防止长文档/长视频 query 的成本爆炸。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

动机：长视频理解在边缘设备上受算力与带宽预算限制，常见的下采样视觉 token 会破坏时序结构，纯文本视频记忆又丢失细粒度视觉属性。观察到视觉-文本对偶性：语言记忆在长程时序上优于密集帧，像素在属性级感知上仍不可或缺。

方法关键点：CFD 采用边云协同。边缘端只做一次离线 captioning，构建双轨叙事索引：事件级故事骨架 + 片段级 micro-log，缓存并跨 query 复用，避免重复 captioning。查询时云端 MLLM 以 story-first 方式在索引上推理，配合轻量 Visual-Need Router 按 query 门控：仅当问题涉及外观、屏上文字、属性消歧等感知需求时，触发有界 keyframe 检索；时序结构类问题保持在语言空间。视觉访问因此成为 query 条件化的一等成本，每 query 帧消费封顶，与视频长度无关。

结果：在长视频基准上实现较强准确率-效率权衡，大幅减少在线视觉处理与带宽消耗。
