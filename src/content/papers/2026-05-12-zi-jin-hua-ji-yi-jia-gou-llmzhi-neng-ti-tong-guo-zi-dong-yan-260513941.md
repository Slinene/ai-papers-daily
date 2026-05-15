---
title: EvolveMem:Self-Evolving Memory Architecture via AutoResearch for LLM Agents
title_zh: 自进化记忆架构：LLM智能体通过自动研究自我优化检索
authors:
- Jiaqi Liu
- Xinyu Ye
- Peng Xia
- Zeyu Zheng
- Cihang Xie
- Mingyu Ding
- Huaxiu Yao
affiliations:
- UNC-Chapel Hill
- UC Berkeley
- UCSC
arxiv_id: '2605.13941'
url: https://arxiv.org/abs/2605.13941
pdf_url: https://arxiv.org/pdf/2605.13941
published: '2026-05-12'
collected: '2026-05-15'
category: LLM
tags:
- LLM
- Agent
- Memory
- Retrieval
- Self-Evolution
- AutoResearch
one_liner: 首个通过LLM闭环诊断自主进化检索配置的记忆框架，实现AutoResearch，无需人工调参
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**  
现有 LLM 智能体的长期记忆系统只进化存储内容，而检索评分函数、融合策略、上下文预算等检索基础设施在部署后冻结。随着记忆规模增长和查询类型多样化，固定检索配置无法适配所有需求（如事实查询需精确匹配，时序推理需时间感知过滤）。真正自适应的记忆应同时进化存储知识和检索机制。

**方法关键点**  
- **结构化记忆存储**：记忆表示为类型化元组（内容、嵌入、类型、元数据），通过 LLM 提取与重试、分块、覆盖率验证等保障提取质量，并用去重、重要性衰减、实体增强保持存储质量。  
- **检索作为可进化动作空间**：多视图检索（BM25 词法、语义嵌入、结构化元数据）独立生成候选集，支持可进化融合模式（SUM、加权和、RRF）和融合权重；可选查询增强（实体交换、查询分解）与答案生成风格、二次验证构成完整 action space，每个维度可被按问题类别覆盖。  
- **自进化引擎**：LLM 诊断模块读取每轮逐问题失败日志，识别根因并提议配置调整；元分析器执行更新，自动回退性能下降的调整，并在停滞时注入随机探索；整个闭环构成 AutoResearch 过程，自主发现如实体交换、查询分解、答案验证等原空间未定义的新维度。

**关键结果**  
在 LoCoMo 基准上，EVOLVEMEM 优于最强基线 25.7%（相对最小基线提升 78.0%）；在 MemBench 上超出最强基线 18.9%。进化配置跨基准正向迁移，在暂未调优的 MemBench 上取得 54.3% F1，继续进化后达 79.2%，远超从头进化的 67.9%。消融实验证实 LLM 诊断比随机搜索增益 9.63 F1，新发现的三项配置维度贡献 7.77 F1。
