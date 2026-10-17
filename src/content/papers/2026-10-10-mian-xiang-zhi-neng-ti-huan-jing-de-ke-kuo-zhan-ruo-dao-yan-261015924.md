---
title: Scalable Weak-to-Strong Verifier Hardening for Agent Environments
title_zh: 面向智能体环境的可扩展弱到强验证器加固
authors:
- Chong Zeng
- Ziqian Zhong
- Kexun Zhang
- Ivan Bercovich
- Ivgeni Segal
- Yuzhen Mao
- Shashwat Saxena
- Aditi Raghunathan
affiliations:
- Stanford University
- Carnegie Mellon University
- Fewshot Corp
- Independent Researcher
arxiv_id: '2610.15924'
url: https://arxiv.org/abs/2610.15924
pdf_url: https://arxiv.org/pdf/2610.15924
published: '2026-10-10'
collected: '2026-10-17'
category: Agent
direction: Agent 环境验证器加固与奖励安全
tags:
- Verifier Hardening
- Reward Hacking
- Agent Environments
- Weak-to-Strong
- LLM Security
one_liner: 隔离验证器沙箱加 hacker-fixer 迭代循环，全自动大幅降低攻击成功率
practical_value: '- 在电商搜索/推荐的 Agent 评估中，若使用程序化规则或 LLM-as-a-judge 给出奖励，可借鉴 hacker-fixer
  循环做上线前攻击审计：用弱模型主动找评估器漏洞，迭代修复后再部署，减少 reward hacking 导致的不准确评测与训练偏误。

  - 多智能体系统里，将 verifier/裁判模块与执行 agent 的状态空间隔离，防止 agent 直接改写奖励信号或评测结果，确保 RL 或 online
  策略的奖励信号干净。

  - 弱到强范式有实用价值：即使当前攻击模型能力较弱，也能产生对更强未来模型的防御增益，适合预算有限时提前加固线上奖励函数或评估器。

  - 加固效果随迭代次数提升，建议设置自动化流水线并预留 hardening budget，周期性重跑而非静态一次性修复。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：Agent 环境用程序化验证器把复杂结果转成奖励，但验证器可被攻击给作弊 agent 满分，导致评估不准、训练偏误。环境规模扩大后需自动加固。  
方法：提出全自动弱到强验证器加固。先建立隔离验证器沙箱，agent 不能直接修改；再用 hacker-fixer 循环，动态发现并修复剩余漏洞。  
结果：在 Terminal Bench、KernelBench、SETA 上大幅降低攻击成功率，如 Terminal Bench 的 unhinted ASR 从 69.9%/43.5%/23.2% 降至 12.1%/7.8%/8.2%；KernelBench 三个强 agent 的 ASR 分别降至 0.0%/0.0%/1.9%。迭代设计随硬化预算扩展，防御随迭代增强，优于静态非迭代基线。早期版本已被 Terminal Bench 官方仓库采纳用于漏洞审计。
