---
title: Visual Contrastive Self-Distillation
title_zh: 视觉对比自蒸馏
authors:
- Yijun Liang
- Yunjie Tian
- Yijiang Li
- Yuqi Jia
- Furong Huang
- Tianyi Zhou
- Di Fu
affiliations:
- University of Maryland, College Park
- University of California, San Diego
- Duke University
- MBZUAI
arxiv_id: '2607.21556'
url: https://arxiv.org/abs/2607.21556
pdf_url: https://arxiv.org/pdf/2607.21556
published: '2026-07-23'
collected: '2026-07-24'
category: Training
direction: 多模态LLM · 在线自蒸馏
tags:
- VCSD
- on-policy self-distillation
- contrastive distillation
- multimodal LLM
- EMA teacher
one_liner: 通过对比原图与内容擦除图的教师分布差异，无需外部教师或特权信号即可高效训练多模态LLM
practical_value: '- 在商品图像理解的生成式推荐任务中，可构造“原图 vs 内容擦除图”的对比条件，让教师模型强化对商品关键特征的响应，抑制背景噪声，提升推荐文案或搜索查询生成的准确性。

  - 使用 EMA 教师进行在线自蒸馏，无需外部强大教师，可降低训练成本。在 RLHF 或生成式检索的训练中，可基于模型自身分布差异构造更优训练目标。

  - 对于 Agent 视觉决策（如 UI 操作），微调时采用该方法可使模型更关注任务相关区域，忽略无关背景，提升复杂界面下的精确操作能力。

  - 方法不增加推理成本，适合部署在电商线上服务中，实现大规模商品图片的实时理解与描述生成。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

现有在线自蒸馏（OPSD）仍需教师与学生之间的信息不对称，通常依赖特权答案或视觉证据。本文提出一种仅由输入条件差异驱动的简化形式——视觉对比自蒸馏（VCSD）。具体而言，在学生模型生成的每个响应前缀处，EMA 教师基于同一提示和前缀产生两个下一 token 分布：一个以原始图像为条件，另一个以内容擦除的控制图为条件。两者的 token 级对数概率差凸显了因实例级视觉内容而增加的候选 token。教师利用该差异锐化其原始图像分布（在合理支持范围内），最终将得到的全分布目标蒸馏给学生。在 ViRL39K 数据集上，VCSD 在 Qwen3-VL 和 Qwen3.5 模型上一致优于匹配的 OPSD：在 Qwen3-VL 上，2B 模型从 62.27% 提升到 67.04%，4B 从 71.30% 到 73.16%，8B 从 72.51% 到 76.26%。该方法无需外部教师、特权答案、视觉证据信号、推理轨迹，也不增加推理成本。
