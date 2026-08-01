---
title: 'Filesystem-Based Memory for LLM Agents: Organization, Evolution, and Sustainability'
title_zh: 基于文件系统的LLM智能体记忆：组织、演化与可持续性
authors:
- Sizhe Zhou
- Sheldon Yu
- Hui Wei
- Junda Wu
- Siru Ouyang
- Yizhu Jiao
- Shijia Pan
- Julian McAuley
- Yu Zhang
- Tong Yu
affiliations:
- University of Illinois Urbana-Champaign
- University of California San Diego
- University of California Merced
- Adobe Research
- Texas A&M University
arxiv_id: '2607.26637'
url: https://arxiv.org/abs/2607.26637
pdf_url: https://arxiv.org/pdf/2607.26637
published: '2026-07-28'
collected: '2026-08-01'
category: Agent
direction: Agent记忆系统设计与评估
tags:
- Agent Memory
- Filesystem
- Organization
- Search Economy
- LLM Agents
- Tool Design
one_liner: 系统探索文件系统记忆，证明组织能显著降低检索成本，但难以维持且无法直接提升答案质量
practical_value: '- 在构建客服/导购Agent记忆时，可直接采用文件系统存储用户历史与知识，利用层次化目录降低大规模记忆的检索token成本（实验中减半）。

  - 将记忆管理拆分为专门的管理智能体，定期合并、更新记忆文件，避免记忆膨胀；但需选用强模型（如GPT-4级）作为管理智能体，否则组织会逐渐恶化。

  - 工具集设计对记忆结构影响不亚于模型本身，应提供可靠的沙盒文件操作环境（ls, grep, cat等），暴露清晰的读写接口，让Agent自主组织。

  - 当前阶段，过度追求完美组织不一定提升下游任务准确率，可优先优化检索效率，待基础能力成熟后再探索组织与答案质量的联动。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM智能体常直接用文件系统目录树管理长期记忆，但缺乏系统性验证：智能体能否在记忆积累、冲突和失效时维持组织？这种组织是否真的带来收益？本文首次对该默认设定进行实证探索。

**方法关键点**：将记忆文件系统操作拆分为三个角色——管理智能体整合与组织输入内容，搜索智能体基于记忆回答查询并引用来源，执行智能体提供任务轨迹并蒸馏为技能文件，实现陈述性记忆与技能的统一存储。在长期对话和具身任务基准上，系统变化记忆形状（智能体组织的层级结构、原始转储、分块检索）、事件流规模、工具套件（沙盒Shell、记忆工具函数、不同搜索工具）以及管理/搜索智能体的强弱，监控回答质量、成本与存储健康度随记忆增长的变化。

**关键结果**：组织化存储在大规模素材下将检索成本约减半，显示‘搜索经济’收益。但除最强管理智能体外，所有设置下组织程度均随记忆增长而衰退；并且无论管理智能体多强，组织本身未能转化为更好的回答质量。此外，仅改变工具集（如从纯Shell到结构化函数）即可像更换模型一样显著重塑存储结构。
