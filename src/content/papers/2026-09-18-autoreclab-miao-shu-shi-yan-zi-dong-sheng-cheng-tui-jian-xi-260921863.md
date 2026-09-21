---
title: 'AutoRecLab: Describe the Experiment, Get the Code!'
title_zh: AutoRecLab：描述实验，自动生成推荐系统实验代码
authors:
- Moritz Baumgart
- Philipp Meister
- Justus Krell
- Michael Schmidt
- Bela Gipp
- Joeran Beel
affiliations:
- University of Siegen
- University of Göttingen
arxiv_id: '2609.21863'
url: https://arxiv.org/abs/2609.21863
pdf_url: https://arxiv.org/pdf/2609.21863
published: '2026-09-18'
collected: '2026-09-21'
category: Agent
direction: Agent 自主科研与代码生成
tags:
- Autonomous Agents
- Code Generation
- RAG
- LLM
- Recommender Systems
- Tree Search
one_liner: 用自然语言提示自动实现推荐系统实验代码，结合RAG、静态类型验证与执行引导树搜索
practical_value: '- 把实验代码生成拆成“需求抽取→原型→验证→迭代扩展”的流水线，可借鉴到内部实验平台：用 LLM 自动将实验配置转成可执行 Python/Java
  代码，减少手工编写 baseline 和评估脚本。

  - RAG 检索内部 RecSys 框架、数据 API 和实验平台文档，能显著减少 LLM 对私有接口的幻觉；结合静态类型检查（mypy/pyright）和执行反馈（跑测试、捕获报错）作为生成质量门禁，比单纯生成代码更可靠。

  - 执行引导的树搜索可复用：对候选代码路径展开、执行、根据结果剪枝，适合离线批量生成多个算法/多数据集实验；文中单次成功运行约 1 美元，说明小规模试跑成本可接受。

  - 该演示主要覆盖学术场景的显式→隐式反馈转换实验，业务落地还需补充线上数据 schema、评测指标、版本管理等约束，但可先作为内部实验脚手架或新人 onboarding
  工具。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：推荐系统研究中的经验评估依赖手工将实验设计转化为可执行代码，过程繁琐且易出错。AutoRecLab 旨在用自然语言提示自动完成 RecSys 实验实现。

**方法关键点**：
- 输入研究想法后，AutoRecLab 先抽取显式实验需求，构建并验证原型，再迭代扩展为完整实验。
- 工作流结合三个核心组件：
  1. **RAG**：检索文档以减少 LLM 幻觉；
  2. **静态类型验证**：在生成后检查代码类型正确性；
  3. **执行引导树搜索**：执行候选代码并根据运行结果进行剪枝和选择。
- 演示任务为显式到隐式反馈转换研究。

**关键结果**：在六种算法、三个数据集的基线对比中，9 次运行有 8 次成功，使用 GPT-5.4-mini 的平均成本约为每次 1 美元。
