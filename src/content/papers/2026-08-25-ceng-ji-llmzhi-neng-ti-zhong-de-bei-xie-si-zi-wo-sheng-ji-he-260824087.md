---
title: 'Knowing When to Ask for Help: Bayesian Self-Escalation in Hierarchical LLM
  Agents'
title_zh: 层级LLM智能体中的贝叶斯自我升级：知道何时求助
authors:
- Nadeem Shaikh
affiliations:
- Independent Researcher
arxiv_id: '2608.24087'
url: https://arxiv.org/abs/2608.24087
pdf_url: https://arxiv.org/pdf/2608.24087
published: '2026-08-25'
collected: '2026-08-26'
category: Agent
direction: 层级LLM智能体自我升级决策
tags:
- Bayesian self-escalation
- model cascade
- optimal stopping
- calibration
- LLM agents
- uncertainty quantification
one_liner: 把生成中途的模型求助建模为基于能力后验的最优停止问题，证明阈值策略并给出校准驱动的后悔界
practical_value: '- 在电商/Agent 级联路由中，不只做 pre-router 或 post-verifier：引入 per-token 或
  per-step 的“能力后验”B_t，在生成中途触发升级，能省下注定失败的 junior 生成成本。真实代码级联里，streaming 升级到 75% 准确率只用
  0.98× junior 成本，而 post-hoc 路由要 1.41×。

  - 原始 entropy / margin / probe 只能当 evidence，不要直接当概率用；用标注轨迹学 competence posterior，训练目标优化
  Brier score 而不是只看 ECE。ECE 低不代表安全，Brier score 同时惩罚 calibration 和 refinement。

  - 把 competence posterior 与决策阈值解耦：成本、延迟预算、senior 模型变化时，只重跑 offline backward induction
  更新阈值表，不用重新训练。适合业务频繁调价、换大模型或调整延迟 SLO。

  - 跨模型交接只传文本 trace、工具调用历史、检索证据，不传 hidden state / KV cache，保持模型无关；这可以复用到小模型 agent
  负责长尾 query、复杂任务再升级大模型的架构。'
score: 8
source: arxiv-stat.ML
depth: full_pdf
---

**动机**：现有 LLM 级联和路由系统要么在推理前选模型，要么在生成完成后打分重试，无法让工作模型在推理中途发现“我已经不行了”并及时把任务交给更强模型。论文把这个问题建模为最优停止：junior agent 维护一个关于自己最终正确性的在线后验，并在继续生成的期望成本超过升级成本时中止。

**方法关键点**：
- 定义 competence posterior B_t = P(Y=1|F_t)，其中 Y 表示 junior 最终答案是否正确；信号 e_t 来自 token entropy、next-token margin 或 semantic entropy probe，但 posterior 是从标注轨迹学到的，不是直接用原始熵。
- 在条件独立信号假设下，belief 更新为 log-odds 累加：ℓ_t = ℓ_0 + Σ λ(e_s)，B_t = σ(ℓ_t)。
- myopic 升级阈值为 τ_t = q − γ/L + (T−t)κ/L；最优策略由动态规划刻画，并只用单调性证明阈值结构，不需要 concavity 或 MLR 假设。
- 核心后悔界：Regret ≤ L·E|B_t − B̂_t| 在 myopic threshold 处成立，说明成本由 posterior 校准误差控制；Brier score 是直接训练目标，ECE 只能作为报警指标。
- 算法上，在线推理是 O(1) per-token belief update，离线 backward induction 计算阈值表；上下文交接只传文本 artifacts，不传 hidden state。

**关键实验**：
- 合成模拟：Bayesian optimal-stopping 在成本 0.111 达到 96.0% 准确率、40% 升级率，优于 fixed-rule 和 post-hoc selective；置信错误污染 30% 时准确率从 95.2% 降到 85.7%，升级率反而下降。
- 真实模型：Qwen2.5-Coder 1.5B→7B 在 MBPP sanitized test 上，junior 62.3%、senior 80.9%；cumulative belief 的 AUROC 从 0.51 升至 0.76；streaming 升级到 75% 准确率只需 0.98× junior 成本，post-hoc 路由需 1.41×。

**最值得记住的一句话**：对自我升级来说，校准比路由策略更关键；confidently wrong 是致命失败模式。
