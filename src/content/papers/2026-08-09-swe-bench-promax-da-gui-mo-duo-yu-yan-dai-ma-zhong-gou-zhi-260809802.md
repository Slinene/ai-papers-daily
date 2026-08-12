---
title: 'SWE-Bench ProMax: Benchmarking Agents on Large-Scale Multilingual Code Refactoring'
title_zh: SWE-Bench ProMax：大规模多语言代码重构智能体基准
authors:
- Yuling Shi
- Jinghan Xu
- Kelin Fu
- Wenhao Zeng
- Shilin He
- Lei Zhang
- Yue Liu
- Zelin Zhao
- Terry Yue Zhuo
- Jialun Cao
affiliations:
- Shanghai Jiao Tong University
- Peking University
- The Hong Kong University of Science and Technology
- Douyin Group
- University of Chinese Academy of Sciences
arxiv_id: '2608.09802'
url: https://arxiv.org/abs/2608.09802
pdf_url: https://arxiv.org/pdf/2608.09802
published: '2026-08-09'
collected: '2026-08-12'
category: Eval
direction: 代码重构 Agent 评估基准
tags:
- Agent
- Code Refactoring
- Benchmark
- Multilingual
- SWE-bench
- LLM
one_liner: 构建多语言、大规模代码重构基准，通过严格清洗暴露模型短板，最佳解决率仅41.2%
practical_value: '- 基准构建的严谨性可迁移：对测试用例的手动审查（剔除过严 / 过宽的测试）和问题描述的精确重写，可应用于推荐系统的离线评估中，避免因标注错误或模糊定义导致的模型能力误判。

  - 协调多文件修改的思路：实例要求同时修改平均11.4个文件，类似推荐系统中需要跨阶段（召回、排序、重排）联合优化的场景，可启发多 Agent 协同编排的设计。

  - 测试规模与真实任务的接近：平均261.6行代码的修改量远超市面基准，提示我们在构建推荐 Agent 评估任务时应尽量贴近线上复杂流程，避免琐碎的任务导致能力饱和。

  - 业务可借鉴点有限：论文核心是代码重构，与电商推荐直接关联弱，但其暴露的大模型在长上下文、跨文件行为保持上的不足，对用 LLM 做推荐 Pipeline 自动编排有警示意义。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：现有 AI 编码 Agent 基准（如 SWE-bench）日趋饱和，且近期审计发现近 60% 未解决问题存在测试缺陷——测试要么过于狭窄拒绝正确方案，要么过于宽泛包含未声明需求，同时前沿模型能从训练数据中直接复现补丁。代码重构需要跨文件协调保持行为不变，是更困难且现实的测试，但缺乏高质量基准。

**方法**：作者推出 SWE-Bench ProMax，一个专家策展的多语言代码重构基准，包含 170 个实例，来自 7 种编程语言（Python, Java, TypeScript, Go, C, C++, Rust）的真实提交。每个实例经过严格的多阶段清洗：issue 描述从零重写以提供精确无歧义的规格，测试套件经人工审核移除过严和过宽的测试。过滤掉复杂度过低或跨文件范围有限的任务，最终得到平均每个实例修改 11.4 个文件、261.6 行代码的大规模挑战集。

**结果**：在两种 Agent 脚手架下评测多个前沿模型，最佳模型（如 GPT-4 系）解决率仅 41.2%，表明基准远未饱和，是对当前 AI 编码 Agent 有意义的挑战。
