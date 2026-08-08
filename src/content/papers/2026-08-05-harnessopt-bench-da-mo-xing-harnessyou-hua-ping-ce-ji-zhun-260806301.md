---
title: 'HarnessOpt-Bench: Evaluating LLMs at Harness Optimization'
title_zh: HarnessOpt-Bench：大模型Harness优化评测基准
authors:
- Varun Ursekar
- Apaar Shanker
- Yash Maurya
- Shehab Yasser
- Vijay S. Kalmath
- Veronica Chatrath
- Yuan Xue
affiliations:
- Scale AI
arxiv_id: '2608.06301'
url: https://arxiv.org/abs/2608.06301
pdf_url: https://arxiv.org/pdf/2608.06301
published: '2026-08-05'
collected: '2026-08-08'
category: Eval
direction: 大模型Harness自动化优化基准测试
tags:
- LLM evaluation
- harness optimization
- agent
- benchmark
- automated optimization
one_liner: 首个评估LLM端到端Harness优化的基准，揭示模型差异大于框架且原生框架不总占优
practical_value: '- 在搜索推荐系统的Agent搭建中，可引入类似Harness优化流程：以LLM自动迭代提示词、工具组合、控制流，基于离线的固定评估预算搜索最优配置，替代纯人工调参。

  - 借鉴信任执行环境（TEE）设计，为优化过程建立沙盒，严格隔离测试集，防止信息泄露，同时跟踪资源消耗与版本历史，确保线上Agent迭代的安全性。

  - 选择优化器模型时优先考虑本基准中表现更强的模型（如GPT‑4o），因其优化增益显著高于弱模型；业务中可先对候选模型进行简易评估，再投入自动化调优。

  - 初始种子Harness对最终增益影响大，推荐由领域专家设计多个有差异的种子基线，再让优化器在预算内探索，以获得更稳定和泛化的性能提升。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM的能力高度依赖其外部的Harness（提示、工具、控制流、内存等）。自动化Harness优化是提升AI系统的重要手段，但社区缺少统一的评估协议。  
**方法**：提出HarnessOpt‑Bench基准——一个在昂贵且随机评估下的端到端优化任务。优化器（一个LLM搭配编码Harness）接收目标Agent的种子Harness、带评级的评估反馈和固定的评估预算，进行迭代修改，最终在模型从未见过的测试集上计算归一化增益。整个过程由信任执行环境（TEE）强制隔离，计量资源消耗并保留版本审计。实验选取5个前沿LLM作为优化器，在4个下游任务上运行111次评分，比较了统一编码Harness与各自原生Harness的表现。  
**关键结果**：(1) 不同优化器模型之间的性能差距明显大于它们所使用的编码Harness差异；(2) 原生Harness并不总是比统一编码Harness带来更优的优化效果；(3) 优化增益高度依赖于下游任务和种子Harness的设定。结论表明Harness优化是一个可测量、有区分度的能力，且存在巨大提升空间。
