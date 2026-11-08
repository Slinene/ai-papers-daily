---
title: 'Benchmarking Large Language Models on Heterogeneous Cognitive and Biomedical
  Knowledge Graphs: The Role of Graph Grounding in Multi-Hop Reasoning and Hallucination
  Mitigation'
title_zh: 异构认知与生物医学知识图谱上的大语言模型基准测试：图接地在多跳推理与幻觉缓解中的作用
authors:
- Ali Sarabadani
- Kheirolah Rahsepar Fard
- Tahereh Jeirani
arxiv_id: '2611.08315'
url: https://arxiv.org/abs/2611.08315
pdf_url: https://arxiv.org/pdf/2611.08315
published: '2026-11-05'
collected: '2026-11-08'
category: Reasoning
direction: LLM 知识图谱多跳推理与幻觉缓解
tags:
- LLM
- Knowledge Graph
- Multi-hop Reasoning
- Hallucination
- Graph Grounding
- Benchmark
one_liner: 基准五个 LLM 在五个异构 KG 上的多跳推理，发现图接地降低幻觉且通用模型优于专用模型
practical_value: '- 在电商推荐或 Agent 系统中，用商品/用户/内容知识图谱对 LLM 输出做接地（graph grounding），可显著降低多跳查询中的幻觉率，尤其适合跨域关系链（如商品-品牌-功效-人群）。

  - 不必优先训练领域专用小模型：通用大模型 + 结构化知识检索在多跳推理上更可靠；若算力受限，可先采用通用模型 API 加本地图数据库，而非微调垂直模型。

  - 设计多层级查询集（从单跳、双跳到多跳）评估业务中 LLM 的知识图谱推理能力，明确性能衰减点，据此决定是否需要混合神经符号架构（LLM 做语义解析，图遍历/符号推理做精确关系链）。

  - 可借鉴其标注一致性框架（Cohen''s kappa / Fleiss'' kappa）来验证自建知识图谱问答数据集的标注质量，保证评估可信度。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：LLM 在生物医学与认知神经科学中应用增多，但其在异构、多关系知识图谱上的可靠推理能力尚不明确，尤其在多跳查询和事实一致性方面。

**方法关键点**：基准测试五个 LLM（GPT-5.1、Gemini 2.0 Pro、Llama 3、Qwen、BioGPT）在五个 KG（DrugBank、NeuroSynth、Cognitive Atlas、Brain Map、GDPKG）上的表现。引入多层级查询数据集，区分 KG-aware（图接地）与 KG-agnostic 两种条件，评估推理深度与事实准确性。标注一致性较高：Cohen's kappa 0.781（范围 0.753-0.807），Fleiss' kappa 0.77。

**关键结果**：通用前沿模型（GPT-5.1、Gemini 2.0 Pro）在多跳与高层推理上显著优于领域专用模型（BioGPT、Llama 3），但从单跳到多跳查询性能明显下降。KG 接地降低了所有模型的幻觉率；有结构化知识接入时，通用模型幻觉率低于专用模型。与假设相反，领域专用模型在无图接地时并未在专门任务上表现出持续优势。结论指向：结合广泛语言能力与结构化领域知识，并根据任务复杂度与算力约束选择 LLM-KG 集成策略，同时讨论面向个性化医疗、认知障碍诊断与可解释 AI 的混合神经符号架构。
