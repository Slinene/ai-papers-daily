---
title: 'Towards Root Memories: Benchmarking and Enhancing Implicit Logical Memory
  Retrieval for Personalized LLMs'
title_zh: 根记忆：隐式逻辑记忆检索基准与增强框架
authors:
- Hongxun Ding
- Xiang Yu
- Chengbing Wang
- Jianfei Xiao
- Keqin Bao
- Wenjie Wang
- Xiangnan He
affiliations:
- University of Science and Technology of China
arxiv_id: '2606.23283'
url: https://arxiv.org/abs/2606.23283
pdf_url: https://arxiv.org/pdf/2606.23283
published: '2026-06-22'
collected: '2026-06-23'
category: Agent
direction: Agent 长程记忆 · 根记忆构建与路由
tags:
- Root Memory
- Implicit Logical Retrieval
- Personalized LLMs
- Memory Benchmark
- Agent Memory
- IMLogic
one_liner: 提出IMLogic基准与RootMem框架，构建可复用决策逻辑的根记忆，路由补足语义检索
practical_value: '- 构建用户根记忆单元：从历史会话提取抽象决策规则（如“用户养猫，推荐环境需考虑猫的安全”）及其证据，用于约束推荐，避免纯语义匹配导致的错误建议。

  - 采用LLM路由器动态激活相关根记忆：新查询到来时，用LLM判定触发哪些预设决策规则，低成本注入逻辑约束，无需全量检索原始记忆。

  - 记忆鲁棒性评测：借鉴IMLogic中“语义相似但逻辑无关”和“语义疏远但逻辑必需”的对抗样本构造法，建立内部评测集，检验搜索/推荐系统中记忆检索的推理能力。

  - 即插即用集成：RootMem可接入现有记忆系统（如embedding检索、图记忆），平均提升26%准确率，离线构建根记忆、在线仅路由，开销可控，适合工程落地。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

## 动机
个性化LLM的记忆检索主要基于语义相似度，容易忽略逻辑相关但语义距离远的记忆（如约束、动机或条件），导致错误推荐和用户信任下降。现有基准未充分评估这种“语义相似但逻辑无关”与“语义疏远但逻辑必需”的冲突。为此，该工作构建了首个针对隐式逻辑记忆检索的基准IMLogic，并提出根记忆框架RootMem。

## 方法关键点
1. **IMLogic基准**：从HaluMem数据集出发，用强LLM挖掘语义记忆(\(m_s\))与逻辑记忆(\(m_l\))对；通过Generator‑Judger‑Refiner多智能体协作生成查询，保证查询与\(m_s\)高语义重叠，但正确回答依赖\(m_l\)；最终包含20个长对话、15k+记忆条目和2,216个QA对。
2. **根记忆构建**：将碎片化历史对话蒸馏为结构化的根记忆单元\(\langle R_i, E_i \rangle\)，\(R_i\)为执行规则（何时及如何影响响应），\(E_i\)为个性化逻辑证据（支持规则的用户事实）。通过LLM抽取器周期性更新，控制单元数量以管理成本。
3. **根记忆路由**：在线推理时，LLM路由器根据查询评估每个根记忆单元的\(R_i\)，激活相关单元。将激活的根记忆与语义检索结果拼接，形成逻辑增强上下文，补足纯语义检索缺失的逻辑约束。

## 关键结果
- 在IMLogic记忆级多选题上，RootMem准确率55.23%，相比最强基线EverMemOS的Query Reconstruction+Reranker (43.41%)相对提升27.23%。
- 在对话级评测中，RootMem集成到MemOS、LightMem、EverMemOS，分别带来29.41%、33.77%、15.89%的相对提升，平均提升26.36%。
- 开放式生成场景下，RootMem仍显著提升性能，如LightMem从16.61%升至26.17% (+57.56%)。
- 消融表明路由器、执行规则和个性化证据缺一不可；框架可跨GPT‑4o‑mini、Qwen3‑30B、GLM‑4.6等骨干泛化。

> 根记忆将碎片化历史提炼为可复用的决策逻辑，通过路由激活补足语义检索，帮助模型恢复语义疏远但逻辑关键的约束。
