---
title: 'The Interaction Tax: When Communication Erases Diversity in Multi-Agent Teams'
title_zh: 交互税：多智能体团队中通信如何抹除多样性
authors:
- Summer Eunhyung Ann
- Haokun Liu
- Chenhao Tan
affiliations:
- University of Chicago
arxiv_id: '2608.23541'
url: https://arxiv.org/abs/2608.23541
pdf_url: https://arxiv.org/pdf/2608.23541
published: '2026-08-24'
collected: '2026-08-25'
category: MultiAgent
direction: 多智能体协作的多样性坍缩与交互税
tags:
- Multi-agent LLM
- diversity collapse
- interaction tax
- MoA
- verifier-scored optimization
- ensemble diversity
one_liner: 完整方案交换会让异构模型解在一轮内趋同并抹掉多样性，独立生成与可定位修复的 critique 才更有效
practical_value: '- 在多候选生成/策略搜索（广告创意、推荐解释、query 改写等）中，优先用多模型独立提案 + 打分器选择/合成（MoA 式），不要让
  agent 互相阅读完整候选输出；这能在预算匹配下保留多样性并避免一轮收敛。

  - 若必须引入 critic/refiner，把 critique 压缩成可验证的具体错误和修复建议（如硬约束违反、价格违规、敏感词、缺失卖点），不要传递完整候选；对容易定位和修复的约束有效，对需要复杂推理的错误可能有害。

  - 异构模型组合前先做策略多样性诊断：检查不同模型/agent 是否真的产生不同结构或策略，还是某个模型总是输出固定高分退化解；不要只看模型家族数量，要看候选聚类和行为模式覆盖。

  - 多 Agent 不一定优于单 Agent Best-of-N；在资源受限的搜推广系统中，先建设强单模型 + 多次采样 + verifier 选择，按需再加轻量
  critique 或选择性信息共享，避免直接上 chain/debate 全量交互。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

## 动机
多智能体 LLM 系统常用于优化类任务，核心假设是不同模型可以发现不同解。但现有文献对交互是否有效存在矛盾：辩论、critique 循环、MoA 等报告收益，而另一些研究表明在相同预算下交互只增加成本。论文指出关键区别是是否让 agent 读取完整候选方案。完整输出交换会让不同模型家族的方案迅速趋同，抹掉多样性，作者称之为 interaction tax。

## 方法关键点
- 在 11 个 verifier-scored 优化任务上测试，包括 Circle Packing、TSP、Erdős、Molecule QED、Knapsack、3AP-Free 等；确定性 verifier 返回标量得分，区分可见 dev evaluator 与隐藏 evaluator。
- 比较 10 种配置：4 个单智能体基线（Single-Shot、Best-of-N、Self-Refine、VGS）和 6 个多智能体工作流（Homo-Chain、Cross-Chain、MAgICoRe、Debate、HPE、MoA）；模型使用 Claude Sonnet 4、GPT-4o、Gemini 2.5 Flash。
- 指标为 MEG（对比最强单智能体基线）和 MIG（对比同 agents 并行独立生成），并用 2×2 因子 diversity × synthesis 检验多样性优势；同时测量 pairwise solution distance 和约束可行性。

## 关键结果
- 每个同模型团队在至少一个任务上得分为 0，而异构团队从不全崩；2×2 因子中 diversity coefficient = +0.188（CI [+0.073, +0.299]，p<0.001），但移除 Erdős 任务后跌至 +0.014，多样性收益是任务依赖的。
- 完整方案交互导致异构团队损失：Chain/MAgICoRe/Debate 的同模型 MIG 为正（+0.051/+0.044/+0.012），异构 MIG 转负（-0.024/-0.035/-0.078），P(same>div) ≥ 88%；MoA 在异构下仍保持 +0.016。
- 多样性坍缩发生在一轮 full-solution exchange：平均 pairwise distance 从 0.315 降到 0.229；5/7 任务上 synthesis 复制最高分 proposer 输出 ≥80%。
- critique 只在错误易定位时有效：Knapsack-50 上 diverse Debate 可行性 10/10 vs same 2/10；3AP-Free-100 上 diverse Debate 0/10 vs same 6/10。
- 没有任何配置在 aggregate MEG 上可靠超过最强单智能体基线；MoA 是唯一 CI 含 0 的配置。

## 最值得记住的一句话
多智能体性能取决于 agent 之间交换什么信息以及何时暴露，而不是 agent 数量；完整候选解交换是弱默认，独立生成 + 选择性信息才是保留多样性的关键。
