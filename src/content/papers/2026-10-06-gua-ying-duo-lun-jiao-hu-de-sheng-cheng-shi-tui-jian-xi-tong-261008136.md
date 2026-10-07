---
title: Adapting Generative Recommenders for Multi-Turn Interaction
title_zh: 适应多轮交互的生成式推荐系统
authors:
- Yu-Chen Den
- Zhi Rui Tam
- Yung-Yu Shih
- Shih-Hsin Wang
- Yun-Nung Chen
- Pu-Jen Cheng
- Eugene Yang
affiliations:
- National Taiwan University
- Johns Hopkins University
arxiv_id: '2610.08136'
url: https://arxiv.org/abs/2610.08136
pdf_url: https://arxiv.org/pdf/2610.08136
published: '2026-10-06'
collected: '2026-10-07'
category: GenRec
direction: 生成式推荐 · 多轮对话交互
tags:
- Generative Recommendation
- Conversational Recommender
- Semantic ID
- Multi-turn Interaction
- Behavioral Replay
- DPO
one_liner: 让生成式推荐模型通过 routing token、history re-anchoring 与 behavioral replay 在多轮对话中保持准确性并可被纠正
practical_value: '- 如果已有生成式推荐模型（Semantic ID），要接入 Agent/对话场景，可参考 routing token + history
  re-anchoring：将是否推荐建模为解码动作，推荐时把用户历史插入到 ItemID 生成前，避免额外路由分类器。

  - 多任务微调时用 behavioral replay（重放原始序列推荐样本）配合 instruction 数据，能有效防止遗忘历史-物品映射，推荐精度不降反升；这比只做对话微调可靠。

  - 处理用户“不喜欢/换一个”等反馈时，用 DPO 构造偏好对（拒绝 item vs 正确 item）可显著降低重复推荐（Repeat@10 从 1.00 降至
  0.27），是可直接复用的纠偏方法。

  - 评估对话推荐质量时用 LLM-as-judge 而非 BLEU/ROUGE，并将路由失误计入准确率（该推荐时未推荐算 miss），更贴近真实线上体验。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**
生成式推荐将物品编码为 Semantic ID，直接从用户历史解码 ItemID，但用户无法在多轮对话中直接纠正当前意图，偏好变化只能等待后续行为反映。对话式推荐允许反馈，但让模型学对话可能覆盖已学到的历史-物品映射。INTEGER 的目标是在不牺牲推荐准确性的前提下加入交互能力。

**方法关键点**
- 推荐作为解码动作：引入 learned routing token `<hist>`，模型自主决定何时推荐；触发推荐后，插入用户历史 H 与 `<rec>`，再进行 ItemID 前缀 trie 约束解码，恢复原始 history-to-item 格式，称为 history re-anchoring。
- 三源混合微调：多轮对话数据 + 序列推荐数据（behavioral replay）+ 通用指令数据（instruction-data rehearsal），共同 SFT，防止对话训练侵蚀推荐能力。
- 项目细化用 DPO：针对拒绝与换一批反馈构造偏好对，抑制重复推荐，学会替换操作。

**关键结果**
在 Amazon Beauty 与 Toys 上，INTEGER 与最强 baseline 相比：Beauty Hits@10 0.051（较最佳 baseline 提升 13.3%）、NDCG@10 0.027、Conv. Q 4.77；Toys Hits@10 0.057 与 PECRS 并列最佳。所有指标显著优于其初始生成式推荐模型 TIGER。消融显示移除 history re-anchoring 或 behavioral replay 各损失约 33% 推荐准确率；去掉 instruction 数据会使 Conv. Q 从 4.14 降至 2.39。路由行为 AUC 0.94，表明模型能区分聊天与推荐时机。DPO 后 Repeat@10 从 1.00 降至 0.27，Golden Hit@10 提升至约 0.36。

最值得记住的一句话：对话是生成式推荐的控制层，而不是推荐信号本身；routing token 决定何时推荐，history re-anchoring 与 behavioral replay 保护历史-物品映射，使对话化改造反而提升推荐精度。
