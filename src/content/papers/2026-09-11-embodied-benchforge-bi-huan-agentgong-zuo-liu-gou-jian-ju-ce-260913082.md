---
title: 'Embodied-BenchForge: A Closed-Loop Agentic Workflow for Embodied Benchmark
  Construction'
title_zh: Embodied-BenchForge：闭环Agent工作流构建具身评测基准
authors:
- Baoyang Jiang
- Fengchun Zhang
- Leyuan Wang
- Haotian Li
- Yida Wang
- Zhe Ji
- Jinshan Lai
- Xi Ren
- Danyang Li
- Zheng Yang
affiliations:
- QiYuan Lab
- University of Electronic Science and Technology of China
- Beijing University of Posts and Telecommunications
- Northeastern University
- Beihang University
arxiv_id: '2609.13082'
url: https://arxiv.org/abs/2609.13082
pdf_url: https://arxiv.org/pdf/2609.13082
published: '2026-09-11'
collected: '2026-09-14'
category: Agent
direction: Agent工作流 · 基准构建自动验证修复
tags:
- Closed-Loop Benchmark Synthesis
- Artifact Dependency Graph
- Verification & Repair
- Skill Orchestration
- LLM Agent
one_liner: 提出闭环基准合成框架，用产物依赖图与需求引导验证修复，自动构建可区分的具身评测基准
practical_value: '- **产物依赖图 + 局部重执行**：在长链路生成流水线（如评测数据合成、商品描述多步生成）中维护中间产物依赖，失败时根据 provenance
  只重跑受影响节点，避免全量重建，显著节省成本与时间。

  - **需求引导的逐级验证契约**：为每个中间产物定义可检查的 schema/领域约束，在传入下游前自动验证，防止局部错误传播。可以直接迁移到 RAG 的文档切分、query
  改写、素材标注等环节。

  - **可复用技能编排**：把类型化技能组合成可执行工作流，跨任务复用同一技能库，适合搭建电商场景下的 Agent 工作流（如选品-文案-投放链路），降低重复开发。

  - **闭环验证-修复循环**：生成后自动评估并触发修复，能提升生成式推荐中 Semantic ID 或商品描述等内容的可用率，可作为数据质量飞轮。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：现有 Agent 基准构建方法要么只覆盖孤立阶段，要么绑定预设环境；多步构建产生的中间产物缺少针对性验证，局部缺陷会传播到最终基准。

**方法关键点**：将基准构建形式化为闭环基准合成，包括前向产物合成与后向验证修复。技能编排的产物合成把类型化、可复用技能组合为可执行工作流；产物依赖图记录中间输出及依赖关系。需求引导的验证修复对每个产物应用特定契约，失败时借助 provenance 触发局部重执行或上游回滚。

**关键结果**：构建了 6 个离线 EQA 基准和 1 个包含 220 个可执行任务的交互基准。在代表性 MLLM 和具身 Agent 上评估显示基准能区分模型的观察理解与闭环执行能力。消融实验验证验证与修复模块有效；修复分析表明局部恢复高效，技能复用分析显示跨基准可复用性。
