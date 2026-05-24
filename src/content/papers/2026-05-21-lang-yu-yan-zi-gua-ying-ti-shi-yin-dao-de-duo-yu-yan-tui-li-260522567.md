---
title: 'LANG: Reinforcement Learning for Multilingual Reasoning with Language-Adaptive
  Hint Guidance'
title_zh: LANG：语言自适应提示引导的多语言推理强化学习方法
authors:
- Yuchun Fan
- Bei Li
- Peiguang Li
- Yilin Wang
- Yongyu Mu
- Jian Yang
- Xin Chen
- Rongxiang Weng
- Jingang Wang
- Xunliang Cai
affiliations:
- Northeastern University
- Meituan Inc.
- NiuTrans Research
arxiv_id: '2605.22567'
url: https://arxiv.org/abs/2605.22567
pdf_url: https://arxiv.org/pdf/2605.22567
published: '2026-05-21'
collected: '2026-05-24'
category: Reasoning
direction: 多语言推理强化学习与语言一致性保持
tags:
- Reinforcement Learning
- Multilingual
- Reasoning
- Language Consistency
- Hint Guidance
- LLM
one_liner: 用语言条件提示和衰减机制引导多语言推理强化学习，在非英语数学任务上提升推理性能且保持语言一致性
practical_value: '- 可借鉴语言条件提示（language-conditioned hints）作为训练辅助信号，在强化学习或 SFT 中引导模型保留期望行为，尤其适用于多语言下的
  Agent 或对话系统。

  - 渐进衰减调度（progressive decay schedule）思路可用于课程学习，先给强信号再逐步撤除，防止模型过度依赖辅助信息，适用于电商搜索中的多阶段训练。

  - 语言自适应开关（language-adaptive switch）根据任务难度动态调整训练策略，可迁移至多语言推荐或客服场景，对不同语言定制优化节奏。

  - 整体框架有助于解决在追求性能时产生的语言漂移问题，对需要保持语言一致性的多语言产品（如多语种商品描述生成）有直接参考意义。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：强化学习（尤其 RLVR）虽在增强大模型多步推理上成效显著，但多语言场景下存在根本权衡：坚持输入语言会严重损害推理质量，优先推理则易导致语言向英语漂移。现有方法难以兼顾推理性能与语言一致性。

**方法**：提出 LANG 框架，核心是利用**语言条件提示**（language-conditioned hints）在非英语推理任务中引导探索方向。为避免模型对提示产生依赖，设计两个关键机制：①**渐进衰减调度**逐步撤除外部脚手架（scaffold），在训练过程中按预设计划降低提示频率；②**语言自适应开关**根据不同语言的学习难度定制衰减步调，难的语言给予更长的提示周期。两者协同使模型最终能脱离提示进行独立推理。

**结果**：在多语言数学基准测试（如 MGSM、MSVAMP 等）上，LANG 大幅提升非英语推理准确率，同时语言一致性指标未见下降；在通用对话任务上同样能促进模型层间更一致的语言对齐，展现出任务泛化性。
