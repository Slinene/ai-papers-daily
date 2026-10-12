---
title: Inducing Process Supervision from Outcome-Only Reinforcement Learning
title_zh: TIPS：仅用结果监督RL训练生成式过程奖励模型
authors:
- Shengda Fan
- Xin Cong
- Zhong Zhang
- Haotian Chen
- Yankai Lin
affiliations:
- Renmin University of China
- Tsinghua University
- University of Electronic Science and Technology of China
- Shanghai Jiao Tong University
arxiv_id: '2609.36641'
url: https://arxiv.org/abs/2609.36641
pdf_url: https://arxiv.org/pdf/2609.36641
published: '2026-09-28'
collected: '2026-10-12'
category: Training
direction: 生成式PRM训练 · 结果监督RL
tags:
- PRM
- GRPO
- Outcome-only RL
- Process supervision
- Generative verifier
- Chain-of-thought
one_liner: TIPS仅用3.2K结果标签轨迹，经GRPO强化验证思维链，ProcessBench F1达85.2，超过更大PRM与强判官
practical_value: '- 在需要过程诊断/归因的 Agent 链路（如导购多轮对话、多工具调用、query 改写规划）中，可用该框架训练一个生成式 step
  judge：让模型输出 CoT + 逐步有效标签 + final label，reward 只看 final label 是否正确，用 GRPO 优化整个序列；推理时直接取
  step_labels 作为过程分，省去人工逐步标注。

  - 优先选有思维链先验的 thinking 模型或 reasoning-distilled 模型做基座。论文中 Qwen3-4B-Thinking 比 Instruct
  多涨 7.5 F1；弱基座容易走“只看最终结论”的 shortcut，逐步判断先升后降，因此可用 ORM 准确率平台期 + 回复长度下降作为早停信号。

  - 对电商推荐/搜索场景，可把该方法用于推荐解释或排序理由的逐句正确性判断，以及 query 规划、工具调用链路的错误步骤定位；但要优先选择步骤正确性直接决定最终结果的
  task（SQL 生成、API 参数校验、数值/规则链路），因为业务最终反馈如点击/转化与单步正确性耦合较弱时收益会显著变小。

  - 训练成本极低：仅需 3.2K 条 outcome-labeled 轨迹即可在 8×A800 上单 epoch 完成，适合为长尾场景快速冷启动一个内部 judge。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
训练强过程奖励模型（PRM）通常依赖人工步骤标注或 Monte Carlo rollouts，前者昂贵难规模化，后者不仅计算量大，还以“从该步是否能推理到正确答案”定义步骤质量，可能偏离步骤本身正确性。论文观察到 LLM 作为结果判官时，常在 CoT 里逐条检查中间步骤；因此反过来想：如果“正确的结果判断”依赖“准确的过程检查”，那么只奖励结果判断是否正确，是否也能强化过程验证能力？

**方法关键点**
- TIPS 让生成式奖励模型按顺序输出：思维链 Z → 逐步标签 Y_i → 最终结果标签 D_hat。
- 奖励只用结果标签：D_hat == D 给 1，否则给 0；不提供任何 step-level 监督。
- 用 GRPO 做 critic-free RL：同一输入采样一组 rollout，组内相对 advantage 作用于整个生成序列，包括 CoT、步骤标签和结果标签。
- 信息论分析给出核心条件：当结果较大程度由步骤正确性决定时，降低结果判断错误率会迫使 CoT 携带步骤正确性信息；这也解释了数学任务迁移强、Agent 任务迁移弱。
- 推理时直接把生成的 step_labels 当过程奖励用。

**关键实验**
- 数学 ProcessBench：TIPS-Qwen3-4B-Thinking-2507 仅用 3.2K 条结果标签轨迹达到 85.2 F1，超过 Qwen2.5-Math-PRM-72B（78.3）、GenPRM-32B（77.6）、GPT-5.4-Instruct（79.4）和 Claude-4.7-Opus（79.3），但低于 o1-mini（87.9）。
- Best-of-8 重排：TIPS-Qwen3-4B-Thinking-2507 在 GSM8K/MATH/College Math/OlympiadBench/Minerva 平均 73.3，高于 197K 规模 ImplicitPRM 的 68.8，接近 Pass@8 oracle 78.1。
- AgentProcessBench：三个基座平均 FirstErrAcc 均提升，thinking 模型增益更大（+5.4、+4.5），但整体弱于数学，说明结果-步骤耦合较弱时迁移有限。
- 消融显示 CoT 是关键：label-only 变体基础 F1 仅 47.5，RL 后几乎不涨；跨 DeepSeek-R1-distilled、Llama、SmolLM、Qwen 等 backbone 均有效。

**最值得记住的一句话**
过程监督可以从结果监督中“免费”涌现，前提是基座有思维链先验，且任务的结果-步骤耦合足够强。
