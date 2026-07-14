---
title: 'LightMem-Ego: Your AI Memory for Everyday Life'
title_zh: LightMem-Ego：面向日常生活的轻量级流式多模态记忆系统
authors:
- Yijun Chen
- Boyi Xiao
- Yixian Zhao
- Haoting Xia
- Buqiang Xu
- Jizhan Fang
- Yanya Li
- Yaqi Zheng
- Xuehai Wang
- Zirui Xue
affiliations:
- Zhejiang University
- South China University of Technology
- Central China Normal University
- Lenovo Group Limited
arxiv_id: '2607.11487'
url: https://arxiv.org/abs/2607.11487
pdf_url: https://arxiv.org/pdf/2607.11487
published: '2026-07-12'
collected: '2026-07-14'
category: Agent
direction: 多模态记忆 · 层次化检索生成
tags:
- Multimodal Memory
- Egocentric AI
- Hierarchical Retrieval
- Personal Assistant
- Streaming Processing
- LLM
one_liner: 一个可部署在手机和AI眼镜上的层次化多模态记忆系统，支持连续积累、组织与检索日常经历
practical_value: '- **对话推荐Agent的记忆架构**：将用户行为流组织为“当前/短期/长期”三层记忆，与电商对话推荐中实时意图、近期行为、长期偏好的分层建模直接对应，可参考其时间对齐与路由检索机制。

  - **流式多模态积累**：对用户第一人称视频、音频流持续处理并按统一时间线存储，可迁移到直播推荐、短视频推荐中对用户行为的细粒度时序建模。

  - **查询驱动的动态路由**：根据问题类型自动选择检索深度（如只需短期记忆的“东西放哪儿”vs需长期记忆的“习惯分析”），可用于智能客服或推荐解释中的上下文选择。

  - **轻量部署设计**：系统在端侧运行，推荐系统的在线特征存储与实时召回也可借鉴其内存压缩与分层方案，降低延迟与资源消耗。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：智能手机与AI眼镜的普及使个人AI助手有能力持续感知日常生活，但回答“我刚才把钥匙放哪了？”“上周三的会议说了什么？”等问题需要一个能够连续积累、组织和检索长期多模态记忆的轻量系统，现有方案难以在端侧实现。

**方法关键点**：系统持续捕捉第一人称视觉和音频流，在统一时间轴上对齐，并将记忆组织为三层：当前记忆（最近几秒）、短期记忆（几分钟到几小时）、长期记忆（几天以上）。对于用户查询，系统通过动态路由将检索指向最合适的记忆层，并利用多模态证据生成答案。整体设计面向流式处理，可在智能手机和AI眼镜上实时运行。

**关键结果**：演示系统支持物品定位、对话回忆、生活摘要、日常习惯发现和个性化建议等任务，代码已开源。
