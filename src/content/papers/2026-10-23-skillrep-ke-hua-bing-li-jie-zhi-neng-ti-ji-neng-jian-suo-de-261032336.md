---
title: 'SkillRep: Characterizing and Understanding the Representation Design Space
  of Agent Skill Retrieval'
title_zh: SkillRep：刻画并理解智能体技能检索的表示设计空间
authors:
- Tianyi Sun
- Pengfei Yao
- Yanze Wang
- Hongda Chen
- Yunyun Han
- Jun Sun
- Chuanrui Hu
- Yafeng Deng
affiliations:
- EverMind, Shanda Group
- Peking University
- Southeast University
arxiv_id: '2610.32336'
url: https://arxiv.org/abs/2610.32336
pdf_url: https://arxiv.org/pdf/2610.32336
published: '2026-10-23'
collected: '2026-10-26'
category: Agent
direction: Agent技能检索 · 表示设计空间
tags:
- agent skill retrieval
- dense retrieval
- query expansion
- background projection
- embedding anisotropy
- hybrid retrieval
one_liner: 首个组合微调、双侧扩展、背景投影与BM25的0.6B技能检索器，SRA-Bench MRR@10领先7.02点
practical_value: '- 在召回/检索项目中，不要孤立评估 LLM 扩展、embedding 校准、BM25 融合；一定要在最强微调 encoder
  上做 leave-one-out/last ablation。论文显示微调会反转 training-free 模块排序：background projection
  从 +5.55 降到 +1.63，query-side expansion 从 +1.40 升到 +6.28。业务里可先用对比微调把双塔/商品 embedding
  校准好，再决定要不要做 query 扩展或去背景。

  - 混合检索优先用 score fusion（按 query 的 top-k 分数分布做 z-score 后线性加权），而不是 RRF。RRF 丢弃分数边界，稀疏通道可能推走
  dense 已高分但 margin 大的正确结果；这对电商搜索/推荐中 BM25 与双塔融合直接可迁移，建议保留 score 的置信度信息。

  - 三个诊断量可复用：background gap、coverage、dilution loss。上线 embedding 检索前，用它们判断是 query 表达不足、语料背景偏移、还是单向量稀释主导失败：前者补
  query expansion；中者做 background projection/whitening；后者考虑 passage-level indexing
  或增加 lexical channel。

  - LLM query 扩展的价值主要在补出目标文档的词，而非改写风格。做电商搜索 query 扩展/改写时，应让 LLM 生成包含商品属性词、卖点词的伪文档或
  pseudo-query，并按 IDF/类目词汇控制生成，避免泛词膨胀。'
score: 8
source: arxiv-cs.IR
depth: full_pdf
---

**动机**：LLM agent 依靠技能文档扩展能力，但请求与技能文档用途、措辞差异大；已有技能检索方法每次只采用一两个表示选择，无法判断组合后的增益，也从未量化“请求-技能差距”本身。

**方法**：SkillRep 在同一个检索器里组合五个表示选择：(1) 用合成 request–skill 对对比微调 Qwen3-Embedding-0.6B；(2) query-side LLM expansion：用 LLM 写两个 hypothetical skills，将请求向量按权重 0.3 向它们的均值移动；(3) document-side expansion：为每篇技能写伪请求，按权重 0.2 移动文档向量；(4) background projection：去掉文档矩阵前两个右奇异方向，再减去低 IDF 泛词方向；(5) BM25 稀疏通道，检索请求+hypothetical skills，并用 z-score 分数融合而非 RRF。新构建 UniPool：从公开注册表整合 111,247 个技能，并对 SRA-Bench gold 去近似重复。

**结果**：SRA-Bench official pool 上 MRR@10 79.21，比同尺寸最强 SkillReason 高 7.02 点，Hit@1 高 9.15；UniPool 上比 SkillSight 高 8.79。SkillsBench 6 项指标中 5 项最优。消融显示：微调收益最大，且会改变 training-free 模块价值排序——background projection 从 +5.55 降到 +1.63，query-side expansion 从 +1.40 升到 +6.28；四个 training-free 模块在 fine-tuned encoder 上重叠，在 untuned encoder 上互补。作者用三个量解释：background、unsaid vocabulary（coverage）和 dilution，并证明 query expansion 增益来自补出 gold skill 的词，BM25 通过计词恢复单向量稀释损失。

**最值得记住**：模块增益必须和底层编码器、以及它缩小的是哪个差距部分一起报告；缩小同一差距的模块重叠，缩小不同差距的模块互补。
