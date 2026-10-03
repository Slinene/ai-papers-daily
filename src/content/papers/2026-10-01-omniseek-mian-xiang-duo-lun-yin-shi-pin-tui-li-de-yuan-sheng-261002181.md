---
title: 'OmniSeek: Native Tool Integration for Multi-turn Audio-Visual Reasoning'
title_zh: OmniSeek：面向多轮音视频推理的原生工具集成
authors:
- Haibo Wang
- Jiteng Mu
- Jialu Li
- Jingru Yi
- Yuanjun Xiong
- Jianming Zhang
- Lifu Huang
- Mingze Xu
affiliations:
- University of California, Davis
- Adobe Research
arxiv_id: '2610.02181'
url: https://arxiv.org/abs/2610.02181
pdf_url: https://arxiv.org/pdf/2610.02181
published: '2026-10-01'
collected: '2026-10-03'
category: Agent
direction: Agent 多轮音视频推理与工具检索
tags:
- Omni-LLM
- Agentic Reasoning
- Multi-turn Tool Use
- Audio-Visual
- Reinforcement Learning
- Chain-of-Thought
one_liner: 将 Omni-LLM 变为主动多轮推理 Agent，动态检索关键音视频片段以支撑跨模态长上下文推理
practical_value: '- 多模态长视频/直播/商品讲解等场景，别让模型一次吞下整个序列；可以借鉴 OmniSeek 的做法，让 Agent 先粗略定位，再调用工具按时间窗口取回关键音频或视觉片段追加到上下文，既省计算又能保持细节证据。

  - 数据冷启动可复用“合成多跳 CoT 轨迹 + SFT + 两阶段 RL”路线：先造带交错的证据检索轨迹让模型学会多轮工具调用，再用可验证奖励做策略优化，适合业务中缺乏真实交互标注的场景。

  - Audio-Visual Necessity 奖励是防止多模态捷径的有效 trick：在训练目标里显式惩罚只依赖单一模态的成功轨迹，可迁移到电商多模态模型，避免模型只抄文本或只靠图片就能答题。

  - 工具返回原始音视频片段而不是高层特征，能保留稀疏关键证据，类似多模态 RAG；在直播切片问答、广告素材审核、智能客服等场景可以直接套用这种“检索-追加-再推理”的循环。'
score: 7
source: arxiv-cs.CV
depth: abstract
---

动机：现有 Omni-LLM 通常单遍被动编码整个音视频流，长上下文中细粒度视觉细节和短暂声音事件容易被无关内容稀释，模型难以定位并组合跨模态证据。

方法关键点：OmniSeek 把证据获取放进推理过程，让模型动态决定“看还是听”、选哪个时间窗口，拿到稀疏但关键的跨模态证据；通过多轮协议把检索到的原始音频或视觉片段追加回上下文，再继续推理。冷启动阶段，用数据引擎合成 OmniTraj-170K，包含多跳 CoT 轨迹和交错音频/视觉证据，先 SFT 教会多轮工具使用行为，再做两阶段 RL 用可验证奖励优化策略。额外引入 Audio-Visual Necessity 目标，显式奖励成功且同时依赖两种模态的轨迹，抑制单模态捷径。

关键结果：在多个基准上，OmniSeek 学会自适应跨模态证据寻求，一致提升音视频推理性能。
