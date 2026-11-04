---
title: 'MoLRSI: A Recursive Self-Improving AI agent for Molecular Discovery'
title_zh: MoLRSI：用于分子发现的递归自改进AI智能体
authors:
- Yikun Zhang
- Xiwei Cheng
- Mingze Yuan
- Yu Zhang
- Brian Shim
- Aarti Krishnan
- Daniel Rosen
- Kunyang Sun
- Yingze Wang
- Zhenfeng Deng
arxiv_id: '2610.39714'
url: https://arxiv.org/abs/2610.39714
pdf_url: https://arxiv.org/pdf/2610.39714
published: '2026-10-29'
collected: '2026-11-04'
category: Agent
direction: Agent 递归自改进搜索策略
tags:
- AI agent
- molecular discovery
- recursive self-improvement
- workflow optimization
- multi-objective
- cross-task memory
one_liner: MoLRSI通过工作流/架构优化与跨任务记忆递归改进搜索策略，抗生素命中率15.9%超专家流程
practical_value: '- 把推荐/搜索策略搜索本身视为可优化的 workflow，用 execution feedback 和历史任务结果更新策略生成器，做
  recursive self-improvement，而不是只自动化固定流程。

  - 建立跨任务记忆：记录不同 campaign 的 workflow 性能与 refinement 结果，作为 few-shot exemplars 或偏好数据蒸馏到
  meta-policy，帮助新任务冷启动。

  - 多目标权衡：显式把 CTR、覆盖率、新颖性等竞争目标转成多目标 scorer，并在每一轮根据线上/离线反馈调整权重，避免固定单目标导致策略退化。

  - 对 Agent 开发：将“设计和调优 workflow”变成可递归优化的环节，LLM 提出 workflow，执行器返回 score + failure trace，再用
  trace finetune/更新 prompt 或 policy，可迁移到 GenRec 的 Semantic ID 搜索等场景。'
score: 7
source: huggingface-daily
depth: abstract
---

动机：分子发现需要在巨大组合空间中平衡抗菌活性、毒性、新颖性等冲突目标，现有 AI agent 多自动化专家固定流程，但不会根据任务经验优化流程本身。

方法：MoLRSI 将“搜索策略”作为可递归改进对象，包含工作流生成/优化、模型架构搜索和跨任务记忆。每轮 workflow 在训练/筛选库上执行，得到性能与反馈；refinement 结果和执行反馈写入记忆，指导后续工作流的生成与策略更新，形成 self-improving loop。

结果：抗生素筛选中，MoLRSI 在相同训练数据和筛选库下实验命中率 15.9%，高于专家流程 8.7%；de novo peptide-MHC binder 设计中产生 8 个实验验证命中，且对靶点优先结合，对照 Claude Science 完全失败。
