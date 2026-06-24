---
title: Towards Fast Domain Adaptation and Fine-Grained User Simulation for Evaluating
  Conversational Recommender Systems
title_zh: 面向对话推荐评估的快速域适应与细粒度用户模拟器
authors:
- Yuanzi Li
- Quanyu Dai
- Xueyang Feng
- Zihang Tian
- Junhao Wang
- Xu Chen
- Zhenhua Dong
- Huifeng Guo
affiliations:
- Renmin University of China
- Huawei Noah’s Ark Lab
arxiv_id: '2606.22803'
url: https://arxiv.org/abs/2606.22803
pdf_url: https://arxiv.org/pdf/2606.22803
published: '2026-06-22'
collected: '2026-06-24'
category: RecSys
direction: 对话推荐评估 · 用户模拟域适应
tags:
- User Simulator
- Domain Adaptation
- Conversational Recommender Systems
- LLM Evaluation
- Prompt Tuning
- Controlled Text Generation
one_liner: 提出自动提示优化与“先想后答”策略的用户模拟器 AdaptSim，实现跨域快速适应和风格可控的对话推荐评估
practical_value: '- 离线评估对话推荐系统时，可借鉴“自动提示生成+开放动作空间”方案，减少针对新域的手动提示工程，快速构建域特定模拟器。

  - “先想后答”（think-then-respond）策略将用户意图与语言风格解耦，可复用于电商对话 Agent 的行为模拟，实现多样化、真实的用户交互。

  - 基于 BFS 的 turn 级成对比较评估框架，能更细粒度地诊断 CRS 各轮次回复质量，可用于电商导购机器人的迭代优化与鲁棒性检验。

  - 若业务中存在多域（如服饰、家电）对话推荐场景，可利用 AdaptSim 的轻量域适应能力快速上线离线评估，减少对人工标注的依赖。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

动机：评估对话推荐系统（CRS）时，现有基于 LLM 的用户模拟器受限——固定提示与预定义动作导致难跨域迁移、无法复制微妙语言风格和动态偏好、评估维度粗糙。

方法：提出 AdaptSim，包含三项设计：1）自动提示生成与优化，结合开放动作机制，减少人工工作并提升域适应速度；2）可控文本生成引入“先想后答”策略（先生成用户意图，再据此生成回复），实现对语言风格的细粒度控制；3）基于广度优先搜索的 turn 级成对比较框架，全面评估 CRS 的基础能力与鲁棒性。

结果：在三个域、四种 LLM 上实验，AdaptSim 生成的对话更真实，能高效可靠地评估 CRS。具体地，域适应时间显著缩短（自动提示生成），用户模拟逼真度（语言风格匹配、偏好一致性）优于基线，评估有效性在多个 CRS 指标上得到验证。
