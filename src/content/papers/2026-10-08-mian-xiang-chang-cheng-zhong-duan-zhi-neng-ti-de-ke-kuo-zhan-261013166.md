---
title: Scaling Agentic Data for Long-Horizon Terminal Intelligence
title_zh: 面向长程终端智能体的可扩展数据合成引擎与 27B 模型
authors:
- Shun Zou
- Ziyu Ma
- Yi Zou
- Yong Wang
- Lin Chen
- Zehui Chen
- Guanhua Chen
- Xiangxiang Chu
- Feng Zhao
affiliations:
- University of Science and Technology of China
- AMAP, Alibaba Group
- Southern University of Science and Technology
arxiv_id: '2610.13166'
url: https://arxiv.org/abs/2610.13166
pdf_url: https://arxiv.org/pdf/2610.13166
published: '2026-10-08'
collected: '2026-10-13'
category: Agent
direction: 终端 Agent 长程数据合成与 SFT
tags:
- Long-horizon
- Terminal Agent
- Data Synthesis
- SFT
- Environment Reconstruction
- RSI
one_liner: TerminalHorizon 自动合成长程终端 Agent 数据，1.5K 环境 SFT Qwen3.5-27B 后在 12 个 benchmark
  全面提升
practical_value: '- 长程 Agent SFT 数据不能只靠环境自动补全，关键要保留“探索-试错-验证”证据链；在电商 Agent 场景（比价、选品、售后排查、广告账户优化）可借鉴“独立执行识别被省略的关键工作”，避免环境和工具过度简化导致模型只会调用工具、不会解决真实问题。

  - 渐进式任务扩展：同一目标下不断加入依赖前序结果的新需求，可构造多阶段、有长期依赖的训练轨迹；适合推荐/广告 Agent 的“分析→策略→执行→复盘”流程，增强模型跨阶段一致性与反馈利用能力。

  - 将环境重构证据显式纳入数据生产 pipeline，可自动化产出高质量 long-horizon trajectories，降低人工标注长程 Agent 数据成本；可结合内部
  terminal/sandbox 工具做 RSI-style 自改进评估。

  - 论文偏 terminal/coding agent，但 SFT 后通用推理提升的结论有迁移价值：可尝试用少量真实业务环境数据微调本地 LLM Agent，重点保留长期反馈与交付物迭代过程。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：终端 Agent 正在从执行本地命令走向完成现实专业任务。短轨迹只能展示命令和工具调用，无法覆盖 Agent 如何通过探索积累证据、基于反馈调整策略、把中间结果转化为最终交付物。长轨迹能捕获这些行为模式，但环境合成往往提前完成或简化了关键工作，反而移除了 Agent 本应执行的探索、实现和验证过程。

**方法关键点**：提出 TerminalHorizon，一个面向长程终端 Agent 的全自动数据合成引擎。它从真实专业工作出发，先通过独立执行识别环境构建时遗漏的关键工作，再用这些证据指导环境重建，避免过度简化。为跨阶段扩展行为模式，它在同一目标下渐进式扩展任务，引入依赖前序结果的新需求，促使 Agent 继续探索和改进。该引擎构建了 1.5K 个任务环境，并基于生成数据对 Qwen3.5-27B 做 SFT，得到 TerminalHorizon-27B。

**关键结果**：在 12 个 benchmark 上取得显著提升，覆盖 coding-agent 任务、真实生产环境 agentic 任务和通用推理。多个 RSI case study 显示，模型在 12 小时研究预算内能继续实验、基于反馈改进方法，并在最终交付物中保留有效改进。
