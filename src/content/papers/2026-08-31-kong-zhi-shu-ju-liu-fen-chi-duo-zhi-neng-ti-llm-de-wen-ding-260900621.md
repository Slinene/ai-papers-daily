---
title: 'Control-Data Flow Separation: Stable Prompt Optimization in Multi-Agent LLMs'
title_zh: 控制-数据流分离：多智能体 LLM 的稳定提示优化
authors:
- Wentao Zhang
- Syed Shariyar Murtaza
- Junaid Ahmad Bhatti
- Utkarsh Soni
- Yifan Nie
- Eugene Wen
- Yuntian Deng
affiliations:
- University of Waterloo
- Manulife
arxiv_id: '2609.00621'
url: https://arxiv.org/abs/2609.00621
pdf_url: https://arxiv.org/pdf/2609.00621
published: '2026-08-31'
collected: '2026-09-02'
category: MultiAgent
direction: 多智能体控制/数据流分离
tags:
- multi-agent LLM
- prompt optimization
- structured control
- protocol stability
- TextGrad
- schema validation
one_liner: 将执行控制协议与可优化文本解耦，用类型化 schema 保证多智能体提示优化不破坏路由/格式，任务性能与稳定性双升
practical_value: '- 在多智能体路由/编排场景（如 query 改写、召回排序、聚合议价）中，把『下一步调哪个 agent / 是否终止 / 输出
  JSON 字段』定义成 Literal/dataclass 控制对象，只允许 controller 消费验证后的控制对象，不要把自然语言当路由协议。

  - 将 schema 脚手架放进 optimizer 不可读写的 frozen prompt slot；只优化 data-facing prompt。配合 bounded
  parse retry 与 default valid fallback，可在 TextGrad/DSPy 等优化下维持 100% 协议有效，避免线上 pipeline
  崩溃。

  - 把任务语义内容（解释、评论、中间结果）留在 unstructured data channel 供其他 agent 与 optimizer 使用，控制层固定后，per-example
  feedback 对任务质量提升更直接；可用 TextGrad 等做端到端 prompt 优化而不担心格式漂移。

  - 工业保险评分案例显示：少量 typed control + 优化后的 prompt 可超过 40+ 行手工领域 prompt，适合电商/广告中规则密集且需要
  LLM 协作的评分、审核类 agent 工作流。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
多智能体 LLM 中，prompt 同时承担生成任务内容与指定执行协议（路由、输出格式、终止信号）的双重角色。端到端 prompt 优化会改动文本，可能意外破坏 controller 依赖的格式/路由约定，导致不是答案变差而是 pipeline 崩溃。例如 Naive TextGrad 在 MARG review 任务稳定性降到 0%。

**方法关键点**
- 控制-数据流分离：每个 agent 输出拆成 control channel 与 data channel。control 是 typed/validated 程序对象（Python dataclass/Pydantic，Literal 闭集），只被 controller 消费；data 是自由文本，供其他 agent 与 optimizer 使用。
- control schema 自动生成冻结的 scaffold prompt slot，optimizer 不可修改；运行时 parse/validate，失败有界重试或 default fallback。
- 路由函数只读取 validated control object，不解析非结构化消息，从而保证优化无法破坏协议。
- 实现为 cdsep Python 库，完整 leader-worker 流程 <40 行。

**关键实验**
在 BBH 单智能体推理、MARG review 生成、synthetic 与 industry-verified insurance underwriting 四个任务上对比 Fixed、Naive TextGrad、DSPy no compile / BootstrapFewShot / MIPROv2。
- Ours 各任务最高：BBH 78.3% vs 74.3%（DSPy BootstrapFewShot）；MARG Jaccard 44.4 vs 43.2（DSPy MIPROv2）；synthetic underwriting 50.0 vs 47.8；industry-verified 36.7 vs 31.7（Partner-Fixed）。
- 100% eventual protocol validity，Naive TextGrad 在 MARG 0%、industry 56.7% 稳定。
- 消融：schema 冻结是稳定性主因，per-example feedback 是质量主因；跨 OpenAI/Anthropic/Google 三族 LLM，Ours 均 100% 稳定，Naive 均 0%。

**最值得记住**
把执行协议从可优化文本中冻结出来，prompt 优化才可能安全地改进多智能体系统。
