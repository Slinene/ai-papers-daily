---
title: 'OmniInteract: Benchmarking Real-World Streaming Interaction for Real-Time
  Omnimodal Assistants'
title_zh: OmniInteract：面向实时全模态助手的流式交互评测基准
authors:
- Xudong Lu
- Xueying Li
- Annan Wang
- Yang Bo
- Jinpeng Chen
- Zengliang Li
- Nianzu Yang
- Rui Liu
- Xue Yang
- Jingwen Hou
affiliations:
- CUHK MMLab
- SJTU
- NTU
- McMaster
- CityUHK
arxiv_id: '2605.26485'
url: https://arxiv.org/abs/2605.26485
pdf_url: https://arxiv.org/pdf/2605.26485
published: '2026-05-25'
collected: '2026-05-31'
category: Eval
direction: 实时多模态交互评测 · 流式视频理解
tags:
- Omnimodal LLMs
- Streaming Interaction
- Online Inference
- Real-time Evaluation
- Full-duplex
- Benchmark
one_liner: 首个通过原生在线流式推理评估全模态LLM的交互基准，系统衡量响应时机、中断处理和嵌套对话能力
practical_value: '- **交互评估体系可直接复用**：定义 interaction slot（trigger、response window、target
  answer）和 IA-QTF1 指标，综合衡量回答内容、时机和不当输出（spill、早响幻觉），可用于评估电商客服助手、直播推荐 Agent 的实时交互质量

  - **原生在线推理范式对 Agent 部署有启发**：要求模型仅依据已发生流内容决策，禁止未来窥探，这对构建真实场景下的生成式推荐或对话式 Agent 有直接指导，避免离线假设导致的性能高估

  - **全双工中断与嵌套交互分析**：通过 Interruption Diagnostic Suite 和 Nested Chain Completion Score，量化模型在被打断后的沉降与上下文恢复能力，可借鉴其设计思路优化多智体协作或用户频繁打断场景下的响应策略

  - **离线能力≠在线表现**：实验发现 MiniCPM-o 从离线到在线数学推理质量下降 0.3358，提示业务迁移时需专门评估在线流式性能，不能仅依赖离线基准'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机
现有视频问答基准多采用离线全量或文本提示的流式推理，无法反映全模态实时助手面临的三大核心挑战：（1）从连续音视频流中自发识别语音意图；（2）在正确时机而非任意时刻给出回应；（3）处理用户打断、嵌套提问和上下文恢复。这些缺陷导致离线高性能模型未必能胜任真实交互。

## 方法关键点
- **交互槽位设计**：将连续流离散化为一系列 temporally grounded 响应机会，每个槽位由触发条件（trigger）、有效回答窗口（[t_start, t_end)）和目标答案组成，覆盖实时响应、主动监测、嵌套提问和连续多步监控四类场景。
- **数据集构建**：自录制210个中文日常交互和英语数学解题视频，并利用现有步骤指导/错误检测数据构造40个长程监控视频，共250段视频、1,430个响应槽位，包含192个中断样例。所有用户查询以语音形式嵌入音频流，保留原始视觉事件与背景音。
- **评估指标**：提出 IA-QTF1（Interaction-Aware Quality-Timeliness F1），通过软 TP 融合核心回答的语义质量与时序衰减，并对溢出、早响幻觉、漏回进行 FP/FN 惩罚。额外设计 Interruption Diagnostic Suite（NOR/PAQ/CSM）和 Nested Chain Completion Score，专项诊断中断与上下文恢复。
- **评估协议**：要求模型通过其原生实时接口以在线流式方式推理，仅可感知过去与当前内容，不可访问未来帧或 ground-truth 边界。

## 关键结果
- 在 1Q1A 场景中，最佳全局 IA-QTF1 仅 0.467（AURA）；在需要连续多步响应的 1QnA 场景中，所有模型均溃败，最高仅 0.052。
- 中断处理：Gemini 倾向保守沉默（无输出率 85.94%），MiniCPM-o 回答更积极（PAQ 0.571）但溢出严重（条件溢出率 83.15%，平均时长 10.07s）。
- 嵌套交互：MiniCPM-o 和 AURA 能部分完成内外回答链（NCCS 分别为 0.284/0.270），而 Gemini 和 Qwen3.5-Omni 在 119/120 对外层问题彻底遗忘。
- 全双工能力退化：MiniCPM-o 在线流式数学推理质量较离线版本降低 0.3358，证明持续监听与并发生成严重损害推理性能。

> 最值得记住的一句话：强离线多模态理解不等于鲁棒实时交互——全双工场景下的响应时机控制、中断处理与上下文恢复是当前模型的主要短板。
