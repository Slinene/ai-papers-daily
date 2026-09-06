---
title: 'Temporal Self-Distillation: Learning Visual State Tracking in Videos Without
  Supervision'
title_zh: 时序自蒸馏：无监督学习视频视觉状态跟踪
authors:
- Shravan Venkatraman
- Wenshuai Zhao
- Mohammad Hassan Vali
- Arno Solin
affiliations:
- Mohamed bin Zayed University of Artificial Intelligence
- ELLIS Institute Finland
- Aalto University
arxiv_id: '2609.04203'
url: https://arxiv.org/abs/2609.04203
pdf_url: https://arxiv.org/pdf/2609.04203
published: '2026-09-03'
collected: '2026-09-06'
category: Training
direction: 自监督时序自蒸馏训练视频状态跟踪
tags:
- Temporal Self-Distillation
- Self-Supervised Learning
- Video Understanding
- State Tracking
- VLM
one_liner: 用时间采样密度作为自监督信号，让稀疏帧学生匹配稠密帧教师的 next-token 分布，无需标签或额外教师即可提升视频状态跟踪
practical_value: '- 视频/直播电商场景：对商品展示、使用过程、库存/数量变化等短视频，用稠密帧采样的同模型输出蒸馏稀疏帧模型，可在不增加线上推理成本的前提下提升状态/数量判断；souping/轻量视觉编码器适配可作为后续增强手段。

  - 无标签数据利用：可以低成本生成合成 clip（物体颜色、数量、位置变化），用 S3T 式的自监督时序蒸馏预训练视频理解模块，再迁移到真实 UGC/广告素材的内容审核或卖点提取。

  - Agent/多模态 LLM 训练：如果业务中有连续视频流（如智能客服/导购 Agent 看商品视频），将时间采样密度作为特权信息，让同一模型在自己的稠密/稀疏视图间做
  next-token 分布蒸馏，不需要额外 judge，能提升跨时间状态跟踪，且不增加部署成本。

  - 如果要改进现有 VLM 在电商视频问答上的表现，可优先考虑对视觉编码器做小规模适配+权重 soup，而非重新训练；论文显示这些组合能稳定提升状态跟踪。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：视频理解中的连续状态跟踪（物体数量/颜色/位置变化）难以仅靠现有自进化/自蒸馏方法提升，因为它们依赖标签或外部 judge、只优化一致性不验证正确性、或只学空间特征，无法维护 running state。

**方法**：S3T 把时间采样密度当作特权信息：同一视频 clip 的稠密采样视图作为 teacher，稀疏视图作为 student，二者共享参数；student 学习匹配 teacher 的 next-token 分布，无需手工标签、独立 teacher 或 reward，也不增加推理成本。模型生成自己的目标，训练完全自包含。

**结果**：在 LLaVA-OneVision-2-8B 上，VSTAT 准确率单模型 +1.74，souping +2.38，额外视觉编码器适配 +2.70；无标签合成 clip 学到能力迁移到真实视频，VSTAT-YouTube 状态跟踪问题 +7.95，MVBench Action Count +4.50；先验自进化方法基本无变化。
