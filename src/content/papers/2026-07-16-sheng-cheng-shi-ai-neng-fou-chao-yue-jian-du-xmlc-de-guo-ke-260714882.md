---
title: Does generative AI supersede supervised XMLC? A Benchmark Study on Automated
  Subject Indexing with German Scientific Literature
title_zh: 生成式 AI 能否超越监督 XMLC？德国科学文献自动主题标引基准研究
authors:
- Maximilian Kähler
- Katja Konermann
- Lisa Kluge
- Markus Schumacher
affiliations:
- Deutsche Nationalbibliothek
arxiv_id: '2607.14882'
url: https://arxiv.org/abs/2607.14882
pdf_url: https://arxiv.org/pdf/2607.14882
published: '2026-07-16'
collected: '2026-07-18'
category: RecSys
direction: 多标签分类 · 长尾标签生成
tags:
- XMLC
- LLM
- Long-tail
- Subject Indexing
- Benchmark
- Multi-label Classification
one_liner: 在极多标签分类中，整体指标监督 XMLC 更强，但长尾与分级相关性上 LLM 生成式方法更优
practical_value: '- 电商商品打标存在大量长尾属性（如小众品类、风格标签），可尝试用 LLM 直接生成标签候选，再结合现有分类器做过滤或置信度控制，提升长尾覆盖率。

  - 对于标签体系极大（百万级）且分布极不均衡的场景，传统 XMLC 方法的二进制指标更优，适合高精度自动打标；LLM 生成在需要人工审校的分级相关性场景中更友好，可考虑混合流水线：先用
  XMLC 出高置信度标签，再用 LLM 补充长尾标签。

  - 论文中使用的 LLM 生成策略（如基于指令微调、少样本提示）可作为构建推荐系统标签生成模块的起点，尤其在冷门商品或新类目自动打标时，可快速冷启动。

  - 在评估阶段引入专业标注员的分级相关性判断，比单一自动评测更能反映业务真实价值。电商标签推荐也可设计类似人工评估环节，衡量标签的可用性而非仅命中率。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：德国国家图书馆需要对数万种德文科学文献自动分配受控主题词，标签集来自综合规范档（GND），规模高达百万级，且呈极端长尾分布。现有的监督式极多标签分类（XMLC）和新兴的生成式大语言模型（LLM）方法孰优孰劣，尤其在长尾标签上的表现，是馆藏自动化面临的关键问题。

**方法关键点**：
- 构建基准：收集最近十年德文科学文献的标题和文摘，与已有专家标引结果对齐。
- 对比方法：传统词汇匹配基线、多种基于 Transformer 的监督 XMLC 模型（如 XR-Transformer、X-Transformer 等），以及三种本文开发的 LLM 生成方法（微调德语 T5 模型直接生成标签、少样本提示 GPT 模型、以及将标签映射为数字编码的生成方案）。
- 评估双重：二元命中评价（与历史标引结果对比）和分级相关性人工评价（由专业图书馆员对推荐标签打分）。

**关键结果**：
- 在总体二元命中指标（如 Precision@k, Recall@k）上，基于 Transformer 密集特征的监督 XMLC 模型表现最佳。
- 但在长尾标签的命中率和人工分级相关性评估中，LLM 生成方法显著更优，尤其对出现频率极低的主题词，LLM 能给出更合理且被馆员采纳的建议。
- 单一方法无法全面胜出，混合策略可能是未来方向。
