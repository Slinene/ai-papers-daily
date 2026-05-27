---
title: 'MAIGO: Mitigating Lost-in-Conversation with History-Cleaned On-Policy Self-Distillation'
title_zh: MAIGO：通过历史清洁化在线策略自蒸馏缓解对话丢失
authors:
- Haoyu Zheng
- Yun Zhu
- Shu Yuan
- Shangming Chen
- Qing Wang
- Wenqiao Zhang
- Jun Xiao
- Yueting Zhuang
affiliations:
- Zhejiang University
- Shanghai AI Laboratory
- Huazhong University of Science and Technology
- Fuzhou University
- Tencent
arxiv_id: '2605.27186'
url: https://arxiv.org/abs/2605.27186
pdf_url: https://arxiv.org/pdf/2605.27186
published: '2026-05-26'
collected: '2026-05-27'
category: LLM
direction: 多轮对话优化 · 在线策略自蒸馏
tags:
- Lost-in-Conversation
- on-policy self-distillation
- multi-turn
- history cleaning
- Qwen
one_liner: 用清理掉先前助手回复的参考分布进行在线蒸馏，消减多轮对话中的自污染，缩小全量 Prompt 与分片对话的准确率差距
practical_value: '- **多轮 Agent 的中间回复污染问题**：在电商导购、工具调用等多轮 Agent 场景，模型生成的中间回复（如过早的推荐、不完整的工具调用）会作为历史上下文影响后续决策。MAIGO
  的思路是直接清理历史中的助手输出，训练模型在干净的用户侧前缀下响应，可借鉴用于构建对历史鲁棒的 Agent 策略。

  - **无需奖励信号的在线自蒸馏**：直接用 EMA 教师模型在清理后的上下文计算参考分布，避免了构造复杂稀疏奖励，可简化多轮 Agent 的微调流程。

  - **自适应可靠性加权**：用学生与参考分布在采样 token 上的对数概率差异生成权重，削弱漂移过大的中间轮次更新，防止模型从错误的自身历史中学习。这个 trick
  可推广到其他在线学习场景，提高信号质量。

  - **全量能力保持分支**：通过概率 ρ 采样全量 Prompt 步骤进行 EMA 自蒸馏，避免分片微调损害模型在完整指令上的表现，对生成式推荐中既要提升多轮体验又要保持单轮推荐质量有借鉴意义。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
大模型在单轮全量指令（FULL view）下表现良好，但在多轮对话中同样的需求分步给出（SHARDED view）时准确率大幅下降，称为 **Lost-in-Conversation (LiC)** 现象。作者发现，其中一个关键原因是模型在中间回合生成的回复会成为后续对话上下文的一部分，这些中间回复可能包含过早假设、部分解或错误状态，进而污染后续推理，产生**自污染**效应。现有方法多依赖稀疏奖励或单轮锚定，但缺乏对中间回复的密集监督。

## 方法
MAIGO 是一种**在线策略自蒸馏**方法，核心是构建**清洁化的历史参考分布**来指导训练：
- **中间回合**：删除此前所有助手回复，只保留用户侧的分片前缀，让学生模型从干净上下文的 EMA 教师分布中学习如何响应，避免继承自身错误。
- **最终答案回合**：保留完整的用户侧对话，并附加一份规范化的全量任务描述，让学生模型从已完成任务的视角恢复答案。
- **自适应可靠性权重**：计算学生和参考分布在采样 token 上的对数概率差异，生成权重，降低漂移轨迹的中间轮次损失。
- **全量视图保留**：以一定概率 ρ 采样全量 Prompt 步进行 EMA 自蒸馏，防止单回合能力退化。
无需验证器奖励、状态标签或推理时的额外脚手架。

## 实验
在 **Math (GSM8K)、Actions (BFCL)、Database (Spider)、Code (HumanEval)** 四个确定性评测任务上，使用 LiC 的 FULL/SHARDED 比对协议。模型为 Qwen2.5-7B-Instruct。比较基准包括 SFT、GRPO、RLSTA。MAIGO 将 SHARDED 平均准确率从 **52.8 → 66.1**，SHARDED/FULL 比从 **66.5% → 84.1%**，而 FULL 平均准确率仅下降 0.7 个点（78.6 vs 79.3）。尤其在 Actions 任务上提升最明显（+29.0）。消融表明中间回合损失和自适应权重均贡献显著。

## 关键一句话
自污染是 LiC 差距中可训练的成分，通过清理历史并在线蒸馏中间回复，能大幅缩小多轮与单轮的差距，且不损失单轮性能。
