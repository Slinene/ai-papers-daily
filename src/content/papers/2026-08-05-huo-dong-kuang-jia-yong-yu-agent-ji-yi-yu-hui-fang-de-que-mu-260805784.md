---
title: 'Activity Frames: Deterministic Screen-Activity Compilation for Agent Memory
  and Replay'
title_zh: 活动框架：用于 Agent 记忆与回放的确定性屏幕活动编译
authors:
- Nossa Iyamu
affiliations:
- Independent Researcher
arxiv_id: '2608.05784'
url: https://arxiv.org/abs/2608.05784
pdf_url: https://arxiv.org/pdf/2608.05784
published: '2026-08-05'
collected: '2026-08-08'
category: Agent
direction: Agent 记忆压缩与成本归因
tags:
- Agent Memory
- Deterministic Compilation
- Screen Capture
- Routine Replay
- Cost Instrument
- Episodic Memory
one_liner: 将屏幕操作编译为缓存友好的结构化记忆，使 Agent 以极低 token 开销准确回答用户日常行为问题并量化例程成本
practical_value: '- **用户行为记忆与复用**：在电商运营、广告优化等 Agent 辅助场景中，可通过被动屏幕捕获将运营人员的操作流（选品、调价、搭建计划）编译成结构化记忆块，替代
  LLM 摘要，减少重复推理的 token 消耗，提升 Agent 对上下文的理解准确率。

  - **零模型回放降低延迟与成本**：已编译的例程可在命中时直接确定性回放，无需模型调用，实现零 token 自动化。适用于高频、重复的标准化操作（如日常报表拉取、状态检查），推动
  Agent 行为从“再生”到“复用”的范式转变。

  - **Agent 成本归因与价值量化**：引入 Routine Overhead Ratio (R) 与可委派重复率 (h)，可前置衡量将人工操作交给 Agent
  的 token 放大倍数与复用上限，指导决策哪些流程适合自动化、预期收益如何，为 Agent 投产提供量化依据。

  - **工程实现借鉴**：采用无模型、确定性的分段编译器，输出 byte-identical，可缓存、可审计，适合在隐私敏感或需要严格复现的零售、金融场景落地，且内存占用极低（86×
  压缩，数十毫秒处理完整日屏采集）。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：当前计算机使用 Agent 仅记录用户的自然语言指令，无法知晓用户实际屏幕操作，导致每次执行重复例程时都需从头推理，消耗大量 frontier 模型 token 且响应延迟。缺乏一种低成本、确定性的记忆编码方式，也无法量化将例程交给 Agent 的成本放大。

**方法**：提出确定性零模型编译器，将被动捕获的屏幕活动流分割为带类型的活动框架（Activity Frame），每个框架附上应用、站点、时间、输入数量及指向原始数据的证据指针，整个过程无模型参与，输出字节一致、可缓存、可审计。编译器同时可作为需求侧成本工具，从被动的人类活动中直接读数，首次测量了例程开销比 R 与委派重复率 h。

**关键结果**：在一名专业用户 51 天、128,756 帧的数据集上，编译器将一天原始捕获压缩 86 倍至约 68ms 内生成提示上下文块，Agent 基于此块回答当日行为问题的准确率达 98.4%（Wilson 95% CI 91.7-99.7%），远超 LLM 摘要的 66-80%。成本测量显示 R 上界为 60-343×，委派重复率 9.0%（样本内）/7.7%（样本外），表明仅约 8% 的 token 消耗需要新模型调用；并演示了命中例程时零 token 的确定性回放。
