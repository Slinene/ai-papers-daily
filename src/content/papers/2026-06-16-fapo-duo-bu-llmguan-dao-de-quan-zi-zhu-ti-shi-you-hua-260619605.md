---
title: 'FAPO: Fully Autonomous Prompt Optimization of Multi-Step LLM Pipelines'
title_zh: FAPO：多步LLM管道的全自主提示优化
authors:
- Paul Kassianik
- Baturay Saglam
- Huaibo Zhao
- Blaine Nelson
- Supriti Vijay
- Aman Priyanshu
- Amin Karbasi
affiliations:
- Foundation AI–Cisco Systems Inc.
- Yale University
arxiv_id: '2606.19605'
url: https://arxiv.org/abs/2606.19605
pdf_url: https://arxiv.org/pdf/2606.19605
published: '2026-06-16'
collected: '2026-06-19'
category: Agent
direction: 自主Agent优化多步LLM管道
tags:
- prompt optimization
- pipeline optimization
- autonomous agent
- Claude Code
- multi-step LLM
- structural bottleneck
one_liner: 让Claude Code自主诊断并优化多步LLM管道，先调提示再改结构，15/18基准胜出，平均+14.1pp
practical_value: '- **自主管道优化Agent**：对电商搜索/推荐的多步LLM管道（如query改写→召回→精排→解释生成），可构建类似的自主Agent自动诊断和优化，从提示到流程结构逐步提升。

  - **结构化诊断归因**：借鉴FAPO检查中间步骤、定位瓶颈的机制，开发推荐链路失败分析工具，区分是检索、推理还是格式化步骤出错。

  - **保守优化策略**：先优化提示，仅当提示优化不足且明确结构瓶颈时才调整管道结构，这种策略在生产环境中风险可控，适合线上实验。

  - **标准化代码库封装**：将推荐管道实现为标准化代码库，使Agent能够进行代码审查和修改，便于自动化迭代，增强系统可维护性。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：多步LLM管道中，检索、推理、格式化等步骤的交互会导致失败，仅进行单轮提示优化易忽略链式瓶颈。  
**方法关键点**：FAPO让Claude Code在标准化代码库内自主优化LLM管道。流程包括：评估管道→检查中间步骤→诊断失败→提出局部修改→验证变体，循环优化以最大化评分。优化策略分两层：优先编辑提示；当提示优化收益不足且归因发现结构瓶颈时，才在允许范围内调整管道结构。  
**关键结果**：在6个基准、3种任务模型共18个比较中，FAPO 15次超越基线GEPA，11次均值±标准差区间完全不重叠，平均提升+14.1pp。在需要结构变更的6个HoVer和IFBench比较中，FAPO全胜且平均提升+33.8pp。在安全任务CTIBench-RCM上，仅靠提示优化即提升GPT-5准确率+4.0pp，Foundation-Sec模型提升+2.0到+7.1pp。验证了“先提示后结构”策略的有效性。
