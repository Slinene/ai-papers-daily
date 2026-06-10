---
title: 'TRACE: A Unified Rollout Budget Allocation Framework for Efficient Agentic
  Reinforcement Learning'
title_zh: TRACE：统一的多轮智能体强化学习 rollout 预算分配框架
authors:
- Heming Zou
- Qi Wang
- Yun Qu
- Yuhang Jiang
- Lizhou Cai
- Yixiu Mao
- Ru Peng
- Xin Xu
- Weijie Liu
- Kai Yang
affiliations:
- Tsinghua University
- Tencent
arxiv_id: '2606.11119'
url: https://arxiv.org/abs/2606.11119
pdf_url: https://arxiv.org/pdf/2606.11119
published: '2026-06-09'
collected: '2026-06-10'
category: Agent
direction: 智能体强化学习 · 树形 rollout 分配
tags:
- Rollout Allocation
- Agentic RL
- Multi-turn RLVR
- Tree-structured Rollouts
- Prefix Value Prediction
one_liner: 将 rollout 预算分配到更可能产生混合奖励的 prompt 根和交互前缀，提升智能体 RL 样本效率。
practical_value: '- **预算分配的层级化思路可以迁移到电商 Agent 对话流**：区分 prompt 层面（用户 query）和中间状态（已执行工具、已获取信息）的扩展价值，在
  Agent 解决用户问题的多轮交互中，对关键决策节点（例如调用搜索 API 前、首轮价格查询后）进行分支探索，避免在确定性高的步骤浪费采样。

  - **轻量级前缀价值预测器设计直接可复用**：用同一预测器估计 prompt 和中间前缀的条件成功概率，以递归树监督的 MSE 回归训练，与下游策略优化解耦。在构建购物助手等
  Agent 时，可以搭建类似的“关键难度”预估模块，指导何时对模型输出进行多次重采样或多路展开。

  - **树形 rollout 生成的工程化实现**：采用“初始化-扩展”两阶段策略（先完成所有 bare rollout，再按 prompt 本地化扩展前缀），能贴合并行推理引擎，减少跨
  prompt 等待。对于高并发线上 Agent 服务，设计 budget 分配时考虑前缀展开的本地化以减少通信开销是重要参考。

  - **混合奖励对比激活更新的视角**：明确只有锚点后代同时出现成功与失败时梯度才有效，因此在生成式推荐或电商搜索 Agent 的训练中，可以有意识地构造成对对比样本（同一前缀下的不同推荐结果），放大有效学习信号，避免在单一结果上浪费计算。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：多轮智能体强化学习（RLVR）中，rollout 预算昂贵且学习信号稀疏。传统方法仅按 prompt 难度分配采样数，忽略同一 rollout 内不同交互回合的前缀状态蕴含的信息量差异。过于简单或困难的实例产生低方差奖励，单一终端奖励难以提供局部信用赋值。该工作将 budget 分配抽象为在 rollout 树锚点上构造“混合奖励对比”——让同一前缀下出现成功与失败两种结果，从而激活有效梯度。

**方法关键点**：
- 将 ReAct 式多轮交互视为树结构，每个 thought-action-observation 回合是一个语义节点，prompt 为根，中间前缀为内部节点，均可成为分支扩展的锚点。
- 提出混合奖励对比分配原则：向最可能产生成功与失败混合后代集的锚点分配更多 rollout 预算。统一了 prompt 过滤、根 rollout 数量分配、中间前缀继续采样这三种决策。
- **TRACE 框架**：两阶段分配——①全局根分配：根据预测器估计的 prompt 条件成功概率，以最大化跨 prompt 的混合奖励概率为目标分配根 rollout 数量；②局部前缀扩展：对每个活跃 prompt，在已有前缀中根据预测概率和已观察分支奖励，分配额外的 continuation 分支，以翻转观察结果。
- 使用共享的轻量级前缀价值预测器 V ~ψ(H)，通过树递归监督（自底向上聚合后代的平均奖励）进行 MSE 训练，仅为分配器服务，与下游策略优化器解耦。
- 最终生成 rollout 树提供给支持树感知的策略优化器（如 group-relative updates），利用根级和前缀级的对比对增强策略梯度。

**关键结果**：在 Qwen3-8B/14B 上，涵盖数学推理（DeepScaler）、多跳问答（HotpotQA）和函数调用（BFCL v4）三个智能体场景。同等 rollout 预算下，TRACE 相比 GRPO、PCL、TreePO（随机树）分别提升：Qwen3-14B Multi-Hop QA 平均准确率提高 2.8 个百分点；数学推理平均从 73.5→74.9；训练过程中的有效对比样本比率（effective ratio）大幅提升，例如 DeepScaler 从 GRPO 的 34.7%→59.7%。消融证实根分配和前缀分配各自贡献且可叠加，且根覆盖宽度比过深扩展更重要。
