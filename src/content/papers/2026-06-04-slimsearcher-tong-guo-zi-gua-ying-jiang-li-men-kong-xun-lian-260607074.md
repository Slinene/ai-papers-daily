---
title: 'SlimSearcher: Training Efficiency-Aware Web Agents via Adaptive Reward Gating'
title_zh: SlimSearcher：通过自适应奖励门控训练效率感知的网页智能体
authors:
- Zequn Xie
- Junjie Wang
- Dan Yang
- Jie Feng
- Yue Shen
- Jian Wang
- Jinjie Gu
affiliations:
- Zhejiang University
- Ant Group
arxiv_id: '2606.07074'
url: https://arxiv.org/abs/2606.07074
pdf_url: https://arxiv.org/pdf/2606.07074
published: '2026-06-04'
collected: '2026-06-10'
category: Agent
direction: 网页智能体的效率感知训练 · 自适应奖励门控
tags:
- Web Agent
- Efficiency Optimization
- Reinforcement Learning
- Reward Shaping
- Pareto Frontier
one_liner: 多阶段门控机制统一 SFT 与 RL，在保持或提升准确率的同时将工具调用轮数减少 17%–58%
practical_value: '- **效率与效果解耦的奖励设计**：可借鉴正确性门控 + 自适应效率锚定的结构，将“任务成功”作为硬约束，效率奖励仅作用于正确轨迹，避免为降低成本而输出空泛答案。在电商
  Agent 多步工具调用（查商品、对比价格、调接口）时，能直接压缩不必要的 API 调用，降低延迟和费用。

  - **SFT 阶段的帕累托过滤**：在构建训练数据时，用联合效率分数（工具次数 + token 数）从多个正确轨迹中选出最简路径，引导模型从冷启动就学习高效模式。对生成式推荐语义
  ID 的生成路径或 Agent 决策链的冷启动数据清洗有直接迁移性。

  - **动态基准避免简洁偏差**：在 RL 优化中，不设固定长度惩罚，而是以本批次内成功轨迹的最优效率作为锚点，自适应计算相对奖励。该方法能避免模型在简单任务上偷懒、复杂任务上过度探索，适合需要按
  query 难度动态调节计算量的场景。

  - **工具与 token 成本分开建模**：分别衡量外部工具调用和内部思考 token 的冗余，可针对性地抑制“盲目工具依赖”和“表演式推理”。电商 Agent
  常出现反复搜索已获取信息、拖长推理文本的现象，此分离设计可精细化控制资源消耗。'
score: 9
source: huggingface-daily
depth: full_pdf
---

**动机**：当前训练范式仅以正确率驱动，促使网页智能体采取“暴力”策略——无差别调用外部工具、生成大量冗余推理步骤，导致盲目工具依赖和表演式推理，计算成本急剧膨胀。这一效率陷阱的根本在于，常规 SFT 接受任何正确的轨迹作为正样本，RL 则只奖励最终成功，隐式鼓励无限制的探探，模型无法区分最小必要路径与臃肿路径。

**方法关键点**：SlimSearcher 提出一个统一的多阶段门控机制，贯穿 SFT 和 RL 两阶段，同时优化准确率与计算效率。
- **三级门控**：正确性门（二进制，不正确则奖励置零）确保效率优化不伤害任务成功；工具效率门将轨迹的工具调用成本与当前批次内最短成功路径对比，通过指数缩放映射为 (0,1] 的乘子；token 效率门采用相同机制压缩冗余推理长度。最终奖励为三者的乘积。
- **SFT 阶段**：用奖励引导的拒绝采样构建训练集。对每个 query 采样多条轨迹，过滤错误轨迹后，按联合效率分数选取帕累托最优轨迹作为训练样本，使模型从初始化阶段即学习高效搜索行为。
- **RL 阶段**：基于 GRPO，组内采样多条轨迹，用上述门控计算每条轨迹的原始奖励，再计算组内优势，更新策略。自适应锚定使优化目标动态趋向当前探索到的经验最小路径，规避固定惩罚带来的简洁偏差。

**关键实验**：在 GAIA、BrowseComp、XBench-DeepSearch、HLE 四个长时域基准上，基于 Tongyi-DeepResearch 和 Qwen3-30B-A3B 两种骨干进行验证。SlimSearcher (SFT+RL) 相比基线，工具调用轮数在 GAIA 下降 48.4%（20.56→10.61），在 BrowseComp 下降 25.2%（63.70→47.63），整体降幅 17%–58%，同时准确率普遍持平或提升。消融实验证实：去掉正确性门导致准确率崩溃（GAIA 降至 0.136），去掉自适应效率锚定则退化为暴力探索，工具调用和 token 消耗显著回升。

**一句话记忆**：通过正确性硬约束与组内效率相对锚定，SlimSearcher 迫使智能体在保证成功的前提下，自主收敛到最小必要路径，而非用平均惩罚逼出短答案。
