---
title: Language Models as AI Research World Models
title_zh: 语言模型作为 AI 研究世界模型
authors:
- Zijun Wang
- Zewen Liu
- Minhua Lin
- Zhaotian Weng
- Zhan Shi
- Bing He
- Yisi Sang
- Dakuo Wang
- Benoit Dumoulin
- Wei Jin
affiliations:
- Amazon
- UC Santa Cruz
- Emory University
- Pennsylvania State University
- UC Santa Barbara
arxiv_id: '2610.12235'
url: https://arxiv.org/abs/2610.12235
pdf_url: https://arxiv.org/pdf/2610.12235
published: '2026-10-08'
collected: '2026-10-10'
category: Agent
direction: AI 研究 Agent 的世界模型
tags:
- Agent
- World Model
- LLM
- Experiment Selection
- Autoresearch
one_liner: 用真实实验历史微调 LLM 作为研究世界模型，显著提升候选实验干预排序与自动研究收益
practical_value: '- 在电商/广告实验中，收集历史 A/B 测试、模型调参、策略变更的实验记录（实验条件 + 结果），用 LLM 微调成环境专属的“策略结果预测器”，对新策略做排序，能减少无效实验成本。

  - 跨业务场景迁移：当新业务（如新推荐位、新广告产品）实验数据少时，用其他相似场景的历史实验数据预训练 world model，可大幅降低对新场景候选策略的选择
  regret（如论文中跨环境减少 78% regret）。

  - 多轮自动实验调优：在固定实验预算下，用 world model 先筛掉低潜候选，再做真实实验验证，能提高最终最优策略的收益（论文中提升 15.8%）；可应用于搜索排序、广告出价、召回策略的自动搜参。

  - 选择 LLM 作为 world model 时，注入领域实验知识比仅更换更强模型或增加推理长度更有效，因此应优先积累内部实验数据并微调。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：AI research agent 能大量生成实验候选，但真实执行代价极高（如 17.1 万 H100 GPU 小时）。需要一种模型预测候选干预的结果，从而在有限预算下选择有潜力的实验。

**方法关键点**：将 LLM 作为 Research World Model (RWM)，喂入实验设计（配置、超参、干预描述）与对应结果，训练/利用其对未见干预的效果排序。数据来自 9 个研究环境（预训练、后训练、推理）共 2,600+ 实验记录。评估指标包括 Spearman 相关性、selection regret、以及多轮 Autoresearch 的最佳增益。

**关键结果**：使用同一环境的历史实验知识可使 RWM 对未见干预的预测 Spearman 提高 +0.27；仅用预训练经验跨环境迁移到 Qwen3 环境时，selection regret 相比零经验降低 78%；在固定预算的多轮自动研究中，in-env 与 cross-env 知识分别将最佳增益提高 15.8% 和 11.6%；13 个 LLM 的消融显示，加入研究知识比更换模型或增加推理更有效。
