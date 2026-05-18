---
title: 'MMSkills: Towards Multimodal Skills for General Visual Agents'
title_zh: MMSkills：面向通用视觉智能体的多模态技能框架
authors:
- Kangning Zhang
- Shuai Shao
- Qingyao Li
- Jianghao Lin
- Lingyue Fu
- Shijian Wang
- Wenxiang Jiao
- Yuan Lu
- Weiwen Liu
- Weinan Zhang
affiliations:
- Shanghai Jiao Tong University
- Xiaohongshu Inc.
- Southeast University
arxiv_id: '2605.13527'
url: https://arxiv.org/abs/2605.13527
pdf_url: https://arxiv.org/pdf/2605.13527
published: '2026-05-13'
collected: '2026-05-18'
category: Agent
direction: 视觉智能体 · 多模态技能复用
tags:
- Multimodal Agents
- Skill Reuse
- GUI Navigation
- Visual Grounding
- Procedural Knowledge
one_liner: 提出多模态技能包（状态卡片+关键帧+文本过程），并通过分支加载机制提升视觉Agent决策。
practical_value: '- 可借鉴多模态技能包构建方式：将电商操作流程（如商品搜索、下单）封装为文本过程+关键状态截图+状态描述卡片，减少Agent推理时的图像上下文开销。

  - 利用非评测的用户交互轨迹（如公开的购物会话）自动生成可复用技能库，通过工作流分组和视觉接地减少人工标注成本。

  - 分支加载机制可集成到电商Agent中：在临时上下文里对比当前界面与技能包中的关键帧，对齐状态后才给出操作建议，避免直接参考静态截图导致的过锚定。

  - 多模态过程知识对外部技能库的补充思路，可推广到生成式推荐中的多模态用户意图理解，用类似状态卡片描述用户当前搜索上下文。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有Agent技能的复用主要依赖文本或代码，而视觉任务中的过程知识天然要求多模态——不仅要知道执行什么操作，还要识别界面状态、判断进展与失败条件。因此需要一种多模态技能包，并解决三个问题：(I) 包内应包含什么内容；(II) 从何处获取；(III) 推理时如何高效运用多模态证据而不引入过多图像上下文或过拟合参考截图。

**方法**：提出MMSkills框架。技能包为紧凑的状态条件化结构，将文本过程与运行时状态卡片、多视角关键帧耦合。利用公开的非评测交互轨迹，通过工作流分组、过程归纳、视觉接地和元技能引导审核，自动生成可复用的多模态技能。使用时，引入分支加载机制：在临时分支中检查选定的状态卡片和关键帧，与实时环境对齐，提炼为结构化指导注入主Agent。

**结果**：在GUI操作与游戏两类视觉Agent基准上，MMSkills均带来一致的性能提升，无论是前沿大模型还是较小规模的多模态模型均受益，表明外部多模态过程知识能有效补充模型内部先验。
