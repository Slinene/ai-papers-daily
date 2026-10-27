---
title: 'Continual Learning Exam: Benchmarking Long-Horizon RSI and Experiential Learning
  in LLM Agents'
title_zh: 持续学习基准：评估 LLM 智能体的长周期经验学习能力
authors:
- Haoyu Zhao
- Sitian Tu
- Yuxuan Huang
- Huichi Zhou
- Zhangyue Yin
- Jiahao Huang
- Jingyuan Xu
- Tianmiao Shi
- Jin Shi
- Nianxi Zhang
affiliations:
- University College London
arxiv_id: '2610.33956'
url: https://arxiv.org/abs/2610.33956
pdf_url: https://arxiv.org/pdf/2610.33956
published: '2026-10-24'
collected: '2026-10-27'
category: Eval
direction: LLM Agent 持续学习能力评估
tags:
- Continual Learning
- Agent Benchmark
- LLM Evaluation
- Feedback
- Revision
one_liner: 构建 600 级递进任务基准，量化诊断反馈与修订对 LLM 智能体经验学习的作用
practical_value: '- 在电商智能体（如客服、选品、广告优化）的设计中，可以采用「多级递进任务」框架：让 Agent 先完成简单任务，成功后再解锁更复杂任务，从而在任务流中自然积累经验，而不是一次性给出完整任务。

  - 引入「失败后诊断反馈 + 一次修订」的机制，能带来中位数 5.3 个百分点的完成率提升；实际系统中可设置轻量级反馈循环，让 Agent 在失败时获得针对性的错误分析并重新生成一次，成本可控。

  - 评估智能体时，不要只看单个 task 的准确率，而应关注跨时间、跨任务的改进幅度和知识保留；这更贴近推荐/广告系统中连续决策、用户反馈驱动的真实场景。

  - 该基准数据可用于后训练 LLM 以增强持续学习能力，从业者可以考虑将业务日志中的成功/失败案例转化为类似的阶梯式训练样本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM Agent 评估大多只看单任务表现，忽略智能体在长时间跨度中通过经验积累实现进步的能力。真实职业工作流（包括电商运营、广告优化等）要求 Agent 不断从过往成功或失败中学习，因此需要一个专门衡量「经验驱动改进」的基准。

**方法关键点**：构建 Continual Learning Exam (CLE) 基准，包含 120 个人工撰写的任务，每个任务组织为 5 级阶梯，共 600 个级别，覆盖 12 个职业领域、89 种专业角色。Agent 必须通过当前级别才能解锁下一级，后续级别依赖之前任务中积累的经验。评估由专门的 evaluation agent 根据人工制定的评分标准进行。对比两种设置：单次提交 vs. 失败后给出诊断反馈并允许一次修订。

**关键结果**：在 17 个 harness–model 配置（使用前沿 LLM）上，反馈与修订带来中位数完成率提升 5.3 个百分点。但最佳系统也仅通过 47.7% 的级别，且只有 23.3% 的任务能完成全部五个级别，说明现有前沿 LLM 在持续经验学习上仍有很大困难。数据也可用于后训练 LLM 以增强持续学习能力。
