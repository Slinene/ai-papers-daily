---
title: 'Scientist World: Grow a Research World for AI-Scientists'
title_zh: 科学家世界：为 AI 科学家构建可执行研究环境
authors:
- Taiming Lu
- Sachin Konan
- Zhuang Liu
affiliations:
- Princeton University
arxiv_id: '2611.08478'
url: https://arxiv.org/abs/2611.08478
pdf_url: https://arxiv.org/pdf/2611.08478
published: '2026-11-05'
collected: '2026-11-06'
category: Other
direction: AI Scientist 可执行环境与评估
tags:
- AI Scientist
- Executable Environment
- Benchmark
- GRPO
- LLM
- Research Automation
one_liner: 将每篇论文转化为可执行环境，作为 AI 科学家的评估与训练场，前沿模型在 74% 任务上超越人类基线
practical_value: '- 可借鉴其“可执行环境 + 基线复现 + 相对提升”的评估框架，将业务中的算法策略（如排序模型、query 改写、创意生成）封装为自动化实验环境，让
  LLM Agent 提出改进并实时验证，减少人工评估成本。

  - 利用大模型科研轨迹对小模型做 SFT/GRPO 蒸馏，在成本敏感的场景（如电商内部小模型做标题优化、广告文案生成）中，用少量标注或轨迹数据提升小模型能力。

  - 记录 Agent 的完整探索轨迹（想法、实验、失败、成功）作为离线数据集，可用于后续策略模型的强化学习训练或错误分析，提高迭代效率。

  - 整体偏学术贡献，业务直接可迁移性有限，但环境构建和轨迹复用思路对自动化实验平台有参考价值。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**  
AI 科学家已经出现，但缺乏可供其成长的“研究世界”。人类科学家依赖数百年的开放问题与共享文献，但这些对 AI 科学家只是可读文本，无法直接运行验证。为此构建 Scientist World，让每篇研究论文变成一个可执行环境，使 AI 科学家可以在其中改进方法、提出新想法。

**方法关键点**  
- 自动化流水线：从论文中抽取开放式研究问题，并复现论文方法作为 baseline。
- 评估方式：AI 科学家进入该环境后，其提出的改进相对人类作者 baseline 的提升量化为 Frontier-Normalized Improvement (FNI)。
- 数据集：发布首批 1,000 个经过验证的环境，并记录 6,400 小时研究轨迹，包含 15,000 个研究想法、43,000 次计算实验，涵盖 idea、experiment、failure、success。
- 训练用途：将研究轨迹作为训练数据，通过 SFT 和 GRPO 提升小模型的研究构思能力。

**关键结果数字**  
- 前沿 AI 科学家在 74% 的任务上已超过人类研究者。
- 从零创新任务中，最佳模型（如 Fable 5.1）得分 76.3，远高于部分前沿模型。
- 小模型经过训练后 research ideation 提升 +158%，达到前沿模型水平。
