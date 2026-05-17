---
title: Compositional Video Generation via Inference-Time Guidance
title_zh: 利用推理时引导实现组合式视频生成
authors:
- Ariel Shaulov
- Eitan Shaar
- Amit Edenzon
- Gal Chechik
- Lior Wolf
affiliations:
- Tel-Aviv University
- Independent Researcher
- Bar Ilan University
- NVIDIA Research
arxiv_id: '2605.14988'
url: https://arxiv.org/abs/2605.14988
pdf_url: https://arxiv.org/pdf/2605.14988
published: '2026-05-14'
collected: '2026-05-17'
category: Multimodal
direction: 组合视频生成 · 推理时引导
tags:
- Compositional Generation
- Inference-Time Guidance
- Cross-Attention
- Diffusion Models
- Classifier Guidance
- Frozen Model
one_liner: 基于交叉注意力图训练轻量组合分类器，在推理时引导冻结T2V模型提升组合正确性，无需微调
practical_value: '- **推理时引导范式可迁移**：在电商图文生成或Agent多模态响应中，若需精确控制实体间关系/属性组合，可利用预训练模型内部的交叉注意力图训练轻量组合分类器，在解码早期步骤注入梯度引导，避免重训基座模型。

  - **冻结大模型+外部引导头**：不微调生成模型本身，仅外挂一个基于冻结VLM backbone的分类器，保持基座模型的泛化能力，适合快速适配新的组合约束（如商品多属性描述、活动文案组合语）。

  - **无布局/框的弱监督组合控制**：无需用户提供空间布局或检测框，仅靠文本提示即可隐式约束组合关系，对电商场景中大批量自动化内容生成（如商品详情视频）有工程简洁性优势。

  - **注意力特征重用**：利用扩散模型已有的交叉注意力图作为组合性特征，训练开销小，可直接嵌入现有生成pipeline，适合资源受限的业务环境进行组合性提升。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：当前的文本到视频（T2V）扩散模型虽然能生成逼真视频，但在细粒度组合理解上表现不佳，例如无法正确呈现“狗向左转”或“猫远离汽车”这类包含实体关系、属性和动作的提示。通常需微调生成器或提供额外控制信号来解决，成本高且不灵活。

**方法**：提出CVG（Compositional Video Generation via Inference-Time Guidance），一种在冻结T2V模型上进行推理时引导的方法。关键观察是：扩散模型中的交叉注意力图已经隐含了提示概念在时空上的定位信息。作者训练一个轻量级组合分类器，以这些注意力图为输入，预测视频是否符合给定的组合标签（如空间关系、动作方向等）。该分类器基于冻结的VLM backbone，能跨语义相关标签迁移，而非仅依赖窄域类别特征。在去噪早期步骤，利用分类器对潜在表示的梯度引导生成过程，使生成视频朝着满足组合约束的方向优化。整个过程无需修改模型架构、微调生成器或要求用户提供布局框等额外输入。

**结果**：在组合式T2V基准上，CVG显著提升了生成视频对提示的忠实度，同时保持了原模型的视觉质量。实验在Wan2.2-14B和CogVideoX-5B等大模型上验证了方法的有效性，且无需重新训练生成器即可改善组合性失败案例。
