---
title: Steering Black-Box Large Language Model Agents with Pitfall Anticipation World
  Model
title_zh: 坑点预测世界模型引导黑盒 LLM Agent
authors:
- Jiongxiao Wang
- Han Ding
- Youzhi Luo
- Yawei Wang
- Yun Zhou
- Linbo Liu
- Panpan Xu
affiliations:
- University of Wisconsin–Madison
- AWS AI
arxiv_id: '2610.29139'
url: https://arxiv.org/abs/2610.29139
pdf_url: https://arxiv.org/pdf/2610.29139
published: '2026-10-20'
collected: '2026-10-27'
category: Agent
direction: 世界模型引导黑盒 LLM Agent
tags:
- World Model
- Agent Steering
- Black-box LLM
- GRPO
- Pitfall Anticipation
one_liner: 用外部世界模型仅预测潜在坑点并选择性介入，SFT+GRPO 训练，显著提升黑盒 LLM Agent 成功率
practical_value: '- 在电商/搜索的 Agent 工作流中，不要每步都注入外部知识；训练一个“坑点检测器”仅在预测到失败风险时介入，可大幅减少 API
  调用并降低对主 Agent 的干扰。可复用 PAWM 的 gate 机制：世界模型输出 `<pass>` 或具体警示，主 Agent 仅在收到警示时才重新考虑动作。

  - 构建训练数据时，利用成功/失败轨迹对比定位关键失误步骤，并用 LLM 生成抽象化、不泄露未来信息的坑点描述；对 `<pass>` 样本进行下采样以平衡正负比例（论文发现
  0.75–1.0 的 pass-to-anticipation 比例最优），可迁移到业务中的异常检测/干预模型训练。

  - 将辅助模型与黑盒主模型用 GRPO 联合训练：以任务成功率为奖励，用 group-relative advantage 更新辅助模型，能显著提高辅助模型在实际
  Agent 中的有效性；训练出的辅助模型可跨多个黑盒主模型迁移，适合作为独立服务部署。

  - 世界模型的输出内容设计：预测“到下一个子目标的多步未来”比预测下一步观察或完整剩余轨迹更有效；单步预测信息量不足，过长预测误差累积且可能误导。在推荐/搜索
  Agent 的规划辅助模块中，应聚焦于有意义的里程碑边界。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
黑盒 LLM Agent（如 Claude Sonnet 4.5）通用能力强，但缺乏特定环境的动态知识，无法通过微调注入。已有外部 steering 方法多聚焦规划辅助，未提供环境如何响应动作的知识。世界模型可填补此空白，但现有工作要么作为模拟器搜索候选动作成本高，要么每步预测下一观察收益低且可能干扰 Agent。论文先通过系统先导研究回答两个核心问题：世界模型应该输出什么、何时介入。

**方法关键点**
- 先导研究发现：输出“到下一个子目标的多步未来轨迹”效果最佳，优于单步预测和完整剩余轨迹；分析表明，改变 Agent 动作的引导主要由坑点预测主导；仅传递坑点预测的 gating 几乎保持全量引导的性能且大幅减少 API 调用。
- 提出 Pitfall Anticipation World Model (PAWM)：选择性介入，仅在预测到潜在失败时输出警示与纠正建议，否则输出 `<pass>` 保持沉默。
- 两阶段训练：① SFT on synthetic pitfall dataset——收集成功/失败轨迹，用 LLM 对比定位关键坑点步骤，生成抽象化的坑点描述和纠正指导，同时下采样 `<pass>` 样本平衡比例；② GRPO co-training——将 PAWM 与冻结的黑盒 Agent 在环境中联合训练，以任务成功率为奖励，用 group-relative advantage 优化辅助模型，并加 KL 约束防止偏离参考策略。

**关键实验**
- 数据集：ScienceWorld 和 WebArena-Lite，Agent 为 Claude Sonnet 4.5，世界模型基座为 Qwen3.5-27B。
- 主要结果：PAWM 将 ScienceWorld 成功率从 54.6% 提升至 78.9%（+24.3%），WebArena-Lite 从 72.7% 提升至 80.4%（+7.7%），超过 RAG、Pre-Task Guidance、Next-Obv/Full-Traj/SubGoal-Traj 等所有 baseline；GRPO 阶段进一步拉大差距。
- PAWM 学到的坑点知识可迁移到 Claude Haiku/Opus、GLM 5、Kimi K2.5 等多种黑盒 backbone。

**最值得记住的一句话**
世界模型的价值不在于每步模拟，而在于在关键坑点处提供到下一个里程碑的多步前瞻性警示。
