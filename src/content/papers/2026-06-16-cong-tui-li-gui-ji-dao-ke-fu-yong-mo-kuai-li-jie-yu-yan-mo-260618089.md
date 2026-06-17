---
title: 'From Reasoning Traces to Reusable Modules: Understanding Compositional Generalization
  in Language Model Reasoning'
title_zh: 从推理轨迹到可复用模块：理解语言模型推理中的组合泛化
authors:
- Lingjing Kong
- Xin Liu
- Guangyi Chen
- Martin Q. Ma
- Xiangchen Song
- Yuekai Sun
- Mikhail Yurochkin
- Taylor W. Killian
- Ruslan Salakhutdinov
- Kun Zhang
affiliations:
- Carnegie Mellon University
- Mohamed bin Zayed University of Artificial Intelligence
- Institute of Foundation Models
- University of Michigan
arxiv_id: '2606.18089'
url: https://arxiv.org/abs/2606.18089
pdf_url: https://arxiv.org/pdf/2606.18089
published: '2026-06-16'
collected: '2026-06-17'
category: Reasoning
direction: 训练与推理中的模块化组合泛化
tags:
- compositional generalization
- SFT
- RL
- latent modules
- reasoning
- training strategy
one_liner: 揭示SFT与RL在LLM推理中非对称互补：SFT提供模块原料，RL分解轨迹提取原子模块实现组合泛化
practical_value: '- **训练范式迁移**：在构建推荐/搜索Agent时，可先通过SFT用组合轨迹（如查询改写→检索→排序的完整链）覆盖所有原子技能，保证基础能力；再用RL重点训练SFT未见过的技能组合，提升泛化性。

  - **数据构建策略**：训练数据应避免只给孤立原子操作（如单独改写或单独排序），而应提供复合任务示例，实验证明复合训练比分离训练带来更强的组合泛化。

  - **RL Fine-tuning 设计**：RL阶段将奖励信号聚焦于新颖组合，鼓励模型探索原子模块的不同路由方式，可有效提升在未见过的搜索场景或用户意图下的表现。

  - **模块化推理架构**：在Agent工作流中可显式抽象出“技能（局部操作）”和“路由（信息选择与组合）”两级原子模块，便于模型复用和重组，降低新任务开发成本。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现代LLM推理能力的跃升依赖SFT与RL结合的后训练流程，但其成功机理尚无明确理论解释。本文提出组合泛化视角，将其形式化为层次化潜在选择模型。

**方法**：将推理轨迹建模为可复用原子模块的级联选择，模块分为“技能”（局部操作）与“路由”（信息选择与组合）。理论推导表明，SFT与RL角色不对称：SFT在组合轨迹中提供原始模块材料，RL则从复合轨迹中分解出潜在原子模块，从而实现组合泛化。通过受控实验验证该理论，设计任务包含不同原子技能的复合配置。

**关键结果**：① RL能够从SFT提供的复合轨迹中提取原子模块，并将其重组成解决新配置；② 在复合轨迹上训练比在孤立原子模块上训练具有更强的泛化能力；③ 有效训练协议：SFT通过组合轨迹确保所有原子模块的覆盖，RL聚焦SFT支持集之外的新颖组合以驱动探索。
