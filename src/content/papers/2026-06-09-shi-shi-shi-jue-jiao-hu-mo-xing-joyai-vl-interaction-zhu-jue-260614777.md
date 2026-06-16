---
title: 'JoyAI-VL-Interaction: Real-Time Vision-Language Interaction Intelligence'
title_zh: 实时视觉交互模型 JoyAI-VL-Interaction：主动决定何时开口的 8B 级视觉模型
authors:
- Dingyu Yao
- Junhao Zhou
- Chenxu Yang
- Chuanyu Qin
- Haowen Hou
- Zheming Liang
- Congcong Wang
- Yuhang Cao
- Shenglong Ye
- Shuai Xie
affiliations:
- JD.com
arxiv_id: '2606.14777'
url: https://arxiv.org/abs/2606.14777
pdf_url: https://arxiv.org/pdf/2606.14777
published: '2026-06-09'
collected: '2026-06-16'
category: Other
direction: 实时视觉交互模型与系统
tags:
- Real-Time Interaction
- Vision-Language Model
- Event-Driven
- Streaming Video
- Delegate
- AdaCodec
one_liner: 首个开源、视觉驱动的 8B 交互模型，每秒自主决策沉默/响应/委派，并配有完整部署系统。
practical_value: '- 直播电商 / 短视频场景可直接借鉴其“每秒决策”范式：模型持续观看直播画面，自主判断何时插话（如提醒主播漏讲卖点、解答观众疑问），而非被动等待提问。

  - 委派（delegate）机制适合复杂任务卸载：当需要生成商品详情页 HTML 或调用知识库时，模型可暂停实时应答，将任务异步交给后端大模型或 Agent，保持对用户的实时存在感。

  - AdaCodec 视频压缩策略（对可预测帧仅用约 16 个 token）大幅降低长流推理成本，适合需要连续观看监控或直播的电商 AI 助手，降低部署门槛。

  - 分层记忆设计（短期缓冲 + 中期文本摘要 + 长期归档）与 vLLM 前缀缓存结合，实现两小时以上连续视频的亚秒级延迟，可用于需要长上下文记忆的在线导购或客服会话。'
score: 10
source: huggingface-daily
depth: full_pdf
---

**动机**：现有大模型多为 turn-based，只在被提问时回答，无法主动捕捉转瞬即逝的视觉事件（如直播中闪过的商品、监控中的异常）。已有产品虽加入轮询触发，但仍非模型内生决策。本文提出“交互模型”范式——模型持续观看视频流，自主决定何时发言、沉默或将难题委派给后台模型，实现“watch-and-do”式实时协作。

**方法关键点**
- **模型架构**：基于 JoyAI-VL-1.0（Qwen3-8B + Qwen3-VL ViT），用 AdaCodec 编码视频流，对可预测帧仅传输运动向量与残差，大幅压缩 token 数。
- **行为决策**：每秒输出三种动作之一：`</silence>`（沉默）、`</response>`（发言）或`delegate`（委派后台）。委派有一套固定协议，后台模型可替换为任意 API/Agent。
- **数据构建**：构建超 400 万条时间对齐流式数据，覆盖主动告警、时间感知问答、实时计数、直播解说、多轮聊天、委派等 6 大类。通过多层级验证代理确保内容与时机正确，并将沉默视为一等标签。
- **训练**：在常规 SFT 基础上使用加权交叉熵（重复沉默 token 权重降至 0.4，响应 token 权重升为 1.5），仅对时序数据使用；随后用 GRPO 进行强化学习，优化秒级决策，奖励正确响应窗口和恰当沉默，惩罚误报。
- **系统设计**：提供完整开源部署栈，包含可插拔 ASR/TTS、可视化 UI、三级分层记忆（短期视觉 token → 中期文本摘要 → 长期归档），基于 vLLM 前缀缓存实现超两小时连续视频亚秒延迟。

**关键结果**：在 6 个真实流式场景（监控告警、实时计数、实时翻译、时间感知、直播解说、长时记忆）共 58 个案例的人工对比中，**JoyAI-VL-Interaction 以 77.6% 胜率击败 Doubao，87.9% 胜率击败 Gemini**。在监控告警场景，对两者均 100% 获胜；实时翻译与计数对 Gemini 全胜。优势集中在事件驱动、时间敏感任务，而基线在时机上表现薄弱。
