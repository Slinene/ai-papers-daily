---
title: 'CAST: Critique-Aware Supervision for Training Reliable Long-Horizon Tool-Calling
  Agents'
title_zh: CAST：用于训练可靠长程工具调用智能体的批判感知监督框架
authors:
- Amir Saeidi
- Zehua Zhang
- Rishitosh Singh
- Naman Ahuja
- Vivek Gupta
- Ali Payani
- Gaowen Liu
- Jayanth Srinivasa
- Chitta Baral
affiliations:
- Arizona State University
- Cisco Research
arxiv_id: '2608.30147'
url: https://arxiv.org/abs/2608.30147
pdf_url: https://arxiv.org/pdf/2608.30147
published: '2026-08-30'
collected: '2026-09-01'
category: Agent
direction: 工具调用 Agent 可靠性训练
tags:
- critique-aware training
- tool-calling agent
- long-horizon reliability
- agentic verification
- policy optimization
- LLM fine-tuning
one_liner: 将稀疏任务结果转化为动作级批判监督，训练小型 critic 与 policy，使 4B/8B 模型在重复运行可靠性上超过大模型
practical_value: '- 在电商智能客服、订单退款等高危长程工具调用场景，可借鉴 CAST 的「离线标注 + 训练轻量 critic + 在线验证」模式：用多智能体框架从历史轨迹中生成动作级对错标签和理由，训练一个
  4B/8B 的小 critic 替代 GPT-4 等大模型做实时动作验证，大幅降低 token 与延迟，同时提升校准度（误报率从 46.8% 降到 13.6%）。

  - 构建训练数据时，利用 privileged information（如真实动作轨迹）让标注更可靠，但 critic 和 policy 在训练与推理时只接触
  step-local context，这种不对称设计值得迁移到业务 guardrail 中：离线有更多信息可用，在线判断只能基于部分观测。

  - 用 critic 验证后的成功轨迹（critique-enriched successful trajectories）对 policy 做 SFT，可以显著降低
  policy 对反馈的抵抗率（约下降一半），让模型在推理时更愿意根据验证信号修正动作，从而提升重复运行一致性（pass^4）。

  - 实验表明，经 CAST 训练的小模型在 pass^4 上超过 Qwen3-32B 和 GPT-OSS-120B，说明在可靠性优先的在线服务中，可以考虑用专门训练的
  4B/8B 模型替代大模型，节省成本同时保证稳定性。'
score: 8
source: huggingface-daily
depth: full_pdf
---

## 动机

长程工具调用智能体（如客服助手）在动态、有状态环境中，单个错误动作（如退款给错误订单）可能导致不可逆失败。现有基于 prompt 的 critic 方法（用 GPT-4 等大模型做验证）开销高且校准差；RL 或 SFT 方法缺乏系统性的动作级验证理由生成。本文针对这种可靠性缺口，提出 CAST 框架。

## 方法关键点

CAST 分三个阶段：
1. **轨迹收集**：用 Qwen3-32B 作为 teacher policy 在 τ-Bench Retail 训练集上运行多次，收集成功和失败轨迹。
2. **动作级验证标注**：设计多智能体验证框架，将动作失败分解为三类：hallucination（幻觉/无依据信息）、domain violation（违反领域规则）、wrong tool usage（错误工具选择）。由 rule extractor、tool extractor、专用 checker 等智能体协作，对每个动作生成结构化 rationale 和 binary label。标注时允许使用 privileged information（如真实轨迹），但 critic 和 policy 在训练/推理时不接触。
3. **训练 critic 和 policy**：用标注数据训练一个轻量 critic 模型（CAST-Critic），损失函数结合 rationale 生成和分类。然后用训练好的 critic 在 rollout 中验证 agent 动作，生成 critique-enriched trajectories；只保留成功的轨迹对 policy 做 SFT，得到 CAST-Policy。推理时支持 standalone 或 critic-guided 两种模式。

## 关键结果

- 在 in-domain Retail 上，CAST-Policy-4B 相对 base instruct 提升 pass^1 18.9%、pass^4 10.4%；相对 RFT 基线，pass^4 额外提升 4.3%（4B）和 2.6%（8B）。
- 4B/8B 的 CAST-Policy 在 pass^4 上超过 Qwen3-32B 最优设置 3.4% 和 1.7%，并优于 GPT-OSS-120B（4B pass^4 16.9% vs 120B 的 5.9%）。
- 在 out-of-domain（Airline/Telecom/Telehealth）上，agentic CAST（policy+critic）比 standalone policy 提升 pass^1 和 pass^4，说明泛化性。
- 与 GPT-4.1 作为 critic 相比，CAST-Critic 误报率从 46.8% 降至 13.6%（4B）和 11.4%（8B），对错误动作的纠正率从约 40-45% 提升至 82-88%。
- 与 PALADIN、EvoTool 等 agentic 框架相比，CAST 在 pass^1/pass^3/pass^4 上平均高出数个百分点，且 critic 模型更小。

## 一句话总结

用结构化验证理由训练小型 critic 并用于 policy 优化，可以让 4B/8B 的长程工具调用智能体在重复运行可靠性（pass^4）上超过 32B 甚至 120B 大模型。
