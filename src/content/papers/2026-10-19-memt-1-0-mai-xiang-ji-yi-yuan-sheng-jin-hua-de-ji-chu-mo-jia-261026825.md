---
title: 'MemT-1.0: Towards Memory-Native Evolution'
title_zh: MemT-1.0：迈向记忆原生进化的基础模型架构
authors:
- Zhiyu Li
- Zeyu Zhang
- Linyun Liu
- Yiwei Bu
- Chenyang Xi
- Xichong Zhang
- Yi Yu
- Yu Yu
- Zhichen Liu
- Yuxiao Yi
affiliations:
- MemTensor Team
arxiv_id: '2610.26825'
url: https://arxiv.org/abs/2610.26825
pdf_url: https://arxiv.org/pdf/2610.26825
published: '2026-10-19'
collected: '2026-10-20'
category: LLM
direction: 记忆原生 LLM · MoS 扩展容量
tags:
- Memory-augmented LLM
- Gated DeltaNet-2
- Mixture-of-Storage
- Native Memory
- Stateful Inference
- Agentic Memory
one_liner: 提出 MemT-1.0，用 Gated DeltaNet-2 与 MoS 将记忆内化为模型原生状态，128K 历史下较 full KV cache
  提速 1.86×、存储降 66×
practical_value: '- 会话/用户记忆建模：用固定大小的 recurrent memory state 替代全量 session KV cache，适合电商导购
  Agent 的长期用户偏好、历史订单与多轮上下文压缩；持久状态可在多个 query 间复用，摊薄历史准备成本。

  - 训练方法：冻结推荐/对话 backbone，只训 memory 参数，用 full-context teacher 做 top-K KL 蒸馏 + CE；业务上可用线上完整上下文模型蒸馏出轻量记忆模块，避免重训大模型。

  - MoS dense routing：当记忆容量不够时扩展多个 memory expert，读写分开路由，比稀疏 MoE 更稳定；可用于用户分群/场景差异化的记忆写入与读取。

  - 经验内化：把检索到的成功操作流程（如售后、选品、谈判策略）写入 memory state 来指导多步 agent，而不是每次都塞进 prompt；可降低 token
  成本并提升行为一致性。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
长程交互、Agent 和个性化场景中，LLM 若依赖 full context 或 RAG，会面临 KV cache 线性增长、存储与延迟开销大、跨 session 信息难以持续积累的问题。MemT-1.0 的目标是把记忆变成模型原生计算的一部分，让模型在固定状态容量下持续读写历史，而不是每次重放原文。

**方法关键点**
- 架构：在保留 backbone 的前提下，在选定 Transformer block 旁路加入 Native Memory Block；动态 local memory 以多层矩阵状态保存在线信息，hyper memory 提供可训练投影与门控。
- 更新机制：用基于 Gated DeltaNet-2 的 stable token-level update 替代前代 token selection；erase/write/forget/readout gates 控制跨轮写入、衰减与读取。
- 容量扩展：Mixture-of-Storage (MoS) 将记忆状态扩展为 E 个 expert，dense 双路由共享地址，写入与读出分别加权，所有 expert 参与计算。
- 训练：先做 backbone preparation；两阶段训练，20B CPT + 14B post-training；用 full-context backbone 作为 teacher 做 off-policy top-K KL 蒸馏 + CE，只优化 memory 参数。
- 模型族：Nano 36B/3B active/10M memory；Flash 288B/17B active/336M memory。

**关键结果**
- 11 个记忆 benchmark 平均：Flash 50.6、Nano 47.0，分别超过最强 parametric baseline 12.5/8.9 分；但仍落后于显式上下文/检索的 textual memory。
- 效率：128K 历史下 Nano 端到端约 1.86× 加速，持久存储相对 full context KV 低 66×；256K 状态约 40 MiB，而 full context 为 5.061 GiB。
- Agentic coding：internalize 检索到的流程经验后，SWE-bench Verified/Multilingual 成功率与一致性超过无经验 agent，接近显式文本经验。
- 扩展性：post-training 两 epoch 内平均从 36.65 升到 46.80；MoS 4 experts 较 2 experts 后期平均提升 2.01–2.69 分。

**最值得记住的一句话**
固定容量的原生记忆状态替代线性增长的 KV cache，是长程 Agent/个性化系统降低存储与延迟、实现跨 session 持续学习的关键路径。
