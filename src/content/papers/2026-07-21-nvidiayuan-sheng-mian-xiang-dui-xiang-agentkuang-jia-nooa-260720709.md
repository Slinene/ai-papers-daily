---
title: 'NVIDIA-labs OO Agents: Native Python Object-Oriented Agents'
title_zh: NVIDIA原生面向对象Agent框架NOOA
authors:
- Paul Furgale
- Severin Klingler
- James Nolan
- Matt Staats
- Gaia Di Lorenzo
- Elisa Martinez Abad
- Christian Schüller
- Razvan Dinu
- Alessio Devoto
- Pascal Berard
affiliations:
- NVIDIA
arxiv_id: '2607.20709'
url: https://arxiv.org/abs/2607.20709
pdf_url: https://arxiv.org/pdf/2607.20709
published: '2026-07-21'
collected: '2026-07-24'
category: Agent
direction: 面向对象Agent编程框架
tags:
- Agent Framework
- Object-Oriented Programming
- LLM Agents
- Python
- Prompt Engineering
- Tool Use
one_liner: 将Agent抽象为Python对象，方法即动作、类型即契约，统一开发者与模型的编程接口
practical_value: '- **推荐Agent工程化**：将推荐逻辑（召回、排序、过滤）封装为Agent类方法，`...` 体方法由LLM动态补全，普通方法保留确定性执行，兼顾灵活性与可控性，适合搜索推荐多步决策。

  - **类型注解即Contract**：利用Python类型提示约束LLM输入输出（如 `ProductQuery → List[ItemId]`），减少prompt模板中的格式说明，自动校验并提高agent可靠性，可直接迁移到现有Pydantic+工具链。

  - **可测试可追踪**：Agent就是普通Python对象，能用pytest单元测试、用标准tracer追踪调用链，解决生产环境Agent行为难复刻、难调试的痛点，尤其适合电商多轮对话推荐中的状态回溯。

  - **事件与上下文API**：通过模型可调用的harness API传递上下文和事件，天然适合构建有状态的多轮对话式推荐/搜索Agent，管理长期记忆与用户意图，避免自建复杂状态机。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：传统Agent开发将prompt模板、工具schema、回调代码、工作流图割裂，导致代码难以测试、追踪和重构。NVIDIA提出NOOA，将Agent统一为Python对象，抹平开发者工具与模型接口之间的鸿沟。

**方法核心**：
- 一个Agent就是一个Python类，其方法对应模型可执行的动作（`...` 方法体由LLM运行时填充）、字段为状态、docstring为prompt、类型注解为输入输出契约。
- 融合六项模型交互关键设计：① 类型化输入输出；② 按引用传递活对象；③ 代码即动作；④ 可编程循环工程；⑤ 显式对象状态；⑥ 模型可调用的harness API（上下文/事件）。
- 框架原生适配Python生态：`asyncio` 异步、类型检查、标准测试工具等。

**关键结果**：
- 在SWE-bench Verified、Terminal-Bench 2.0等智能体基准上证实模型能有效使用该接口。
- 在ARC-AGI-3交互推理评测中，将多智能体世界模型系统压缩为编写了一页skill的单Agent，并取得性能提升。
- 与14个主流Agent框架对比，NOOA率先同时覆盖上述六项能力，且多项理念已被社区采纳为实验性特性。
