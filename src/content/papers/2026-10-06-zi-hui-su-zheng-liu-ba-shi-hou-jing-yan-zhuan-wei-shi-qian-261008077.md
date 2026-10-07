---
title: 'Self-Retrospection Distillation: Turning Post-hoc Experiences into Prior Foresight'
title_zh: 自回溯蒸馏：把事后经验转为事前前瞻
authors:
- Haoxiang Zhang
- Qinglin Chen
- Hiroaki Hayashi
- Zhuofeng Li
- Siming Zhang
- Jiaxin Zhang
- Jixuan Chen
- Fang Wu
- Pan Lu
- Silvio Savarese
affiliations:
- Salesforce AI Research
- UC San Diego
- Texas A&M University
- Stanford University
arxiv_id: '2610.08077'
url: https://arxiv.org/abs/2610.08077
pdf_url: https://arxiv.org/pdf/2610.08077
published: '2026-10-06'
collected: '2026-10-07'
category: Training
direction: RLVR 辅助损失 · 事后到事前蒸馏
tags:
- RLVR
- self-distillation
- prospective learning
- hindsight
- LLM agent
- training
one_liner: 用事后交互轨迹蒸馏出交互前可预测的知识/失败模式，让每条 rollout 均贡献监督，最高提升 24.2 pp
practical_value: '- 在强化学习训练电商导购/搜索 Agent 时，不要只依赖 scalar reward：把每个会话/交互轨迹的事后信息（成功所需知识、失败原因）作为监督，训练模型在交互前输出前瞻性描述。成功轨迹预测用户可能关心的知识点，失败轨迹预测易错点/陷阱；该输出仅作训练目标，推理时不生成，不增加线上成本。

  - 对奖励稀疏或组内 reward 一致的场景（大量会话无转化、点击稀疏），GRPO 等 group-relative 方法会丢弃全失败/全成功的 rollout
  组；SRD 这类逐轨迹事后监督不依赖组内 variance，能从失败样本中榨取价值。2B 模型在全失败组占 98% 时仍能达到 60.6% 成功率，说明可以复用线上大量负反馈会话做冷启动训练。

  - 具体实现用 stopped-gradient 的同一模型当 teacher，输入额外包含 gold solution 或 error annotation，与
  student 的前瞻 rollout 做 token 级 JSD 对齐；只选 pitfall 视角通常比 knowledge+pitfall 更稳定且计算更便宜，不要盲目堆多个辅助头。

  - 纯 self-distillation 在工具交互任务上可能不稳定（9B OPSD 在 HotpotQA/2Wiki/LCB 低于 vanilla），引入前瞻蒸馏能稳定训练并恢复单调
  scaling；在复合 RL+蒸馏目标（RLSD）中也可叠加，通常 +SRD 提升明显。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**  
RLVR 只使用 scalar outcome reward，当 rollout 组内 reward 完全一致（全失败或全成功）时，group-relative advantage 归零，整组轨迹被丢弃。这尤其发生在长程推理/Agent 任务中：策略太弱时全失败，太强时全成功，大量交互信息被浪费。事后轨迹里其实包含丰富信号：任务需要哪些知识、哪些步骤容易错，但这些只被用于更新行为策略。论文提出用这些事后经验监督交互前的前瞻预测。

**方法关键点**  
- 提出 prospective learning：让策略在交互前预测任务可能需要的知识（KNOWLEDGE）和可能出现的失败模式（PITFALL），用事后轨迹提供的 privileged hindsight 作为监督。foresight 只作训练目标，推理时不生成。
- SRD 实例：在同一 policy 下，按 rollout 成功/失败选择 knowledge/pitfall 视角；学生从 task 和 environment context 生成 foresight token 序列；stopped-gradient self-teacher 额外看到 gold solution 或 error annotation，对同一序列做 token 级分布对齐，损失用 JSD。
- 可以轻量叠加在 GRPO/OPSD/RLSD 上，辅助损失权重 λ=0.01。
- 消融发现 pitfall 通道比 knowledge 更有效且便宜；同时用 knowledge+pitfall 无显著收益，甚至可能下降。

**关键实验结果**  
- 在 10 个工具集成推理和长程 Agent 基准（Math/Code/Search/Agentic，Qwen3.5-4B/9B）上，+SRD 普遍提升：最高 +24.2 pp（9B OPSD+SRD 在 AIME26）。
- 4B GRPO+SRD 在 Math/Code/Search 平均分别提升 +10.03/+8.33/+8.05 pp。
- 2B 设置下，GRPO 在 98% 组全失败时最终 0.0% 成功，同样 rollout 预算加 SRD 达到 60.6%。
- SRD 修复了纯 self-distillation 的不稳定：9B OPSD 在 HotpotQA/2Wiki/LCB 低于 vanilla，加 SRD 后恢复到高于 vanilla 且 Math 单调 scaling。
- Token 分析显示 SRD 主要重新分配预测预算：增加规划性语言和概念命名，减少 inline 数学符号/数字。

**最值得记住的一句话**  
把“事后才知道的坑和知识”蒸馏成“行动前就能说出来的预判”，让每条经验都有监督价值，即使 reward 没有区分度。
