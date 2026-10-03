---
title: 'JevSpawn: Adaptive Agentic Inference through Compositional Action Spaces'
title_zh: JevSpawn：组合动作空间实现自适应智能体推理
authors:
- Haoyang Su
- Weiran Huang
affiliations:
- Fudan University
- Shanghai Jiao Tong University
- Shanghai Innovation Institute
arxiv_id: '2610.00437'
url: https://arxiv.org/abs/2610.00437
pdf_url: https://arxiv.org/pdf/2610.00437
published: '2026-09-29'
collected: '2026-10-03'
category: Agent
direction: Agent 组合动作空间加速推理
tags:
- Agentic Inference
- Jev-style Models
- Compositional Action Spaces
- Parallel Action Spawning
- Branch Selection
- Latency Reduction
one_liner: 通过组合动作空间与并行生成-反馈选择，将 Jev-style 快速概率预测引入自适应 Agent 推理，降低延迟并提升任务性能
practical_value: '- 在电商推荐 Agent 的多轮交互或工具调用中，将离散候选动作（如商品候选、Query 改写选项）编码为有限字段，使用 Jev-style
  概率预测并行生成多个动作候选，替代逐 token 生成，显著降低推理延迟，适合对时延敏感的场景。

  - 利用共享动作结构和前缀缓存（prefix/KV cache）：多个并行分支共享相同上下文前缀时，仅计算一次前缀，减少重复计算；在长会话推荐中可缓存用户历史与系统提示，提升吞吐。

  - 借鉴反馈驱动的分支选择与保留备选：根据环境反馈（点击/转化）对并行候选剪枝，同时保留未选分支以便在后续步骤中恢复，增强推荐策略的鲁棒性，类似多臂老虎机的探索-利用平衡。

  - 无需额外训练，可直接集成现有 LLM Agent 框架，降低工程落地成本。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM agent 逐 token 生成推理和动作，多轮交互导致高延迟与计算开销；Jev-style 模型虽能快速概率预测，但要求预先定义有限动作字段，限制了从自然语言指令中动态派生动作的自主任务求解。

**方法关键点**：JevSpawn 通过组合动作空间连接自然语言任务与有限概率探索。核心包括并行动作生成（parallel action spawning）、反馈驱动的分支选择、表示修订、以及从保留候选中恢复。共享动作结构和模型前缀减少重复生成与上下文计算，无需额外训练。

**关键结果**：在八个 benchmark 任务上，对比七个 agent baselines 和一个 TypeSafe Jev variant，JevSpawn 实现更优的任务性能和更快的导航速度，平均延迟比最快 baseline 低 15.6%。
