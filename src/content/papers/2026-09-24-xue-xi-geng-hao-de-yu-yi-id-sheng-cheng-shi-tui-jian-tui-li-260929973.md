---
title: Learning Better Reasoning for Generative Recommendation with Semantic IDs
title_zh: 学习更好的语义 ID 生成式推荐推理
authors:
- Mengdan Zhu
- Yufan Zhao
- Sophie Di
- Yao Zhao
- Tao Di
- Yulan Yan
- Sridhar Iyer
- Liang Zhao
affiliations:
- Emory University
- Microsoft
- Cornell University
arxiv_id: '2609.29973'
url: https://arxiv.org/abs/2609.29973
pdf_url: https://arxiv.org/pdf/2609.29973
published: '2026-09-24'
collected: '2026-09-27'
category: GenRec
direction: 生成式推荐 · Semantic ID 推理优化
tags:
- Generative Recommendation
- Semantic IDs
- Reasoning
- Reinforcement Learning
- Best-of-N
- GRPO
one_liner: 通过 Best-of-N 筛选高预测效用推理轨迹，并用排序感知 RL 持续优化生成式推荐推理
practical_value: '- 在生成式推荐 SFT 阶段，不要直接使用教师模型生成的 CoT，而是对每个样本采样多条推理轨迹，计算其对 ground-truth
  item 的增量似然 Δ=log p(y*|h,z)-log p(y*|h)，只保留 Δ 最高且为正的轨迹。业务中可显著提升 top-1 和 NDCG，且成本可控（N=5
  即可）。

  - RL 阶段用 catalog 前缀树约束 beam search 生成合法 item ID 排序列表，奖励使用 NDCG@10 而非 exact match：NDCG
  能区分“目标排在 rank 2 还是 rank 100”的推理质量，让策略学会把目标推到更靠前位置；GRPO 组内归一化在 16 条/样本的规模下稳定有效。

  - SID 与语言对齐是推理的前置条件：混入 SID↔title 双向翻译、历史序列 narrative 以及通用推理语料，可防止 LLM 在推荐任务上丧失通用能力，并让
  Semantic ID 获得语义/行为接地。

  - 推理长度会随 RL 自动缩短，无需长度惩罚；有效的推荐推理是压缩到对排序最有用的信息，而非越长越好。这提示在业务中可以把“推理质量”定义为其带来的 ranking
  gain，而不是可读性。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

## 动机

生成式推荐用 Semantic ID 将 item 检索变为序列生成，进一步引入显式 CoT 推理可以总结用户兴趣、推断偏好转移。但推理并非天然有益：对同一条历史，不同推理轨迹可能提取不同信息，甚至互相冲突；不可靠的推理会误导后续 SID 生成，并且若在 SFT/RL 阶段不加区分地学习，会强化虚假推理模式。核心问题是如何从模型自身生成中识别并进化出对下游排序真正有用的推理轨迹。

## 方法关键点

**三阶段 Evo-Rec 框架：**
1. **SID-Language 对齐**：将新引入的 Semantic ID tokens 与文本语义和用户行为对齐。包含 SID history→SID、SID history→title、title history→SID、title history→title、title–SID 双向翻译、教师生成的 SID–text 交错数据，并混入通用 reasoning 语料保持 LLM 能力。
2. **Best-of-N Rejection Sampling SFT**：对每个历史采样 K 条候选 CoT，用冻结模型计算每条轨迹对 ground-truth item 的增量预测效用 Δ=log p(y*|h,z)-log p(y*|h)。只保留 Δ 最高且 >0 的轨迹做 SFT。关键：收益来自对候选按效用排序，而不是简单拒采。
3. **Ranking-aware RL**：策略采样 G 条推理，每条推理先通过 catalog 前缀树约束的 beam search 生成有序 top-B item 列表，用 ground-truth 的 rank 构造 NDCG@10 reward，再用 GRPO 更新策略。奖励同时包含检索命中与排序折扣，比 exact match 提供更细粒度信号。

## 关键实验

在 Amazon Review 的 Games、Office、Industrial 三个数据集上，对比判别式（Caser、GRU4Rec、SASRec）、经典生成式（TIGER、HSTU、LETTER、LC-Rec）、推理增强（ReaRec、R2ec、SIDReasoner）基线。Evo-Rec 在所有指标上一致最优。Games 上 R@5 从 0.0710 提升到 0.0847（+19.3%），N@10 从 0.0563 提升到 0.0746（+32.5%），且 NDCG 增幅高于 Recall，说明排名位置被有效前移。消融显示 Best-of-N 显著优于随机/简单拒采；beam search 优于 constrained sampling；纯 NDCG 奖励优于 Exact Match、Prefix Match 和 NDCG+Recall。推理长度随 RL 训练下降而性能提升，表明有效推理更依赖信息质量而非长度。

## 最值得记住的一句话

推荐推理的关键不是生成更多推理，而是根据其带来的下游排序收益来选择、优化并持续进化推理轨迹。
