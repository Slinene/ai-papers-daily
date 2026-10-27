---
title: Hallucination-Aware Multi-Agent RAG via Internal Attention Rewards
title_zh: 幻觉感知的多智能体 RAG：用内部注意力信号做奖励塑形
authors:
- Runsong Jia
- Qian Chang
- Mengjia Wu
- Ciprian Doru Giurcăneanu
- Jie Lu
- Yi Zhang
affiliations:
- University of Technology Sydney
- University of Auckland
arxiv_id: '2610.35056'
url: https://arxiv.org/abs/2610.35056
pdf_url: https://arxiv.org/pdf/2610.35056
published: '2026-10-26'
collected: '2026-10-27'
category: RAG
direction: 多智能体 RAG · 注意力奖励塑形
tags:
- Multi-Agent RAG
- Hallucination Reward
- Attention Head Norms
- PPO
- LoRA
- Faithfulness
one_liner: 用 TruthfulQA 校准的注意力头范数 critic 作为幻觉风险奖励，联合优化多智能体 RAG 的 query 规划、证据选择和答案生成，同时提升任务指标并降低幻觉率
practical_value: '- 将生成链路拆成 query planner / evidence selector / answer generator 三个
  role-specific LoRA adapter，共享 frozen backbone，用统一 terminal reward 做 cooperative
  PPO；电商问答、商品摘要、广告文案生成等场景可以用较低训练成本同时优化多个子策略。

  - 用 attention head norms 训练轻量离线 critic（TruthfulQA 校准）作为 hallucination 风险 reward
  shaping 项，无需每次 rollout 调用外部 LLM judge，工程开销小，且可跨任务迁移到业务数据，不必为每个业务域标幻觉标签。

  - 保持 backbone 和 critic 冻结，只更新低秩 adapter，避免奖励函数漂移；先监督 warm start 再 RL，降低探索难度；风险惩罚权重
  λ 需要小量（论文用 0.08）平衡 task reward 与风险信号。

  - 评估时不要只看 EM/F1，可引入 AHR（Answer Hallucination Rate）分离“答案重叠”与“证据忠实度”；内部信号适合作为弱监督辅助，而非替代任务奖励。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

## 动机
RAG 系统即使检索到正确证据，仍可能生成证据不支持的额外声明，而现有多智能体 RAG 通常用 EM/F1 等任务奖励优化所有 agent，这类奖励偏向答案与参考文本的重叠，对忠实度的惩罚很弱。同时，基于外部 LLM judge 的忠实度评估成本高、难作为稠密 RL 奖励。因此需要一种可以从生成过程内部、低成本获取的幻觉风险信号。

## 方法关键点
- 将 RAG 分解为三个 cooperative agents：Query Planner、Evidence Selector、Answer Generator，每个 agent 用一个 role-specific LoRA adapter 挂在 frozen backbone 上，共享参数但角色不同。
- 从 generator 的注意力头输出范数中提取 token-level 特征，通过 TruthfulQA truthful/false pairs 选择 truth-correlated heads，并用这些头的 mean pooling 特征训练一个轻量 MLP critic，输出幻觉风险 H∈[0,1]，训练后保持冻结。
- 共享 terminal reward 设为 R = αR_task − λH，其中 R_task 用 F1；三个 agent 共享同一 reward，但各自只更新自己的 LoRA adapter，通过 cooperative PPO 优化。
- 先用监督数据 warm start 三个 adapter，再进入 PPO，避免 RL 从零探索动作格式。

## 关键实验
在 RAGTruth、HotpotQA、2WikiMultiHopQA 三个 benchmark 上，用 Qwen3-8B、Llama3-8B、Llama2-13B 三个 backbone 评估。与最强 multi-agent baseline MMOA-RAG 相比，该方法在平均 R/A、EM、F1 上分别提升 +2.35、+0.95、+1.29（Qwen3-8B）。在 RAGTruth 的 Answer Hallucination Rate 上，Qwen3-8B 从 MMOA-RAG 的 31.98% 降至 21.24%，绝对降幅 10.74 点。消融显示去掉 critic 后平均 R/A 下降 3.31 点、F1 下降 2.59 点；冻结任一 agent 的 RL 更新都会带来性能回退，其中 generator 影响最大。

最值得记住的一句话：内部注意力 head norm 携带可迁移的 truthfulness 信号，可以作为廉价的训练期奖励塑形，但应作为 task reward 的补充而非替代。
