---
title: 'RefCaptioner: Multi-Reference Image-Grounded Video Captioning'
title_zh: RefCaptioner：多参考图像指导的视频描述后训练框架
authors:
- Tengfei Liu
- Yang Shi
- Yuran Wang
- Xiaohan Zhang
- Yuqing Wen
- Yuqi Tang
- Qixun Wang
- Zhuoran Zhang
- Xuanyu Zhu
- Weihong Lin
affiliations:
- Peking University
- Kling Team
- National University of Singapore
- Shanghai AI Lab
- CASIA
arxiv_id: '2607.28509'
url: https://arxiv.org/abs/2607.28509
pdf_url: https://arxiv.org/pdf/2607.28509
published: '2026-07-29'
collected: '2026-08-01'
category: Multimodal
direction: 多参考图像约束的视频描述后训练
tags:
- Video Captioning
- Image Grounding
- GRPO
- Post-training
- Multi-Reference
- Hierarchical Coverage
one_liner: 提出多参考图像指导的视频描述任务，用分层覆盖折扣GRPO实现短语级绑定与干扰拒绝
practical_value: '- 多参考图像指导的描述生成可直接迁移到电商商品视频描述：输入多张商品图，生成确保细节对齐（颜色、款式）的文案；可通过类似的分层覆盖奖励避免遗漏关键属性。

  - 混合数据SFT保持通用能力的策略适用于垂直领域的LLM微调，防止灾难性遗忘；在训练电商领域的生成式推荐模型（如商品描述生成）时，可混合通用数据与领域数据。

  - 分层覆盖折扣GRPO的强化学习思路可用于优化生成式推荐中的多实体绑定与一致性，例如在生成广告文案时强制提及多个卖点图像，并通过奖励塑造提升描述的事实准确性。

  - MRVBench构建的评估方法（多参考绑定、干扰项拒绝）可借鉴到多模态推荐系统的离线评估中，用于检测生成的推荐理由是否忠实于输入的多张商品图。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有视频描述模型无法将描述短语与多张参考图像显式绑定，导致细节错配或遗漏。为此，论文定义了多参考图像指导的视频描述新任务，要求生成的事实描述必须通过短语级引用与对应图像关联。

**方法**：提出RefCaptioner两阶段后训练框架。第一阶段为混合数据SFT，保持通用视频描述能力；第二阶段采用**分层覆盖折扣的GRPO（Group Relative Policy Optimization）** 强化学习，联合优化四项能力：参考图像选择、短语级绑定、干扰图像拒绝、跨参考一致性。覆盖折扣项鼓励描述覆盖所有参考图像特征。训练数据包含20,000个视频和171,354张参考图像。同时构建了**MRVBench**基准，评估事实性和多参考绑定能力。

**结果**：在开放源模型中取得最优综合性能，同时在标准视频描述基准上保持竞争力。人类评估显示，RefCaptioner的描述更受标注者偏好，且能帮助开源和闭源视频生成模型更忠实地重建源视频，表明描述的事实准确性更高。
