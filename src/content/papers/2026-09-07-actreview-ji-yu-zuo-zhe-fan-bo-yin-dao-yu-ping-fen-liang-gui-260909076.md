---
title: 'ActReview: Rebuttal-Guided Training Data and Rubric Rewards for Actionable
  Peer Review Generation'
title_zh: ActReview：基于作者反驳引导与评分量规奖励的可操作同行评审生成
authors:
- Yiling Ma
- Yilun Zhao
- Sihong Wu
- Ziyu Chen
- Manasi Patwardhan
- Arman Cohan
affiliations:
- Yale University
- University of Chicago
- TCS Research
arxiv_id: '2609.09076'
url: https://arxiv.org/abs/2609.09076
pdf_url: https://arxiv.org/pdf/2609.09076
published: '2026-09-07'
collected: '2026-09-14'
category: Training
direction: LLM 后训练 · 行动导向评审生成
tags:
- LLM
- GRPO
- Peer Review
- SFT
- Actionable Feedback
- Rebuttal
one_liner: 用作者 rebuttal 揭示的修改动作作为潜在监督，构建 ActReview-40K 并后训练模型生成可操作且带证据的评审建议
practical_value: '- 用交互反馈作为弱监督信号：rebuttal 与 review 的对齐类似于电商评价回复、客服工单中用户申诉/追问能暴露真实意图，可用于训练解释生成或建议
  Agent。

  - 候选感知、弱点特定 rubric 奖励可迁移到推荐理由/诊断报告生成：将输出质量拆成多个细粒度 rubric，结合候选集合用 LLM 判定或规则奖励做 GRPO，提升生成质量与可控性。

  - 局部证据检索与 grounding 机制适合需要引用商品/内容原文做可信推荐解释、搜索结果摘要或 push 文案的场景，能缓解幻觉并提升可验证性。

  - 人类评估中技术准确性仍有 gap，提示业务上线 LLM 建议类功能时应加入技术准确性抽检与领域知识约束，不能只看流畅度和 actionability。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**  
LLM 越来越多用于提交前自审，用户需要的不仅是弱点识别，而是能指导具体修改的行动导向反馈。现有评审生成常停留在诊断层面，缺少可操作的 revision plan。

**方法关键点**  
将任务分解为诊断声明生成和修改建议生成两个子任务。核心洞察：作者 rebuttal 会暴露解决 reviewer concerns 的可行动作，因此可作为 revision-oriented feedback 的潜在监督。从 OpenReview 真实 review-rebuttal 线程构造 ActReview-40K：对齐 reviewer weakness 与 author response，并用局部论文证据 grounding 反馈。后训练 Qwen3-8B-Base：先多任务 SFT，再用 GRPO 配合候选感知、弱点特定 rubric 奖励进行优化。另构建人工标注的 ActReview-Bench，含 1,000 个实例评估诊断质量与修改有用性。

**关键结果**  
ActReview 在 actionability 和 grounding 上超过此前专门 review 生成模型，与强 prompt-based LLM 保持竞争力；人类评估显示 revision usefulness 提升，但技术准确性仍有差距。分析表明模型能泛化到 held-out papers，且对独立评委具有鲁棒性。
