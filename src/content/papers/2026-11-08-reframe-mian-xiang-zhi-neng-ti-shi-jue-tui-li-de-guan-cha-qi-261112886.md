---
title: 'Reframe: Observation-Aligned Multi-Teacher On-Policy Distillation for Agentic
  Visual Reasoning'
title_zh: Reframe：面向智能体视觉推理的观察对齐多教师在线策略蒸馏
authors:
- Haozhi Yuan
- Handong Li
- Yifan Zhang
- Qianshan Wei
affiliations:
- Nanjing University
- Institute of Automation, Chinese Academy of Sciences
arxiv_id: '2611.12886'
url: https://arxiv.org/abs/2611.12886
pdf_url: https://arxiv.org/pdf/2611.12886
published: '2026-11-08'
collected: '2026-11-11'
category: Training
direction: Agentic VLM 后训练 · 观察对齐
tags:
- Agentic RL
- GRPO
- Multi-Teacher Distillation
- Visual Reasoning
- Tool Use
- Observation Alignment
one_liner: Reframe 通过观察对齐的强化学习与多教师蒸馏，缓解视觉 Agent 忽略工具返回观测的问题
practical_value: '- **观察依赖奖励可迁移到多模态 Agent 训练**：电商搜索/推荐中的 Agent 常调用商品图、评论区、OCR 等工具，但模型可能忽略返回信息。可借鉴
  GD-GRPO 的 evidence-aware reward，对“是否实际使用工具观测”给予显式奖励，减少观察忽略。

  - **随机丢弃原始输入可提升工具增益**：Ground-Drop 机制随机去除原始图像/文本，强制模型依赖工具返回证据。在商品视觉问答、多模态搜索 rerank
  等场景，可用类似 dropout 训练提升工具调用收益。

  - **OG-MOPD 可用于离线轨迹修复与蒸馏**：将低质量工具动作替换为规范动作并从修复后观察继续 rollout，能改善 on-policy 蒸馏的数据质量。对电商
  Agent 的历史日志，可先修复错误工具调用再蒸馏，提升策略质量。

  - **无需 SFT 冷启动降低落地门槛**：Reframe 证明可直接从预训练 VLM 开始 RL + 蒸馏，避免任务特定 SFT 数据准备，适合快速迭代现有
  Agent 策略。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：视觉 Agent 通过工具获取细粒度证据，但常出现 observation neglect——模型调用了工具却不使用返回的观测，导致后续推理几乎不受影响；同时低质量的动作会限制后续蒸馏可用的证据。

**方法关键点**：Reframe 将观察状态本身作为对齐目标，分两阶段。第一阶段 Ground-Drop-GRPO (GD-GRPO) 训练空间/时间专家，使用 evidence-aware rewards，并随机丢弃原始视觉输入，强制策略依赖工具返回的观测。第二阶段 Observation-Gated-MOPD (OG-MOPD) 在 rollout 中识别并替换低质量工具动作，用规范动作修复观察，然后从修复后的状态继续多教师蒸馏。两阶段互补：先学会依赖工具观测，后续就能从观察修复中受益。整个过程无需任务特定 SFT 冷启动。

**结果**：在 14 个图像和视频基准上，Reframe 优于 Mix-RL 和 vanilla MOPD。消融显示 GD-GRPO 相比 outcome-based GRPO 显著提升 observation dependence 和 tool gain。
