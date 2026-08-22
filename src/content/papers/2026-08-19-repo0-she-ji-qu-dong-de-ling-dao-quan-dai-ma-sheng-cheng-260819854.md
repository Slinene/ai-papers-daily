---
title: 'Repo0: Design-Driven Zero-to-All Code Generation'
title_zh: Repo0：设计驱动的零到全代码生成
authors:
- Silin Chen
- Haoyi Teng
- Xiaodong Gu
- Yuling Shi
- Jiale Huang
- Yongpan Wang
- Hongyu Zhang
- Haibing Guan
affiliations:
- Shanghai Jiao Tong University
- Chongqing University
arxiv_id: '2608.19854'
url: https://arxiv.org/abs/2608.19854
pdf_url: https://arxiv.org/pdf/2608.19854
published: '2026-08-19'
collected: '2026-08-22'
category: Other
direction: LLM Agent 零到全代码生成与结构演化
tags:
- Code Generation
- LLM Agent
- Dual-DAG
- Modularity
- Test-Driven Development
one_liner: 通过 Dual-DAG 显式架构状态与模块化度量引导结构演化，实现从需求到完整仓库的生成
practical_value: '- 将复杂 Agent 工作流（如推荐系统多阶段 pipeline）显式建模为需求层与组件层 DAG，并维护两层对齐关系，避免多模块各自生成导致的接口漂移与集成困难。

  - 借鉴模块化度量（内聚/耦合）驱动的结构迭代思路：在生成式推荐或多 Agent 系统中，先收敛模块边界与依赖关系，再进行实现，可减少返工。

  - 测试驱动开发（TDD）方式可直接迁移：从业务需求（如推荐场景的预期行为）先生成可执行的测试用例，以测试通过率作为生成质量的核心信号。

  - 显式设定结构收敛条件（如模块化指标不再显著变化），为复杂生成任务的迭代停止提供可量化判据，避免无限循环。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有 LLM 代码生成 agent 大多假设仓库已有既定架构，不能处理从零构建整个软件项目的场景；需要同时完成模块化架构设计与代码实现。

**方法关键点**：Repo0 维护显式架构状态 Dual-DAG，包含需求级 DAG、组件级 DAG 及二者对齐关系。流程从自然语言需求出发，通过结构化动作迭代演化组件边界，用模块化指标（内聚/耦合）引导，直到结构收敛；收敛后该架构指导测试驱动开发（先生成测试，再生成通过测试的代码）。

**关键结果数字**：在 RepoCraft 六个真实仓库上，使用 GPT-5 mini 和 DeepSeek V3.2，Repo0 在所有设置下均取得最高 Functionality Coverage 与 Pass Rate；相比最强仓库规划基线 RPG，Functionality Coverage 提升最多 20.08 个百分点，Pass Rate 提升最多 29.74 个百分点。消融实验验证 Dual-DAG 架构状态、模块化引导结构演化及显式收敛均对效果有重要作用。
