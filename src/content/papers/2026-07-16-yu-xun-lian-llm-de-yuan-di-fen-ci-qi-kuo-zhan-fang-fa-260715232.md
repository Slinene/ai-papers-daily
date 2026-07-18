---
title: In-Place Tokenizer Expansion for Pre-trained LLMs
title_zh: 预训练 LLM 的原地分词器扩展方法
authors:
- Jimmy T. H. Smith
- Tarek Dakhran
- Alberto Cabrera
- Simon S. Lee
- Paul Pak
- Aditya Tadimeti
- Tim Seyde
- Maxime Labonne
- Alexander Amini
- Mathias Lechner
affiliations:
- Liquid AI
arxiv_id: '2607.15232'
url: https://arxiv.org/abs/2607.15232
pdf_url: https://arxiv.org/pdf/2607.15232
published: '2026-07-16'
collected: '2026-07-18'
category: Training
direction: LLM 分词器工程 · 多语言高效推理
tags:
- tokenizer expansion
- multilingual
- on-device
- embedding initialization
- continued pre-training
- BPE
one_liner: 通过继续 BPE 合并和两阶段微调，无需重训即可扩展分词器，将低资源语言 token 数压缩 2-4 倍，解码提速 2.2-3.7 倍
practical_value: '- 需要支持新语言或新增领域词汇（如电商术语、产品 ID）时，可沿用原分词器继续做 BPE 合并，避免重建词典和重新预训练

  - 新 token 嵌入用已有子 token 嵌入的均值初始化，能加速收敛，此技巧可迁移到推荐系统新增 Semantic ID token 的场景

  - 两阶段适应：先冻结主干仅训练嵌入层，再全模型继续预训练，可降低迁移成本，适合在线模型热更新

  - 端侧部署的推荐 Agent 或对话模型可通过分词器扩展减少 token 碎片，直接降低解码延迟与能耗'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：预训练 LLM 的分词器通常按早期语料分布分配词汇，后期加入的语言（如印地语、泰语）会被过度切分，导致 token 数暴增，推高延迟和计算开销。这对端侧紧凑模型尤为严重，因为嵌入层参数占比较高，增大词汇表会显著增加单 token 解码带宽。

**方法**：提出原地分词器扩展方案。在现有 BPE 合并规则基础上，用多语言语料继续合并，确保原有 token 绝大多数保留，新 token 能精确分解为已有子 token。嵌入层：保留 token 的原始嵌入直接复制，新 token 嵌入用其子 token 嵌入的均值初始化。训练分两步：先只训练嵌入层，再全模型继续预训练，以恢复原始检查点质量。

**结果**：在 LFM2-8B-A1B（8B MoE）模型上将分词器从原词汇量扩展到 128K，印地语和越南语 token 数分别减少约 2.4 倍和 2.6 倍，泰语最高达 4.0 倍。综合大词汇表带来的单 token 成本，估算这些语言每字符解码速度提升 2.2–3.7 倍。发布模型权重与分词器，并记录了反面的调优经验。
