---
title: Synthesize and Reward -- Reinforcement Learning for Multi-Step Tool Use in
  Live Environments
title_zh: 合成并奖励：面向在线环境的多步工具调用的强化学习
authors:
- Ibrahim Abdelaziz
- Asim Munawar
- Kinjal Basu
- Maxwell Crouse
- Chulaka Gunasekara
- Suneet Katrekar
- Pavan Kapanipathi
affiliations:
- IBM Research
arxiv_id: '2606.03892'
url: https://arxiv.org/abs/2606.03892
pdf_url: https://arxiv.org/pdf/2606.03892
published: '2026-06-02'
collected: '2026-06-03'
category: Agent
direction: Agent 多步工具使用 · 强化学习奖励设计
tags:
- Tool Use
- Reinforcement Learning
- Multi-turn Tool Calling
- Programmatic Reward
- GRPO
- MCP
one_liner: 提出 PROVE 框架，通过 live MCP 环境、状态感知合成与无 judge 的多组件程序化奖励，用 RL 提升多步工具调用
practical_value: '- **状态感知的数据合成**：通过依赖图和 live 状态采样生成多轮轨迹，确保参数引用真实实体，避免合成数据不可执行，可直接用于训练电商
  Agent（如查询商品、下单、退款）。

  - **无 judge 的分解式程序化奖励**：将奖励拆分为有效性、覆盖率、效率惩罚、工具名奖励、参数值匹配，不需要 LLM judge。效率惩罚采用复杂度自适应的调用预算，能抑制模型无意义的多余工具调用，对生成式推荐的多步骤控制有直接参考价值。

  - **适应性效率惩罚**：根据任务所需的 ground-truth 调用数动态设置预算（B = n_gt + ceil(n_gt * 0.5)），超过预算才受罚，既鼓励探索又避免冗余，这种设计可以迁移到多步
  Agent 的步骤数约束。

  - **RL 训练优于 SFT**：用相同数据做 SFT 会导致 τ2‑bench 性能下降，而 RL 保持提升，说明执行反馈和奖励信号对多步对话行为至关重要，提示我们应在实际业务中耦合
  RL 训练循环而非单纯依赖 SFT。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**：训练 LLM 完成多步工具调用（选对 API、填对参数、处理依赖）是部署自主 Agent 的关键挑战，但现有方法存在三重障碍：执行环境多用静态缓存，缺少状态相关的失败模式；合成查询常脱离服务器实际状态，导致工具调用无法执行；单纯基于召回覆盖率（recall）的奖励会激励模型发出冗余调用。

**方法**：提出 PROVE 系统，由三个部分组成：
1. **20 个有状态 MCP 服务器**：覆盖金融、生产力、商业、旅行等领域，共暴露 343 个工具，提供会话级状态隔离，既用于数据合成也用于 RL 训练。
2. **状态感知合成管线**：自动发现工具依赖图，采样 live 服务器状态作为实体约束，通过状态机驱动教师 LLM 生成多轮对话并重放验证，产生约 13K 训练样本（含多轮 MCP 对话、澄清对话和拒答样本），无人工标注。
3. **五组件程序化奖励**：有效性（分三级判断：函数名存在、参数齐全、执行成功）、覆盖率（按依赖顺序匹配 GT 步骤）、适应性效率惩罚（根据 GT 调用数给予弹性预算，超出即罚）、工具名奖励（奖励选择正确的工具名称）、参数值匹配奖励（对齐正确的参数值）。最终奖励为这五项加权求和，权重固定，无需外部 judge 模型。

**实验**：在 Qwen3‑4B、Qwen3‑8B、Qwen2.5‑7B、Granite‑4.1‑8B 四个基模型上使用 GRPO 训练 350 步，仅调学习率，训练数据 13K。BFCL Multi‑Turn 上 Qwen3‑4B 提升 10.2 点，τ2‑bench 上 Qwen2.5‑7B 提升 6.8 点，T‑Eval 上 Qwen2.5‑7B 提升 6.5 点；所有模型在 τ2‑bench 无退化，而相同数据做 SFT 会让多数模型在该基准下降。奖励消融表明，适应性效率预算和工具名信号最重要，移除二者各造成约 9 点总指标下降。

**关键结论**：一个紧凑的、完全程序化的奖励，结合 live 环境和状态感知合成数据，可以一致地提升多步工具调用能力，无需大规模数据流水线或昂贵 judge 模型。
