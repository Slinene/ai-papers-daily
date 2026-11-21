---
title: Learning to Think with Images Faithfully via Adaptive Data Selection
title_zh: 通过自适应数据选择学习忠实思考图像
authors:
- Yu Zhao
- Jiaxin Zhang
- Rohit Saxena
- Fazl Barez
- Pasquale Minervini
- Yiwen Guo
affiliations:
- University of Edinburgh
- LIGHTSPEED
- University of Oxford
- Independent Researcher
- Miniml.AI
arxiv_id: '2611.26199'
url: https://arxiv.org/abs/2611.26199
pdf_url: https://arxiv.org/pdf/2611.26199
published: '2026-11-19'
collected: '2026-11-21'
category: Multimodal
direction: VLM 视觉工具使用保真训练
tags:
- VLM
- Tool Use
- Faithfulness
- Data Selection
- Visual Reasoning
- Multimodal
one_liner: 提出自适应数据选择与 adaptiveness reward，让 VLM 更忠实地使用缩放工具，视觉搜索基准 SOTA
practical_value: '- 自适应训练样本筛选：在多模态商品理解或视觉搜索中，当模型已能用低分辨率图像答对时，继续提供缩放工具只会让它学会忽略工具；应动态剔除“无工具也能答对”的样本，保留需要工具证据的困难样本，避免捷径学习。

  - 工具调用忠实性奖励设计：在 Agent 推荐对话里，如果模型调用商品属性 API 后未使用返回信息，可在奖励中加入 faithfulness 项，鼓励“用了工具就真用信息，不用就直答”，提升推理可解释性和成本控制。

  - 细粒度视觉数据合成管线：可复用“小目标定位 + 可验证细节问题生成”流程，为电商商品图（标签、纹理、瑕疵）自动生成 QA 对，用于训练或评测多模态检索 /
  审核模型。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**
- 视觉语言模型（VLM）在识别小目标、密集文本等细节上有感知瓶颈；Thinking with Images (TwI) 通过主动裁剪/缩放来增强细粒度视觉推理，但分析发现 TwI 模型经常调用工具却不真正依赖缩放区域，导致工具使用不忠实。
- 根因在训练数据：很多问题无需缩放即可回答，模型可忽略返回证据仍答对；随着训练，模型更擅长不用工具，不忠实行为加剧。

**方法关键点**
- 提出自适应数据选择策略：根据模型不断变化的回答能力筛选训练样本，保留那些“正确缩放证据仍能帮助模型答对”的问题，从而保持缩放工具的效用。
- 构建数据合成管线：定位小物体并围绕其细粒度细节生成可验证问题。
- 引入 adaptiveness reward：当缩放不必要时鼓励工具无关的直接回答，引导模型灵活判断。

**关键结果数字**
- 视觉搜索基准：V* 提升 +11.6%，HR-Bench 4K 提升 +7.9%，HR-Bench 8K 提升 +9.4%，达到 SOTA。
- 多模态幻觉基准上优于 TwI 基线。
- 结论：提高 TwI faithfulness 不牺牲 accuracy，且无需直接监督推理过程。
