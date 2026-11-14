---
title: 'The Value of Thinking: Learning When to Reason in Hybrid Decision Models'
title_zh: 思考的价值：混合决策模型中学习何时推理
authors:
- Zhengxu Yu
- Ke Xu
- Meng Fang
- Haitham Ammar
- Weilin Luo
- Jun Wang
affiliations:
- Huawei Noah's Ark Lab
- University of Liverpool
- University College London
arxiv_id: '2611.16961'
url: https://arxiv.org/abs/2611.16961
pdf_url: https://arxiv.org/pdf/2611.16961
published: '2026-11-11'
collected: '2026-11-14'
category: Reasoning
direction: LLM 自适应推理路由，零或完整推理
tags:
- adaptive reasoning
- hybrid decision model
- token efficiency
- RL
- agentic tasks
one_liner: 提出零或T token推理范式，用轻量路由估计思考价值并自适应调用慢思考，大幅降低推理成本
practical_value: '- 线上 LLM 推理成本控制：把常规/低难度请求（意图分类、简单属性抽取）走 fast 模式零显式 token，仅高价值/高风险请求触发完整
  CoT；用 λ 按请求预算或延迟约束动态调节开销，而不是统一缩短所有请求的思维链。

  - 推荐/搜索中的 query 改写、商品属性结构化、用户意图理解可做 fast/slow 双模：fast 用 backbone 隐式表征直接预测，slow 走完整推理校对；路由模块只读
  fast 的 last hidden state 或校准 logits，轻量部署，不动主模型。

  - 对只有业务长期回报（GMV、转化、任务完成率）而无步骤级标签的 agentic 工作流（多轮商品筛选、自动客服/谈判），可借鉴 CDPO：用 episode-level
  return 训练路由策略，让“是否再调用一次大模型推理”成为可优化策略，而不是人工规则。

  - 具体 trick：路由 block 估计 value of thinking 并与可配置 λ 比较，相当于把推理预算做成 SLA 旋钮；大促期间可提高 λ
  全局降本，高价值会员或复杂售后可调低 λ 保证质量。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 adaptive-reasoning 方法要么缩短显式 CoT、要么切换模式，但答案仍逐 token 生成，推理成本与延迟难以真正归零。核心问题从“想多少”转向“想或不想”：能否让单个模型在 fast 模式下零 token 直接产出答案，仅在推理回报高于成本时启用完整慢思考？

**方法关键点**：
- HDM 用一个 frozen backbone 同时服务两种模式：fast 走单次前向的 implicit thinking，不生成中间 token；slow 走完整自回归推理，消耗 T tokens。
- 轻量 self-routing block 从 fast 模式已产出的隐式表征估计 “value of thinking”：slow 相对 fast 的期望效用增益；只有当该值高于按请求设定的价格 λ 时，才路由到 slow。
- 对无逐决策标签的 episodic agentic 任务，提出 CDPO：用 episode-level return 训练路由策略，做 calibrated decision policy optimization。

**关键结果**：在 JevBench 上 HDM-4B 达到 0.857，略高于 Jev 的 0.851（+0.7%），中位耗时 0.179s vs 0.652s（-72.5%）；MiniWoB 上 HDM-27B 在保持任务表现的同时 token 成本降低 80.1%。在 MMLU-Pro、AGIEval、GPQA-Diamond、BANKING77 等基准上也得到验证。
