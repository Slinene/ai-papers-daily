---
title: 'Macaron-A2UI: A Model for Generative UI in Personal Agents'
title_zh: 'Macaron-A2UI: 面向个人助手的生成式UI模型'
authors:
- Fancy Kong
- Congjie Zheng
- Murphy Zhuang
- Rio Yang
- Sueky Zhang
- Hao Fu
- Gene Jin
- Song Cao
- Kaijie Chen
- Andrew Chen
affiliations:
- Mind Lab
arxiv_id: '2605.24830'
url: https://arxiv.org/abs/2605.24830
pdf_url: https://arxiv.org/pdf/2605.24830
published: '2026-05-23'
collected: '2026-05-26'
category: Agent
direction: 生成式UI · 智能体交互
tags:
- Generative UI
- Personal Agents
- LoRA
- Reinforcement Learning
- A2UI-Bench
one_liner: 提出Macaron-A2UI，通过LoRA微调与强化学习训练，无需模式提示即超越全模式基线，让智能体动态生成交互界面。
practical_value: '- **对话式电商中的偏好收集**：可借鉴轻量级UI动作生成（如多选、滑块、确认按钮），在对话推荐中动态收集用户偏好，避免纯文本交互的低效。

  - **高效微调大模型**：使用LoRA对70B+模型进行参数高效微调，在生成式UI任务中取得强效果，对需要定制化界面生成的电商Agent有直接工程复用价值。

  - **RL优化生成质量**：将UI生成视为序列决策问题，通过奖励模型优化整体交互体验，可迁移至对话式推荐系统的多轮交互优化。

  - **评估基准构建**：A2UI-Bench提供可控评估维度，可参考其设计思路构建面向电商场景的UI生成评测集，衡量信息收集、偏好精炼等子能力。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：静态文本聊天正成为个人智能体处理复杂用户任务的瓶颈，生成式UI能动态合成界面控件，但现有方法缺乏大规模数据和针对性训练。

**方法**：从异构对话源构建大规模生成式UI语料，引入A2UI-Bench可控评估基准。基于30B、235B、754B模型，先用LoRA进行有监督微调（SFT）使模型学会生成自然语言与可执行UI动作，再用奖励驱动的强化学习（RL）进一步优化。

**结果**：最佳Macaron-A2UI模型在无模式提示下达到75.6分（A2UI-Bench），超越最强的全模式提示基线模型。开源了模型、基准和评估协议。
