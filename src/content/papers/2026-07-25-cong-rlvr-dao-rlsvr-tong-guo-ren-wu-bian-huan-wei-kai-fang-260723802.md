---
title: 'From RLVR to RLSVR: Task Transformation Induces Self-Verifiable Rewards for
  Open-Ended LLM Self-Improvement'
title_zh: 从 RLVR 到 RLSVR：通过任务变换为开放领域 LLM 引入自验证奖励
authors:
- Qinsi Wang
- Jing Shi
- Huazheng Wang
- Kun Wan
- Yiran Wu
- Bo Liu
- Qingyun Wu
- Hai Helen Li
- Yiran Chen
- Handong Zhao
affiliations:
- Duke University
- Adobe Inc.
- Oregon State University
- Pennsylvania State University
- Amazon
arxiv_id: '2607.23802'
url: https://arxiv.org/abs/2607.23802
pdf_url: https://arxiv.org/pdf/2607.23802
published: '2026-07-25'
collected: '2026-08-03'
category: Training
direction: LLM 自我改进 · 自验证奖励 · 多智体博弈
tags:
- RLVR
- self-play
- self-improvement
- multi-agent
- open-ended tasks
- reward engineering
one_liner: 借用自监督学习的任务变换思想，将开放任务重构为基于信息不对称的自我博弈游戏，自动产生可验证训练奖励
practical_value: '- 对缺少可靠奖励的生成式任务（如文案生成、对话推荐、创意内容），可通过设计信息不对称的多智能体游戏来生成监督信号，避免依赖外部奖励模型或人工评判。

  - 交替优化策略：轮流更新“表演者”与“检测者”，防止策略停滞与奖励崩溃，可在自对弈场景中保持持续改进压力。

  - 角色优势估计（RAE）：当不同角色面临不对称难度时，通过减去角色专项基线来校准优势，避免因角色固有偏差损伤策略，可迁移到有角色差异的合作/博弈训练中。

  - 分组投票机制：多玩家集体决策比单一评判更鲁棒，可以借鉴到多模型投票评估或集成式的自监督反馈系统中。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：RLVR（可验证奖励的强化学习）在数学、编码等确定性领域效果显著，但开放任务（如摘要、写作）缺乏客观验证器，现有替代方案依赖人类偏好或 LLM 评判，引入评估偏差、能力瓶颈和额外推理成本。受自监督学习构造前置任务的思想启发，本文提出 RLSVR，将开放任务转化为内部规则能自动产出可验证奖励的代理环境，从而扩展到非可验证领域。
**方法关键点**：
- **任务变换范式 RLSVR**：对原始任务注入隐变量 z，构造观察并根据隐变量生成多个输出，再通过规则检验对 z 的推理，使奖励完全可验证。
- **SpyRL 实例**：基于“谁是卧底”游戏，n 个智能体中有一名间谍接收降级输入，其余平民接收完整输入，所有智能体执行相同目标任务（摘要、写作、数学求解），然后互相投票识别间谍；间谍身份由环境预设，投票正确性完全可验证。
- **两阶段耦合优化**：表演阶段根据被投票数给予零和奖励（间谍被投多则得负奖励，平民被投少则得正奖励），检测阶段用 GRPO 风格优化投票准确率；交替更新两个策略，保持动态博弈。
- **角色优势估计**：为抵消角色不对称带来的奖励偏差，采用 RAE 对每个角色的奖励分别校准。
**关键结果**：
- 在 GovReport、WritingPrompts 等非可验证任务上，SpyRL 的 ROUGE-L 比 Absolute Zero 高 1–4 个点，GPT-4o 评估赢率超过 75%；在创意写作上，人类评估也显著偏好。
- 在 GSM8K、AIME 等可验证数学任务上，SpyRL 仍比 R-Zero 和 Absolute Zero 有 2–5 个百分点的提升。
- 消融：去掉交替优化或间谍机制导致性能迅速饱和；分组人数 n=5 收益最大；信息降级比例（20% vs 40%）影响不敏感。
**核心洞察**：可验证性不必是任务的内禀属性——通过任务变换，我们可以为任何任务制造出确定的奖励信号，从而让 RLVR 扩展到开放领域。
