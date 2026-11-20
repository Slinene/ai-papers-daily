---
title: Learning Generative Ranking Policies for Whole-Page Optimization
title_zh: 学习整页优化的生成式排序策略
authors:
- Chen Qiu
- Zhigang Hua
- Qi Xu
- Jizhe Zhang
- Sha Hua
- Ren Mao
- Luke Simon
affiliations:
- Meta Platforms, Inc.
arxiv_id: '2611.25527'
url: https://arxiv.org/abs/2611.25527
pdf_url: https://arxiv.org/pdf/2611.25527
published: '2026-11-19'
collected: '2026-11-20'
category: GenRec
direction: 生成式重排 · 整页策略优化
tags:
- Whole-Page Optimization
- Generative Re-ranking
- Policy Improvement
- Recommendation
- Beam Search
one_liner: 提出整页策略提升，用当前生成器补全候选页面并按完整页面得分重加权逐位目标，训练生成式重排器
practical_value: '- 在电商/信息流混排中，需要同时优化原生与广告条目、满足间距约束时，可以训练一个生成式重排器：对每个候选用当前生成器补全剩余页面，用完整页面得分估计
  Q(s,a)，再重加权当前位置概率，替代在线 beam search，降低延迟且无需 evaluator 查询。

  - 方法中的 partial-scoring 技巧：只对 top-κ 概率候选和随机探索候选进行完整页面评分，保持未评分候选概率不变，能大幅减少训练计算，同时保留探索性，适合候选池大的业务场景。

  - 使用当前生成器进行 rollout 构造 target 是关键，冻结旧生成器会导致质量下降；工程实现上可每轮更新生成器并重新采样数据，形成自我提升循环，避免固定目标过时。

  - 生成器训练完成后用贪心解码即可达到或超过宽度 32 的 prefix-score beam search，且无 evaluator 查询，生成时间显著更低，适合线上低延迟服务。'
score: 9
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：推荐页面作为整体被消费，item 间存在竞争与互补，最佳页面不是单个最优 item 的简单拼接。整页优化需联合选择与排序，但可行页面组合爆炸，无法枚举；在线 evaluator 搜索成本高。现有生成式重排方法要么对采样页面所有选择使用同一页面级信号，要么模仿固定目标列表，随着生成器改进目标不变，导致次优。

**方法关键点**：
- 提出 whole-page policy improvement，交替训练：每轮固定当前生成器 π_k，采样页面得到 partial pages；对每个 partial page 的候选，放置候选后让 π_k 补全剩余页面，用 evaluator 给完整页面评分，得到 Q(s,a) 估计。
- 按公式 q_k(a|s) ∝ π_k(a|s) exp(Q(s,a)/τ) 重加权当前位置概率，得到逐位目标分布；用交叉熵拟合参数化生成器；更新后的生成器下一轮构造新数据与目标。
- partial-scoring：只对被选中的候选集合（top-κ 概率 + 随机探索）进行完整页面评分，保持未评分候选概率不变，减少计算。
- 理论保证：精确更新非减页面分数，重复精确 full updates 收敛到最优页面分数（初始生成器支持集内）。
- 服务时贪婪解码，无 evaluator 查询。

**关键实验**：
- 数据集：KuaiRand-1K（多目标选择与排序，L≤15/28/54）、RL4RS-SeqSlate（约束重排，L=18/27/36）、工业内容流混排（L≤20）、合成基准（已知最优页面）。
- 对比 baseline：生成式推荐 GoalRank、DeGRe、GFN4Rec、HAC，RL 算法 PPO、TD3N、GRPO。
- 结果：KuaiRand-1K 平均提升 34.35% vs 最强 baseline 32.75%；RL4RS 平均提升 7.09% vs 6.43%；工业数据集提升 13.92% vs 12.75%。与 prefix-score beam search 对比，生成器贪心解码在全部宽度和设置下得分更高，无 evaluator 调用，生成时间显著更低（工业 0.075 ms/page vs width32 30.8 ms/page）。合成基准达到 97.16% 最优，页面上下文贡献最大（22.15%），说明优势来自整页决策。消融显示完整页面评分优于仅候选自身分数，用更新后生成器构造数据优于冻结 π0。

**最值得记住的一句话**：用当前生成器补全候选页面并按完整页面得分重加权当前位置目标，迭代自我提升，替代在线 beam search。
