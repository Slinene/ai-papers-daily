---
title: 'GraphRAG on Consumer Hardware: Benchmarking Local LLMs for Healthcare EHR
  Schema Retrieval'
title_zh: 消费级硬件上的GraphRAG：本地部署LLM医疗EHR schema检索评测
authors:
- Peter Fernandes
- Ria Kanjilal
affiliations:
- California Polytechnic State University
arxiv_id: '2605.20815'
url: https://arxiv.org/abs/2605.20815
pdf_url: https://arxiv.org/pdf/2605.20815
published: '2026-05-20'
collected: '2026-05-24'
category: RAG
direction: GraphRAG本地部署可行性评估
tags:
- GraphRAG
- LLM
- Benchmark
- Local Deployment
- Knowledge Graph
- EHR
one_liner: 在8GB消费GPU上评测GraphRAG，发现7B以下模型无法完成管道，本地检索优于全局摘要
practical_value: '- 图谱RAG部署时，模型参数最好≥7B，否则结构化输出不稳定，易导致管道失败；对电商知识图谱等应用，选型要避开过小模型。

  - 本地检索（local retrieval）在延迟和事实准确性上均优于全局摘要，且幻觉更少，适合电商实时问答或隐私敏感场景，可优先采用。

  - 知识图谱实体丰富度与最终答案质量解耦，评估时需分开关注索引和生成阶段，不能仅凭图谱规模选模型。

  - 消费级GPU（8GB VRAM）足以运行GraphRAG全管道，为中小团队本地化部署生成式搜索或推荐系统提供了成本可行的参考。'
score: 6
source: arxiv-cs.IR
depth: abstract
---

**动机**：医疗EHR数据复杂且受隐私法规严格限制，依赖云端LLM带来成本、延迟及合规风险。需验证GraphRAG在消费级硬件上本地部署的可行性与模型选型标准。

**方法**：实现Microsoft GraphRAG管道，基于真实EHR schema文档，通过Ollama在单块8GB VRAM GPU上部署四个开源模型——Llama 3.1 8B、Mistral 7B、Qwen 2.5 7B、Phi-4-mini 3.8B。从索引效率、知识图谱质量、查询延迟、答案质量、幻觉率等维度，对比全局检索与本地检索两种模式。

**关键结果**：
- 参数<7B的模型无法可靠输出有效结构化数据，Phi-4-mini未完成管道，揭示GraphRAG存在实用容量阈值。
- Llama 3.1构建知识图谱最丰富（1,172实体），但最佳答案来自Qwen 2.5（3.3/5分），表明图谱规模与问答质量解耦。
- 本地检索在所有模型中均优于全局摘要：延迟降低，事实依据更扎实，幻觉明显减少。
- Mistral 7B出现退化重复行为，提示小型模型在结构化生成中的不稳定性。

结论：GraphRAG在消费级硬件上可行，但需谨慎选择≥7B的模型并优选本地检索策略。
