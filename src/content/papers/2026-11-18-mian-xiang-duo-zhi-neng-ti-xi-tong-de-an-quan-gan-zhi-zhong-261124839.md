---
title: 'Kaer: Security-Aware Replanning for Multi-Agent Systems'
title_zh: 面向多智能体系统的安全感知重规划框架
authors:
- Tushin Mallick
- Evan Rose
- Matthew Laws
- Alina Oprea
- Cristina Nita-Rotaru
affiliations:
- Northeastern University
arxiv_id: '2611.24839'
url: https://arxiv.org/abs/2611.24839
pdf_url: https://arxiv.org/pdf/2611.24839
published: '2026-11-18'
collected: '2026-11-19'
category: MultiAgent
direction: 多智能体安全重规划与防御
tags:
- Multi-Agent Systems
- Security
- Replanning
- Prompt Injection
- LLM Orchestration
- Defense
one_liner: 提出Kaer框架，通过抽象诊断模板和确定性修复算子隔离不可信Agent反馈，防止重规划被提示注入劫持
practical_value: '- 在多Agent业务编排中，不要让orchestrator直接消费子Agent原始文本反馈进行重规划；可引入结构化诊断模板（如错误码、失败类型、建议操作枚举），阻断提示注入面。

  - 将重规划操作限制为预定义的确定性修复算子（如重试、换工具、回退、人工接管），避免让LLM自由生成修改指令，降低被劫持风险。

  - 对重规划后的计划增加策略校验层，例如校验工具调用权限、数据访问范围、步骤依赖，确保修改计划满足安全约束。

  - 如果业务中有不可信/第三方Agent或用户生成内容参与流程，可借鉴Cintra的对抗测试思路，构建重规划阶段攻击样本评估系统鲁棒性。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：多智能体系统（MAS）常用orchestrator生成初始计划并动态重规划，但恶意Agent可以在反馈中嵌入指令劫持重规划过程。现有防御只覆盖工具访问控制或静态策略执行，重规划阶段无防护。

**方法关键点**：
- 提出Kaer框架，将不可信Agent反馈转化为抽象诊断模板，隔离planner与原始反馈内容；
- 重规划动作限制为一组确定性修复算子，避免自由生成；
- 所有修改后的计划必须通过预设策略校验；
- 构建Cintra基准，包含需要重规划的用户任务和针对重规划阶段的对抗目标。

**关键结果**：在Cintra上对比未防御的Magentic-One和SOTA防御ControlValve，Kaer取得最高鲁棒性，同时保持与ControlValve相当的效用；抽象故障模板在部分任务上略微限制效用，但整体实现安全的动态计划修改。
