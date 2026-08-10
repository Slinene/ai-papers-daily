---
title: 'CreativeInstruct: Scalably Teaching LLMs to Balance Quality, Creativity, and
  Diversity'
title_zh: CreativeInstruct：可扩展地教大语言模型平衡质量、创意与多样性
authors:
- Ananya Sahu
- Mohit Bansal
- Elias Stengel-Eskin
affiliations:
- Columbia
- UNC Chapel Hill
- University of Texas at Austin
arxiv_id: '2608.07460'
url: https://arxiv.org/abs/2608.07460
pdf_url: https://arxiv.org/pdf/2608.07460
published: '2026-08-07'
collected: '2026-08-10'
category: Training
direction: 可控创意指令微调 · 特殊令牌注入
tags:
- Instruction Tuning
- Creativity
- Diversity
- RL
- Graph Edit Distance
one_liner: 通过在指令微调中引入 [StartCreativity] 令牌，使 LLM 在保持后训练质量的同时恢复基模型的创意多样性
practical_value: '- 在电商推荐文案、对话式推荐等需要创意和多样性的场景，可通过插入类似 [StartCreativity] 的特殊 token
  控制生成风格，在不牺牲质量的前提下提升多样性。

  - 图编辑距离的结构多样性指标可以用于评估推荐理由、产品描述或 push 消息的叙事结构多样性，弥补纯词汇或语义指标的不足。

  - 在 RL 训练前先用 CreativeInstruct 增强基模型的创造性，能显著提升后续 RL 的效果，这对用 RL 优化推荐策略或对话 Agent 的探索能力有直接借鉴。

  - 单一模型即可平衡质量与创意，避免部署多个模型或蒸馏带来的推理开销，适合线上低延迟生成任务。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：后训练（如指令微调、RLHF）虽然大大提升 LLM 的指令遵循、推理和安全能力，但通常降低输出的多样性和创造性，损害需要显式或隐式创意的任务。

**方法**：提出 CreativeInstruct，一种可扩展的指令微调方法。核心是在训练数据中插入特殊的 [StartCreativity] 令牌，教模型在生成时注入「创意跨度」，从而偏向更具创造性的生成。同时，引入基于图编辑距离的结构多样性指标，用于捕捉叙事层面的变化，弥补传统词汇和语义多样性指标的不足。

**关键结果**：在叙事生成任务上，CreativeInstruct 匹配或超出了多模型基线和输出蒸馏方法的多样性，同时不牺牲质量。人工评估中，标注者认为 CreativeInstruct 的生成比后训练模型更有创意的比例达 70.3%。在 RL 实验上，从 CreativeInstruct 检查点开始 GRPO 训练，在 AMC 上提升约 4%，在 MATH 上提升约 5 个百分点，表明创意模型是更好的 RL 基底。
