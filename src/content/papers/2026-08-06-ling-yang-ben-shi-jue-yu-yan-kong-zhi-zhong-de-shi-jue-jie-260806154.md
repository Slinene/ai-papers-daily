---
title: Visual Grounding in Zero-Shot Vision-Language Control
title_zh: 零样本视觉-语言控制中的视觉接地评估与守护
authors:
- J. de Curtò
- Dayani Plasencia
- Diego Sánchez
- I. de Zarzà
affiliations:
- BARCELONA Supercomputing Center
- Universidad Pontificia Comillas
- University of Florida
- University of Illinois Urbana-Champaign
- LUXEMBOURG Institute of Science and Technology
arxiv_id: '2608.06154'
url: https://arxiv.org/abs/2608.06154
pdf_url: https://arxiv.org/pdf/2608.06154
published: '2026-08-06'
collected: '2026-08-09'
category: Eval
direction: VLM视觉接地评估与选择性辅助守护
tags:
- Visual Grounding
- Vision-Language Model
- Zero-Shot Control
- Symmetry Consensus
- Ablation Study
- Autonomous Driving
one_liner: 输入消融实验揭示VLM零样本控制普遍缺乏视觉接地，对称共识守护者实现可靠危险检测。
practical_value: '- **对称一致性守卫**：利用原始与反射视图的预测一致性筛选可靠模型，此法可迁移至多模态推荐——对商品图片做水平翻转等增广，检查模型预测是否对称，剔除不一致的弱模型，提升鲁棒性。

  - **输入消融诊断**：盲图、重复帧、反射对照组能暴露模型是否真正利用视觉信息。可仿照设计线上诊断流程，排查推荐模型中的模态依赖假象。

  - **选择性弃权策略**：在低置信度时弃权，牺牲少量覆盖换取大幅精度提升，适合电商风控或内容审核等高风险场景，结合阈值动态开关辅助决策。'
score: 6
source: arxiv-cs.CV
depth: abstract
---

**动机**：VLM 被直接用作零样本自动驾驶控制器，但轨迹成功可能来自仿真动力学与保守先验，而非真正视觉理解，需要系统评估其视觉接地能力。

**方法**：设计输入消融电池——盲图、重复相同输入、车道轴反射、非视觉基线等，在 9 个直接动作模型、6 个结构化局部 VLM 及一个 VLM-MPC 层次上测试，分析 32,874 次调用。重点检验纵向（危险感知）与横向（左右转）的镜像等变一致性。随后提出泄漏受控的对称共识守护者：用少量校准帧选出对原始和反射视图预测一致的模型组合（Gemma4-12B + Qwen3.5-9B），冻结 2-of-4 危险投票，在保留帧上评估。

**关键结果**：多数模型图像不变或近乎常数，常数 SLOW 策略甚至优于脚本控制器；能识别纵向危险的模型仍无法在反射下正确变换 LEFT/RIGHT。无一局部 VLM 满足联合接地标准。但作为对照，图像确定性检测器可精确估计领先间隙（MAE 0.090m）且完美镜像等变，说明视觉信息充足，故障是模块化的。守护者达到 0.954 平衡准确率（95% CI [0.895,0.990]），弃权时承诺准确率 0.973（覆盖 82.4%）。离线模块重放实现 0.934 动作一致与确切镜像等变。结论：当前 VLM 应作为有限、选择性的危险辅助，而非整体零样本控制器。
