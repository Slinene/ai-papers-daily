---
title: 'SEAL: Synergistic Co-Evolution of Agents and Learning Environments'
title_zh: SEAL：智能体与学习环境的协同共进化
authors:
- Yihao Hu
- Zhihao Wen
- Xiujin Liu
- Pan Wang
- Xin Zhang
- Wei Wu
affiliations:
- Ant Group
- Westlake University
- University of Michigan–Ann Arbor
- University of Science and Technology of China
arxiv_id: '2605.24426'
url: https://arxiv.org/abs/2605.24426
pdf_url: https://arxiv.org/pdf/2605.24426
published: '2026-05-22'
collected: '2026-05-27'
category: Agent
direction: 智能体与环境协同进化训练
tags:
- LLM Agents
- Tool Use
- Environment Co-evolution
- Failure Diagnosis
- GRPO
- Self-improvement
one_liner: 利用可执行验证器为基础的失败诊断作为共享信号，协同进化训练界面与策略，显著提升低资源多轮工具使用学习
practical_value: '- **训练时界面增强而不改评估基准**：在工具调用训练中，可对工具描述进行轻量注解（如标注必填参数、枚举值范围），并针对失败返回结构化修复提示，不改变API或评估协议，为强化学习提供更密集的监督信号，类似推荐系统中细化反馈。

  - **失败诊断驱动的重要性加权**：在GRPO等策略优化中，利用可执行规则将失败归类（参数错误、工具缺失等），根据故障可归因性分配轨迹权重，优先学习有明确修正方向的失败，可在电商多轮Agent训练中加速收敛、提升样本效率。

  - **闭环式环境-策略协同迭代**：收集当前策略的失败分布（失败画像），动态调整训练界面（暴露约束提示、错误恢复建议），形成“策略暴露短板→环境针对性辅导→策略内化”的闭环，适合需要快速适应新任务或新工具的Agent系统。

  - **低资源高效起步**：仅用400个训练样本便取得显著提升，适用于标注数据稀缺的业务场景（如新工具上线、冷启动），可快速验证Agent能力边界。'
score: 8
source: huggingface-daily
depth: full_pdf
---

### 动机
LLM智能体的自进化通常只优化策略或只调整环境，导致训练时学习环境无法追踪策略能力前沿，反馈信号静态且弱关联（Agent-Environment Misalignment）。在多轮工具使用中，稀疏的二元奖励难以定位失败根源，样本效率低下。

### 方法关键点
- **可执行验证基础失败诊断**：利用执行轨迹中的解析错误、schema校验、状态变化等可执行证据，将每轮交互标注为具体失败类型（如参数不匹配、工具缺失、恢复失败等），不依赖LLM评判，保持诊断客观且可复现。
- **训练界面协同进化**：基于全局失败画像，在训练时对工具描述追加约束说明（必填、枚举值）、将底层错误转化为结构化修复提示，但不改变工具语义或评估协议，只在训练期暴露。
- **诊断指导的advantage加权**：根据不同失败类型的可归因性和修正引导价值设定权重（如无效调用权重高，最终回答错误权重低），缩放GRPO的优势项，使优化更聚焦于有明确改进方向的轨迹。
- **闭环迭代**：收集rollout → 失败诊断 → 聚合失败画像 → 更新训练界面 → 加权策略优化，反复循环。评估时移除所有训练期增强，与标准RL同等条件对比。

### 关键实验结果
- 在BFCL V3多轮工具使用集上，仅用400样本训练，Qwen2.5-7B-Instruct的SEAL提升26.25个平均点，超越Vanilla RL 9.50点；ToolACE-2-8B提升14.75点，超出Vanilla RL 8.25点。
- 在BFCL V4和τ2-bench等OOD任务上同样获得正向迁移，展现行为泛化而非过拟合。
- 消融显示环境侧适应与诊断加权互补，全量SEAL优于单侧变体。

### 核心收获
“联合进化训练界面与策略，将失败诊断作为共享信号，能让低资源工具使用学习更聚焦、更高效，这一思路对Agent训练的工程落地具有直接启示。”
