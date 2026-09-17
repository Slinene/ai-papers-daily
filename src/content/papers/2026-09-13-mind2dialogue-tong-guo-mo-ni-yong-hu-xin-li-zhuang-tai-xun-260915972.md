---
title: 'Mind2Dialogue: Training Human-Aware Language Models by Simulating User Mental
  States'
title_zh: Mind2Dialogue：通过模拟用户心理状态训练人本感知语言模型
authors:
- Zixuan Wang
- Yufan Zhou
- Jinzhou Tang
- Xinle Yu
- Chengjun Wu
- Lyumanshan Ye
- Zhaoxiang Feng
- Letian Peng
- Adyasha Patra
- Fan Bai
affiliations:
- UC San Diego
- KU Leuven
- University of Illinois Chicago
- The Ohio State University
- Johns Hopkins University
arxiv_id: '2609.15972'
url: https://arxiv.org/abs/2609.15972
pdf_url: https://arxiv.org/pdf/2609.15972
published: '2026-09-13'
collected: '2026-09-17'
category: Training
direction: 用户心理模拟 · 人本感知LLM训练
tags:
- user simulation
- theory of mind
- personalization
- privileged distillation
- human-aware LLM
- mental state
one_liner: 用心理引导模拟器生成共享心理状态对话，并以特权蒸馏训练更懂用户信念与目标的LLM
practical_value: '- 会话式推荐/导购 Agent：可借鉴其用户模拟器，为每次会话维护潜在偏好/目标状态，并用 Oracle 基于该状态生成高质量回复，再通过特权蒸馏训练线上模型——线上只需对话历史，不需要真实心理状态。

  - 个性化评测：将个性化与心智理论结合，评估模型能否从用户话中推断偏好并据此行动，可迁移到推荐系统的用户理解指标，而不仅看点击/转化。

  - 数据增强：在电商对话数据稀缺时，用心理引导模拟器生成覆盖多变用户人格和演化意图的合成数据，用于微调导购、客服或选品 Agent，降低人工标注成本。

  - 多轮交互建模：共享演化心理状态可视为用户长期兴趣与短期意图的状态跟踪，提升搜索/推荐长会话一致性。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 助手训练数据很少显式基于用户未言明的信念与目标，导致模型难以长期协作；而用户心理状态不可直接观测，监督信号难以规模化。

**方法关键点**：提出 Mind2Dialogue，先构建心理学引导的用户模拟器，在保留个人特征的同时随对话更新共享心理状态，驱动用户行为并指导 Oracle 助手生成知情回复；再用特权蒸馏，让模型学习 Oracle 回复，但部署时只能看到用户可观察话语，不能访问心理状态。评估结合个性化与心智理论。

**关键结果数字**：在完整 Mind2Dialogue 语料上训练后，Qwen、Llama、OLMo 指令微调基线的所有个性化指标均提升；偏好跟随生成提升 26.6–40.9 个百分点，且 Qwen 与 Llama 在信念与行动推理上也受益。
