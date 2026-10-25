---
title: 'HERD: Harness-Evolving Recursive Distillation for Continual Learning'
title_zh: HERD：面向持续学习的 Harness 演进递归蒸馏
authors:
- Xun Sun
- Thanh Thi Nguyen
- Thuy-Trang Vu
affiliations:
- Monash University
- University of the Sunshine Coast
arxiv_id: '2610.31401'
url: https://arxiv.org/abs/2610.31401
pdf_url: https://arxiv.org/pdf/2610.31401
published: '2026-10-22'
collected: '2026-10-25'
category: Training
direction: 持续学习混合框架 · 递归蒸馏
tags:
- Continual Learning
- LLM
- Distillation
- In-Context Learning
- Harness
one_liner: 提出混合持续学习框架 HERD，用 harness 技能库与有界残差记忆结合双锚漂移约束蒸馏，实现新任务获取与低遗忘。
practical_value: '- 在电商/Agent 持续迭代中，可借鉴「skill/harness + 有界高残差样本库」做快速适配：新任务/新类目先用上下文技能处理，只把模型反复出错的高价值样本沉淀为记忆，避免全量重训。

  - 蒸馏策略：定期把 harness 记忆蒸馏回基座模型时，采用双锚点（初始 checkpoint + 上一版蒸馏模型）做漂移约束，能缓解长时间递归更新中的遗忘，适合需要频繁发版/增量训练的推荐模型或
  Agent policy。

  - 资源固定：HERD 在固定 memory 与 compute 预算下运行，给生产环境提供了一个可落地的约束范式：不无限增长上下文/记忆，通过递归蒸馏滚动内化经验，保持线上成本稳定。

  - 注意：论文面向通用 LLM 持续学习，不是推荐系统专用；但其中「技能库 + 残差记忆 + 双锚蒸馏」的架构可迁移到多域推荐、搜索 query 策略或客服 Agent
  的持续优化。'
score: 6
source: arxiv-cs.CL
depth: abstract
---

动机：持续学习中参数方法面临灾难性遗忘和可塑性丧失；非参数方法（prompts/skills/harness）受上下文长度和文本压缩损失限制。HERD 提出混合框架，兼顾 harness 的高效上下文学习与参数化累积。

方法关键点：在 harness 侧，持续精化 skills 捕捉可复用模式，并将 skills 无法覆盖的高残差样本保留在有界记忆；在参数侧，采用双锚点（dual anchors）的漂移约束蒸馏，把 harness 经验内化为参数能力，同时减少长递归运行中的遗忘。整个过程在固定记忆和计算预算下进行。

关键结果：在 TRACE+17 的 25 阶段任务流上，HERD 在新任务获取上匹配最强参数基线，同时表现出最少的遗忘和最强的通用能力保持。
