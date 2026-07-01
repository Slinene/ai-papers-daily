---
title: 'TheoremGraph: Bridging Formal and Informal Mathematics'
title_zh: TheoremGraph：桥接形式化与非形式化数学
authors:
- Simon Kurgan
- Evan Wang
- Eric Leonen
- Sophie Szeto
- Luke Alexander
- Artemii Remizov
- Jarod Alper
- Giovanni Inchiostro
- Vasily Ilin
affiliations:
- University of Washington Math AI Lab
arxiv_id: '2606.25363'
url: https://arxiv.org/abs/2606.25363
pdf_url: https://arxiv.org/pdf/2606.25363
published: '2026-06-23'
collected: '2026-07-01'
category: Other
direction: 数学知识图谱 · 形式化-非形式化链接
tags:
- Mathematics
- Dependency Graph
- Lean 4
- Graph Extraction
- Semantic Matching
- Dataset
one_liner: 构建统一语句级依赖图，连接非形式化数学文献与形式化库，发布提取工具与匹配数据集。
practical_value: '- 多源抽取与置信度标记策略：从非结构化文本（如商品描述、用户评论）提取实体关系时，可同时记录提取器来源，让下游按需权衡精度与覆盖率，适用于商品知识图谱构建。

  - 跨域实体对齐的轻量方案：将不同平台/模态的实体用生成式自然语言简短描述（slogan）映射到共享嵌入空间，通过余弦门控+LLM裁决筛选高置信度匹配，可用于跨电商站点的商品对齐或冷启动语义链接。

  - 图扩展（graph expansion）增强检索：在召回/排序阶段，利用知识图谱的一阶邻居扩展实体表征，不依赖昂贵重排模型即可接近有监督重排效果，适合低延迟推荐场景。

  - 工程化 MCP 接口与 API 设计：论文发布的 extractor、HTTP API、MCP 接口为构建内部可检索知识图谱工具链提供了可复用的架构参考。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：数学知识以语句及依赖关系为核心，但非形式化论文仅提供粗糙的文档级引用，形式化库虽有精细依赖却规模受限。为打通两者，需要构建统一的语句级依赖图。

**方法**：
- 非形式化侧：从 arXiv 数学论文中解析出 1170 万个定理环境，采用多种启发式抽取器恢复 1830 万条候选有向依赖边，每条边标注抽取器来源，供下游权衡精度与覆盖率。
- 形式化侧：开发 LeanGraph，在 Lean 4 编译器 elaborator 阶段提取依赖，覆盖 25 个 Lean 项目，产生 388,105 个声明节点和 1130 万条类型化边。
- 桥接两侧：为每个声明生成自然语言“slogan”，用嵌入模型映射到共享语义空间，通过余弦相似度链接；用 LLM 裁判验证，在 ≥0.8 余弦阈值得到 47,952 个匹配，阈值 ≥0.9 时裁判接受率 87%。

**关键结果**：
- 构建了目前最大的数学语句级统一依赖图。
- 在形式化概念检索任务上，用名字-签名表示加图扩展，Recall@10 达到 0.775，仅比使用 LM 重排的 LeanSearch v2（0.780）低 0.5 个百分点，且无需重排器。
- 完整发布数据集、抽取器、HTTP API 及 MCP 接口，支持数学搜索、归因与检索增强推理。
