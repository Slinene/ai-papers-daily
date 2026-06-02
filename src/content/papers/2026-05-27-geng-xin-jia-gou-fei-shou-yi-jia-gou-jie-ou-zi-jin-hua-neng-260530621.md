---
title: 'Harness Updating Is Not Harness Benefit: Disentangling Evolution Capabilities
  in Self-Evolving LLM Agents'
title_zh: 更新架构非受益架构：解耦自进化LLM智能体的两种核心能力
authors:
- Minhua Lin
- Juncheng Wu
- Zijun Wang
- Zhan Shi
- Yisi Sang
- Bing He
- Zewen Liu
- Tianxin Wei
- Zongyu Wu
- Zhiwei Zhang
affiliations:
- The Pennsylvania State University
- UC Santa Cruz
- Amazon
- Emory University
- UIUC
arxiv_id: '2605.30621'
url: https://arxiv.org/abs/2605.30621
pdf_url: https://arxiv.org/pdf/2605.30621
published: '2026-05-27'
collected: '2026-06-02'
category: Agent
direction: 自进化LLM智能体能力解耦分析
tags:
- Self-Evolving Agents
- Harness Engineering
- Capability Analysis
- LLM Agents
- Instruction Following
one_liner: 揭示模型更新外部架构（harness-updating）与受益能力（harness-benefit）分别与基础能力脱钩，并指出弱模型受益低源于架构激活与遵循失败。
practical_value: '- **将算力与优质模型优先分配给任务执行 agent，而非 evolver**：evolver 模型产生的最终增益差异最多仅
  3.1 个百分点，且不单调依赖模型规模；post-evolution 性能主要受 agent 基础能力支配。

  - **针对弱模型 agent 强化“架构激活”训练**：弱模型（如 Qwen3-32B）的技能加载率仅 25.1%，常因多键格式错误而失败；应设计严格单键的加载动作，或在训练中显式学习“主动查询并注入
  harness 组件”的元动作。

  - **增强长时域指令遵循能力以维持架构指导**：弱模型加载技能后，沿轨迹遵循度从 0.52 骤降至 0.13；可在训练中加入轨迹级指令一致性奖励，或采用分阶段验证来维持
  adherence。

  - **简化架构交互协议以降低工程摩擦**：将 harness 调用设计为显式、单键、机器易解析的动作（如 `load_skill` 独立 key），避免与推理内容混合，可提升弱模型的激活成功率。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
LLM Agent 越来越多地通过外部架构（prompts, skills, memories, tools）来执行任务，自进化方法能通过历史执行证据自动更新这些架构以提升性能。然而，现有评级只关注端到端增益，未能区分“产生有效架构更新”的能力（harness-updating）与“从更新中受益”的能力（harness-benefit），不清楚哪种模型擅长哪一环节。本文对两种能力进行解耦分析，揭示其与模型基础能力的非直观关系，为 agent 系统设计提供依据。

**方法关键点**  
- 形式化 harness-self-evolution 协议：固定模型权重，通过迭代执行任务、收集执行证据、调用 evolver 更新 harness 来实现。  
- 定义 harne​​ss-updating 度量：固定一组锚定 agent，计算 evolver 在不同 agent 上的平均增益。  
- 定义 harne​​ss-benefit 度量：固定一组锚定 evolver，计算 agent 在不同 evolver 下的最大增益。  
- 在三类基准（SWE-bench Verified、MCP-Atlas、SkillsBench）上，对 6/7 个模型（Claude Opus 4.6、Sonnet 4.6、Haiku 4.5、Qwen3-235B、Qwen3-32B、Qwen3.5-9B、GPT-OSS-120B）进行全配对实验。
- 针对弱模型受益不足的现象，开展了 harness 激活率、遵循率、轨迹阶段遵循度等细粒度诊断。

**关键实验结果**  
- **harness-updating 与基础能力几乎扁平**：不同 evolver 产生的增益差异最多 3.1 个百分点，Qwen3.5-9B 的更新效果与 Opus 4.6 相当，甚至在某些任务上领先。  
- **harness-benefit 非单调**：中等基础能力模型获益最大（如 Qwen3-235B 在 SWE 上 +19.3pp），而弱模型（Qwen3-32B +4.4pp）和强模型（Opus 4.6 +2.6pp）增益偏低。  
- **弱模型两大失败模式**：① 架构激活失败——技能加载率仅 25.1%，常因多键请求格式错误；② 架构遵循失败——加载后遵循率仅 14.2%，且随轨迹推移遵循度急剧下降（0.52→0.13），强模型则稳定（0.89→0.80）。  
- 最终性能由 agent 基础能力主导，同一 agent 变体 evolver 的得分差异远小于不同 agent 间的性能鸿沟。
