---
title: Text-Guided Visual Representation Learning for Robust Multimodal E-Commerce
  Recommendation
title_zh: 文本引导的视觉表征学习：电商多模态推荐中稳健应对促销遮挡
authors:
- Yufei Guo
- Jing Ma
- Tianlu Zhang
- Shijie Yang
- Yanlong Zang
- Weijie Ding
- Pinghua Gong
- Jungong Han
affiliations:
- Tsinghua University
- JD.COM
arxiv_id: '2605.17366'
url: https://arxiv.org/abs/2605.17366
pdf_url: https://arxiv.org/pdf/2605.17366
published: '2026-05-17'
collected: '2026-05-19'
category: RecSys
direction: 生成式推荐 · 多模态表征 · 双流视觉连接器
tags:
- Multimodal
- I2I Retrieval
- MLRM
- Q-Former
- Gating
- Robustness
one_liner: 用结构化元数据引导视觉 token 提取，双流解耦并门控校准，显著提升海报式商品图的检索鲁棒性。
practical_value: '- **双流视觉解耦 + 可靠性门控**：将视觉证据分为元数据锚定流和探索流，并通过 cSigmoid 门控进行通道级校准，可迁移到任何多模态商品
  embedding 的视觉侧，解决营销图像干扰问题。

  - **用标题信号衡量图文一致性**：利用 CLIP 全局嵌入计算 image–title 余弦相似度作为门控输入，无需额外标注，可直接用于电商场景的视觉质量判定和自适应融合。

  - **冗余缩减正则鼓励互补性**：对双流输出做跨流同维去相关，避免两路学到冗余信号，增强联合表征的信息量，适合在对比学习框架下提升检索泛化。

  - **MLRM 范式优于端到端 MLLM**：同等视觉编码器下，轻量连接器 + 检索优化 LLM backbone 的推理 FLOPs 仅需 35G，比 2-4B
  MLLM 低 8-20 倍，而 Hit Rate 高出 3-5 个绝对点，为工业 I2I 召回提供高性价比方案。'
score: 10
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
电商商品图常包含促销贴片、装饰背景等噪声，传统 MLRM 连接器（如 Q-Former）会将视觉注意力偏向这些无产品关联的显著区域，损害 item-to-item (I2I) 检索的细粒度区分能力。简单的中心裁剪等预处理仅能缓解边界噪声，无法区分有害遮挡和有用上下文。需一种选择性利用视觉证据的方法，既抑制贴片干扰，又保留文本未覆盖的互补视觉线索。

## 方法关键点
- **Hybrid-Query Connector (HQC)**：将查询拆分为两部分——由商品元数据（标题/品牌/类目）压缩初始化的“元数据锚定语义查询”和随机初始化的“探索式学习查询”，分别提取元数据一致区域和互补视觉细节。
- **Dual-Gated Vector Modulation**：用 centered-sigmoid 生成逐通道门控向量，对两流嵌入进行残差缩放。元数据流的门控输入包括 image–title 相似度得分、全局图像特征及两流摘要；探索流的门控仅依赖图像和流内信息。实现根据噪声水平自适应调节。
- **Redundancy-Reduction Regularizer**：对双流池化后的向量计算跨流同维相关性矩阵，惩罚对角线元素，迫使两流编码互补而非冗余信息。
- **训练方式**：冻结视觉编码器（中文 CLIP-ViT-B/16），LoRA 微调 LLM，联合 InfoNCE 对比损失与冗余缩减正则训练。

## 关键结果
在电商平台真实全量商品池（约 13.4 万候选）上，TGQ-Former 使用 Qwen3-Embedding-0.6B 骨干时 H@100 达 69.13%，比最强连接器基线 NoteLLM-2 提升 6.04%，比 Perceiver-Resampler 提升 8.07%。与 2-4B 级 MLLM 对比，H@100 高出 3.45 个绝对点，且推理 FLOPs 仅 35.43G，远低于 InternVL3-2B 的 724G 和 Qwen3-VL-4B 的 592G。消融实验证实双流查询、门控调制和冗余正则均带来正向增益。

> 一句话记住：用元数据当“语义锚”引导 Q-Former 注意力，再靠双流门控和互补正则让视觉表征在促销噪声中依然稳健。
