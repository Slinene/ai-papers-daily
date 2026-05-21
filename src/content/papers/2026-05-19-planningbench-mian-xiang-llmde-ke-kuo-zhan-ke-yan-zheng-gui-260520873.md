---
title: 'PlanningBench: Generating Scalable and Verifiable Planning Data for Evaluating
  and Training Large Language Models'
title_zh: PlanningBench：面向LLM的可扩展、可验证规划数据生成框架
authors:
- Ziliang Zhao
- Zenan Xu
- Shuting Wang
- Hongjin Qian
- Yan Lei
- Minda Hu
- Zhao Wang
- Shihan Dou
- Zhicheng Dou
- Pluto Zhou
affiliations:
- Renmin University of China
- Tencent Hunyuan Team
- Beijing Academy of Artificial Intelligence
- The Chinese University of Hong Kong
arxiv_id: '2605.20873'
url: https://arxiv.org/abs/2605.20873
pdf_url: https://arxiv.org/pdf/2605.20873
published: '2026-05-19'
collected: '2026-05-21'
category: Training
direction: 生成式规划数据 · 可控难度与自动验证
tags:
- planning
- synthetic data
- reinforcement learning
- verification
- LLM training
- constraint-driven
one_liner: 从真实场景抽象出任务-约束分类，通过闭环合成生成可验证规划数据，兼顾评估与强化学习训练
practical_value: '- **可控数据生成范式**：约束驱动合成 pipeline 从真实场景抽象任务-约束分类，可迁移至电商复杂任务（如物流调度、大促排期、库存分配）的规划数据生成，突破固定基准的限制。

  - **可验证奖励设计**：每个实例绑定自动验证清单，同时检查约束满足与目标优化，可作为强化学习 reward，保证 Agent 在长序列决策中保持全局一致性。

  - **奖励确定性至关重要**：偏好确定最优解，避免多个可行解导致奖励信号分散；在训练多目标协调的 Agent 时，应优先构造明确的最优指标以稳定训练。

  - **难度自适应分级**：按约束层级（基础/中等/困难）和状态化约束分档，通过动态调整采样概率实现难度递增，适合生成难度可控的训练集。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
现有 LLM 规划基准多为固定实例集，覆盖范围窄、难度控制粗糙（仅依赖长度或需求数量），且缺乏可扩展的自动生成与验证机制。规划任务需要模型协调时间、资源、约束与长期目标，局部可行未必全局一致，因此亟需一种能按需生成多样化、可验证规划数据的方法，同时支撑评估与训练。

### 方法关键点
- **任务-约束分类体系**：从真实规划场景抽象出 6 大类 30+ 任务类型，每类关联通用、任务特定、状态化三层约束，并划分为基础、中等、困难三个难度等级。
- **闭环合成 pipeline**：Generator 采样任务-约束配置并实例化为问题；Responder 求解；Critic 基于自动验证清单评分。若实例被完全解出，则通过指数移动方式提升中、高难度约束的采样概率，实现难度自适应增强。
- **自动验证清单**：每个实例附带 checklist，覆盖输入条件、资源/时间窗口、输出格式及确定最优解目标，可直接用于评估和强化学习奖励。
- **训练偏好**：优先构造具有确定最优解的实例，以提供清晰、定向的奖励信号，避免因过多可接受解而导致训练不稳定。

### 关键结果
- **评估**：GPT-5.4-xhigh 的 All-pass 仅 63.17%，其他模型均低于 54%，且 Avg-pass 与 All-pass 的差距显著（如 GPT-5.4-medium 的 Avg-pass 90.03% vs. All-pass 58.09%），表明模型常满足局部约束却无法达成全局可行计划。错误分析显示 60%–83% 的失败源于计算/分配错误，而非格式问题。
- **训练**：在 300 个 PlanningBench 实例上进行 GRPO 训练后，Qwen-A3B-30B 在 TravelPlanner 上的平均 All-pass 从 28.85% 提升至 46.86%，ChinaTravel 的 All-pass 从 50.92% 提升至 58.36%；在 Multi-Challenge、IFEval、Collie 等指令遵循基准上综合得分由 38.74% 升至 45.80%。采用确定最优解的 Syn-PlanningBench 比无确定最优的 Syn-NotDetOptimal 训练动态更稳定，增益更显著。

> 确定或明确的最优解能提供更稳定和定向的奖励信号，这对规划导向的强化学习至关重要。
