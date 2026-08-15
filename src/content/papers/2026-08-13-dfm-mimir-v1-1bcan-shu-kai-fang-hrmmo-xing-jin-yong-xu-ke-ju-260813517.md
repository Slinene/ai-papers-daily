---
title: 'DFM Mimir v1: An Open HRM Delivering Frontier Performance at 1B Parameters
  Using Only Permissible Post-Training Data'
title_zh: DFM Mimir v1：1B参数开放HRM模型，仅用许可数据达前沿性能
authors:
- Peter Schneider-Kamp
- Jacob Nielsen
- Gianluca Barmina
- Kenneth Enevoldsen
- Lukas Galke Poech
affiliations:
- University of Southern Denmark
- Ordbogen A/S
- Aarhus University
arxiv_id: '2608.13517'
url: https://arxiv.org/abs/2608.13517
pdf_url: https://arxiv.org/pdf/2608.13517
published: '2026-08-13'
collected: '2026-08-15'
category: Training
direction: 1B参数开放HRM语言模型
tags:
- HRM
- 1B LLM
- permissible data
- Danish
- open-source
- post-training
one_liner: 用HRM架构与161个许可数据集训练1B模型，英语有竞争力并刷新丹麦语SOTA
practical_value: '- **合规数据策略可落地**：业务中常受用户隐私、版权数据限制；Mimir 用 161 个许可数据集训出 1B 可竞争模型，说明「只使用许可数据」不必然牺牲性能。电商/广告团队可优先构建高质量合规数据集（如平台内脱敏行为、商品描述、客服会话）做模型训练或微调。

  - **小模型 + 高效架构值得关注**：HRM 使 1B 参数接近 4B 性能，若其层级推理能降低解码步数或提升推理效率，适合线上生成式推荐/Agent 的低延迟约束；可试验类似层级生成语义
  ID 或分步 query 生成。

  - **多语言混合训练启示**：针对小语种或垂直域数据稀缺，将稀缺语言与高资源语言任务混合训练能提升目标语言表现；跨境电商、多语言 query 推荐可借鉴。

  - **完全开放基座便于快速验证**：Hugging Face 可直接获取，合规风险低，适合作为多语言业务原型的基座模型，快速测试 prompt/微调效果。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

现有 LLM 训练常依赖大规模不可许可数据，抬高开放/合规模型研究门槛；丹麦基础模型项目需要纯许可数据下从零训练可用的基座模型。

**方法关键点**
- 采用 Hierarchical Reasoning Model (HRM) 架构，1B 参数，从零训练，仅用许可后训练数据。
- 混合 161 个数据集，覆盖英语、数学/代码、丹麦语三类能力，在 20 个基准上评测。

**关键结果**
- 全面超越原始 HRM-Text 1B；与更大模型 Qwen 3.5 4B、Gemma 4 E2B 竞争。
- 英语达到强竞争力，丹麦语刷新 SOTA。
- 模型已在 Hugging Face 开放。
