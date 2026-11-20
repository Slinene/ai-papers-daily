---
title: 'CompoundingKernel: Self-Improving from Zero to First'
title_zh: CompoundingKernel：从零到第一的自改进内核生成
authors:
- Qian Qu
- Hongyang Wang
- Wenbo Chen
- Yichuan Li
- Jingguo Liu
- Xian Li
- Xuan Wang
- Ruochen Wen
- Leo Fan
- Yiming Yan
affiliations:
- Amazon
arxiv_id: '2611.19230'
url: https://arxiv.org/abs/2611.19230
pdf_url: https://arxiv.org/pdf/2611.19230
published: '2026-11-13'
collected: '2026-11-20'
category: MultiAgent
direction: 多 Agent 自改进搜索与外部记忆
tags:
- multi-agent
- LLM
- self-improving
- search
- external-memory
- code-generation
one_liner: 多 Agent 自改进搜索从零生成 GPU 内核，凭外部记忆与并行评估在 SOL-ExecBench 三榜登顶
practical_value: '- 可借鉴其「外部档案 + lineage」的记忆设计：将每次成功策略/查询/模型配置及改进路径持久化，作为控制器选父本的依据，实现跨实验的累积优化，适合生成式推荐的
  prompt、召回 query、排序策略搜索。

  - 用 LLM 控制器做「exploit vs explore」决策：读取历史成功案例，选择微调父本或直接尝试新设计，给并行子代理分配不同方向；推荐系统做自动策略搜索时可替代固定
  tree/UCB，结合离线评测或小流量做正确性/效果检查。

  - 正确性/效果判定必须外置：不在 LLM 内部自评，而由独立 evaluator（离线指标、A/B 数据、线上回放）给出硬信号，可大幅减少错误累积，提升可复用性。

  - 工程上：先提升测量/评测吞吐，再考虑增加 agent 数量；一个 warm restart 修复让评估速率提升 3.6 倍，说明 agent 系统的工程瓶颈常在评测链路而非模型并发，推荐系统同理，需优先优化数据加载、缓存或
  runner。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：GPU 内核编写困难，底层性能优化超出普通 LLM 代码生成能力。目标让 LLM agent 从零开始搜索优化内核，不依赖参考实现或官方分数。

**方法关键点**：每个问题维护外部档案，保存所有正确内核及其 lineage；LLM 控制器读取档案，决定选择父本或尝试新设计，并为每个并行子代理分配一个方向；正确性由模型外部的检查器判定，而非 LLM 自评；上千个 agents 并行运行，通过一次 warm restart 修复将评估速率提升 3.6 倍。

**关键结果**：在 SOL-ExecBench 的 L1、L2 和 Quantization 三榜排名第一；235 个问题全部获得站点验证的正确内核；在 209 个 public-board 问题上比基准快 4.40 倍。在相同 wall time 下，击败 coded UCB style tree，35/38 问题胜出，正确尝试次数为其 2.4 倍。可扩展瓶颈是可靠测量的速率，而非 agent 数量。
