---
title: 'From Pattern Recognizers to Personalized Companions: A Survey of Large Language
  Models in Mental Health'
title_zh: 从模式识别器到个性化伴侣：心理健康领域大语言模型综述
authors:
- He Hu
- Yucheng Zhou
- Qianning Wang
- Yingjian Zou
- Chiyuan Ma
- Juzheng Si
- Jianzhuang Liu
- Zitong Yu
- Laizhong Cui
- Fei Ma
arxiv_id: '2609.25186'
url: https://arxiv.org/abs/2609.25186
pdf_url: https://arxiv.org/pdf/2609.25186
published: '2026-09-20'
collected: '2026-09-24'
category: LLM
direction: LLM 心理健康应用 · 智能体演进
tags:
- Mental Health
- LLM Survey
- Cognitive Agent
- Personalized Companion
- Longitudinal Support
one_liner: 梳理LLM在心理健康中从被动评估工具到共情对话者再到有状态个性化陪伴智能体的三阶段演进，并系统综述了智能体架构与评测资源
practical_value: '- 三阶段演化框架可映射到电商推荐 Agent：从静态内容理解/分类 → 单轮对话式推荐 → 有状态、跨会话的个性化陪伴（长期偏好追踪），适合用来规划团队内部
  LLM 推荐能力升级路径。

  - 重点借鉴 Agent 架构中的 Memory 设计：区分长期用户画像（Profile）与短期会话状态，并引入记忆压缩/检索机制，解决电商搜索/推荐中跨 session
  用户意图漂移与个性化不足问题。

  - 评测体系从“单次回答准确率”转向“纵向满意度、信任与留存”的思路，可迁移到搜索推荐评估：建立面向用户长期价值（如复购率、负反馈率、会话深度）的 LLM 评估指标。

  - 隐私保护与去标识化（de-identification）在用户数据敏感场景（如健康、电商行为）有直接参考，可为推荐 Agent 接入用户画像时提供合规与降敏方案。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：心理健康问题全球高发，传统服务受限于资源、成本、污名与隐私；LLM 具备可及、可扩展的交互能力，但领域研究碎片化，缺少演进框架。

**方法关键点**：以三阶段演进为主线组织文献——Phase I：LLM 作为被动信息工具与模式识别器，用于心理评估；Phase II：作为共情对话者，支持无状态即时交互；Phase III：作为纵向个性化陪伴，实现有状态认知智能体。系统梳理了支撑这一路径的核心技术、Agent 架构模块（Profile、Memory、Reasoning、Planning）以及数据集与基准的演进。

**关键结果**：综述提供了一个清晰的发展叙事和未来研究路线图，并公开维护资源库；指出当前前沿集中在有状态、个性化、负责任的心理健康 Agent，但高质量纵向数据和长期效果评测仍是瓶颈。
