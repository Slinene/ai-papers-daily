---
title: 'MyPCBench: A Benchmark for Personally Intelligent Computer-Use Agents'
title_zh: 'MyPCBench: 个性化计算机代理评测基准'
authors:
- Lawrence Keunho Jang
- Andrew Keunwoo Jang
- Jing Yu Koh
- Ruslan Salakhutdinov
affiliations:
- Carnegie Mellon University
arxiv_id: '2606.16748'
url: https://arxiv.org/abs/2606.16748
pdf_url: https://arxiv.org/pdf/2606.16748
published: '2026-06-14'
collected: '2026-06-19'
category: Agent
direction: 个性化Agent评测 · 桌面环境
tags:
- Personalization
- Computer-Use Agents
- Benchmark
- LLM Agents
- Desktop Automation
- Web Tasks
one_liner: 首个模拟真实用户数字生活的个性化计算机代理基准，揭示跨应用长链任务的高失败率
practical_value: '- 在电商Agent评测中，可类似构建含用户历史订单、偏好、收货地址的模拟桌面/浏览环境，使评测更贴近真实部署。

  - 关注长链跨应用任务（如搜索商品→比价→下单→售后）的评估，模型在这些场景下易失败，需专项优化。

  - 引入用户数字踪迹（日历、邮件、聊天记录）作为上下文，可能提升Agent个性化表现，但评测显示当前模型仍难以有效利用。

  - 对于需要登录态或隐私数据的工作流，离线模拟环境比在线评估更安全且可重复。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有计算机代理评测使用空白桌面和通用应用状态，忽视真实个人助理所需的个性化上下文（登录信息、历史数据、跨应用记忆），导致评测与部署差距大。

**方法**：构建 MyPCBench，在 Linux 桌面上配置 17 个模拟真实 Web 应用（邮箱、日历、银行、购物等），全部填充一个典型角色（Michael Scott）的完整数字生活数据。定义 184 个任务，覆盖从简单查询到跨多应用的长链操作，均源自 OpenClaw 社区的真实用户请求。使用统一的 computer+bash 工具接口测试 6 个闭源/开源模型。

**结果**：最强模型 Claude Opus 4.6 仅完全解决 55.4% 的任务，是唯一超过 50% 的模型。失败主要集中在需要跨多个应用和长轨迹的任务上，表明个性化对代理压力最大。环境与任务集已开源。
