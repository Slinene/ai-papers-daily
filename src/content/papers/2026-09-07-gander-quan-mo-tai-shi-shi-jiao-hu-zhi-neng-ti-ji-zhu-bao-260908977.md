---
title: Omni Interaction Agent Technical Report
title_zh: Gander：全模态实时交互智能体技术报告
authors:
- Orantqing
- Shengpeng Ji
- Junlong Tong
- Jialong Zuo
- Dongjie Fu
- Di Cao
- Yangzhuo Li
- Shangda Wu
- Franz
- Evan
affiliations:
- Hunyuan Speech Team, Tencent
- Zhejiang University
- Shanghai Jiao Tong University
- The Chinese University of Hong Kong
- Nanyang Technological University
arxiv_id: '2609.08977'
url: https://arxiv.org/abs/2609.08977
pdf_url: https://arxiv.org/pdf/2609.08977
published: '2026-09-07'
collected: '2026-09-10'
category: Agent
direction: 全模态实时交互Agent
tags:
- Omni Interaction
- Full-duplex
- Streaming
- Multi-modal
- Agent
- Thinker-Talker
one_liner: 提出Gander，融合多模态感知、全双工流式交互与Agent能力的端到端模型，通过小脑-大脑协同与Thinker-Talker架构实现低延迟实时交互
practical_value: '- 将实时交互与复杂任务推理拆分为两级：轻量流式“小脑”负责即时响应、追问与澄清，重模型“大脑”负责意图解析、工具调用与规划，电商导购/客服Agent可据此降低首响延迟并节省推理成本。

  - 全双工可中断机制适合语音购物、直播互动等场景：用户可随时打断，模型可主动给出中间反馈或反问，建议在会话式推荐中引入此类异步主动交互，避免死等完整query。

  - 采用chunk级统一token流表示多模态输入输出，可借鉴到流式ASR+LLM+TTS的搜索/推荐语音链路，减少模块间等待与传输开销，提高整体低延迟体验。

  - 评估需覆盖背景噪声、多人交互与backchannel等真实环境压力测试，语音搜索/推荐Agent上线前应补充类似鲁棒性评测，而非仅看离线对话质量。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：传统turn-based对话范式无法满足视频、语音、文本多模态流式输入下的实时全双工交互需求，用户在复杂工作流Agent场景中需要随时打断、获得中间反馈或主动追问。

**方法关键点**：
- Gander采用Cerebellum-Brain协同框架：Cerebellum负责实时交互与全模态对话，Brain处理复杂推理与高层Agent任务，两者通过工具调用和Agent编排运行时持续通信。
- Cerebellum内部基于流式Thinker-Talker架构，将用户输入与模型输出在chunk级别扁平化为有序token流，统一表示以支持低延迟连续交互。
- 模型支持视频、语音、文本三类模态的流式输入，实现自然全双工交互，既能被动响应也能主动提供反馈或提问。

**关键结果**：
- 在会话能力、全模态理解、交互能力、Agent智能四个维度上进行内部人类评估，Gander保持了SOTA开源模型的自然表达口语对话能力，并在全模态交互上达到有竞争力的表现。
- 在背景噪声干扰、多人交互、backchannel等真实场景中表现出鲁棒性。
- 开放模型、代码与数据，便于社区复现与研究。
