---
title: 'PalmClaw: A Native On-Device Agent Framework for Mobile Phones'
title_zh: PalmClaw：移动端原生设备能力工具化 Agent 框架
authors:
- Hongru Cai
- Yongqi Li
- Ran Wei
- Wenjie Li
affiliations:
- The Hong Kong Polytechnic University
- Hangzhou Diagens Biotechnology Co., Ltd.
arxiv_id: '2607.13027'
url: https://arxiv.org/abs/2607.13027
pdf_url: https://arxiv.org/pdf/2607.13027
published: '2026-07-13'
collected: '2026-07-17'
category: Agent
direction: 移动端原生 Agent 架构 · 设备能力工具化
tags:
- On-Device Agent
- Mobile Agent
- Tool Use
- Device Tools
- Execution Boundaries
- LLM Agent
one_liner: 将手机能力封装为结构化工具，任务成功率相对提升11.5%，完成时间锐减94.9%
practical_value: '- 在移动端电商 Agent（自动比价、下单、提醒）中，将设备功能封装为严格参数化工具，可替代脆弱的 GUI 模拟，提升任务成功率。

  - 工具定义需明确输入参数与结构化返回，形成清晰执行边界——这一设计与推荐系统中 API 封装（如商品搜索接口）的设计原则一致，可降低 Agent 规划复杂度。

  - 长操作序列（如多步 GUI 点击）合并为单次设备工具调用，大幅缩短耗时（实验减少 94.9%），对实时性要求高的搜索/推荐后链路执行有直接借鉴意义。

  - 若构建 LLM 驱动的搜索推荐助手，借鉴其设备工具抽象方法，可将每个数据源、模型服务明确定义为工具，使 Agent 调度更稳定可追溯。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有移动 Agent 依赖 GUI 模拟操作（点击、滑动），步骤冗长、依赖界面状态、执行边界模糊，无法直接调用手机传感器与功能，效率低且不可靠。

**方法**：PalmClaw 原生运行在手机上，管理会话、记忆、技能、工具和 Agent 循环。将设备能力（如短信、相机、闹钟）封装为“设备工具”，每个工具具有明确的参数定义、结构化返回值和清晰的执行边界。Agent 在循环中直接调用这些工具，而非模拟屏幕交互，从而缩短决策链、提高动作可控性。

**结果**：在常用任务基准上，比最强基线方法相对提升 11.5% 的任务成功率；完成时间减少 94.9%；且设置负担更低。通过执行边界追踪展示了每个工具调用的起止与状态转换，验证了原子化操作的优势。
