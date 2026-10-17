---
title: 'SERO: Learning from Executable Oracle Continuations for Long-Horizon Agentic
  Reinforcement Learning'
title_zh: SERO：从可执行 Oracle 续推中学习长时程智能体强化学习
authors:
- Dingyi Rong
- Yue Shi
- Chaofan Ma
- Zongrui Wang
- Jiezhang Cao
- Yixin Cao
- Liang He
- Ning Liu
affiliations:
- Shanghai Artificial Intelligence Laboratory
- Shanghai Jiao Tong University
- Tongji University
arxiv_id: '2610.19397'
url: https://arxiv.org/abs/2610.19397
pdf_url: https://arxiv.org/pdf/2610.19397
published: '2026-10-13'
collected: '2026-10-17'
category: Training
direction: 长时程 Agent RL 的可执行 oracle 续推训练
tags:
- SERO
- oracle continuation
- policy-reachability weighting
- long-horizon RL
- agentic RL
- on-policy distillation
one_liner: 将训练期 oracle 多步续推作为辅助监督，并用前缀可达性权重控制离策略深度，提升长时程 Agent RL 的 OOD 表现。
practical_value: '- 在多轮会话型业务（导购/搜索/推荐 Agent）中，可维护训练期 oracle（强规则、大模型或人工策略），从线上策略实际到达的状态恢复环境并执行后续
  oracle 动作，把整条“可执行分支”而非单步纠正作为 SFT/RL 辅助监督；推理时完全移除 oracle，不增加线上成本。

  - 引入 policy-reachability weighting：用冻结策略对 oracle 前缀的 likelihood 乘积衰减深层监督，避免在策略不兼容的深度离策略状态上乱学；随策略提升自动延长有效监督
  horizon。可迁移到多步推荐/对话策略蒸馏，对 OOD 流量更稳。

  - 将 oracle 辅助 loss 与 base RL 解耦：不改动 reward/advantage/importance ratio，降低与现有 credit
  assignment 方法（如 GRPO、GraphGPO）的集成成本，业务上可作为插件式模块，关掉 λ_O 即可回退到原方法。

  - 如果业务环境支持状态快照恢复，可构造 counterfactual 续推数据用于诊断和训练；若不支持，也可用真实日志回放近似，但需注意状态-环境一致性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
长时程 agentic RL 的难点在于：rollout 未访问到有用未来时，credit assignment 也无法给未出现的行为提供监督。On-policy distillation 虽引入教师指导，但通常只监督纠正动作或前缀，未直接把 oracle 控制的未来轨迹当作可执行训练数据。

**方法关键点**
- SERO 从 on-policy 轨迹中选取失败 rollout 的某个 state，恢复环境快照，训练专用 oracle 在真实环境中继续执行多步动作，直到任务完成或预算耗尽。
- 对每个 oracle 动作计算 length-normalized local compatibility z_k，用前缀乘积 w_k=∏_{j<k}z_j 作为 policy-reachability weight；根动作权重为 1，深层目标在前缀不被当前策略支持时被抑制，随策略兼容性提升自动延长监督深度。
- 分支级 improvement gate：比较同 horizon 下 on-policy suffix 与 oracle 续推的回报差，clip 到 [0,1] 后乘到后续损失上，过滤无改进的 oracle 分支。
- 辅助目标 L_SERO 与 base RL（GRPO/GiGPO/HGPO/GraphGPO）解耦，只加在策略 loss 上，不动 advantage、reward 和 importance ratio；oracle 和状态恢复仅训练期使用，推理时移除。

**关键实验**
在 ALFWorld 和 WebShop 上，用 Qwen2.5-1.5B/7B-Instruct 验证。GraphGPO+SERO 在 1.5B 上将 ALFWorld seen/unseen 从 90.63/88.02 提到 95.83/91.67，WebShop 严格成功从 77.93 提到 79.27；7B 下 ALFWorld unseen 提 11.20 点。消融显示：只监督根动作反而降低 unseen 性能；用完整可执行续推带来明显收益，再加 policy-reachability weighting 在 unseen 上再加 3.39 点。

**一句话**
可执行的多步 oracle 续推比单步纠正强，关键是按策略对 oracle 前缀的可达性来控制离策略深度监督。
