---
title: 'DARS: Dual-Level Credit Assignment RL with Structured Reasoning for Instruction-Based
  Image Editing'
title_zh: DARS：双层信用分配强化学习与结构化推理的图像编辑框架
authors:
- Haoxiang Cao
- Jiajiong Cao
- Xuanpu Zhang
- Changqian Yu
- Chaoqun Wang
affiliations:
- South China Normal University
- KlingAI Research
arxiv_id: '2608.20161'
url: https://arxiv.org/abs/2608.20161
pdf_url: https://arxiv.org/pdf/2608.20161
published: '2026-08-20'
collected: '2026-08-23'
category: Multimodal
direction: 多模态图像编辑 · 强化学习信用分配
tags:
- RL
- Credit Assignment
- Planner-Renderer
- Instruction-based Image Editing
- Structured Reasoning
- VLM
one_liner: 提出 DARS，在 planner-renderer 图像编辑中通过模块间与模块内双层信用分配，将最终奖励分解为局部监督信号，提升 RL 训练效率
practical_value: '- 在多阶段推荐/Agent 系统中（如 planner-renderer 或召回-排序），用 multi-plan multi-render
  rollouts 估计模块间和模块内的 reward variability，作为 soft module routing 权重，替代简单的联合 RL 端到端更新，可避免梯度分配不公导致模块优化失衡。

  - 让 LLM 输出结构化字段（如意图、对象、动作、约束四字段）而非自由文本，配合 prefix-gated reward 和 token-level advantage
  reweighting，可将最终业务指标（如成交、点击）奖励分解到关键生成的 token，提升生成式推荐理由/query 的可控性和训练效率。

  - 自适应课程：利用 rollout 的平均奖励作为样本难度指标，动态调整训练集中难易样本比例，适合电商场景中长尾/困难样本（如复杂意图 query、小众商品）的针对性优化。

  - 跨模块与模块内双层信用分配框架可扩展到“LLM 生成 query -> 检索器执行”的两阶段系统，解决最终指标不好归因于 query 生成还是检索执行的问题。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：指令化图像编辑采用 planner-renderer 两阶段：VLM 生成编辑计划，扩散模型执行计划。仅用最终图像奖励训练 RL 效率低，因为差结果无法区分应更多优化 planner 还是 renderer；且 planner 的自由推理链难以定位到具体错误 token。为此提出 DARS。

**方法关键点**：
- 跨模块信用分配：通过 multi-plan multi-render rollouts 估计 between-plan 和 within-plan reward variability，用于 soft module routing，确定每个样本更应侧重更新 planner 还是 renderer；rollout 平均奖励作为难度估计，用于自适应课程。
- Planner 内部信用分配：引入四字段结构化推理输出，配合 prefix-gated reward 和 token-level advantage reweighting，将 outcome-level 反馈转化为对 planner 内部关键 token 的局部监督。

**关键结果**：在五个 benchmark 上，DARS 在相同 backbone、数据、奖励模型和 rollout budget 下，超过 Joint RL baseline，且在推理密集型编辑任务上提升最大。
