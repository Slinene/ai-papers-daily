---
title: 'ReTrace: Distilling Tool-Using Agents into Planner-Free Workflows'
title_zh: ReTrace：将工具使用智能体蒸馏为无规划器工作流
authors:
- Kaiyuan Hou
- Yang Ping Kuo
- Indranil Bhattacharya
- Rohith Nama
- Arushi Gupta
- Carlos D. Castillo
- Prathap Ramachandra
- Xiaofan Jiang
- Francesco Carbone
affiliations:
- Columbia University
- Amazon
arxiv_id: '2611.14492'
url: https://arxiv.org/abs/2611.14492
pdf_url: https://arxiv.org/pdf/2611.14492
published: '2026-11-10'
collected: '2026-11-11'
category: Agent
direction: Agent 蒸馏 · 工作流编译
tags:
- Agent Distillation
- Workflow Compilation
- Trace Mining
- Planner-Free
- LLM Agents
- Business Process Automation
one_liner: 从 SOP 和少量带推理的 agent 轨迹中提取条件规则，编译成运行时无需 LLM 规划的可复用工作流
practical_value: '- 高频 SOP 流程适合编译成确定性工作流：运行时不再调用 LLM 选步，τ2-bench 单任务从 170s 降到 1.3s，企业成本降
  24%；电商/客服/审核等大量重复流程可直接借鉴。

  - 必须保留 agent 每一步的 reasoning，而不只是 tool call：reasoning 能恢复动作发生的条件、输入来源和未执行分支，在 τ2-bench
  上提高 6.2 点，企业完成率提高 8.8 点；短流程收益有限。

  - 用规则文档 IR 做中间表示，只有最后的代码生成依赖平台，可同时输出 Python 和平台工作流图，方便在沙箱和内部编排平台间迁移。

  - 用训练失败样本对生成的工作流做 repair（反馈失败输入、执行步骤和标签），能进一步逼近 agent：τ2-bench 从 66.7% 提升到 81.2%，SOP-Bench
  从 80.6% 提升到 87.8%。

  - 工程实现上，用静态检查 + 沙箱 + 重放检查防止规划调用；对长 trace 不要给生成器太多完整轨迹，否则代码生成质量下降。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

## 动机
业务过程自动化会反复执行同一套 SOP。LLM agent 能读懂自然语言 SOP，但每一步都要调用 LLM 规划、路由和转换数据，在高频执行时带来巨大延迟和 token 成本。生产平台数据显示，91.8% 的自动化是运行时规划的 agent，但最高频执行的 7 个自动化都是固定工作流。因此，把 agent 执行经验一次性编译成运行时无需 LLM 规划的工作流，有明确的降本增效价值。

## 方法关键点
- 输入：一条 SOP 和 k 条带推理的 agent 轨迹，每条轨迹由 (reasoning, tool, inputs, result) 组成。
- 三阶段构建：
  1. **Extraction**：逐步骤用 LLM 提取条件 `g_t`、意图动作 `α_t`、工具、输入来源 `ω_t`，并标记推理中提到但未执行的分支。
  2. **Aggregation**：先逐 trace 对照 SOP 总结，再跨 trace 合并成紧凑的规则文档 IR：`(完成检查 χ, 有序规则列表 ⟨(g_j, α_j)⟩)`，每条规则带证据引用。
  3. **Synthesis**：从 IR 生成 Python 代码或平台工作流图，运行时由代码选择下一步，不再调用 LLM 做 planning。
- 核心 insight：agent 的 reasoning 往往说明 why，而 tool call 只说 what；只用 tool call 会丢失条件与未执行分支。
- 只最后阶段依赖平台，IR 可复用到不同编排平台；生成后可用训练失败样本 repair，只改代码不改 IR。

## 关键实验与结果
- 数据集：τ2-bench telecom 40 个测试任务，SOP-Bench 8 个域 744 个测试样本，内部生产平台 79 条流程。
- 主要对比：original agent、zero-shot、few-shot、execution-only、AWM、Skill Factory、BPOP。
- τ2-bench：ReTrace 达到 75.8% 成功率，agent 为 80.6%，但时间从 170s 降到 1.3s；去除 reasoning 成功率下降 6.2 点。
- SOP-Bench：ReTrace 80.6%，repair 后 87.8%，超过 agent 的 85.5%。
- 生产平台：ReTrace 完成率 93.8%（agent 96.8%），成本降低 24%；去除 reasoning 完成率下降 8.8 点。
- 高频流程构建成本约在 75 次执行后回收。

## 最值得记住的一句话
把 agent 的推理（why）和工具调用一起编译成规则文档，再生成运行时无 LLM 规划的工作流，比直接把原始轨迹喂给代码生成器更可靠、更省成本。
