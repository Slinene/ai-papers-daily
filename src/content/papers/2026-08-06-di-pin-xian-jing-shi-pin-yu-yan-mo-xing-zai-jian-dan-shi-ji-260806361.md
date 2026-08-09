---
title: 'The Low Frequency Trap: Video Language Models Fail at Simple Event Bookkeeping'
title_zh: 低频陷阱：视频语言模型在简单事件计数上失败
authors:
- Sarvesh Baskar
- Zikui Cai
- Shayan Shabihi
- Anirudh Satheesh
- Muhammad R. Islam
- Udari Madhushani Sehwag
- Tom Goldstein
- Furong Huang
affiliations:
- University of Maryland, College Park
- Scale AI
arxiv_id: '2608.06361'
url: https://arxiv.org/abs/2608.06361
pdf_url: https://arxiv.org/pdf/2608.06361
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: 视频语言模型时序推理评估
tags:
- Video-Language Models
- Event Counting
- Temporal Reasoning
- Evaluation
- Diagnostic Benchmark
one_liner: 视频语言模型在事件计数上呈现阶段性失效，瞬态事件几乎无法可靠计数，高频高计数下准确率仅0.2%。
practical_value: '- 在电商视频推荐、直播回放分析中，若需计数关键事件（如商品展示次数、动作步骤），须意识到 VLMs 对瞬时事件极不可靠，应避免依赖此类计数。

  - 可借鉴「参数化合成视频 + 事件跟踪」的评估范式，在内部自建可控诊断基准，快速定位模型在时间维度上的能力边界。

  - 对于视频广告曝光频次校验等任务，单纯增加帧率并不能保证模型忠实地恢复事件序列，需结合事件级真值审计，防止指标虚高。

  - 若在推荐 Agent 中使用 VLMs 理解用户行为视频，应优先选择对持久状态变化敏感的模型架构，并避免在高频动作场景下直接使用计数类信号。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

## 动机
现有视频基准将事件计数、速率、持续时间、视觉复杂度纠缠在一起，难以隔离模型的真正失败模式。已有程序化基准仅评估最终答案，未审计模型所报告的事件序列是否与真实事件链匹配。

## 方法
提出基于事件跟踪的参数化剖析方法，设计三类受控视频任务：弹跳球碰壁（持续接触）、视觉闪烁（瞬态）、类别状态转换（持久状态）。在 2190 个视频中，独立改变事件计数 N 和频率 F 并固定渲染。每个视频都包含可执行的事件跟踪真值，支持能力曲面估计和逐时间戳评估。以 Gemini 3.6 Flash 为主要测试模型。

## 关键结果
- 以 80% 可靠性阈值衡量，Gemini 对持久状态转换可在 0.5 Hz、1.0 Hz 下可靠计数最多 12 次事件，但对瞬态闪烁事件完全没有可靠计数区域，说明事件表征类型（持久 vs 瞬态）决定了模型能否访问证据。
- 在高计数、高频率区间，仅 0.2% 的最终计数完全正确，模型仅恢复 18.1% 的真值事件。
- 提升采样帧率虽将弹跳球准确率从 19.6% 提升至 29.3%，但报告序列与真值一致的比例仅 3.7%，帧数增加会抬高分数而不提供忠实事件恢复。
- 不同提示策略收益有限，真实世界视频评估同样显示成功集中在低事件计数场景。
- 该方法将视频评估从聚合准确率转向详细的时序推理失败诊断。
