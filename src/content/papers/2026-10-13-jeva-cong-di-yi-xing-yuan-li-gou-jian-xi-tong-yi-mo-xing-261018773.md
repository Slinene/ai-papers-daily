---
title: 'Jeva: System One Models from First Principles'
title_zh: Jeva：从第一性原理构建系统一模型
authors:
- Qi Li
- Xinchao Wang
affiliations:
- National University of Singapore
arxiv_id: '2610.18773'
url: https://arxiv.org/abs/2610.18773
pdf_url: https://arxiv.org/pdf/2610.18773
published: '2026-10-13'
collected: '2026-10-14'
category: LLM
direction: LLM 决策原生架构 · 系统一模型
tags:
- System One
- Decision Architecture
- Cacheable
- Null Detection
- Permutation Invariance
- LoRA
one_liner: 提出 Jeva 决策原生架构，解耦候选编码与请求判断，实现空结果感知、置换不变、候选可扩展与跨请求缓存
practical_value: '- 候选库（商品/广告/工具/标签）用独立 encoder 离线编码成 option memory，在线请求只做 state refinement，尤其适合候选项重复率高的推荐/广告检索场景；set
  cache + hybrid cache 可大幅降低 p50 延迟。

  - 输出层 factorize 为 coverage gate + conditional softmax：在推荐/广告中区分“无可用商品/不投放”和“候选间排序”，避免直接
  softmax 的 logK 先验，提升拒答与空结果判断。

  - 候选顺序不敏感：用 permutation-equivariant aggregation 天然保证重排商品/工具候选不翻转决策，无需数据增强或一致性 loss。

  - 用 LoRA 适配大模型做 decision head，统一 Choice/Noul/Score 接口，支持多任务（是否推荐、选哪个、打分）共用同一决策栈。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
系统一模型用 typed output 做低延迟决策，但现有联合编码把 request 和 candidates 当序列输入，存在候选顺序敏感、输出空间固定、无法区分“无答案”与“候选间不确定”、重复计算候选表示等问题。工具/文档/标签等候选可复用，需要决策原生架构解耦编码与判断。

**方法关键点**
- 共享 encoder 独立编码 request 和每个 option，得到初始 state 与 option vectors；decision stack 只 refine request state，读 immutable option memory。
- 单 block 用 query 对 option keys 的熵正则注意力聚合证据，更新 state；支持 set-dependent preference reversal。
- 输出分为 coverage gate ρ 与 conditional q：ρ 显式估计是否存在可用候选，避免 flat softmax 的 logK bias；Choice/Noul/Score 统一读法。
- 对称聚合 + shared scoring 实现 permutation-equivariant probabilities；option 语义向量和 layer-wise K/V 投影可跨请求缓存；复杂度与 K 线性。
- 训练用 Qwen3.5-4B，LoRA rank 64，可训练参数 13.37M；混合 typed/intent/verification/reading/large-candidate 课程。

**关键结果**
- Jeva-4B 在 BANKING77 K=8/16 达 92.05/91.62，MASSIVE 90+；Typed Decisions 78.30，接近 InternDecision-4B 的 78.70。
- 16-candidate null detection AUROC 98.66，5.02% FPR 下查全 93.88%；600 个 Choice 候选重排零 flip，mean TV 3.17e-08。
- K=2048 ToolRet 上 69.88% 准确率，超 JevK5 的 67.47%；长度感知 batching 带来 7.85× p50 延迟下降；候选表示复用带来最高 27.86× median speedup。

**最值得记住的一句话**
把候选当成可缓存 memory、request 当成要被 set-conditioned 的 state，是系统一决策正确性和低延迟的结构性解法。
