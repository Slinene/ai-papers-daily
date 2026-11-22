---
title: 'DailySafe: Benchmarking Dynamic Safety Awareness in Everyday Multi-Turn Multimodal
  Interactions'
title_zh: 日常多轮多模态交互中动态安全意识的基准评测
authors:
- Xuankun Rong
- Xinhao Deng
- Wenzhang Jiang
- Ziheng Peng
- Siyuan Liang
- Wenke Huang
- Pablo Arbelaez
- Mang Ye
affiliations:
- Wuhan University
- Ant Group
- Tsinghua University
- State Key Laboratory of Complex & Critical Software Environment
- Renmin University of China
arxiv_id: '2611.26298'
url: https://arxiv.org/abs/2611.26298
pdf_url: https://arxiv.org/pdf/2611.26298
published: '2026-11-18'
collected: '2026-11-22'
category: Eval
direction: 多模态 LLM 动态安全评测基准
tags:
- Multimodal LLM
- Safety Benchmark
- Multi-turn Interaction
- Dynamic Safety Awareness
- Evaluation
one_liner: 提出 DailySafe 基准，评测多模态大模型在日常多轮多图任务中动态识别上下文安全风险的能力
practical_value: '- 在电商客服/导购 Agent 中，用户上传商品图并多轮追问（如“这个除霉剂小孩碰到怎么办”），安全风险随图片和历史对话逐步暴露；可借鉴
  DailySafe 的“动态安全感知”框架，在每轮结合历史图片与文本做风险重判，而不是只对当前 query 独立审核。

  - 构建评测集的方法——从真实用户对话主题和文档化安全知识出发，按领域/任务树枚举日常场景——可以迁移到业务安全回归库建设，减少长尾安全场景遗漏。

  - 对 RLHF/DPO 安全策略训练，建议引入多轮多图正负样本，标注“支持合法目标+需要安全提醒”的细粒度标签，让模型学会在助人同时插入风险提示，避免纯拒答带来的体验损失。

  - 多模态内容审核侧可借鉴其“渐进式证据揭示”设计，构造必须跨 turn 关联图片与文本才能判定的样本，用于上线前压测模型短上下文和视觉理解短板。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
多模态大模型（MLLMs）越来越多用于日常任务，但现有安全评测主要聚焦孤立有害请求或对抗攻击，忽略正常多轮、多图交互中风险随上下文动态呈现。例如看似无害的请求，结合之前动作和视觉观察可能成为安全关键场景。因此论文提出 Dynamic Safety Awareness：跟踪任务条件变化、识别隐含上下文风险，并提供安全有用的辅助。

**方法关键点**  
构建 DailySafe 基准：195 个自然多轮多图像交互，覆盖 10 个日常领域、42 个任务类别。数据基于真实用户对话话题和文档化安全知识，设计跨轮次和图片逐步揭示安全证据；使用 case-specific 安全标注，既考察风险识别与处理，也要求模型支持用户合法目标，而非简单拒答。

**关键结果数字**  
公开 benchmark 规模：195 个多轮多图样本、10 领域、42 任务类别，将多模态安全评测推向更真实的日常 AI 助手场景，为后续动态安全能力评估提供基准。
