---
title: 'MemSteer: Turning User Histories into Supervision for Agent Memory Optimization'
title_zh: MemSteer：将用户历史转化为智能体记忆优化监督
authors:
- Jie Huang
- Cuiling Lan
- Qize Yu
- Xiulian Peng
- Yan Lu
affiliations:
- Peking University
- Microsoft Research Asia
arxiv_id: '2610.39276'
url: https://arxiv.org/abs/2610.39276
pdf_url: https://arxiv.org/pdf/2610.39276
published: '2026-10-28'
collected: '2026-11-03'
category: Agent
direction: 智能体记忆设计自动优化
tags:
- Agent Memory
- Memory Optimization
- Synthetic QA
- Evidence Grounding
- LLM-as-a-Judge
one_liner: 从无标注用户历史自动生成证据支撑的 QA 监督，用于迭代优化记忆存储、检索与上下文构造
practical_value: '- **用自动生成的 QA-evidence 监督替代人工标注**：在个性化记忆、用户画像、会话上下文的评估与优化中，可以从用户历史自动构建问题-答案-证据三元组，作为弱监督信号，避免昂贵的标注。

  - **证据引导的失败归因**：把错误响应定位到存储、检索或生成阶段，能精准指导设计修改。类似推荐系统中定位召回、排序或重排问题，提升迭代优化效率。

  - **跨用户迁移 + 目标用户继续优化**：先用一组用户学习共享记忆设计，再用目标用户历史生成的 QA 继续微调，适合冷启动场景。

  - **盲答案恢复与源审计保证数据质量**：合成数据必须通过可验证的检查才能用于训练或评估，这可以作为数据清洗和评估集构建的通用流程。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：Agent 需要外部记忆系统存储和检索用户历史，但不同用户的内容、模态和组织方式差异很大，一个固定记忆设计难以适配所有用户。现有自动记忆设计优化方法依赖下游任务的成功/失败信号或人工标注 QA；而个人历史常缺乏明确的执行反馈，人工构造 QA 和证据成本又高。因此需要把无标注用户历史自动转化为可用于优化记忆系统的监督信号。

**方法关键点**：
- **MemSteer 框架**：从无标注历史生成 `(question, answer, evidence)` 三元组。
  - 图引导材料准备：把用户记录组织成图，通过路径扩展采样上下文受限的 material bundle；
  - 证据锚定的答案规划：LLM 首先生成结构化 plan，显式指明事实、来源 span、各记录贡献及组合操作，通过程序化检查后再生成问题；
  - 源基础验证：语义审计 + 盲答案恢复，确保问答可回答且证据覆盖。
- **MemSteer-Opt 优化器**：利用生成监督评估记忆设计；证据引导失败诊断，将错误归因到 storage、retrieval 或 answering 阶段；按失败类别分层采样反馈，提出设计修改；不更新模型参数，仅优化存储、检索和上下文构造。
- 生成的监督也可提供给现有优化器 M* 和 MemEvolve。

**关键结果**：
- 在 ATM-Bench 上，MemSteer-Opt 将 Question Score 从 54.9 提升到 68.3（+13.4），Hard 子集从 8.2 提升到 29.1（+20.9），证据召回 R@10 从 61.7 提升到 84.1（+22.4）；与人工标注的 Official-QA 相比，主集 QS 高 1.1 分。
- 在 RHELM 上，MemSteer 使准确率提升 4.1 分（无外部数据）和 6.6 分（有外部数据），与 Official-QA 差距小于 1 分。
- 生成的监督也使 M*（+6.0 主集 QS）和 MemEvolve（+18.6 主集 QS）受益；跨用户迁移后可继续用目标用户生成的 QA 改善效果。

最值得记住的一句话：**可验证的自动生成 QA-evidence 监督，使记忆设计优化无需人工标注或下游任务反馈，并通过证据定位失败阶段实现有效迭代。**
