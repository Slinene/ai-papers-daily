---
title: 'Vortex: Efficient and Programmable Sparse Attention Serving for AI Agents'
title_zh: Vortex：面向AI Agent的高效可编程稀疏注意力服务系统
authors:
- Zhuoming Chen
- Xinrui Zhong
- Qilong Feng
- Ranajoy Sadhukhan
- Yang Zhou
- Michael Qizhe Shieh
- Zhihao Jia
- Beidi Chen
affiliations:
- Carnegie Mellon University
- Rice University
- National University of Singapore
arxiv_id: '2606.06453'
url: https://arxiv.org/abs/2606.06453
pdf_url: https://arxiv.org/pdf/2606.06453
published: '2026-06-04'
collected: '2026-06-06'
category: Other
direction: 稀疏注意力服务系统 · AI Agent 自动化研究
tags:
- sparse attention
- LLM serving
- programmable system
- AI agent
- KV cache
- paged tensor
one_liner: 一个将稀疏注意力算法表达、部署与评估深度融合到LLM服务框架中的系统，使AI Agent可自动生成并迭代优化稀疏注意力，实现高达3.46倍吞吐提升且保持精度。
practical_value: '- **可编程的稀疏注意力抽象（vFlow）**：通过两阶段（缓存预处理与查询索引）的简单编程模型，快速实现各种动态稀疏模式，避免大量重写底层算子的工程开销，可直接借鉴到推荐模型中对长序列注意力的定制化改造。

  - **兼容现有服务基础设施的vTensor抽象**：原生支持分页KV cache、prefix caching等，确保理论加速转化为端到端吞吐提升，这种“不破坏现有栈”的设计思路可迁移到推荐系统大模型推理优化中，减少与生产环境的脱节。

  - **AI Agent 驱动的算法自动搜索与迭代**：论文展示了AI代理利用Vortex一次性生成多样性稀疏算法并在长周期自主优化，形成精度-吞吐 Pareto
  前沿，此类结合系统快速反馈的自动化调优流水线可应用于推荐模型的超参数搜索或结构优化。

  - **随机化 radix top-k 的精度-速度权衡**：通过随机早停降低 top-k 计算开销，可应用于推荐系统中高效召回或注意力选择阶段的 top-k
  操作，在轻微精度损失下换取显著加速。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：随着推理型、Agentic系统等长边界生成增多的场景，KV cache移动成为LLM服务的主要瓶颈，稀疏注意力成为缓解该瓶颈的关键技术。然而，在现有服务系统（如vLLM、SGLang）中实现新的稀疏注意力算法工程量大、缺乏可编程性，且难以与分页KV cache、prefix caching等组件兼容，导致理论加速难以转化为实际吞吐收益，严重拖慢人和AI Agent的探索速度。Vortex为此设计了统一的编程模型和高效后端，桥接稀疏注意力研究与实际部署。

**方法关键点**：
- **vFlow前端语言**：嵌入Python，采用单请求心智模型，将稀疏注意力分解为`forward_cache()`（查询无关预处理）和`forward_indexer()`（查询相关索引构建），通过组合GeMM、Top-K、Gather等原生算子灵活表达各类算法（如Block Top-k、Quest、Double Sparse等）。
- **vTensor页面中心张量抽象**：封装物理分页布局，提供逻辑连续视图，使算子可在批处理页式张量上高效组合执行，避免直接处理底层非连续内存。
- **执行优化**：包含负载规划、算子核融合减少中间数据搬运，以及随机早期终止的Radix Top-k加速动态索引构建；复用FlashInfer、TRT-LLM等注意力后端，并补充专用MLA解码核以支持新架构（如GLM-系列）。

**关键结果**：
- **AI Agent创新与迭代**：Claude Code、Codex等一次性生成20种结构多样的稀疏注意力算法，Sonnet 4.6平均指标最佳；在Qwen3-1.7B上，18小时自主优化循环最终取得AIME24上3.46×吞吐提升（11,894 vs. 3,437 tok/s）且保持精度（38.96 vs. 38.54 mean@16）。
- **新架构适配**：针对MLA架构的GLM-4.7-Flash设计rope-aware块稀疏，获得4.7×端到端加速，且精度持平。
- **大规模部署效率**：在H200 GPU上，对比SGLang集成环境，Block top-k在AMC23/AIME24上最高3.60×/3.60×吞吐提升，Quest达2.98×；P95延迟降低11.7~12.8倍；在229B模型（MiniMax-M2.7，4卡B200 TP=4）上仍实现1.37×吞吐提升。
