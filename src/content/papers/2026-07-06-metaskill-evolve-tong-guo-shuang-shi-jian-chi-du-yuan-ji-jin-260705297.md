---
title: 'MetaSkill-Evolve: Recursive Self-Improvement of LLM Agents via Two-Timescale
  Meta-Skill Evolution'
title_zh: MetaSkill-Evolve：通过双时间尺度元技能进化实现 LLM Agent 递归自改进
authors:
- Zefeng Wang
- Minxi Yan
- Jinhe Bi
- Sikuan Yan
- Volker Tresp
- Yunpu Ma
affiliations:
- LMU Munich
- The Chinese University of Hong Kong
- MCML
- MemAgents Lab
arxiv_id: '2607.05297'
url: https://arxiv.org/abs/2607.05297
pdf_url: https://arxiv.org/pdf/2607.05297
published: '2026-07-06'
collected: '2026-07-07'
category: Agent
direction: Agent 递归自改进 · 双时间尺度进化
tags:
- agent self-improvement
- meta-skill
- two-timescale
- LLM agents
- recursive self-improvement
- skill evolution
one_liner: 提出双时间尺度框架，让 Agent 的任务技能和元技能（改进流程）都能递归自进化，提升长程任务表现
practical_value: '- **技能文件自动演进**：可将推荐对话 Agent 的回复策略、多轮流程写为 Markdown 技能文件，由 Agent 根据交互反馈自我反思、改写，减少人工维护成本

  - **双层进化机制**：慢速更新“如何改进”的元技能（分析/检索/分配/提议/进化配置），快速更新具体任务技能，使 Agent 能适应不同任务分布，可迁移到推荐策略的自适应优化

  - **单一冻结模型复用**：整个改进流水线共享一个冻结 LLM，无需额外训练，适合线上部署 Agent 快速迭代实验

  - **整体借鉴**：在推荐/搜索场景中，为 Agent 引入可编辑的技能库，并记录执行轨迹，用 LLM 从失败案例自动提炼改进规则，实现持续自提升'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent 面临长程开放任务时，固定的手写技能文件无法适应任务多样性。现有 Agent 自改进（如 EvoSkill、GEPA）仅优化任务技能（做什么），而改进流程（如何改进）始终保持不变，限制了适应能力。

**方法**：提出 MetaSkill-Evolve，一个双时间尺度递归自改进框架。每个任务分支携带一个任务技能 \(s\) 和一个分支局部元技能 \(m=(\psi,\sigma,\alpha,\pi,\varepsilon)\)，五个分量分别参数化分析器、检索器、分配器、提议器和进化器这五个流水线代理。任务技能在快速循环中依据执行踪迹自我重写，元技能在更慢的循环上应用同一流水线作用于自身进行进化，无需额外模型或目标。所有流水线代理共享一个冻结的主干 LLM。

**结果**：在 OfficeQA、SealQA、ALFWorld 三个 Agent 基准上，相比无技能、静态技能和单层进化基线均有显著提升，测试准确率相对原始主干分别提高 **+23.54、+16.09 和 +1.92 个百分点**，验证了递归元技能进化的有效性。
