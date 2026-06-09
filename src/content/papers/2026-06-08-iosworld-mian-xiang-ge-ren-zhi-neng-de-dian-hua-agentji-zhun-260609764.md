---
title: 'iOSWorld: A Benchmark for Personally Intelligent Phone Agents'
title_zh: iOSWorld：面向个人智能的电话Agent基准测试
authors:
- Lawrence Keunho Jang
- Mareks Woodside
- Geronimo Carom
- Andrew Keunwoo Jang
- Jing Yu Koh
- Ruslan Salakhutdinov
affiliations:
- Carnegie Mellon University
arxiv_id: '2606.09764'
url: https://arxiv.org/abs/2606.09764
pdf_url: https://arxiv.org/pdf/2606.09764
published: '2026-06-08'
collected: '2026-06-09'
category: Agent
direction: 移动端Agent评测 · 个人化推理
tags:
- mobile agents
- personalization
- iOS
- benchmark
- multi-app reasoning
one_liner: 首个以持久用户身份为中心的交互式iOS模拟器基准，涵盖133个跨应用任务，强调个人化智能与多应用推理。
practical_value: '- **构建跨应用的个性化评测**：可借鉴其思路，在电商场景中构造包含用户历史订单、支付、邮件、客服、社交等多应用数据，设计需要跨应用推理和记忆的任务，评估Agent是否能理解用户偏好与上下文，而不是孤立执行单步指令。

  - **LLM-as-Judge的轨迹级评估**：使用GPT-5.4-Mini对整个操作轨迹进行自动评判，人工验证κ=0.77，成本低且可靠。可直接迁移到Agent业务流程的离线评测，替代部分人工验收。

  - **小模型对额外结构化上下文的利用瓶颈**：视觉+XML模态下GPT-5.4-Mini和Qwen3.5不升反降，说明提供界面结构信息并非总是利好，容量小的模型会被额外token压垮。在工程中为Agent补充页面结构或工具描述时，需评估模型是否具备足够的上下文处理能力。

  - **模拟器环境与种子数据设计**：通过虚构用户、持久化种子数据构建可复现的测试环境，适合在隐私敏感且需要真实用户行为的电商推荐或Agent评测场景中快速构建仿真台。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
现有手机Agent基准测试缺乏个性化维度，任务只针对空白应用状态，没有持久用户身份和历史数据，无法评估Agent对用户习惯、偏好的推理能力。iOSWorld填补了这一空白：它是一个围绕单一虚构用户（Jordan Avery）构建的交互式iOS模拟器基准，包含26个定制应用，应用间通过共享联系人、交易、行程等实现数据互联，提供跨应用连续性和记忆要求。

**方法关键点**
- **环境与任务**：26个SwiftUI应用覆盖金融、消息、旅行、餐饮等10个生活域，133个任务分为单应用（27）、多应用（60，跨2-8个应用）和记忆/个性化（46，需推断隐含模式）三类。
- **观测与行动空间**：评估两种模态——仅视觉（Vision-only）与视觉+XML（XCUITest导出的界面结构树），行动空间包括坐标点击、键入、滑动等，视觉+XML可额外用元素标识直接定位。
- **评估框架**：以GPT-5.4-Mini作为轨迹级评判者，与人工标注一致性达κ=0.77，主要度量二元通过率，并辅以步骤级评分和准则评分。
- **模型与配置**：测试5个前沿商用模型（Opus 4.6、Sonnet 4.6、GPT-5.4等）和1个开源模型（Qwen3.5 35B-A3B），均在50步预算内运行。

**关键结果**
- 总体最佳配置（视觉+XML）通过率52%，其中单应用93%，多应用仅37%，记忆类54%。
- 视觉+XML大幅提升强模型表现：Opus从26%升至52%（+25.6pp），Sonnet从29%升至47%（+18.0pp），但GPT-5.4-Mini和Qwen3.5下降，显示出对额外上下文容量不足。
- 失败模式分析：51%的失败因步数耗尽，23%为过早停止。多应用任务仍是最难类别，步数预算曲线显示多应用和记忆类仍在40步后继续提升。

**最值得记住的一句话**
即使给Agent装上眼睛（视觉），再给上界面说明书（XML），跨多应用推理和从个人历史中发现模式仍然是当前最强模型在手机环境中面临的巨大挑战。
