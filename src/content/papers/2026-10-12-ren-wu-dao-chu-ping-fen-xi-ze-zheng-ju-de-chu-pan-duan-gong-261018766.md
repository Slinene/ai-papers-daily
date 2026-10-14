---
title: 'Rubrics from the Task, Verdicts from Evidence: Pointwise Rubric Rewards with
  Tool-Augmented Judges'
title_zh: 任务导出评分细则，证据得出判断：工具增强的逐点 Rubric 奖励模型
authors:
- Tianci Liu
- Haoyu Wang
affiliations:
- University of Tennessee
- University at Albany
arxiv_id: '2610.18766'
url: https://arxiv.org/abs/2610.18766
pdf_url: https://arxiv.org/pdf/2610.18766
published: '2026-10-12'
collected: '2026-10-14'
category: LLM
direction: LLM 奖励模型与 Rubric 评估
tags:
- Rubric Reward Model
- RLHF
- Tool-Augmented Judge
- Preference Accuracy
- Policy Optimization
- Distillation
one_liner: 提出 ReVeR，从指令本身推导评分细则并用工具增强逐点评分，通过标签盲蒸馏训练，超越 pairwise rubric RM
practical_value: '- **从指令本身推导评分细则，避免响应偏置**：在电商推荐/Agent 评测中，构建 reward 或评估模型时，不要仅从已有候选回答归纳准则，先从任务指令或用户需求出发生成硬规则和分级原则，提升评估的泛化性与公平性。

  - **工具增强判官提升机械约束处理能力**：对于需要精确标量、结构化约束或事实核验的推荐文案、搜索改写、Agent 动作评估，让 judge 主动调用工具（如代码执行、数据库查询）从证据得出判断，而非单纯阅读，可显著提高指令遵循类指标。

  - **标签盲蒸馏降低数据成本**：用偏好标签仅过滤教师模型输出，生成大量 rubric-reasoning 与 judging 轨迹，可复用到需要大量过程监督数据的奖励模型训练中，适合资源有限的业务场景。

  - **偏好准确率与下游策略效用不必然一致**：部署奖励模型时不要只盯偏好准确率，需联合下游生成策略的线上指标和 rubric fidelity 联合验证，尤其在
  RL 微调后可能出现“高分低质”脱节。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 rubric-based 奖励模型（RM）多从观察到的候选响应中归纳评分准则，引入响应偏置；判官仅靠阅读难以处理机械约束；pairwise 判官只给相对偏好，不便直接用于策略优化。

**方法关键点**：提出 ReVeR，包含两个组件：①从指令本身推理生成硬规则和分级原则，而非依赖候选响应；②工具增强判官独立评估响应，从证据得出判断。二者通过 label-blind distillation 训练：偏好标签仅用于过滤教师模型输出，得到 ReVeR-Traces 大规模轨迹数据集（rubric-reasoning 和 judging）。

**关键结果**：ReVeR 在平均偏好准确率上超过 pairwise rubric RM，尤其在指令遵循类任务上优势明显；在 test-time scaling 和下游策略优化上也更优。进一步发现：generator RL 提升偏好准确率但降低 rubric fidelity；更高偏好准确率不必然带来更好下游策略，表明 rubric fidelity、偏好准确率和下游效用是不同属性。
