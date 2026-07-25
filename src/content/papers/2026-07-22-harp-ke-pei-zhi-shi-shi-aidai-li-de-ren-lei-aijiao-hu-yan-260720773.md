---
title: 'HARP: The Human--AI Research Platform'
title_zh: HARP：可配置实时AI代理的人类-AI交互研究平台
authors:
- Zeshu Zhu
- Natalie Friedman
- Kevin Weatherwax
- Emily Eiben
affiliations:
- BTPX Innovation Lab
- BTPX User Assistance
arxiv_id: '2607.20773'
url: https://arxiv.org/abs/2607.20773
pdf_url: https://arxiv.org/pdf/2607.20773
published: '2026-07-22'
collected: '2026-07-25'
category: Other
direction: 人机交互实验工具
tags:
- HCI
- LLM interaction
- configurable agents
- experimental control
- behavioral logging
- user study platform
one_liner: 提出可精细控制LLM行为并记录键入、删除等微观交互数据的实验平台，支撑系统研究AI设计选择如何影响用户
practical_value: '- 在电商/推荐场景中，可复制其 **系统测试不同回复风格（如技术术语密度、解释长度）对用户信任、记忆和决策影响** 的方法，用于优化购物助手、推荐解释或客服机器人的话术设计。

  - 借鉴 **记录提示编写时长、删除次数、按键停顿** 等细粒度行为指标，补充到现有A/B测试中，捕捉用户对推荐结果或查询建议的犹豫与认知负荷，超越仅看点击率。

  - 平台设计思路提醒我们：**在Agent实验阶段就应内置可配置的参数体系（如system prompt、temperature、max tokens）和自动化的问卷触发点**，便于迭代优化交互体验。

  - 当需要比传统可用性测试更严格地对比LLM变体时，可参考其“受控模拟场景+实时智能体”范式，保证条件均衡与生态效度。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：研究人与LLM的对话式交互时，传统静态原型无法还原实时AI的动态响应，而常规日志又缺少用户输入前的编辑、犹豫等过程性行为，导致难以系统评估AI设计选择对用户的影响。

**方法关键点**：开发了Human–AI Research Platform (HARP)，将受试者置于受控模拟场景中与可实时配置的AI代理对话。研究者能统一控制不同实验条件下的系统提示、模型参数、响应特征（如专业度、长度），并按需触发调查问卷；平台自动记录提示编写耗时、响应延迟、文本删除、按键停顿等微观行为，未来将纳入语音、表情和手势分析。

**结果与应用示例**：论文通过一项实验展示平台能力，研究LLM输出的技术特异性和响应长度对信息保留的影响。该平台为评估AI交互设计提供了可控、可复现、细粒度的行为与自报告结合的测量框架。
