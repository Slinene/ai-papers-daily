---
title: 'PhysCaP: Grounding Code-as-Policy Agent with Physics-Informed Exploration'
title_zh: PhysCaP：物理信息探索增强的代码即策略智能体
authors:
- Chen-Yu Lin
- Jing-Wen Chen
- Hsueh-En Chang
- Hung-An Chen
- Sheng-Hsun Chang
- Chi-Pin Huang
- Fu-En Yang
- Min-Hung Chen
- Yi-Ting Chen
- Yu-Chiang Frank Wang
affiliations:
- National Taiwan University
- NVIDIA Research
- National Yang Ming Chiao Tung University
arxiv_id: '2608.21031'
url: https://arxiv.org/abs/2608.21031
pdf_url: https://arxiv.org/pdf/2608.21031
published: '2026-08-20'
collected: '2026-08-25'
category: Agent
direction: Agent 主动探索与物理属性估计
tags:
- Code-as-Policy
- Physics-Informed Exploration
- Dual-Agent
- Active Perception
- Training-Free
one_liner: 引入物理信息探索层与双智能体设计，以更少交互估计物体质量与刚度，提升主动感知效率
practical_value: '- 交互式推荐/对话式 Agent 可借鉴 Planner-Prioritizer 双层设计：Planner 决定何时向用户提问或停止探索，Prioritizer
  用启发式优先级过滤候选问题，避免过度打扰用户，同时降低 LLM 调用成本。

  - 免训练物理属性提取的思路可迁移到用户/商品潜在属性推断：利用点击、滚动、停留等隐式交互信号估算价格敏感度、质量感知等，无需额外标注或传感器。

  - 在需要在线探索的推荐策略中，不要盲目试错：先用先验知识过滤不合理动作，再对剩余候选按信息增益排序，可显著减少实验次数和线上成本。

  - 工程实现上，Prioritizer 采用规则化启发式而非 LLM 打分，能兼顾效果与推理时延，适合高并发在线场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：VLA 策略依赖被动观测，难以推断物体质量、刚度等潜在物理属性，影响机器人操作；现有交互式方法容易过度探索或失效。

方法：PhysCaP 在 code-as-policy 框架上增加物理信息探索层，包含免训练物理属性提取模块，利用机器人本体感知直接估计质量与刚度，无需额外传感器。采用双智能体设计：Planner 决定何时探索、何时停止；Prioritizer 过滤不合理交互，并用启发式优先级分数对剩余交互排序，实现高效、定向探索。

结果：在真实桌面任务（寻找隐藏物体、检测空罐、识别成熟牛油果）和 LIBERO 仿真任务中，PhysCaP 相比被动基线及朴素交互基线，以更少交互次数和更短执行时间达到可比性能；消融实验验证了物理属性提取模块的有效性。
