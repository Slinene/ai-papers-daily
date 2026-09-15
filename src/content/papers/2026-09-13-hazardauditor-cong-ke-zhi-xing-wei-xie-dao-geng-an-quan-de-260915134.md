---
title: 'HazardAuditor: From Executable Threats to Safer Computer-Use Agents'
title_zh: HazardAuditor：从可执行威胁到更安全的计算机使用智能体
authors:
- Yunhao Feng
- Ruixiao Lin
- Ming Wen
- Yanming Guo
- Xingjun Ma
- Yutao Wu
- Xinhao Deng
- Shouling Ji
affiliations:
- Ant Group
- Zhejiang University
- Fudan University
- Hunan Institute of Advanced Technology
- Shanghai Innovation Institute
arxiv_id: '2609.15134'
url: https://arxiv.org/abs/2609.15134
pdf_url: https://arxiv.org/pdf/2609.15134
published: '2026-09-13'
collected: '2026-09-15'
category: Agent
direction: 智能体安全执行守卫与策略优化
tags:
- Agent Safety
- Guard Model
- Execution Grounded
- Policy Optimization
- Computer-Use Agents
one_liner: 执行级安全审计框架 HazardAuditor，通过跨框架事件规范化和 GuardPO 序列级优化，显著提升计算机使用智能体安全守卫准确率
practical_value: '- 对电商/广告 Agent（如自动选品、自动投放、智能客服）的安全监控：不要只审 prompt 和最终回复，要记录并审计运行时的浏览器/终端/文件系统事件流，用统一的
  canonical event 表示跨系统行为，才能捕获多步操作组合出的恶意目标。

  - GuardPO 训练技巧可直接迁移到内容安全审核、推荐理由生成、广告文案审核等生成式 guard 模型：将确定性的安全/不安全标签转化为序列级 advantage，并把
  rationale 和 verdict 区域做长度归一化，避免长解释霸占梯度，让模型的决策部分真正主导优化。

  - 跨框架异构 agent 的事件规范化思路可复用于多套推荐/搜索 agent 系统：定义统一的事件 schema（如 click、query、tool_call、file_write），把不同
  agent 框架的执行日志转成同一格式，便于训练一个通用安全守卫模型，而不是每个系统单独维护规则。

  - 执行级评估集构建方法值得借鉴：在受控沙箱中跑通 Claude Code、Codex 等不同 agent，采集真实执行轨迹作为 guard 训练数据，比静态构造的
  prompt-response 对更贴近线上安全风险。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：计算机使用智能体越来越多地操作浏览器、终端、文件系统和外部服务，安全风险来自运行时行为而非单纯生成内容。现有 guard 模型针对静态 prompt/response，难以适配 agent 执行过程；现有可执行安全平台只输出评估结论，缺乏跨异构 agent 框架的统一监督信号。

**方法关键点**：HazardAuditor 构建执行级基础设施，在受控环境中运行 Claude Code、Codex、Hermes、OpenClaw 等异构 agent，将其交互归一化为规范事件表示（canonical event representation），实现跨框架监督。针对生成式 guard 的训练缺陷，提出 Guard Policy Optimization（GuardPO）：将确定性的安全结果转换为序列级优势，并对 rationale 和 verdict 区域做长度归一化，使安全决策而非长解释成为梯度更新的有效单元，解决 token-level 目标下长 rationale 主导优化的问题。

**关键结果**：在多个基准和异构计算机使用系统上，HazardAuditor 相比最强 prior guard 准确率最高提升 16.5 个百分点。代码、模型和评估工件将开源。
