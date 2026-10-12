---
title: Matched-Context Group Policy Optimization for LLM Agent Training
title_zh: 匹配上下文分组策略优化用于 LLM Agent 训练
authors:
- Chenxu Zhang
- Yaorui Shi
- Wenlong Zhang
- Jianchao Tan
- Zihan Wang
- Yiming Cheng
affiliations:
- Imperial College London
- University of Science and Technology of China
- Meituan
- Tsinghua University
arxiv_id: '2610.13755'
url: https://arxiv.org/abs/2610.13755
pdf_url: https://arxiv.org/pdf/2610.13755
published: '2026-10-09'
collected: '2026-10-12'
category: Training
direction: LLM Agent 强化学习 · 长程信用分配
tags:
- LLM Agent
- Group Policy Optimization
- Credit Assignment
- Preference Learning
- Long-Horizon
- Critic-free RL
one_liner: 通过匹配任务进度与状态构造加权动作偏好，提升长程 LLM agent 稀疏回报下的信用分配
practical_value: '- 利用任务规则提取可观测的 rubric progress（如已匹配属性、价格满足、页面状态）作为状态补充，与 state summary
  联合定义动作比较上下文，避免因进度差异导致信用错配；在电商导购 Agent 中可借鉴：用已完成步骤（搜索、详情、加购）标注状态，减少不同会话阶段的错误对比。

  - 从有限日志或 rollout 数据构造动作偏好时，采用 opposite-fold 交叉标注：一半数据提取候选动作，另一半估计结果证据，降低自相关偏差；适用于从历史会话日志生成离线策略优化信号。

  - 根据支持样本数动态缩减偏好权重（n/(n+κ)），防止小样本高方差偏好主导训练；在业务中构造 session-level 偏好对时，可对低支持度的对比自动降权，提高训练稳定性。

  - 无需 critic 模型，只附加一个 weighted pairwise objective 即可接入现有 PPO/GRPO 流程，保留原始历史上下文；便于在已有
  Agent 训练框架上增量实施。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
长程 LLM agent 训练需要把稀疏终局反馈分配给中间决策。现有 group-relative RL 常按重复状态分组，但相同状态摘要可能对应不同任务进度，导致动作结果对比混入先前进度差异，信用分配失真。如何从有限 rollout 组中提取可靠、有支持的局部动作偏好是核心问题。

**方法关键点**
- MCGPO 通过 **Match–Label–Learn** 三阶段构造加权动作偏好。
- **Match**：用 pre-action state summary + observed rubric progress (C,F) 定义比较上下文 g；按 exact→coarse 两级状态匹配规则，选择两个动作都有支持证据的最小粒度，支持度至少 m=1。
- **Label**：将固定 folds 分离候选决策与终局证据（opposite-fold），用相反折的终局成功率差标注偏好方向；计算 evidence weight c = |Δ|·n/(n+κ)·q_resolution，融合对比幅度、支持度收缩和分辨率因子。
- **Learn**：基于原始 token 历史的 length-normalized log-prob change 定义 pairwise loss softplus(-[dθ(+)-dθ(-)])，与 GraphGPO task objective 联合优化，保留 critic-free 训练和原始响应历史。

**关键实验**
在 ALFWorld 和 WebShop 上，用 Qwen2.5-1.5B/7B 和 Qwen3-4B/8B 训练，对比 matched GraphGPO。MCGPO 平均成功提升：ALFWorld +1.04/1.46 pp（1.5B/7B），WebShop +1.09/0.47 pp（Qwen2.5）；Qwen3 WebShop 提升 +3.96/5.16 pp（4B/8B）。消融显示 shuffled rubric 下降 2.34/0.63 pp，candidate-progress labels 下降 1.41/3.13 pp；移除 pairwise loss 下降 1.41/0.78 pp。联合 state–rubric 匹配在全部四个 representation-control 设置中取得最高均值，超过 state-only 3.96–9.90 pp、rubric-only 5.15–9.01 pp。

**最值得记住的一句话**：用任务进度和状态共同定义比较上下文，结合相反折终局证据和支持度加权，能从有限 rollout 中稳定提取有意义的动作偏好。
