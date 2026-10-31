---
title: 'AskStream: When and What to Ask Proactively under Uncertainty in Streaming
  Video Understanding'
title_zh: AskStream：流式视频理解不确定性下何时与如何主动提问
authors:
- Lu Wang
- Zhuoran Jin
- Longxiang Wang
- Junhong Chen
- Yupu Hao
- Yao Xu
- Daojian Zeng
- Yubo Chen
- Kang Liu
- Guang Liu
affiliations:
- Institute of Automation, Chinese Academy of Sciences
- Beijing Academy of Artificial Intelligence
- Hunan Normal University
- Minzu University of China
arxiv_id: '2610.38678'
url: https://arxiv.org/abs/2610.38678
pdf_url: https://arxiv.org/pdf/2610.38678
published: '2026-10-27'
collected: '2026-10-31'
category: Agent
direction: 多模态流式视频主动交互智能体
tags:
- Proactive Interaction
- Streaming Video
- Uncertainty
- MLLM
- Benchmark
- Ask-F1
one_liner: 引入主动 ask 动作的流式视频理解基准，评估模型在视频与用户不确定性下的提问与回答策略
practical_value: '- 在电商直播、视频客服等流式交互场景中，可把 Agent 的动作空间从 wait/answer 扩展为 wait/ask/answer：当模型对用户意图或视频内容置信度低时，主动发起澄清问题，避免停止等待或生成幻觉答案。

  - 参考 AskStream 的帧级时间窗标注，把“何时提问”建模为序列决策问题；在真实流式视频数据上标注每一帧或每一时间窗应执行 wait/ask/answer，用于训练主动交互策略。

  - 设计类似 Ask-F1 的评估指标，同时考虑回答质量、提问代价与等待收益，而不只看最终答案准确率；在推荐/广告交互中可迁移为“澄清问题的性价比”，平衡打扰率与信息增益。

  - 落地成本提示：该基准集中于视频理解，工业界需先构建领域内不确定性标注，但可复用其问题定义与评测框架来低成本启动。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：流式视频理解正从被动响应转向主动交互，但现有 proactive 范式假设回答问题所需信息已完整，模型只能 wait 或 answer。真实场景中视频内容和用户意图常存在不确定性，导致模型无限等待或产生幻觉回答。

**方法关键点**：提出 AskStream 基准，重新定义主动交互为三种动作：wait、ask、answer。模型可在回答前主动请求缺失信息。该基准覆盖视频与用户两类不确定性，包含 4 类任务、8 个子任务；收集 438 个视频，人工标注 2,714 个帧级时间窗，每个窗口标记为 wait/ask/answer。支持多选与开放式设置，并提出 Ask-F1 综合指标评估提问策略、回答质量和等待成本。

**关键结果**：在 Ask-F1 上最强模型仅达到 52.18%，表明现有 MLLM 在不确定性下主动信息寻求能力严重不足。
