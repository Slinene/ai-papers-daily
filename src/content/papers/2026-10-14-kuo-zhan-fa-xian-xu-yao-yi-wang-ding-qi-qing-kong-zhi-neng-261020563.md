---
title: Scaling Discovery Requires Forgetting
title_zh: 扩展发现需要遗忘：定期清空智能体状态并保留最佳候选
authors:
- Shangyin Tan
- Ben Zhou
- Lakshya A Agrawal
- Jialin Zhang
- Yilin Chen
- Qiuyang Mang
- Donghyun Lee
- Dennis Jacob
- Koushik Sen
- Alex Dimakis
affiliations:
- UC Berkeley
- Stanford
- Bespoke Labs
arxiv_id: '2610.20563'
url: https://arxiv.org/abs/2610.20563
pdf_url: https://arxiv.org/pdf/2610.20563
published: '2026-10-14'
collected: '2026-10-15'
category: MultiAgent
direction: 多智能体自动发现 · 遗忘重置机制
tags:
- LLM Agents
- Multi-Agent
- Forgetting
- Autoresearch
- Search
- Optimization
one_liner: 单agent/并行/通信式多智能体自动研究都会平台期，周期性遗忘会话与搜索状态、仅保留全局最佳候选可解锁探索并提升最多15%
practical_value: '- 在电商/广告/推荐场景用 LLM agent 做长期自动优化（prompt 策略、召回/排序超参、文案生成迭代）时，不要维持单一长
  session；周期性清空上下文和 workspace、只保留 best candidate，可显著恢复探索性，避免 agent 只做小改。

  - 多智能体协作建议异步、token-free 共享每位 agent 的最佳候选与分数（类似 git commit/diff），不要互相读完整方案；这样既能传播好点子，又降低同质化和
  token 开销。

  - 把 agent 的编辑行数、thinking tokens、空 turn 比例作为平台期信号，触发遗忘或重启；例如 VLIW 任务中 66% 花费消耗在无候选空转，这类指标可用于早停或重置。

  - 遗忘后的 fresh context 每轮成本约减半（如 AHC014 team: $15.32 vs $24.67），同样预算下分成多轮重置比持续更长更划算；在搜索/调参
  agent 中可优先采用多轮重置。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM autoresearch agents 通过迭代提出候选、评测、再改进来发现新方案。扩展方式有三种：单 agent 长时间跑、多 agent 并行、并行 agent 通信协作。但实验显示三种方式都会在预算耗尽前平台期：agent 积累历史后越来越保守，编辑行数和 reasoning tokens 持续下降，大量预算被空转消耗。例如 VLIW kernel 任务中，单 agent 有 66.2% 的 spend 花在没有产生候选的空 turn 上。

**方法关键点**
- 提出 **forgetting**：周期性丢弃所有 agent 的 session、候选历史和 filesystem 状态，只保留全局最佳候选；新 agent 用空上下文从该候选重新开始，形成多个 round。
- 与团队通信结合：4 个 agent 并行，每个 proposal 前通过 git commits 查看 peers 的最佳候选与分数；通信异步且 token-free。Forget 时全体从 global best 重启。
- 实现为 reducer 控制的 harness：候选是版本控制中的 commit，judge 评分；forget 时清空 workspace 中旧候选，只留 best。

**关键实验与结果**
在 AHC014、VLIW kernel、Frontier-CS Q171、nanochat-autoresearch 四个任务上，对比 1 agent、4 parallel agents、team with forgetting，三者预算相同。Team with forgetting 在所有任务上最优：相对 parallel agents 提升 1.9%–15%，平均约 10%；相对单 agent 最高提升 39%（AHC014 mean 1103 vs 795）。32/36 次 forget 在下一轮产生新最佳，第一轮 forget 增益最大。从同一平台期状态出发，forget 比 continue 增益更高且成本约低一半：team 设置下 forget +9.2%（$15.32）vs continue +1.4%（$24.67）。机制分析显示 forget 后编辑行数恢复约 50 行、reasoning tokens 翻倍，而继续则编辑仅几行。

**最值得记住的一句话**
对开放式发现，agent 被允许记住什么，和它被给予多少计算量同样重要。
