---
title: 'AURA 2.0: From User-Driven Responses to Model-Initiated Conversations in Streaming
  Video'
title_zh: AURA 2.0：从用户驱动响应到流媒体视频中的模型主动对话
authors:
- Shuhan Li
- Huankang Guan
- Xintong Guo
- Yang Bo
- Yuyang He
- Dunyuan Xu
- Jingyan Chen
- Fang Liu
- Tsz Kin Wan
- Jinpeng Chen
affiliations:
- Huawei Research
- CUHK MMLab
- HKUST
arxiv_id: '2611.17048'
url: https://arxiv.org/abs/2611.17048
pdf_url: https://arxiv.org/pdf/2611.17048
published: '2026-11-12'
collected: '2026-11-15'
category: Multimodal
direction: 流式视频LLM · 模型主动对话与工具调用
tags:
- Streaming Video
- LLM
- Model-Initiated Conversation
- Tool Calling
- Visual Grounding
- Open-source
one_liner: 在流媒体视频LLM中引入模型主动对话、流感知工具调用和交互式视觉定位，实现领先开源性能
practical_value: '- **MIC 借鉴**：在直播电商或短视频推荐中，模型可基于当前视频内容主动发起交互（如提醒优惠、推荐商品），而非仅响应用户
  query，可能提升用户参与和转化。

  - **SATC 流式工具调用**：实时推荐或客服 Agent 可根据视觉和对话上下文实时调用商品库、价格、库存等外部工具，并将结果融入对话，增强推荐准确性和响应及时性。

  - **LHIM 长时记忆**：维护长会话上下文，对电商客服或个性化推荐 Agent 保留用户历史交互和偏好，避免信息丢失，提升个性化体验。

  - **IVG 视觉定位**：在视频广告或商品展示中，模型可定位用户标记物体或输出边界框，实现图文对齐，可用于商品识别、比价、虚拟试穿等交互功能。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**  
现有 AI 助手仅在用户提示时响应，忽视视频流中的主动对话机会，无法充分利用实时视觉信息。AURA 2.0 旨在从被动响应转向模型主动发起对话，增强流媒体视频交互。

**方法关键点**  
- **Model-Initiated Conversation (MIC)**：模型识别视觉流中值得讨论的话题，在合适时机主动发起对话，无需用户 query。  
- **Stream-Aware Tool Calling (SATC)**：利用当前视觉和对话上下文调用外部工具，并将返回信息融入交互。  
- **Interactive Visual Grounding (IVG)**：支持用户输入和模型输出中的视觉定位，可识别用户标记的对象并生成帧对齐的边界框。  
- 构建专用流式交互数据集，采用三阶段训练整合新能力；引入 **Long-Horizon Interaction Memory (LHIM)** 保持长视频流中的上下文连续性。

**关键结果**  
在公开流式基准上，AURA 2.0 在开源流式模型中取得领先性能；针对性评估验证了 MIC、SATC、IVG 三项新交互能力。模型权重和推理代码已开源。
