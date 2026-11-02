---
title: 'Search When Needed, Proceed When Reliable: Metacognitive Reliability Supervision
  for Efficient Agentic Search'
title_zh: 需要搜索时搜索，可靠时继续：面向高效智能搜索的元认知可靠性监督
authors:
- Minhao Sun
- Zhijing Wu
- Xian-Ling Mao
affiliations:
- Beijing Institute of Technology
arxiv_id: '2610.41738'
url: https://arxiv.org/abs/2610.41738
pdf_url: https://arxiv.org/pdf/2610.41738
published: '2026-10-30'
collected: '2026-11-02'
category: Agent
direction: Agentic RAG 搜索决策强化学习
tags:
- Agentic Search
- RAG
- Process Reward
- Uncertainty Estimation
- GRPO
- Metacognition
one_liner: 用局部结论的序列不确定性估计可靠性，为搜索/不搜索决策构建过程奖励，在 GRPO 中提升搜索效率与准确率
practical_value: '- 将局部结论的 sequence uncertainty 作为可靠性信号，可用于对话推荐/购物助手中判断模型对中间结论的自信程度，决定是否调用商品知识库、搜索或
  RAG；无需额外标注，推理时零开销。

  - 对“搜索/不搜索”决策分别设计 process reward：不搜索时奖励高于校准阈值的可靠性，搜索时奖励检索前后可靠性的增量，而非只看最终答案是否正确；这能直接迁移到
  Agent 工具调用策略的强化学习训练。

  - 用 matched probes 估计 counterfactual reliability change，可推广到其他工具调用：固定同一状态，比较有/无工具返回结果的可靠性差异，作为工具价值的无偏监督。

  - 实验结果提供可复用结论：该策略在 single-hop 查询上减少约 20.9% 搜索调用，multi-hop 上增加 6.6%，说明可按问题复杂度动态分配检索/工具调用，适合电商搜索中查询类型分流的成本优化。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

Agentic RAG 中，模型在每个中间步骤都要决定是继续用当前参数知识推理，还是发起搜索获取外部证据。仅用最终答案正确性或轨迹级反馈存在信号模糊：正确答案可能掩盖过度搜索或侥幸猜对；有用检索未必直接改善最终答案。需要区分“结论碰巧正确”与“当前信息能否可靠推出结论”，从而直接监督搜索决策。

## 方法关键点

- **可靠性估计**：用 sequence uncertainty（生成 conclusion tokens 的平均负对数似然）作为局部结论可靠性代理。先用 frozen backbone 在 50k 搜索状态上每个状态采样 32 个结论，拟合 uncertainty→accuracy 的经验映射 f_m。
- **No-search 决策评分**：Current-State Reliability Score S_cur = R_ns - b_m，其中 b_m 是校准参考；鼓励模型在可靠时继续，不可靠时不要不搜索。
- **Search 决策评分**：Search-Action Reliability Score ΔR = R_evid - R_cf，通过 matched probes 比较有/无检索证据时的可靠性变化，奖励真正带来可靠性增益的搜索。
- **过程奖励与训练**：将 rollout 内所有动作得分平均作为 process reward，叠加 answer + format reward 进行 GRPO 训练；推理时不增加任何 probe 或校准开销。

## 关键实验

在 NQ/HotpotQA 上训练，评估 7 个 QA 基准。Qwen2.5-7B 达到 avg CEM 69.3，超过最强基线 HiPRAG 2.1 点，且七个数据集全部提升；全量对比中搜索调用 overall 减少 6.8%，其中 single-hop QA 减少 20.9%，multi-hop QA 增加 6.6%，显示任务自适应搜索分配。跨骨干（Qwen2.5-3B、Llama-3.2-3B）也有稳定提升；ablation 证明双评分组合和 empirical mapping 贡献显著。

## 最值得记住的一句话

区分“结论是否碰巧正确”与“当前信息能否可靠推出结论”，用检索前后可靠性的变化直接监督搜索决策，而不是依赖最终答案正确性。
