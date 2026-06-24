---
title: 'MEMPROBE: Probing Long-Term Agent Memory via Hidden User-State Recovery'
title_zh: MEMPROBE：通过隐藏用户状态恢复审计 Agent 长期记忆
authors:
- Enze Ma
- Yufan Zhou
- Wei-Chieh Huang
- Jie Yang
- Huanhuan Ma
- Zixuan Wang
- Chengze Li
- Chunyu Miao
- Philip S. Yu
- Zhen Wang
affiliations:
- University of Illinois Chicago
- KU Leuven
- UC San Diego
arxiv_id: '2606.24595'
url: https://arxiv.org/abs/2606.24595
pdf_url: https://arxiv.org/pdf/2606.24595
published: '2026-06-23'
collected: '2026-06-24'
category: Eval
direction: Agent长期记忆的可审计评估
tags:
- Long-term Memory
- Agent Evaluation
- Memory Recovery
- Benchmark
- LLM Agent
- User State Reconstruction
one_liner: 将 Agent 记忆视为可审计产物，从遗留记忆重建隐藏用户状态，直接量化记忆质量
practical_value: '- **恢复审计评估**：对电商客服、推荐对话等 Agent 系统，定期从记忆库中重构已知用户属性（如偏好、历史事实），与真实值比对，而非仅看下游任务指标，直接暴露记忆质量。

  - **分离写入与检索诊断**：采用“全量导出（dump_all） vs 系统 top-k 检索”的双模式对比，快速定位是记忆写入遗漏还是检索索引不足，指导优化写入策略或检索模块。

  - **强化情景记忆绑定**：针对用户单次关键交互（如退货纠纷原因），要求记忆系统不仅存储事件表面，还要保留事件与后果的因果链，提升后续个性化推荐的上下文深度。

  - **检索感知的整合策略**：在写入时即考虑后续检索场景，将原始对话转化为简洁、可检索的结构化摘要，确保关键偏好能在有限的 top-k 召回中命中，避免“存储了却拿不出”的困境。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

### 动机
当前 Agent 长期记忆的评估几乎完全依赖下游行为（问答正确性、个性化回复质量），即便无记忆的 Agent 也能在这些指标上几乎饱和。这无法反映记忆系统真正形成的持久用户模型，也未能分离“证据写入”与“检索可达”两个关键环节。为直接衡量记忆本身，本文提出将记忆视为可审计的后交互产物，通过从 Agent 遗留记忆中重建隐藏的用户状态来评估记忆质量。

### 方法关键点
- **隐藏用户状态银行**：构建 50 个合成用户，每个携带 31 个隐藏维度（涵盖技能、知识、片段事件、自我模型、交互偏好），基于 O*NET、HEXACO 等真实来源生成，作为评测基准。
- **防泄漏任务生成**：每个维度对应一个日常协助任务，任务描述不得直接透露目标维度；通过盲审批评筛选，确保答案无法从任务本身直接猜出。
- **交互与记忆记录**：合成用户与配备记忆的 Agent 完成多轮对话，Agent 仅在交互过程中读写记忆，隐藏状态从不暴露。
- **双模式恢复评分**：交互结束后，从最终记忆库中用两种方式重建每个维度：全量导出（dump_all）和系统自身的 top-5 检索（retrieve）。通过填空模型+LLM 裁判给出 0–1 分，并计算类别平衡的恢复得分 \(B\)。
- **失败归因**：对低分维度进行三阶段归因，区分任务设计缺陷、Agent 诱导不足、用户模拟器过于保守或纯粹记忆故障。

### 关键结果
- 所有系统（包括无记忆基线）任务完成率均接近 100%，但全量恢复得分 \(B\) 仅在 0.61–0.62（amem、longctx_full、mem0），top-k 检索下更降至 0.47–0.54。
- 全量存储最强的 longctx_full 在检索模式下被 amem 反超，说明原始证据保留不等于可检索。
- 失败归因表明，多数不可恢复案例属于记忆故障（证据已出现但未写入或无法检索），存储的证据中有大量在检索时不可达。
- 类别难度分化：交互偏好类维度最易恢复，片段记忆（Episodic Memory）最难，其恢复率仅为偏好的 1/3~1/2，根源在于系统难以绑定事件与其因果后果。

**核心启示**：任务成功不代表形成了可恢复的用户状态，长期记忆需要从存储产物本身评估，并着力解决检索可达性与片段因果绑定的问题。
