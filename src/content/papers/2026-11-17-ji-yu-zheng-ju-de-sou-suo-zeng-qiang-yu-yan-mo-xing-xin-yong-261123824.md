---
title: Evidence-Based Credit Assignment for Search-Augmented Language Models
title_zh: 基于证据的搜索增强语言模型信用分配
authors:
- Wen Wang
- Jindong Wang
- Jiahua Bao
- Tu Yongsiqi
- Yihao Liu
- Junwei He
- Wenkui Fan
affiliations:
- University of the Chinese Academy of Sciences
- Tencent
- Harbin Institute of Technology
- Renmin University of China
- Peking University
arxiv_id: '2611.23824'
url: https://arxiv.org/abs/2611.23824
pdf_url: https://arxiv.org/pdf/2611.23824
published: '2026-11-17'
collected: '2026-11-19'
category: Training
direction: 搜索 Agent RL 信用分配
tags:
- credit assignment
- search-augmented LLM
- GRPO
- evidence potential
- RL training
- multi-hop QA
one_liner: 提出 ECA：用冻结策略在仅问题+文档上的参考答案似然变化构造证据势能，为搜索步提供辅助信用，提升多跳搜索 RL
practical_value: '- 多轮检索/工具调用 Agent 做 RL 时，若只有 terminal reward，可加一个 evidence potential
  辅助信用：冻结策略，输入“问题+已去重检索文档”，teacher force 参考答案的对数似然，作为该步文档效用的代理，无需标注支持文档或训练 process
  reward model。

  - 在困难 query 上 rollout 经常全失败，GRPO outcome advantage 为零，可借鉴 cross-fold normalization：把同组
  rollout 分成两折，用对折统计标准化 evidence return，避免自身稀疏高值 return 被归一化抵消，让失败样本中检索质量差异仍能提供梯度。

  - Novelty gating 很实用：当新一轮检索没有引入新文档 ID 时，将该步正 advantage 截断为 ≤0，能显著降低重复 query 率（42%→25%），可用于电商导购/客服
  Agent 控制冗余搜索，同时保留搜索预算。

  - 信用放置要精确：辅助 advantage 只加到 search 动作（含前置 think 和 query token），不加到最终 answer token。实验显示若只加
  query token 或广播到全部 token，效果都差于 GRPO，说明“决定查什么”的 reasoning token 也需要被奖励。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多轮搜索增强 LLM 用 terminal answer reward 做 RL 时，每个 trajectory 的所有搜索动作共享同一个 outcome advantage，无法区分有用检索与冗余 query；当一组 rollout 全部答错时，GRPO advantage 归零，即使不同 rollout 检索到不同证据也失去梯度。

**方法关键点**
- 提出 evidence-only answer potential Φ(D)：冻结当前 policy snapshot，用 prompt 仅包含 question + 去重文档集 D，teacher-force 最短 canonical answer y* 的长度归一化对数似然，排除 generated thoughts 和查询措辞，隔离文档证据效用。
- 两种 return 构造：ECA-Step 按步 clip Δ 到 [-2,2] 再求和；ECA-Horizon 保持 telescoping horizon gain（终端 potential − search 前 potential），避免 clip 破坏多步证据累积。两者共享 cross-fold normalization、novelty gating、search-local token assignment。
- Cross-fold normalization：每个 question 的 8 个 rollout 拆成 4+4 两折，以对折统计标准化，避免 full-group 归一化下单一高值 return 的 magnitude 被自身均值/方差抵消。
- Novelty gating：当该搜索未引入新文档 ID 时，正 credit 置 0，抑制重复 query；辅助 advantage λ=0.1 只加到 search 动作（含前置 reasoning 与 query token），不污染最终答案。
- 训练：Qwen2.5-3B/7B-Instruct，8,192 题训练池，256 步、每步 32 题 × 8 rollouts，E5-base-v2 检索 Wikipedia18，H=3 搜索预算。

**关键实验**
在 7 个 Search QA 基准共 51,713 测试题上，ECA-Horizon 在 3B 达 38.22 macro EM（vs GRPO 37.19，+1.03 pp），在 7B 达 42.62（vs GRPO 37.82，+4.80 pp），超过 RLOO 与 GiGPO。3B 上 ECA-Horizon 在 97.8% 的全失败 rollout 组中恢复了非零辅助 advantage；重复 query 率从 GRPO 的 42.40% 降至 24.84%。Zero-shot MultiHop-RAG 上 7B 达 89.22 EM（vs GRPO 82.84，+6.38 pp）。

**最值得记住的一句话**
检索类 Agent 的 RL 信用分配，可以用冻结策略在“问题+已检索文档”上的参考答案似然变化构造 evidence-only potential，并将辅助 advantage 仅赋给搜索动作，从而在全失败样本中仍能区分检索质量。
