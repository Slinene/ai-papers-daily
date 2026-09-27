---
title: 'C3M: Cross-Session Multimodal Memory Maintenance for Long-Horizon Tasks'
title_zh: C3M：面向长程任务的跨会话多模态记忆维护
authors:
- Xueshu Chen
- Yan Wang
- Zihao Xue
- Jiefu Li
- Zhenfang Liu
- Jayden Chen
- Zhen Bi
- Jungang Lou
affiliations:
- Huzhou Normal University
- Alibaba Group
- University of Waterloo
arxiv_id: '2609.29735'
url: https://arxiv.org/abs/2609.29735
pdf_url: https://arxiv.org/pdf/2609.29735
published: '2026-09-24'
collected: '2026-09-27'
category: Agent
direction: Agent 跨会话多模态记忆维护
tags:
- multimodal memory
- long-horizon tasks
- memory maintenance
- budgeted routing
- provenance preserving
- agent memory
one_liner: 提出有界索引、关系感知更新与预算路由相结合的跨会话多模态记忆维护机制
practical_value: '- 在电商购物助手/客服 Agent 中，不要过度压缩历史会话；可维护一个固定大小的 active index，指针式保留原始商品图、对话截图、订单状态等源证据，后续按需展开，避免丢失
  fine-grained visual cues。

  - 借鉴 relation-aware updates：区分 redundant / complementary / incompatible 观察，不要仅凭文本或图片
  embedding 相似就合并记录；不同商品属性、状态或时间版本必须保留，避免把“同款不同色/不同卖家”的相似商品搞混。

  - 采用 budgeted routing：查询时先用小预算检索索引页，再对选中的页按固定 reader budget 展开源证据，可迁移到 RAG 用户记忆或广告创意上下文中，控制
  LLM context 开销并提高检索选择性。

  - 保留 provenance 和时间区分，方便后续审计、刷新和个性化推荐；在推荐系统里可用类似机制维护跨会话用户画像，索引指向原始行为序列而非抽象摘要。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：长程任务需要跨会话保存并在未来恢复证据，但内存预算有限且查询盲态；现有压缩会丢弃细粒度视觉线索，或把语义相似但实际不兼容的观察混在一起。

方法关键点：C3M 维护一个有界的 active index，指向持久化的 text-image 源证据；关系感知更新会合并安全冗余，同时保留互补和不兼容记录；查询时采用 budgeted routing，先用固定预算选择有用的索引页，再在固定 reader budget 下展开其关联源证据。整体形成紧凑、可溯源的多模态记忆组织，保留时间差异和来源链。

关键结果：论文摘要未给出具体数值指标，侧重机制设计；代码已开源，可用于下游可靠推理。
