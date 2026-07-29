---
title: 'WorkSurface-Bench: Benchmarking Enterprise Agents on Multi-Surface Knowledge
  Routing'
title_zh: WorkSurface-Bench：企业智能体多知识面路由评测基准
authors:
- Hao Liang
- Meiyi Qiang
- Sizhe Qiu
- Linzhuang Sun
- Wentao Zhang
affiliations:
- Peking University
- Zhongguancun Academy
- University of Chinese Academy of Sciences
arxiv_id: '2607.25765'
url: https://arxiv.org/abs/2607.25765
pdf_url: https://arxiv.org/pdf/2607.25765
published: '2026-07-28'
collected: '2026-07-29'
category: Agent
direction: 智能体知识路由能力评测
tags:
- Surface Routing
- Enterprise Agent
- Benchmark
- Multi-Surface
- Knowledge Retrieval
- Tool Selection
one_liner: 提出面路由概念并构建基准，分离评测智能体选择知识源与使用知识源的能力
practical_value: '- 在电商 Agent 中可借鉴“面路由”概念，将知识源归类为文档（商品描述）、表格（销量/库存）和图（商品关联/用户图谱），先让
  Agent 选择合适的面再处理，提升准确性和效率。

  - 分离评测 Route F1 和 Answer Accuracy，帮助定位 Agent 失败根因：是选错数据源还是后续推理错误，可迁移到内部 Agent 评测体系。

  - 实验证明去除无关工具可以改善路由和效率，工程实现时可让 Agent 先进行面筛选，再暴露对应工具，减少干扰。

  - 参考可审计答案构建方式：表格用可执行查询验证、文档用文本片段 grounding、图用来源追溯，适合企业内构建可信评测集。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：企业智能体通常需要综合文档、表格和依赖图等异构知识源，但现有评测未区分智能体是否先选择了正确的知识源。为此引入“面路由”（surface routing）能力评测。
方法：基于 Workspace-Bench-Lite 构建 1,151 个原子任务，覆盖文档、表格、图及跨面问题。参考答案可审计：表格答案通过 DuckDB 查询执行复现，文档答案锚定验证文本片段，图答案追溯来源注释。评测 4 种模型骨干在 6 种 Agent 设置下的 27,624 条无协议错误轨迹。核心指标为 Route F1 和 Answer Accuracy。
结果：在受限工具访问下，路由 F1 高达 98.7–99.8%，但答案准确率仅 56.1–75.3%，说明选对面是必要不充分条件。提供表面提示提升 3/4 模型的答案，而去除无关工具主要改善路由与效率。人工审计 200 抽样任务全部通过质量标准，多数票一致。
