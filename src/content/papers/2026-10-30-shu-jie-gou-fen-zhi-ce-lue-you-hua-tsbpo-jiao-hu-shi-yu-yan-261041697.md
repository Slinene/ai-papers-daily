---
title: 'TSBPO: Tree-Structured Branching for Policy Optimization in Interactive Language
  Agents'
title_zh: 树结构分支策略优化 TSBPO：交互式语言智能体训练
authors:
- Rui Yu
- Chong Mu
- Jinchuan Zhang
affiliations:
- University of Electronic Science and Technology of China
arxiv_id: '2610.41697'
url: https://arxiv.org/abs/2610.41697
pdf_url: https://arxiv.org/pdf/2610.41697
published: '2026-10-30'
collected: '2026-11-02'
category: Training
direction: 交互式语言智能体策略优化
tags:
- TSBPO
- policy optimization
- tree-structured sampling
- credit assignment
- language agents
- RL
one_liner: TSBPO 用树结构采样与更新统一解决交互式语言智能体训练的采样、延迟信用分配和多 token 损失聚合
practical_value: '- 将 rollout 构建为物理树，并用 likelihood-fitted Root/Branch allocator 在固定预算下优先展开高风险分支：这个思路可迁移到电商导购
  Agent 的模拟训练，减少无效交互采样，把探索预算集中在信息增益大的状态。

  - 信用分配不用全局奖励做蒙特卡洛，而是比较同父兄弟片段和同任务/观测状态的相对优势：适合多轮推荐对话中延迟转化信号，能被归因到具体话术或动作轮次，减少奖励噪声。

  - 多 token 动作聚合采用完整 response 内 token surrogate 求和并按 active turns 归一化，避免直接按 response
  长度平均导致的梯度消失：生成式推荐中的商品标题/文案策略梯度可直接复用这一项。

  - 固定 checkpoint + 多次随机 episode 取平均成功率作为评估，比单次最优模型更可靠，适合上线前回归评测 Agent 稳定性。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

训练交互式语言智能体从终端反馈学习时，需要同时决定采样哪些任务/状态延续、把延迟奖励分配给哪个决策、以及如何把多 token 动作的损失聚合成策略梯度。TSBPO 在一个训练循环内用树结构采样到更新统一处理这三个问题。

方法关键点：
- 用 likelihood-fitted Root/Branch allocator 在固定 rollout 预算下，根据保留的任务/状态证据优先展开可能产生对比终端结果的延续，提高样本效率。
- 在重放的物理树上，trajectory advantages 比较同父兄弟片段；observation-group step advantages 比较相同任务/观测状态下的结果，避免全局延迟奖励造成高方差。
- actor 更新时对完整 response 内 clipped token surrogates 求和，并按 active turns 归一化，避免策略梯度项被响应长度平均。

结果：使用 Qwen2.5-1.5B actor，固定 checkpoint 在 ALFWorld 取得 97.79% 已见、96.64% 未见随机成功率；WebShop 500 个测试目标在每目标 6 次随机 episode 下达到 81.07% 每 episode 成功率。WebShop step-term 消融为 75.93%，ALFWorld 聚合比较显示 complete-turn weighting 带来更高的命令有效性。
