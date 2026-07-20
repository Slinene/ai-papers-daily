---
title: Recursive Harness Self-Improvement
title_zh: 递归护栏自我改进：少量迭代提升智能体性能上限
authors:
- Hyunin Lee
- Jinglue Xu
- Jeffrey Seely
- Donghyun Lee
- Matei Zaharia
- Yujin Tang
affiliations:
- Sakana AI
- UC Berkeley
arxiv_id: '2607.15524'
url: https://arxiv.org/abs/2607.15524
pdf_url: https://arxiv.org/pdf/2607.15524
published: '2026-07-16'
collected: '2026-07-20'
category: Agent
direction: Agent 自我优化 · 提示级迭代改进
tags:
- Agent Self-Improvement
- Harness Optimization
- Multi-Agent Systems
- Test-Time Scaling
- Prompt Engineering
one_liner: 提出RHI，通过提示级迭代优化智能体循环，仅需少量样本即可超越最大推理设置并降低60%成本
practical_value: '- 在电商推荐或搜索的Agent工作流中，可对编排提示（harness）进行任务特定的迭代优化，而无需依赖模型推理深度，从而以更低成本获得更优性能。

  - 利用成对比较反馈自动优化多智能体间的信息流，提升复杂任务（如多轮对话推荐、用户意图理解）中上下文管理的有效性。

  - RHI的轻量级特点（仅需少量迭代与低推理努力Agent）表明，实际业务可快速微调Agent编排模板，避免昂贵的手工设计或重训练。

  - 实验显示性能增益源于改进的上下文管理而非更长推理，提示优化Agent间通信机制（如工具调用、中间结果传递）可能比堆叠推理步骤更高效，对商品检索或广告策略Agent有参考意义。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：在模型与护栏协同进化下，护栏的推理轨迹可作为模型训练数据，但提供商构建的脚手架更新成本高。亟需一种任务特定、轻量级的用户护栏优化方法，以提升后续轨迹质量并降低计算开销。

**方法**：提出**递归护栏自我改进（RHI）**，将护栏抽象为智能体循环的提示级规范，并利用其修订历史中的成对比较反馈进行迭代优化。核心是在少量迭代中，让低推理努力的智能体通过自我修正提示完成性能跃升。

**结果**：在30个合成机器学习研究任务（覆盖量化金融、机器人、药学）上，仅需数次RHI迭代，低推理努力智能体即可超越对应的最大推理设置或超强基线，推理成本最高降低60%。进一步分析发现，增益主要来自任务特定上下文管理的改善（更高效的智能体间信息流），而非延长推理轨迹。该工作给出了RHI隐式优化目标的信息论解释，为模型-护栏协同进化下的持续学习提供了实用算法。
