---
title: 'DualEvolve: Dual-Level Self-Evolution of Mechanism and Orchestration for Recommendation'
title_zh: DualEvolve：推荐系统机制与编排的双层级自演化
authors:
- Tianqi Gao
- Chenxu Wang
- Wenxuan Yang
- Yueqi Mou
- Biao Tang
- Ming Liu
- Peng Yan
affiliations:
- Independent Researcher
- Meituan
arxiv_id: '2611.04439'
url: https://arxiv.org/abs/2611.04439
pdf_url: https://arxiv.org/pdf/2611.04439
published: '2026-11-03'
collected: '2026-11-04'
category: RecSys
direction: LLM Agent 自进化推荐 · 双层优化
tags:
- Self-Evolution
- Recommender Systems
- LLM Agents
- Thompson Sampling
- Process Reward
- Harness Optimization
one_liner: 同时演化推荐模型代码和 Agent 编排，用过程质量反馈与 Thompson 采样在 64 个比较中全部优于现有自演化方法
practical_value: '- 将「任务指标」和「过程质量」分离：模型晋升只依赖固定验证分数和噪声/成本门控，Agent 编排更新只看过程质量（决策质量、实验严谨性、分析深度、新颖性），避免只追最终分数导致的过拟合或错误方向。

  - 推荐模型 AutoML 或 LLM 自动调参中，采用两档 fidelity screening：低预算粗筛候选，高预算再验证，配合 noise floor
  和 cost coefficient 决定是否晋升，能明显降低 full-budget 训练次数。

  - 外层编排动作选择用 Thompson sampling 从 KEEP / EDIT HARNESS / EDIT SKILL 中采样，下一轮过程 reward
  残差更新后验；比确定性 argmax 更能保持探索，实现简单、可复用。

  - 把任务特定经验（inside wiki）与外部论文先验（outside wiki）解耦，迁移时只搬 evolved harness/skill rules，不搬原始日志，便于跨业务/数据集复用；同时固定评估器和晋升规则，防止
  LLM agent 搜索时篡改评估逻辑或利用捷径。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
LLM agent 正在越来越多地自动化推荐系统的开发循环，但现有方法主要依据候选模型的最终任务分数选择更新，缺少对实验过程质量的独立信号。例如，负结果后正确调整方向与忽略失败重复相似修改，可能在模型分数上没有区别，但长期搜索效率差异巨大。因此需要同时改进推荐模型和 Agent 本身的工作流。

## 方法关键点
- **内层机制演化**：固定 GLM-5.2 的 diagnoser、proposer、coder、analyst、refiner 五个角色，对推荐模型及训练代码进行诊断、假设、实现和修正。候选先经低精度筛选，再经高精度验证。
- **固定晋升门控**：候选只按验证分数增益与训练成本决定是否替换 incumbent，阈值包含噪声地板和成本系数，防止噪声或慢训练候选被误晋升。
- **外层编排演化**：每轮结束后用过程质量 reward 评估实验过程，包括决策质量、实验严谨性、分析深度和新颖性；用 Thompson sampling 从 KEEP / EDIT HARNESS / EDIT SKILL 中选择动作，下一轮过程 reward 残差更新动作后验。
- **记忆结构**：inside wiki 存储任务特定候选记录和经验教训，outside wiki 提供离线论文知识快照。
- **奖励完整性**：验证评估器和晋升规则固定，Agent 不可编辑；静态审计防止访问评估数据。

## 关键实验
在 MovieLens-1M 和 Amazon Reviews 2023 的 CDs&Vinyl、Baby、Software 三个子集上，结合 NCF、NGCF、SASRec、GRU4Rec 共 16 个 setting、64 个 setting–metric 比较。DualEvolve 在全部 64 个比较中测试均值高于 Base、OpenEvolve 和 DeepEvolve；相对 DeepEvolve 的宏平均提升为 HR@5 +7.6%、NDCG@5 +9.0%。消融显示移除 inside wiki、替换 Thompson sampling 为确定性 argmax、固定规则不更新、或用任务增益替代过程 reward 都会带来下降，尤其 Task-Gain 在 Baby/NGCF 上下降最多。迁移实验中，从 Baby/NGCF 或 Baby/NCF 演化出的 harness/skill 规则迁移到 Software/NGCF，显著优于不迁移。成本方面，token 使用比 DeepEvolve 少 49–63%。

最值得记住：**任务分数决定模型是否晋升，过程质量决定 Agent 下一轮怎么改，二者分离是防止自演化推荐系统奖励黑客的关键。**
