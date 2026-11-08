---
title: 'Terminal-style Mathematical Modeling Bench: The First Agentic and Verifiable
  Benchmark for Mathematical Modeling'
title_zh: 终端式数学建模基准：首个智能体可验证数学建模评测集
authors:
- Xiaojun Wu
- Cehao Yang
- Xuhui Jiang
- Chengjin Xu
- Jia Li
- Jian Guo
affiliations:
- IDEA Research
- The Hong Kong University of Science and Technology (Guangzhou)
- DataArcTech Ltd.
arxiv_id: '2611.08237'
url: https://arxiv.org/abs/2611.08237
pdf_url: https://arxiv.org/pdf/2611.08237
published: '2026-11-05'
collected: '2026-11-08'
category: Eval
direction: Agent 评估 · 可验证数学建模基准
tags:
- Agent
- Benchmark
- Mathematical Modeling
- Verification
- LLM
- Evaluation
one_liner: 首个将完整竞赛级数学建模任务 Agent 化、可验证化的终端基准，方向感知评分与两层可行性校验，开源模型接近闭源。
practical_value: '- 可迁移到推荐/广告 Agent 数值策略离线评估：方向感知单边评分避免惩罚优于人工基线的策略（如自动调参、出价、创意生成），让“超越优秀历史方案”不会被负向评分，这对评估
  LLM 生成改进方案特别有用。

  - 两层可行性验证：程序化 gate 先筛明显违反业务规则的结果（如预算、ROI、库存约束），再用形式化或规则引擎做硬校验；不可行策略直接清零，可防止 Agent
  输出看似合理但不可执行的推荐。

  - 多参考评分 panel：对生成式推荐或文案评估，使用多个人工/历史最优答案作为参考集而不是单一 ground truth，减少偏差，提升排序稳定性。

  - 低成本模型结论：2.54 美元开源模型接近强闭源模型（59.81% vs 64.58%），可作为离线评估/轨迹采集的替代，降低大规模 Agent 迭代成本。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：数学建模将开放问题转化为假设、模型、解和建议，结果必须兼具数值接近可信参考和物理可行性；现有基准要么只评分解题片段，要么用 LLM 裁判改报告，数值未经校验。

**方法关键点**：覆盖 18 道 2023–2025 CUMCM/MCM 真实赛题，在容器化终端提供原题、官方附件与图表；Agent 输出一个 JSON artifact，只对最终问题的数值核心评分，参照特等奖论文复现。两个关键设计：方向感知单边评分，击败锚点不被扣分；两层可行性验证——程序化 gate 覆盖 6 类可判定不变式，另加 624 条 Lean4 义务，不可行答案硬性清零。每个任务用多位人类特等奖论文组成的 panel 作参考，而非单一报告。

**关键结果**：7 个多模态模型 ×3 种子中，最强 multi-reference O-EVAL 达 64.58%，$2.54 开源模型为 59.81%，仅需 1/100 成本。基准将数学建模的数值核心变成可复现、机器可检查的信号，用于评估长程建模能力并收集 agent 轨迹。
