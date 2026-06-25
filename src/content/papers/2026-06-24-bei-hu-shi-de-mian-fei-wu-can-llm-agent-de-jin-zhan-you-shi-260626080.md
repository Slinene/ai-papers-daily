---
title: 'Neglected Free Lunch from Post-training: Progress Advantage for LLM Agents'
title_zh: 被忽视的免费午餐：LLM Agent 的进展优势
authors:
- Changdae Oh
- Wendi Li
- Seongheon Park
- Samuel Yeh
- Tanwi Mallick
- Sharon Li
affiliations:
- University of Wisconsin–Madison
- Argonne National Laboratory
arxiv_id: '2606.26080'
url: https://arxiv.org/abs/2606.26080
pdf_url: https://arxiv.org/pdf/2606.26080
published: '2026-06-24'
collected: '2026-06-25'
category: Agent
direction: Agent 过程评估 · 优势函数
tags:
- Progress Advantage
- Process Reward Model
- LLM Agents
- Reinforcement Learning
- Uncertainty Quantification
- Test-Time Scaling
one_liner: 从 RL 后训练中直接提取策略与参考策略的对数概率比作为隐式过程奖励，无需训练专用奖励模型。
practical_value: '- **零成本过程评估**：直接使用 RL 微调后 checkpoint 与其参考 checkpoint（如 base 模型）的
  log概率比作为每步动作的进展优势，可替代昂贵且难以泛化的过程奖励模型训练，适合电商场景下多轮对话、工具调用等 agent 轨迹的实时监控。

  - **Best-of-N 采样提升成功率**：在需要探索温度高、重试多次的任务（如对话式客服、复杂搜索流程）中，使用进展优势对候选轨迹评分并选择最佳轨迹，可显著提升任务完成率，实验在
  τ2-Airline 等 agent 基准上超越专门训练的奖励模型。

  - **Agent 轨迹不确定性量化**：将轨迹级进展优势作为成功的预测信号，可在无额外训练下准确判断 agent 交互是否可能失败，用于风险控制或在线干预；实验在多个模型上
  AUROC 达 0.865，优于置信度基线和预训练 PRM。

  - **故障步骤定位**：在多智体或工具调用链条中，通过最小化每步进展优势来定位导致失败的关键步骤，辅助线上问题诊断和信用分配，几乎达到专门训练方法的精度。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
构建面向 LLM Agent 的过程奖励模型（PRM）面临严峻挑战：交互轨迹长、动作不可逆、环境反馈随机，使得人工标注和蒙特卡洛估计均不可行。而现有隐式过程奖励方法仅适用于确定性推理任务，无法直接用于随机 MDP 的 agent 场景。研究希望找到一种无需额外训练、直接可用的过程级信号，以支持推理时的轨迹评分、不确定性估计和故障诊断。

**方法关键点**
- **进展优势定义**：在 KL 正则化或裁剪式 RL 后训练下，最优策略 π̃* 与参考策略 π_ref 的对数概率比  \( \beta \log \frac{\tilde{\pi}^*(a|s)}{\pi_{\text{ref}}(a|s)} \) 精确等于最优优势函数 A*(s,a)，即使在环境状态转移随机的 MDP 中也成立（命题1）。
- **无需专用训练**：该信号天然存在于标准 RL 流水线产出的 checkpoint 对中，覆盖 GRPO、DAPO 等主流算法（命题2）。
- **聚合策略**：可对 token 级进展优势进行求和、平均、极值或位置加权，形成步级或轨迹级评分，适配不同下游任务。
- **参考策略选择**：参考策略与行为策略的距离需适中，可通过模型合并方法（如 TIES）微调参考，提升信号质量。

**关键实验与结果**
- **基准测试**：覆盖 BFCLv4-MT、WebShop、AgentDojo、τ2-bench（Airline/Retail）四个 agent 基准，以及 Gemma4-4B、Qwen3.5-9B、Qwen3-14B、Olmo3-7B 四个模型家族。
- **推理时扩展（Best-of-8）**：进展优势平均将成功率提升至 38.8%（Gemma4）和 62.1%（Qwen3.5），分别超出最佳训练奖励模型 15.5% 和 11.3%，在需要探索温度的任务上优势显著。
- **不确定性量化**：τ2-Airline 上轨迹级 AUROC 达 0.865（Gemma4），超越所有基线（包括 Claude Sonnet-4.6 和 ThinkPRM），说明其可作为可靠的失败预测信号，且能外推至不同策略生成的轨迹。
- **故障归因**：在 Who & When 基准上定位关键错误步，准确率接近专门训练的 AgenTracer，证明其细粒度信用分配能力。
- **消融分析**：仅用单一策略的对数概率效果远差于进展优势，聚合方式（如取 min 或 max）对任务敏感，参考策略距离需通过 merging 调优。

**核心结论**
进展优势提供了一个理论上坚实且工程上即插即用的过程级评估信号，使得 RL 后训练产出的策略对天然具备“免费”的 PRM 能力，可广泛用于 agent 系统的推理时监控与优化。
