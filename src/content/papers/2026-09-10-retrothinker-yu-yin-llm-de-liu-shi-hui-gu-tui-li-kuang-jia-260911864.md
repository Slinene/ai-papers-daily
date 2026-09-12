---
title: 'RetroThinker: Enabling Retrospective Thinking in Speech LLMs'
title_zh: RetroThinker：语音 LLM 的流式回顾推理框架
authors:
- Yi-Jen Shih
- Puyuan Peng
- Abdelrahman Mohamed
- David Harwath
affiliations:
- The University of Texas at Austin
- FAIR, Meta Superintelligence Labs
arxiv_id: '2609.11864'
url: https://arxiv.org/abs/2609.11864
pdf_url: https://arxiv.org/pdf/2609.11864
published: '2026-09-10'
collected: '2026-09-12'
category: Reasoning
direction: 流式语音 LLM 自我修订推理优化
tags:
- SpeechLLM
- CoT
- DPO
- self-correction
- streaming reasoning
one_liner: 通过 SFT+length-based DPO 让流式 SpeechLLM 自我修正 CoT，GSM8K 相近延迟下绝对准确率 +11%
practical_value: '- 多阶段后训练组合可迁移：先 SFT 构造带显式“回顾/修订”痕迹的推理数据，再用 length-based DPO 优化早期推理修订，可用于训练对话式推荐
  Agent 的推理链，让模型在用户输入过程中边听边想、自我纠错，降低最终响应延迟。

  - 长度感知的 DPO 可控制推理 token 长度，避免 CoT 过长导致线上推荐/搜索 Agent 的 TTFT 恶化；在搜索推荐场景可把“延迟-准确率”作为显式偏好信号加入偏好优化。

  - 流式自我验证与前向修正思路可迁移到实时多轮 Agent：当用户 query 尚未说完时启动候选解释/推荐理由生成，并在后续 token 流中动态修正，而非等完整输入后再推理，适合语音购物、实时广告文案生成等场景。

  - 需要注意本工作基于语音 token 模型，与电商文本 Agent 不完全同构；可直接借鉴的是训练框架和偏好设计，而非模型架构。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：SpeechLLM 直接消费语音 token，可降低级联 ASR-LLM-TTS 延迟并保留韵律等副语言信息，但在复杂推理上落后文本 LLM；实时口语交互带来严格延迟限制，现有 CoT / concurrent reasoning 仍面临准确率-延迟权衡。

**方法关键点**：RetroThinker 以 Moshi 流式 SpeechLLM 为基础，采用多阶段后训练：先用带“回顾式思考”痕迹的数据进行 SFT，使模型学会在推理中自我验证与前向修正 CoT 步骤；再用 length-based DPO 优化早期推理（用户说话时并发推理）的回顾行为，鼓励在不大幅增加 token 长度的情况下进行必要修订。

**关键结果**：在 GSM8K 上，相比非回顾式基线，RetroThinker 在相近延迟下实现 11% 绝对准确率提升，说明流式自我修正能改善推理准确率同时控制延迟。
