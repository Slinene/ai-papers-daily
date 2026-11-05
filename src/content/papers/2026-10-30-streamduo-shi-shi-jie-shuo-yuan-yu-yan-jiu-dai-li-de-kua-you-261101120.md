---
title: 'StreamDuo: A Live Commentator and a Research Agent for Unseen Games'
title_zh: StreamDuo：实时解说员与研究代理的跨游戏流式解说
authors:
- Zixian Gao
- Penghao Luo
- Xiangcheng Cao
- Lixin Xiu
- Ziqi Cai
- Zhen Li
- Erwin Wu
- Kaipeng Zhang
affiliations:
- Alaya Lab
- The University of Tokyo
- Georgia Institute of Technology
- Peking University
- Institute of Science Tokyo
arxiv_id: '2611.01120'
url: https://arxiv.org/abs/2611.01120
pdf_url: https://arxiv.org/pdf/2611.01120
published: '2026-10-30'
collected: '2026-11-05'
category: Agent
direction: Agent 主动知识检索与流式解说
tags:
- Agent
- RAG
- Streaming Commentary
- Information-Gain
- Self-Distillation
- Cross-domain
one_liner: 配对可训练解说员与冻结研究代理，用信息增益标记与自蒸馏训练，在未见游戏上提升实体召回并减少泄漏
practical_value: '- 将“何时查询外部知识”作为可训练决策：用信息增益标签标注训练样本，让模型学会只在答案有助于匹配目标输出时才触发 RAG/工具调用，避免过度检索带来的延迟和噪声。在电商搜索推荐中可用于解释生成、Query
  改写或商品知识补充的 gating 策略。

  - 冻结知识检索侧、只训练决策/生成侧：架构上把外部知识库和检索器保持冻结，仅微调轻量的策略模型，降低跨品类/跨域迁移成本。电商中可固定商品知识库，微调推荐解释或对话策略模型。

  - on-policy self-distillation 处理不完美工具返回：用能看见理想答案的模型副本作为教师，蒸馏给使用噪声检索结果的在线策略，增强对检索质量波动的鲁棒性。这适用于外部
  API/知识库返回不稳定时的生成任务。

  - 异步知识增强设计：查询结果约 2 秒后注入，直播流不阻塞。在实时推荐或对话系统中可先给出兜底生成，后续补充信息，避免延迟影响用户体验。'
score: 6
source: huggingface-daily
depth: abstract
---

现有流式视频 LLM 解说模型通常在训练和测试使用同一游戏，跨游戏时能迁移解说时机但无法迁移游戏世界知识，导致无法叫出角色、地点等实体。

StreamDuo 采用双代理架构：可训练的解说员（commentator）配一个冻结的研究代理（research agent），后者读取所玩游戏的 wiki。当解说员识别到不确定的实体时，将当前帧发送给研究代理；约 2 秒后，研究代理返回少量 wiki 条目，直播流持续进行。训练只在《博德之门 3》单个游戏上进行，分两阶段：先用信息增益标签让解说员学会只在“答案能帮助它说出人类解说员实际内容”时才提问；再用 on-policy 自蒸馏，从能看到理想答案的自身副本学习如何有效利用带噪声的返回结果。

在十个未见游戏上测试，StreamDuo 的实体召回从 0.082 提升到 0.116（对比同样数据训练的 Proact-VL），源游戏泄漏从 9.9% 降至 1.0%，同时获得最佳解说时机和最高的人工评判生动性及整体质量。
