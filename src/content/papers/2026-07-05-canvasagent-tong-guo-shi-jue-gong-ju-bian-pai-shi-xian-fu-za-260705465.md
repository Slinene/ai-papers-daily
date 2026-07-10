---
title: 'CanvasAgent: Enabling Complex Image Creation and Editing via Visual Tool Orchestration'
title_zh: CanvasAgent：通过视觉工具编排实现复杂图像创建与编辑
authors:
- Hairui Zhu
- Yiying Yang
- Tengjin Weng
- Ziyu Lu
- Xiao Yao
- Xiaoyang Ye
- Lin Ma
- Wenhao Jiang
affiliations:
- Guangdong Laboratory of Artificial Intelligence and Digital Economy (SZ)
arxiv_id: '2607.05465'
url: https://arxiv.org/abs/2607.05465
pdf_url: https://arxiv.org/pdf/2607.05465
published: '2026-07-05'
collected: '2026-07-10'
category: Multimodal
direction: 多模态代理 · 视觉工具编排
tags:
- multimodal agent
- tool orchestration
- image editing
- GRPO
- dataset
- SFT
one_liner: 提出数据集 CanvasCraft 与多模态代理 CanvasAgent，通过 SFT+GRPO 训练，实现多工具协同的复杂图像编辑工作流
practical_value: '- 电商商品图复杂编辑（多步骤生成、分割、文字叠加、增强）可借鉴多工具代理编排思路，将现有图像模型封装为工具，由 LLM 代理按需调用，实现自动化工作流。

  - CanvasCraft 数据构建方式：自动合成多步编辑轨迹（生成→定位→分割→替换→融合），可迁移至构建商品图像处理指令数据集，用于训练客服或运营代理。

  - SFT+GRPO 两阶段训练范式与混合奖励（结果质量+过程合理性）可用于推荐或搜索代理的多步决策优化，提升轨迹合理性与最终效果。

  - 代理在 rollout 中实时检查中间图像状态并动态修正工具选择，该闭环反馈机制可启发构建商品推荐可视化解释代理，按中间反馈调整推荐策略。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：复杂图像创作常需串联生成、分割、编辑、文字叠加等多种模型，现有工具使用代理缺乏可执行的大规模轨迹监督，难以应对多工具协同与中间状态动态调整。

方法：构建 CanvasCraft 数据集，含 140K 完整可执行轨迹与 10K RL 任务规范。设计 CanvasAgent，先通过监督微调（SFT）学习推理-行动轨迹，再使用 GRPO 与混合奖励（结合结果质量与过程合理性）优化。推理时，代理在多轮交互中检查中间图像、跟踪视觉资产，自适应调整工具决策。

结果：在最终图像质量和轨迹行为两个维度评估，CanvasAgent 在复杂多工具图像创建工作流中相比基线显著提升，验证了数据集与两阶段训练的有效性。
