---
title: Online Safety Monitoring for LLMs
title_zh: LLM在线安全监控的简单阈值方法
authors:
- Mona Schirmer
- Metod Jazbec
- Alexander Timans
- Christian Naesseth
- Maja Waldron
- Eric Nalisnick
affiliations:
- UvA Bosch-Delta Lab, University of Amsterdam
- University of Wisconsin Madison
- Johns Hopkins University
arxiv_id: '2607.02510'
url: https://arxiv.org/abs/2607.02510
pdf_url: https://arxiv.org/pdf/2607.02510
published: '2026-07-02'
collected: '2026-07-03'
category: Eval
direction: LLM在线安全监控与风险控制
tags:
- Online Monitoring
- LLM Safety
- Risk Control
- Threshold Calibration
- Verifier Signal
one_liner: 简单的阈值监控结合风险控制校准，在线安全检测性能媲美复杂序贯检验方法
practical_value: '- 在Agent或搜索推荐系统的在线生成链路中，可外接一个安全验证器（如毒性分类器），对其输出分数做阈值判决，实现实时拦截有害内容。

  - 阈值通过风险控制方法（如设置可接受误报率上限）在线校准，无需依赖标注数据，适合动态生产环境。

  - 简单阈值方案工程成本低且效果好，与复杂的序贯假设检验监控器性能相当，可优先尝试。

  - 监控粒度为流式 token 级别时，可将验证器部署在低延迟推理管道，及时中止不安全生成，避免后续风险。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：尽管经过对齐训练，LLM 在部署时仍可能产生不安全输出，且离线评估无法覆盖所有实时场景，因此需要在线实时监控并触发警报。  
**方法**：提出一种轻量级在线监控器，利用外部验证模型（如安全分类器）输出一个信号，通过对该信号做阈值判决来决定是否报警；阈值通过风险控制（risk control）框架校准，旨在把错误报警率控制在一个预设范围内。该方法无需在线标注，且计算开销低。  
**结果**：在数学推理和红队测试数据集上，这一简单设计的监控性能与基于序贯假设检验的更复杂监控器相当，能有效检测不安全生成，同时保持风险可控。
