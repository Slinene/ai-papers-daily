---
title: 'The Tasteful Agent: Measuring and Improving Taste in Long-Horizon Tasks'
title_zh: 有品位的智能体：长时程任务中决策品味的测量与提升
authors:
- Wenbo Pan
- Zhichao Liu
- Shujie Liu
- Jingying Zeng
- Chin-Yew Lin
- Xianfeng Tang
- Yan Lu
- Qi He
- Xiaohua Jia
affiliations:
- City University of Hong Kong
- Microsoft
arxiv_id: '2609.25804'
url: https://arxiv.org/abs/2609.25804
pdf_url: https://arxiv.org/pdf/2609.25804
published: '2026-09-21'
collected: '2026-09-23'
category: Agent
direction: 长时程智能体决策品味测量与蒸馏
tags:
- taste
- long-horizon
- decision fork
- distillation
- agent evaluation
one_liner: 构建 Taste-Bench 从真实 agent 轨迹自动挖掘决策分叉，度量并蒸馏长时程决策品味
practical_value: '- 可在电商/广告/Agent 场景中复用「决策分叉」挖掘思路：从线上 A/B 轨迹或 agent 自我纠错日志自动构造偏好对，无需人工标注，为选品策略、召回方案、创意方向等中间决策建立
  taste 评估集。

  - 蒸馏时用「见过正确分支的 teacher 生成推理链、student 只看到分叉前上下文」的 privileged-context 方法，适合把历史成功/失败路径的
  hindsight 迁移成轻量 advisor 模型，对 query 改写、商品筛选、广告投放策略等长流程决策提供实时建议。

  - 两选项判断任务（如新旧策略对比、生成式候选筛选）建议采用正反序两次回答均正确才算对的评分，缓解 LLM 位置偏置；工程实现上可直接借鉴。

  - 将 advisor 判断注入 executor 上下文能显著提升端到端成功率（论文中正确建议 +24.4pp、蒸馏学生 +19.1pp），可在推荐 agent
  工作流中对关键 fork 注入模型建议。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM agent 在长时程任务中常需在关键节点做方向选择（如实现哪种方案、测试哪个假设），这些决策影响全局，但现有 benchmark 只测端到端成功，无法度量中间决策质量（称为 taste）。且人工标注成本高，难以扩展。核心观察：轨迹的后续部分为前期选择提供了事后证据；多尝试轨迹会在决策点分叉，结果差异可标注更优方向。

**方法关键点**
- 定义决策分叉（decision fork）：同一任务两条尝试在共享前缀后分叉，或单条轨迹中自我纠错形成 detour；分叉前隐藏后续，让模型选择候选方向。
- 自动挖掘：从工程（SWE-bench Pro 自采 2677 条运行）与研究（MALT 公开 RE-Bench/HCAST 1132 条运行）轨迹池中，用生成模型提取 parallel forks 和 detour forks；再用过滤去掉 trivial（仅看候选可猜）和 undecidable（完整轨迹下评判不一致）。
- 得到 502 题 Taste-Bench，2×2 设计：parallel/detour × engineering/research；人工复核 100 题，172 个显式判断与挖掘标签一致率 98.8%。

**关键实验**
- 14 个前沿模型评估，最佳 GPT-5.6 Sol 平均准确率 59.7%，随机线 25%；时间跨度越长越难（in-prefix 62.3% 降到 more-work 21.0%）；加大推理预算无提升。
- 蒸馏实验：Qwen3.6-27B + LoRA，用 privileged teacher 蒸馏推理而非仅拟合标签；在 task-disjoint 工程测试上，student 准确率从 30.0% 提升到 47.9%；将 student 建议注入 executor，held-out SWE-bench Pro 成功率从 14.6% 提升到 33.7%，接近正确建议上限 39.0%。

**最值得记住的一句话**：taste 可以通过轨迹事后证据自动测量，并且蒸馏能将长时程判断从教师迁移到学生并带来端到端收益。
