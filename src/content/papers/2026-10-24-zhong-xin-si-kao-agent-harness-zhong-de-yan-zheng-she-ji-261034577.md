---
title: Rethinking Verification in Agent Harnesses
title_zh: 重新思考 Agent Harness 中的验证设计
authors:
- Zhengxin Zhang
- Erkang Zhu
- Yin Lin
- Claire Cardie
- Bolin Ding
- Jingren Zhou
affiliations:
- Cornell University
- Alibaba Group
arxiv_id: '2610.34577'
url: https://arxiv.org/abs/2610.34577
pdf_url: https://arxiv.org/pdf/2610.34577
published: '2026-10-24'
collected: '2026-10-28'
category: Agent
direction: Agent 验证设计与低成本 critic 扩展
tags:
- Agent Verification
- Critic
- Test-Time Scaling
- SWE-bench
- Terminal-Bench
- Coding Agents
one_liner: 系统对比 17 种 agent 验证设计，独立低费 critic 带来 5.9–9.5pp 编码提升且成本仅 1.13–1.25×
practical_value: '- 在电商 Agent 工作流（自动生成 SQL、商品文案、广告素材、数据分析报告）中，把最终验收拆给独立 critic，而不是让执行
  agent 自查；critic 可用低成本模型，上下文只给任务要求和 diff/changes，不给完整轨迹，可降低 critic token 29–43% 且效果更稳。

  - 对可视化/交互产物（如落地页、创意 Banner、可交互配置器），在 critic 指令中要求调用渲染/截图工具做视觉检查；VisualBench 显示 changes
  + visual inspection 净偏好最高（+23.8pp）。

  - 用系统提示词注入简洁 verification instruction，并在每次代码/文件修改后插入 after-edit reminder，可作为低成本
  default；但不要轻易使用完成时自我复查完成门，容易显著抬高成本。

  - 如需继续 scale，优先增加独立 critic 数量（width）并合并反馈后一次修订，比多轮 review（depth）更省总成本（约 19% lower）；避免让主
  agent 多次重复执行。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent harness 决定何时检查、谁来检查、如何修正，但现有工程验证设计靠经验启发，缺少系统性 trade-off 证据。验证直接影响编码 agent 的质量和 token 成本，需要按生命周期拆解。

**方法关键点**
- 按生命周期分四层：L0 初始验证指令、L1 执行中提醒、L2 完成门自查、L3 独立 critic 审查。
- 17 种设计，控制消息角色、触发时机、critic 上下文（changes vs trajectory；task-first vs claim-guided）、review 轮数/个数。
- 环境为 E2B sandbox，critic 可运行检查但不可改文件；7 个前沿 coding model，Qwen3.7-Plus 作 critic。
- 基准：Terminal-Bench、SWE-bench Verified、内部 VisualBench（18 个可视化/交互任务，盲评功能与视觉质量）。

**关键结果**
- L0/L1 平均增益温和且依赖模型：TB +3.3～+5.4pp，SWE +3.1～+3.6pp；输出 token 不增或下降。
- L2 完成门可能大幅提高成本（拒绝式 1.60–1.76× TB / 1.48–1.56× SWE），增益有限。
- L3 独立 review 最佳：TB +5.9–9.5pp、SWE +3.9–6.6pp，成本仅 1.13–1.25× / 1.00–1.04×；VisualBench 净偏好 +13.2～+23.8pp，超过 L0–L2。
- Changes-based 优于 trajectory；多 critic/多轮可再提升至 +3.5pp，多 critic 更省成本。

**最值得记住**：在 harness 验收前加独立低费 critic，只看任务+变更，用可执行失败引导主 agent 修复，比让 agent 自我复查更划算。
