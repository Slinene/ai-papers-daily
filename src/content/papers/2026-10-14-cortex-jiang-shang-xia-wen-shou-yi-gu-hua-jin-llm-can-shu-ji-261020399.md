---
title: 'Cortex: Consolidating Context into Parametric Memory'
title_zh: Cortex：将上下文收益固化进 LLM 参数记忆
authors:
- Jintian Zhang
- Feng He
- Xinnian Liang
- Ziwen Xu
- Haoming Xu
- Haojing Huang
- Shuangzhi Wu
- Ningyu Zhang
affiliations:
- Zhejiang University
- ByteDance Seed
- Tsinghua University
arxiv_id: '2610.20399'
url: https://arxiv.org/abs/2610.20399
pdf_url: https://arxiv.org/pdf/2610.20399
published: '2026-10-14'
collected: '2026-10-15'
category: Training
direction: LLM 记忆固化 · 参数更新
tags:
- Memory Consolidation
- LLM
- FFN Update
- Continual Learning
- Knowledge Editing
- Distillation
one_liner: 用前瞻性重演与 FFN-only 低秩/结构化更新，把上下文增益蒸馏为可堆叠的参数记忆，兼顾 CR 与 RR
practical_value: '- **Agent 经验与临时规则沉淀**：可把商品知识、活动政策、API 文档、成功轨迹等上下文，先用冻结模型生成“预期查询+上下文条件回答”，再蒸馏到
  0.74M–2.73M 的小型 FFN adapter；无需把完整上下文塞进 prompt 或检索库，适合高频、确定性的商户规则/接口知识固化。

  - **架构选择**：只更新 FFN/MoE，冻结 attention、router 和 backbone；Structural 新增非线性通道比低秩 Synaptic
  更擅长代码/API 类可复用过程，且 MoE 用 shared branch 给所有 token 直接训练曝光，减少遗忘、提升 CR。

  - **训练目标 trick**：用 top-K_v 截断 KL + 对齐后 FFN hidden-state MSE 监督，teacher 带上下文、student
  不带；这对少样本、要保 base 能力的高保续更新很有效。历史 query replay 只留 query、不存 context，降低隐私和存储成本。

  - **落地边界**：CR/RR 的权衡在实体邻近知识上仍明显，组合推理/可移植性（portability）是短板；建议只固化高频、低歧义技能，开放生成仍保留
  RAG/prompt 兜底。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM 在上下文辅助下可显著提效，但上下文移除后增益消失；外部检索依赖召回质量，参数化记忆能让能力跨会话累积。论文将记忆巩固形式化：更新后模型无上下文时恢复上下文增益（CR），同时保留非目标能力（RR），统一知识编辑、技能学习、行为引导等任务。

**方法关键点**
- **前瞻重演**：用冻结的更新前模型，根据上下文生成预期查询和上下文条件回答，构造训练数据，不访问评测集。
- **更新位置**：仅 FFN/MoE。Synaptic 对现有投影加低秩增量；Structural 新增非线性通道；MoE 使用共享新增分支，提高每 token 训练曝光，router 冻结。
- **蒸馏目标**：teacher 带上下文、student 不带上下文，引入截断 top-K_v KL 与 post-FFN hidden-state MSE；历史 query replay 只保留 query，不存上下文。

**关键实验**
- 测试床覆盖 agent 经验、API 学习、persona 引导、知识抑制、事实编辑五类任务；backbone 4B–120B dense/MoE。
- 50 步连续事实编辑（Qwen2.5-14B）：Cortex-Structural CR 88.9%、RR 99.8%，每步新增参数仅 0.74M；显著超过 AlphaEdit、MEMIT、ROME 等基线。
- ALFWorld 上 CR 可超 100%，说明固化后可超过上下文提示；但 τ2-Bench 上表现仍弱，提示任务难度影响显著。

**最值得记住**：上下文收益可以蒸馏成小参数 FFN 更新，形成低存储、高保续的“参数化记忆”；核心瓶颈不在恢复本身，而在可移植性与邻近知识选择性。
