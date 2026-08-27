---
title: 'The Handoff Tax: Continuing Non-Native Trajectories in LLM Agents'
title_zh: 交接税：LLM Agent 续接非原生轨迹的代价
authors:
- Roy Ganz
- Mor Shpigel Nacson
- Adi Kalyanpur
- Ron Litman
affiliations:
- AWS
arxiv_id: '2608.24358'
url: https://arxiv.org/abs/2608.24358
pdf_url: https://arxiv.org/pdf/2608.24358
published: '2026-08-24'
collected: '2026-08-27'
category: Agent
direction: LLM Agent 模型交接与成本-质量权衡
tags:
- LLM agents
- model handoff
- trajectory interface
- cost-quality
- SWE-bench
one_liner: 首次系统研究 LLM Agent 中途切换模型时非原生轨迹对成本-质量权衡的影响，发现升级昂贵、降级更优
practical_value: '- 在多模型路由/级联系统中，避免把低成本模型的完整对话历史直接交给高成本模型（Raw escalation），可改为只传递工作状态（如中间结果、已编辑文件）或压缩摘要，以减少
  token 成本并避免低质轨迹锚定接收方。

  - 降级场景（强模型转弱模型）中，保留强模型的轨迹（推理、工具调用）比只保留最终输出更重要，轨迹中的思考过程能帮助弱模型延续工作；因此可设计选择性的上下文保留策略。

  - 使用归一化指标 QRec（质量恢复率）和 CSRet（成本节省保持率）评估切换策略，而非只看绝对成本或 pass rate，能更好对比不同模型对和切换接口的综合性价比。

  - 难度感知切换：在易/中任务上模型切换通常不划算，在难任务上使用精简上下文（Traj-drop 或 Compact）才可能获得成本效益；可将任务难度估计纳入切换决策。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
LLM 编码 Agent 运行长任务，涉及数十次模型调用和工具使用。用户常在低成本低能力模型（LC）和高成本高能力模型（HC）之间切换：当 LC 卡住时升级到 HC，或当难推理完成后降级到 LC。这种切换要求接收方续接另一个模型产生的非原生轨迹。现有工作多关注路由/级联，但未系统研究交接界面和轨迹信息对成本-质量权衡的影响。

## 方法关键点
- 在 SWE-bench Verified（500 个真实 GitHub issue）上，使用 mini-swe-agent 环境，测试 Claude Haiku 4.5/Opus 4.7 和 GPT-5.6 Luna/Sol 两组模型对。
- 切换方向：升级（LC→HC）和降级（HC→LC）；切换时机按难度校准的步数百分位（p5-p50，7 个点）。
- 交接界面：Raw（完整轨迹）、Compact_pre（前模型摘要）、Compact_suf（后模型摘要）、Traj-drop（丢弃轨迹仅保留工作树）。
- 指标：pass rate、成本、QRec（质量恢复率，相对 HC 优势）、CSRet（成本节省保持率，相对 LC 优势），在匹配的 switched subset 上比较。

## 关键实验与结果
- Raw 升级只能恢复不到一半的 LC-HC 质量差距（Claude QRec 47%，GPT 36%），且成本显著增加；Claude 中 Raw 升级比丢弃 LC 工作并从头重启 HC 更贵（$1.61 vs $0.90/$1.12），即被严格支配。
- Raw 降级提供有利的成本-质量中间点：Claude LC 保留大部分成本优势（CSRet 80%），GPT 保留大部分质量优势（QRec 79%）。
- 接口存在方向性对偶：减少 LC 轨迹信息（Traj-drop/Compact）改善升级质量；而保留 HC 轨迹对降级质量重要，Traj-drop 降级质量下降（Claude QRec 28% vs Raw 50%）。
- 成本机制：Raw 升级使 HC 每步调用更贵（Claude 2.2x），Traj-drop 降级使 LC 步数增加（Claude 1.6x）。
- 难度影响：在 hard 任务上，精简上下文接口的升级才比 HC-only 便宜，easy/medium 不划算。
- 扩展到 LiC 和 BrowseComp：信息动态影响切换价值，延迟需求有利于强后缀（升级 QRec 86%），渐进搜索升级能恢复质量但不省钱。

## 最值得记住的一句话
在 LLM Agent 中，交接的不是对话而是另一个模型的认知轨迹；如何传递这些轨迹（完整/压缩/丢弃）对成本-质量影响巨大，升级时应减少低质轨迹，降级时应保留强质轨迹。
