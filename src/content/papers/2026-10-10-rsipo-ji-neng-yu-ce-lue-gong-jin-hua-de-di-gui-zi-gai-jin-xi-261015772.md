---
title: 'RSIPO: Recursive Self-Improving Policy Optimization for Agentic Reinforcement
  Learning via Skill-Policy Co-Evolution'
title_zh: RSIPO：技能与策略共进化的递归自改进Agent强化学习
authors:
- Fan Zhang
- Hao Wu
- Jinyang Wu
- Hongyu Qu
- Zheng Lian
- Xiao Luo
- Yefeng Zheng
- Bo Zhang
- Haoxuan Li
- Pheng-Ann Heng
affiliations:
- CUHK
- THU
- NUS
- Tongji University
- UW-Madison
arxiv_id: '2610.15772'
url: https://arxiv.org/abs/2610.15772
pdf_url: https://arxiv.org/pdf/2610.15772
published: '2026-10-10'
collected: '2026-10-14'
category: Agent
direction: Agent 强化学习 · 技能-策略共进化
tags:
- Agentic RL
- On-Policy Self-Distillation
- Skill Evolution
- Empirical Bayes
- RLVR
- GRPO
one_liner: 用重放增益奖励技能生成并以经验贝叶斯校准教师信任，实现技能-策略共进化
practical_value: '- 可借鉴「执行检查」机制到购物/搜索 Agent 技能库更新：让 Agent 从自身轨迹中改写技能，用同一初始状态下带技能重放
  vs 无技能控制组的效用差作为 reward，不依赖外部 judge 模型或额外标注数据，特别适合可重置的仿真购物、离线检索沙盒。

  - Type-level empirical Bayes shrinkage 对任务级重放增益降噪后再映射为教师信任系数 ωx，可直接替代 OPSD/蒸馏中均匀信任权重；电商场景中不同品类/任务类型难度差异大，按类型池化增益能减少不可靠教师信号对策略的损害。

  - 对可重置环境可低成本采纳，但线上不可重置环境需额外处理；重放增加 K 次 rollout 与训练成本，可考虑只在部分任务上做执行检查、用早停或小 K 控制开销。

  - 技能 reward 用「该技能增益 - 同类型平均增益」做中心化，避免绝对增益偏差，适合在在线技能更新中稳定策略梯度；无效技能用固定惩罚 ρ，且搜索类任务可设
  ρ=0 防止格式不稳定。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

Agentic RL 的混合框架通常把 RLVR 的轨迹级优势与 OPSD 的 token 级监督结合，教师以 agentic skills 为特权上下文评分学生策略。但现有方法的技能来自静态外部库或离线训练的生成器，技能生成不随策略增强而在线进化；实验中 SFT 技能数据只有 0.25% 来自成功轨迹，而 RL 训练后策略成功率迅速超过 80%，分布偏移严重。同时，教师监督并非始终可靠：在 ALFWorld 上，技能增强教师有 5.5%–22.4% 的任务表现不如学生，尤其当学生对该任务已有部分成功时。均匀信任教师会阻碍学习，GRPO+OPSD 甚至在部分模型上低于 GRPO。

## 方法关键点

RSIPO 保持 RLVR 与 OPSD 分支，新增执行检查模块，用重放增益驱动技能与策略共进化。

- **执行检查**：对每个任务，将 G 个 rollouts 随机均分为 evidence 集与控制集；从 evidence 中选择一条轨迹改写技能 sx，用技能增强教师从相同初始状态重放 K 次，与控制组比较效用差 Δx。效用定义为成功且步数越快越高：u(τ)=I(R=1)(1−α T/Tmax)。
- **类型级经验贝叶斯收缩**：按任务类型聚合 Δx 的均值、平方、噪声方差，估计类型均值和任务间真实方差，计算后验均值 ĝx，将噪声大的增益向类型均值收缩，得到可靠的任务级教师优势估计。
- **技能进化**：以 Δx − 类型均值作为技能 token 的 reward，用 reward-weighted log-likelihood 优化技能生成；无效技能给固定惩罚 ρ，不收缩 reward 以保持策略梯度的无偏性。技能由当前策略从自身轨迹写成并按执行效果奖励，因此 on-policy 地随策略共同进化。
- **信任校准蒸馏**：将收缩后的增益 ĝx 映射为信任系数 ωx=clip(1+κĝx,0,ωmax)，用于加权 OPSD 损失；ωx=0 可禁用不可靠教师的蒸馏，ωx 最大为 2 增强可靠教师影响。
- 总目标 L = L_RLVR + λ_OPSD L_OPSD(ω) + L_skill，一次优化步同时更新策略执行与技能生成。

## 关键实验与结果

在 ALFWorld 与 7 个搜索问答数据集上，用 Qwen2.5-3B、Qwen2.5-7B、Qwen3-1.7B 对比 13 个基线。ALFWorld 上 Qwen2.5-7B 平均成功率 98.6%，比最强基线 SEED 高 2.5%，比标准 GRPO 高 17.4%；Qwen2.5-3B 达 95.7%，比 SEED 高 3.9%。搜索任务上 Qwen2.5-7B 平均准确率 50.8%，超过所有基线，比 GRPO 高 8.8%。无需 test-time skills 仍超过使用 test-time skills 的 Skill-Prompt*、Skill-GRPO*。消融显示 dynamic trust 和 skill evolution 分别带来 3.6% 和 5.6% 的提升，两者互补。

最值得记住的一句话：**技能的在线价值应当通过“同一初始状态下的重放增益”来测量，并用任务类型级经验贝叶斯收缩校准对教师监督的信任。**
