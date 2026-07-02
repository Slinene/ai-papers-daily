---
title: Hierarchical Experimentalist Agents
title_zh: 层次实验型智能体：通过主动实验进行上下文自我改进
authors:
- Abhranil Chandra
- Sankaran Vaidyanathan
- Utsav Dhanuka
- Varun Gandhi
- Scott Niekum
affiliations:
- University of Massachusetts Amherst
arxiv_id: '2606.29315'
url: https://arxiv.org/abs/2606.29315
pdf_url: https://arxiv.org/pdf/2606.29315
published: '2026-06-27'
collected: '2026-07-02'
category: Agent
direction: LLM Agent主动实验与技能学习
tags:
- Active Experimentation
- Skill Library
- In-context Learning
- Self-Improvement
- Physics Simulation
- Tool Use
one_liner: LLM通过主动实验动态学习可复用技能库，在未见物理任务中成功率从2%提升至77%
practical_value: '- **新场景主动探索机制**：在推荐或广告系统中，面对新用户群体或新品类时，可借鉴 HExA 的分层实验设计——高层规划探索方向（如尝试不同召回策略），低层执行具体干预并记录结果，形成可复用的“技能”模板（如特定人群的优惠券推送策略），避免盲目
  random AB test。

  - **在线学习技能库**：将推荐系统优化过程抽象为“技能”（如某类 CTR 提升技巧），每次实验后的成功策略存入上下文技能库，下次类似场景可直接组合调用，类似
  HExA 的 `learn_from_experience`，减少重复探索成本。

  - **跨场景技能迁移**：HExA 从简单物理任务中学习的技能可零样本迁移到困难任务（44% 成功率）。在推荐中，可在一个小流量域（如新频道）学到的有效策略（如冷启动物料组合方式）迁移至主域，降低冷启动成本。

  - **上下文技能组合**：HExA 通过上下文学习将实验产生的技能组合成复杂策略，业务中可用类似思路将多个简单推荐规则（召回、过滤、排序规则）作为可组合的“技能块”，Agent
  根据当前场景动态拼接，无需重新训练模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：当前 LLM Agent 依赖静态知识、搜索或检索，在全新领域（如复杂物理系统）中无法通过主动探索获取新知识，导致长周期任务失败。需要赋予 Agent 主动实验的能力。

**方法**：提出 HExA（层次实验型智能体），这是一个纯上下文、无训练的自我改进框架。它采用层次化结构：上层规划实验以回答查询或完成任务，下层调用工具执行实验并收集数据。关键组件包括：1）迭代实验设计，根据当前假设生成实验；2）从实验经验中学习可复用技能库（如某个操作的组合技巧），技能以自然语言形式存入上下文；3）整合实验证据决策或回答问题。整个过程无需监督信号、预言机或离线数据。

**结果**：在基于 PHYRE 2D 物理环境的 Interphyre 基准上，Claude Sonnet 4.6 在最难关卡仅 2% 成功率，HExA 将同一模型提升至 77%；开源模型亦有显著提升，并超越 ReAct、Reflexion 基线。仅使用从简单任务中学到的技能且不再主动实验时，HExA 仍获 44% 成功率，验证了技能的可重用与泛化能力。
