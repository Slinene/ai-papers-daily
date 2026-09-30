---
title: Learning Meta-Skills for Agent Harness Design in Test-Time AI4AI
title_zh: 测试时 AI4AI 中面向 Agent 脚手架设计的元技能学习
authors:
- Cheng Qian
- Kunlun Zhu
- Beibin Li
- Zhenhailong Wang
- Heng Ji
affiliations:
- Apodex
- University of Illinois Urbana-Champaign
arxiv_id: '2609.38143'
url: https://arxiv.org/abs/2609.38143
pdf_url: https://arxiv.org/pdf/2609.38143
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 元技能与执行环境构建
tags:
- Meta-Skills
- Harness Construction
- AI4AI
- Test-Time Adaptation
- Self-Improvement
- Execution Feedback
one_liner: 提出通过 Builder 从 Target 执行反馈学习元技能，并物化为脚手架以提升固定权重 Agent 的表现
practical_value: '- 将“教模型解题”拆成“教构建者设计支持”：用 (when, provide, use) 三字段沉淀执行反馈中的共性失败/负担，而非只蒸馏任务技能；在电商
  Agent 工作流中可用于提炼“何时需要价格/库存校验、提供什么工具、谁负责最终判断”的运维原则。

  - 支持要以“可执行脚手架”交付，不要直接把同一批 skill 塞给下游 Agent：让 Builder 把元技能编译成 memory、controller、verification、工具包装等；论文中
  Builder 交付比直接给 Target 平均高 12.02 个百分点，说明把语义知识转成持久状态/控制流是收益来源。

  - 同一模型可同时当 Builder 与 Target，不更新权重也能通过“学会给自己搭环境”自改进；适合线上 Agent 系统在 fixed model 下做轻量自举，尤其是反复出现的协调/提交流程。

  - 技能访问默认全量 bank 给 Builder，通常优于 BM25 top-2（本文 5/6 设置全量更好）；当 bank 变大再做考虑互补性的检索，并结合开发集反馈做回滚/选择性保留，避免过拟合。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**
Agent 的效果不仅取决于模型推理能力，还取决于执行环境。已有 test-time AI4AI 常直接给 Target 技能或搜索 harness，但缺少把构建经验沉淀为可复用支持原则的机制。该工作研究如何让 Builder 从 Target 执行反馈中学习“元技能”，并在测试时用固定 bank 构建新任务的执行脚手架。

**方法关键点**
- 定义 meta-skill = (when, provide, use)：when 识别何时需要支持，provide 说明提供什么能力/资源，use 说明 Target 如何使用并保留判断责任。
- 开发阶段：Builder 从空 bank 开始，为每个开发任务构建 harness；Target 执行后，Builder 根据公开轨迹和分数执行 keep / add / revise，每批最多更新一条且需引用证据。
- 测试阶段：冻结 bank，Builder 接收 full bank 或 BM25 top-2，为每个任务构建新的任务专用 harness；可编辑七类组件：instructions、memory、context、composed tools、execution control、verification/recovery、workspace。
- 模型权重全程固定；执行预算只限制 Target，不计 Builder 构建成本。

**关键实验**
在 Harness-Bench 和 NewtonBench 上，GPT-5.6-Sol 作为 Builder，Gemini-3.6-Flash、Qwen3.8-Flash、GPT-OSS-120B 作为 Target。全 bank 元技能达到 65.31% macro-average，比 no-skill Builder 高 8.95 个百分点，比同一 bank 直接交付给 Target 高 12.02 个百分点；同一模型同时充当 Builder 与 Target 时，平均比 no-skill 构建高 18.71 个百分点。NewtonBench 控制器消融中，移除 controller 对 Gemini 损失达 13.36 个百分点。

**最值得记住的一句话**
将构建经验转化为可执行支持，而不是只提高解题知识，是提升固定权重 Agent 系统的关键。
