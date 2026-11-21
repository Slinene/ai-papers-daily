---
title: 'ZeroVLN: Learning to Navigate without Supervised Fine-Tuning of the VLM Brain'
title_zh: ZeroVLN：无需对 VLM 大脑监督微调的导航学习
authors:
- Zixuan Huang
- Yang Zhou
- Guli Zhang
- Sunzhu Li
- Hongyan Xie
- Zehao Chen
- Fuzhen Zhuang
- Kaixuan Wang
- Xiaozhi Chen
- Yikun Ban
affiliations:
- Beihang University
- Zhuoyu Technology, Shenzhen, China
- Zhejiang University
arxiv_id: '2611.26414'
url: https://arxiv.org/abs/2611.26414
pdf_url: https://arxiv.org/pdf/2611.26414
published: '2026-11-18'
collected: '2026-11-21'
category: Agent
direction: Agent 慢快策略联合 RL 优化
tags:
- VLN
- VLM
- Reinforcement Learning
- Agent
- Tool Calling
- Slow-Fast
one_liner: 提出 ZeroVLN，在零导航域 SFT 下用工具调用与闭环 RL 联合优化 VLM 慢策略和动作专家快策略
practical_value: '- 业务 Agent 中可借鉴：对通用 LLM/VLM 不做领域 SFT，通过 tool-calling 接口让模型输出自然语言决策，由专门执行器完成具体动作，避免基座能力退化。

  - 分层 slow-fast 架构：慢策略负责语义级决策/工具选择，快策略负责低延迟连续执行；推荐/搜索场景可让 LLM 只输出高层意图（如 query 改写方向、选品策略），由策略网络执行具体排序或出价。

  - 闭环 RL 联合优化：不要只依赖 SFT，可在模拟环境或线上沙箱中同时优化决策模型与执行策略，提升协同效果。

  - 基座模型更新安全：可借鉴其监控权重位移和通用能力保留的方法，作为上线前的安全指标。'
score: 6
source: huggingface-daily
depth: abstract
---

## 动机

代表性 VLN 方法通常将 VLM 大脑与可学习动作头耦合，并在导航域数据上微调 VLM 以预测几何目标。但这种适配会显著改变基座 VLM 权重，导致通用视觉能力下降。

## 方法关键点

ZeroVLN 提出慢-快导航框架，完全不进行导航域 SFT。VLM 大脑不预测几何目标，而是配备语义工具调用接口，用自然语言向动作专家传达移动决策。训练分两步：先适配动作专家执行这些移动请求，再通过闭环强化学习联合优化 VLM 的移动决策与动作专家的连续执行。

## 关键结果

在相同导航 episode 上训练后，ZeroVLN 在标准 VLN-CE 连续环境基准上显著优于代表性基于 SFT 的分层 VLN 方法，同时只对 VLM 大脑权重造成轻微变化，并大幅保留其通用能力。ZeroVLN 是首个零导航域 SFT 的慢-快 VLN 框架，也是首个在 VLN-CE 中通过闭环 agentic RL 联合优化慢策略与快策略的方法。
