---
title: 'StreamArena: Toward Continuous, Interactive, and Long-Horizon Agentic Streaming
  Video Understanding'
title_zh: StreamArena：面向连续交互的长时流式视频理解基准与双层架构
authors:
- Xichen Zhang
- Guankai Li
- Yinghao Zhu
- Shijian Wang
- Sitong Wu
- Shaozuo Yu
- Meng Chu
- Yuan Lu
- Jiaya Jia
affiliations:
- The Hong Kong University of Science and Technology
- Xiaohongshu Inc.
- The University of Hong Kong
- The Chinese University of Hong Kong
arxiv_id: '2608.05703'
url: https://arxiv.org/abs/2608.05703
pdf_url: https://arxiv.org/pdf/2608.05703
published: '2026-08-05'
collected: '2026-08-10'
category: Agent
direction: 长时间流式视频理解Agent架构
tags:
- streaming video understanding
- multimodal agents
- long-horizon memory
- two-tier architecture
- proactive interaction
- tool use
one_liner: 提出小时级流式视频理解基准StreamArena和双层架构StreamMind，解耦实时交互与长期多模态记忆
practical_value: '- **异步记忆与实时交互解耦**：前后端分离架构可借鉴到电商直播监控中，前端快速响应实时关键词检测、用户提问，后端异步构建直播长时记忆并支持历史事件搜索，避免阻塞交互。

  - **多模态持久状态复用**：后端构建持久化的多模态记忆（非纯文本），保留视觉证据，降低重复压缩损失，可用于长时间直播流的商品出现记录、主播话术回溯等场景，减少重复计算。

  - **主动干预能力**：StreamMind的主动监控模块可迁移至直播推荐系统，在检测到预设事件（如商品展示、主播口播优惠）时主动向用户推送提示卡片，提升互动转化。

  - **外部工具集成**：架构支持按需调用外部搜索，可应用于实时查询商品详情、比价等，增强Agent在电商场景中的实时信息获取与回答准确率。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有流视频理解评测依赖短视频片段和选择题，简单模型仅用最后四帧即可超越复杂流模型，且答案选项泄露语言捷径，无法评估真实连续场景中的长时理解与交互能力。

**方法**：构建**StreamArena**基准，包含243段平均88.8分钟的全长视频及3646个开放问答，覆盖实时感知、历史回溯、主动交互、多模态工具使用四类能力。发现现有方法在连续交互与长期理解间存在张力：仅保留近帧丢失历史，文本转换丢失视觉证据，反复压缩损坏细节。提出**StreamMind**双层架构：前端独立调度延迟敏感的交互与主动监控，后端异步构建持久多模态记忆、执行历史召回与外部搜索，复用持久状态降低查询延迟。

**结果**：StreamMind在四项能力上均超越现有流基线，并通过状态复用显著降低查询响应时间。
