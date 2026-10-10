---
title: 'Opera: A Verbal Critic Framework for Long-horizon Coding Agents'
title_zh: Opera：面向长程编码 Agent 的语言化批评框架
authors:
- Kai Mei
- Zhiyuan Hu
- Yutong Dai
- Juntao Tan
- Yifan Zhang
- Dingjie Song
- Dimitris N. Metaxas
- Silvio Savarese
- Ran Xu
- Zeyuan Chen
affiliations:
- Salesforce AI Research
- Rutgers University
- Lehigh University
arxiv_id: '2609.33987'
url: https://arxiv.org/abs/2609.33987
pdf_url: https://arxiv.org/pdf/2609.33987
published: '2026-10-07'
collected: '2026-10-10'
category: Agent
direction: Agent 执行期批评与反馈闭环
tags:
- Agent Critic
- Long-horizon
- Feedback Tracking
- Self-correction
- SWE-Bench
- On-policy Distillation
one_liner: 将每次纠正视为持久化笔记并跟踪到问题解决，显著提升编码 Agent 的 resolve rate 并支持蒸馏训练
practical_value: '- 对电商/广告场景中的长周期 Agent（自动选品、广告投放、多轮购物助手），把每次干预/纠正变成持久化 note 并跟踪到闭环，而不是发完反馈就结束；配合周期性+事件驱动触发器，避免在任务进行中过早打断。

  - 诊断问题用 typed operators（如重复动作、过早完成、缺乏验证），可迁移到推荐/搜索 Agent 的轨迹诊断：定义可枚举的高频失败模式，比开放生成
  feedback 更可控、可审计。

  - 反馈投递前先做 evidence audit，只基于可见轨迹批评，降低 LLM critic 幻觉和误判；对推荐解释、query 改写评估等 critic
  模块同样适用，可减少误导性反馈。

  - 用 critic-guided rollouts 蒸馏成 on-policy 微调数据，使小模型（如 Qwen3.5-9B）推理时无需 critic 也能保持提升，适合线上低延迟的推荐/广告
  Agent 部署；这是一个可复用的训练数据生产范式。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：长周期 coding agent 需要及时纠正，但现有 critic 只评估轨迹和生成反馈，不追踪反馈后行为，反馈可能误判未完成工作或没有解决根因。

**方法关键点**：Opera 将每次纠正作为持久化 note，跟踪至问题解决。触发机制包括周期性和事件驱动；用 typed operators 诊断问题；投递前对照可见证据审计反馈；追踪后续动作区分表面服从与实际解决。作为 test-time critic，可在推理时监督 policy agent。

**关键结果**：在 Terminal-Bench 2.1、SWE-Bench Pro 子集、DeepSWE v1.1 上，使非 critic agent 的 resolve rate 最多提升 12.4/15.0/8.9 个百分点；在三个 benchmark 上均取得 critic baseline 中最高平均 resolve rate；自评也能提升。Opera-guided rollouts 用于微调 Qwen3.5-9B，held-out SWE-Bench Pro 仓库 resolve rate 提升 10.2 个百分点，无需推理时 critic，且切换到 Terminus-2 harness 仍保持性能，而直接切换会下降。
