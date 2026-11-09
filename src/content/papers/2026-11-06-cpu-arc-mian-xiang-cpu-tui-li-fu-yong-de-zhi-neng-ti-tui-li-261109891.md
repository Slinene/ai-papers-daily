---
title: 'CPU-ARC: Agentic Reasoning Caching for on-CPU Reasoning Reuse'
title_zh: CPU-ARC：面向 CPU 推理复用的智能体推理缓存
authors:
- Peter Belcak
- Greg Heinrich
- Saurav Muralidharan
- Shizhe Diao
- Pavlo Molchanov
affiliations:
- NVIDIA
arxiv_id: '2611.09891'
url: https://arxiv.org/abs/2611.09891
pdf_url: https://arxiv.org/pdf/2611.09891
published: '2026-11-06'
collected: '2026-11-09'
category: LLM
direction: LLM 推理缓存 · 语义函数
tags:
- LLM caching
- Semantic Functions
- Agentic Systems
- Reasoning Reuse
- CPU Inference
- Cost Reduction
one_liner: 把 LLM 推理轨迹编译成可复用 CPU 语义函数缓存，在数学/科学基准上匹配前沿模型并降本 16–291 倍
practical_value: '- 对电商/广告/搜索里高频、模板化、参数变化的 agentic 任务（商品属性抽取、query 分类、规则校验、广告文案合规检查、价格/库存计算），可以把大模型推理
  trace 编译成参数化 Python 语义函数缓存；入口先用 try-cache-first，miss/error 再 fallback 到完整 LLM。

  - 关键工程 trick：函数间用自然语言描述而非固定变量名引用输入和调用子函数，配合 `do()`/`load()` 原语，能同时鲁棒 prompt 改写和参数替换；这比
  KV cache 或 semantic similarity cache 更适合线上 prompt 经常微调的场景。

  - 先算回本点再上线：构建成本约为源模型 12–84 倍，单次调用节省 16–291 倍，AIME 难度任务约 13 次重复回本，GSM8K 这类简单任务约 90
  次；所以优先缓存昂贵、高频、逻辑稳定的推理，而不是便宜短任务。

  - 稳定后的语义函数网络可以静态编译成纯 Python，去掉向量检索和 embedding 引擎；目标模型用 fine-tuned 1B 级别小模型即可，进一步压缩成本，同时代码可异步人工/AI
  审查，满足可解释性和合规要求。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
LLM 每次推理都从零求解，即使同一类问题只是换个参数或措辞，也会重复大量相同的推理工作。现有系统级缓存要么是 KV cache/对话前缀这类单块缓存，对输入扰动不鲁棒；要么是模块化缓存，仍需完整生成回答。该工作尝试把“解搜索”与“解执行”解耦，将 LLM 的推理轨迹编译成 CPU 可执行的代码，从而在重复的 agentic 负载中降低成本和延迟。

**方法关键点**
- Agentic Reasoning Cache 用 builder 模型分析源模型推理 trace，将其转化为参数化 Python 程序；程序由 semantic functions 组成，每个函数代表一个可复用的逻辑步骤。
- 函数间通过自然语言描述和示例引用输入、调用子函数，而不是固定变量名，因此可以适应 rephrasing 和 reparameterization。
- 核心运行时原语包括 `load`、`do`、`narrate`、`lm`、`extract`、`convert`、`invoke_tool`；Context 维护栈式 memory layers，用 CPU 向量库做语义检索。
- 构建分五阶段：输入输出隔离、推理分解、参数识别、规划、实现；候选函数经过语法检查、原始参数测试、judge 验证和抽取鲁棒性测试后才注册。
- 缓存稳定后可静态编译成纯 Python，消除运行时 embedding 和向量检索；调用时只使用小模型做参数抽取、分类或数值提取。

**关键结果**
在 MATH-500、AIME 2024–2026、GPQA Diamond、GSM8K、MMLU-Pro、SciBench 上，cache 正确率在 7/8 个 benchmark 上达到或超过源模型 Claude Opus 4.5；例如 AIME ’25 上 cache 93.3% vs 源模型 83.3%。
扰动的 phrasal/parametric/combined 通过率普遍超过 90%。
单次调用成本约 $0.0004–$0.0019，相比源模型节省 16–291 倍；构建成本为源模型的 12–84 倍。AIME 难度任务约 13 次重复调用回本，GSM8K 约 90 次。

**最值得记住的一句话**
高质量推理可以脱离原始 LLM，被编译成由自然语言描述相互调用的可执行语义函数，在 CPU 上廉价、鲁棒、可审查地复用。
