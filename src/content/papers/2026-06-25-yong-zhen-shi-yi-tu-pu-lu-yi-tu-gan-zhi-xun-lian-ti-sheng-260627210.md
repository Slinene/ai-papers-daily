---
title: 'Paved with True Intents: Intent-Aware Training Improves LLM Safety Classification
  Across Training Regimes'
title_zh: 用真实意图铺路：意图感知训练提升LLM安全分类
authors:
- Jeremias Ferrao
- Niclas Müller-Hof
- Iustin Sîrbu
- Traian Rebedea
- Yftah Ziser
affiliations:
- University of Groningen
- University Politehnica of Bucharest
- NVIDIA
arxiv_id: '2606.27210'
url: https://arxiv.org/abs/2606.27210
pdf_url: https://arxiv.org/pdf/2606.27210
published: '2026-06-25'
collected: '2026-06-28'
category: Training
direction: 意图感知训练增强安全分类
tags:
- intent-aware training
- safety classification
- GRPO
- DPO
- AIMS dataset
- faithful intent
one_liner: 将用户意图作为显式中间信号，跨SFT/DPO/蒸馏/RL范式提升安全分类器鲁棒性，GRPO奖励意图保真度达最优
practical_value: '- 在电商/Agent安全审核中，可将用户意图作为中间特征引入分类器，用少量人工标注（如AIMS仅1724条）提升对困难样本的判别力

  - 借鉴意图条件蒸馏思路：在蒸馏安全判别模型时，让学生模型同时学习推理过程与最终意图，优于仅蒸馏推理

  - 将意图保真度设为奖励函数，通过GRPO等RL方法直接优化安全分类的忠实性，可离线或在线微调

  - 构建“提示→意图→标签”三阶段pipeline，在线上推理时引入意图生成步骤，以可控延迟换取更高准确率，形成帕累托前沿'
score: 6
source: arxiv-cs.CL
depth: abstract
---

**动机**：LLM安全分类面临虚假拒绝或漏判，因为有害性常取决于用户潜在意图而非表面文本。仅用提示-标签对训练的分类器缺乏对意图的显式建模。

**方法关键点**：
- 提出 **AIMS** 数据集（1,724条困难安全提示），每条含人工标注的意图描述与二值危害标签，形成 `(prompt, intent, label)` 三要素。
- 在 **SFT** 中同时预测意图与标签；在 **DPO** 中利用模型生成的意图错误构建偏好对；在**推理蒸馏**中引入意图条件，让学生模型学习“先推理再生成意图再判定”；将**GRPO** 的奖励设为意图保真度，直接优化生成意图与真实意图的一致性。
- 所有范式均将意图作为中间表征，意图条件蒸馏优于纯推理蒸馏，GRPO在多个外部基准上取得最高平均F1，且意图感知模型形成推理延迟与F1的帕累托前沿。

**关键结果**：
- 在5个外部安全基准上，GRPO意图奖励训练的模型平均F1最高（相比基线SFT提升显著）。
- 意图条件蒸馏在多数教师-学生对中超越仅推理蒸馏。
- 仅利用1,724个样本的AIMS即可训练出有竞争力的安全分类器，证明意图信号紧凑且高质量。
