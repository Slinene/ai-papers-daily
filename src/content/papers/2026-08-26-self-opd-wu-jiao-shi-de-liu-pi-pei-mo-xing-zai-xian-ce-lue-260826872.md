---
title: 'Self-OPD: On-Policy Distillation for Flow Matching Models without Teacher'
title_zh: Self-OPD：无教师的流匹配模型在线策略蒸馏
authors:
- Shiyi Zhang
- Mushui Liu
- Yunze Tong
- Wanggui He
- Siyu Zou
- Jinlong Liu
- Yunlong Yu
- Jian Song
- Hao Jiang
- Pipei Huang
affiliations:
- Tsinghua University
- Zhejiang University
- Alibaba Group
arxiv_id: '2608.26872'
url: https://arxiv.org/abs/2608.26872
pdf_url: https://arxiv.org/pdf/2608.26872
published: '2026-08-26'
collected: '2026-08-29'
category: Training
direction: 流匹配模型对齐 · 无教师自蒸馏
tags:
- Flow Matching
- On-Policy Distillation
- Self-Supervised
- Multi-Objective
- Generative Models
one_liner: 提出无需任务专属教师的在线策略蒸馏框架，将学生自探索转为逐步监督，超越现有 RL 与 OPD 方法
practical_value: '- **无教师自蒸馏思想可迁移到生成式推荐或 LLM 对齐**：业务中训练任务专属教师模型成本高，可借鉴 Self-OPD 的分支自探索机制，让学生模型通过自身多步采样获得优势信号，减少对复杂教师网络的依赖。

  - **多目标奖励融合技巧**：在电商搜索/推荐中常需同时优化点击、转化、多样性等指标，Self-OPD 在 reward 层面融合归一化分数而非在梯度层面直接加权，能缓解目标冲突，可在多目标
  RL 或 LLM 微调中尝试。

  - **分支探索 + 优势加权更新**：生成式推荐或文案生成场景中，可使用类似“确定性基线 + 随机分支”的方式产生多样化候选，通过奖励对比计算优势，再用 pull-push
  目标引导模型，可能提升生成结果的 reward 对齐效率。

  - **工程实现上注意 SDE 候选与方差归一化**：该方法引入 SDE 分支和方差归一化来稳定训练，对于训练不稳定或高方差的 RL 任务有借鉴意义，但需注意计算开销翻倍。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 on-policy distillation (OPD) 依赖任务专属教师模型，训练成本高，且师生分布差异会导致生成轨迹上的误差累积。流匹配模型的对齐需要更高效的监督信号。

**方法关键点**：Self-OPD 完全去掉教师，在每个 timestep 将确定性下一状态预测分支为 K 个随机 SDE 候选，并用 ODE 采样器 rollout，通过奖励对比确定性自参考基线获得归一化优势。优化时采用 all-branch pull-push 目标：高优势分支吸引学生，低优势分支排斥，同时引入方向感知衰减和 SDE 方差归一化。多目标对齐直接在 reward 层融合归一化分数，避免梯度冲突。

**关键结果**：在单一和混合奖励基准上，Self-OPD 无需任务专属教师即可超越之前的 RL 和 OPD 方法。
