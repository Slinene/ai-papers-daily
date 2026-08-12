---
title: 'VibeLifeBench: Can Your Life Agent Be Proactive and Persistent in a Living
  World?'
title_zh: VibeLifeBench：多周生活世界中主动持久的生活助理评测基准
authors:
- Xiaohongshu Inc
affiliations:
- Xiaohongshu Dots Studio
- Evolvent AI
arxiv_id: '2608.10875'
url: https://arxiv.org/abs/2608.10875
pdf_url: https://arxiv.org/pdf/2608.10875
published: '2026-08-10'
collected: '2026-08-12'
category: Eval
direction: 长周期主动式 Agent 评测
tags:
- Long-horizon
- Proactivity
- Persistence
- LLM Agents
- Benchmark
- Everyday-life Assistance
one_liner: 提出了首个衡量 LLM agent 在长期变化世界中主动性与持续性的评测基准，发现所有前沿模型得分极低
practical_value: '- 电商购物助理等长期交互场景可借鉴：agent 需具备主动察变能力（如价格波动、库存变化），而不仅是响应指令。

  - 评测需覆盖三个维度：最终状态、行动及时性、隐含约束遵守——业务中类似“隐含约束”（如不打扰用户休息）往往比明面要求更重要。

  - 模拟世界“时间自动推进且变动沉默”的设计，可直接复用到长期推荐或营销推送的离线回测框架，强制 agent 周期性重检。

  - 开源的任务与环境可作为构建“长期主动推荐 agent”的测试床，验证上下文保持与跨会话连贯性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM agent 评测大多基于静态、短会话的请求，无法反映日常生活中持续数周、环境持续变化、且许多约束未明说的情况。真实生活助理要求 agent 在无人提示时主动决策、察觉悄然变化并保持计划的连贯性，现有基准均未覆盖。

**方法**：提出 VibeLifeBench，包含 200 个长期任务，覆盖 10 个日常生活领域（如多周旅行、租房纠纷、家庭装修）。每个任务在包含 22 个模拟服务（日历、邮件、天气等）的脚本化多周时间线中进行，世界按其自身时钟推进，很多变化不会主动通知 agent，只有主动重新检查状态才能发现。评分采用细粒度加权检查，仅读取 agent 实际留下的痕迹，综合评估最终状态、行动及时性以及是否遵守了未说明的约束。

**关键结果**：测试 7 款前沿模型，所有模型得分均很低，暴露出当前 agent 在长期持久性与主动性方面的严重不足。该基准将开源。
