---
title: 'AutoSim: A Self-Improving User Simulator for Conversational Search Evaluation'
title_zh: AutoSim：面向对话搜索评估的自改进用户模拟器
authors:
- Saber Zerhoudi
- Jelena Mitrovic
- Michael Granitzer
affiliations:
- University of Passau
- Interdisciplinary Transformation University Austria
arxiv_id: '2610.28054'
url: https://arxiv.org/abs/2610.28054
pdf_url: https://arxiv.org/pdf/2610.28054
published: '2026-10-20'
collected: '2026-10-21'
category: Eval
direction: 用户模拟器自改进 · 评估真实性
tags:
- User Simulation
- Conversational Search
- Evaluation
- Self-Improving Agents
- Adversarial Training
- Sim2Real
one_liner: Prompt 级自改进无法消除对话搜索模拟器与真实用户行为差距，权重级对抗微调把判别 AUC 降到 0.45 并修正评估偏差。
practical_value: '- 如果要在搜索/推荐/Agent 离线评估里用 LLM 用户模拟器，别指望 prompt 或少样本把「模拟用户」变真实；准备少量真实用户对话或行为日志，用
  LoRA/权重级对抗 SFT 训练生成器。论文的四轮 rejection sampling 流程可直接复用：冻结判别器，采样候选 utterance，保留最像人的样本再
  SFT，然后刷新判别器。

  - 上线前给模拟器加两道检查：一是真实 vs 模拟判别器 AUC 或人工判别，不只看平均 query 长度、礼貌比例；二是在真实用户无结果/低召回的高难度 query
  上比较模拟 query 的 nDCG 或召回，防止模拟器掩盖检索失败。

  - 把「评估判断」和「用户生成」解耦：排序有效性来自强 LLM judge，不必让 judge 自改进；judge 与 generator 用不同模型家族，避免
  self-preference/verbosity bias。业务上可复用为：LLM relevance judge 保持与人工标注或 A/B 结果对齐，生成器单独做真实性校准。

  - 对生成式推荐/QueryRec 或多轮 Agent 用户建模：不要只学最终答案或短 query 表层长度，要匹配真实 query 与完整需求之间的语义对齐；短
  query 不一定需求聚焦，需额外测 query-need alignment。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：对话搜索系统需要大规模离线评估，但 LLM 用户模拟器行为不可信：强模型扮演用户时写长而礼貌的完整请求（37.5 词 vs 真实 12.8 词），真实-模拟判别器 AUC 达 0.88，并且这种偏差可能扭曲系统评估结论。

**方法关键点**：
- 在 TREC iKAT 上先把 gap 拆成 relevance judge 与 utterance generator：judge 已与 NIST 高度一致，问题在生成器。
- AutoSim 保留混合 orchestration 状态，暴露两个可编辑组件：judge prompt 和 utterance generator；自改进 loop 用 held-out 校准分流做接受检查，避免回归。
- 比较 prompt-level 与 weight-level 自改进：weight-level 用 Qwen2.5-3B + LoRA warm-start，再做对抗 rejection sampling SFT；每轮冻结判别器，采样候选 utterance，保留最像人的样本，再刷新判别器，重复 4 轮。

**关键结果**：
- TREC iKAT 2023/2024/2025 系统排序 Kendall τ=0.66/0.91/0.91（p≤0.002）；去掉 persona 仍 τ=0.79；跨语料 CAsT 2020 τ=0.56。
- 真实-模拟判别 AUC：默认 prompt 0.88，手写/tuned/few-shot prompt 均 ≥0.85；weight-level 降至 0.45，人工读完整对话也难以区分。
- 在真实用户几乎检索不到相关段落的 iKAT 2024 上，prompt 模拟器高估 nDCG +0.136，默认模拟器在真实用户失败回合有 57% 仍返回相关段落；weight-level 偏差 +0.014，CI 含 0。

**最值得记住**：只看平均长度、礼貌比例等 summary metrics 会误判模拟器；必须用 adversarial discriminator 和困难回合上的 effectiveness bias 测试，prompt 级优化关不掉 sim2real gap，权重级自改进才同时决定真实性和评估有效性。
