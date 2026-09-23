---
title: 'FIRE: Failure-Informed Runtime Engineering for Reliable Language-Model Agents'
title_zh: FIRE：面向可靠语言模型智能体的失败知情运行时工程
authors:
- Nikita Agarwal
- Nivedit Jain
affiliations:
- Failproof AI
arxiv_id: '2609.26048'
url: https://arxiv.org/abs/2609.26048
pdf_url: https://arxiv.org/pdf/2609.26048
published: '2026-09-22'
collected: '2026-09-23'
category: Agent
direction: LLM Agent 可靠性运行时策略
tags:
- LLM Agents
- Runtime Policies
- Failure Recovery
- Reliability
- Terminal-Bench
- Action Denial
one_liner: 通过运行时注入定向指令与动作拒绝，不改权重与用户提示，显著提升代理重复成功率
practical_value: '- 对购物导购/搜索推荐 Agent，可记录失败轨迹中失败前的状态（如即将执行危险 shell 命令或改写 query 前），在此状态注入简短定向自然语言纠正，并可选拒绝特定动作，不改模型权重或系统提示，作为低成本可靠性补丁

  - 评估 Agent 可靠性时引入 pass^2（两次尝试均成功）而非只看 best-of-2；在电商场景如自动选品/广告文案 Agent，更贴近“稳定交付”要求，能暴露“偶尔成功但不可依赖”的问题

  - 用低 tier 模型 + 失败知情策略可逼近甚至超过高 tier 模型裸跑，同时成本约一半；在预算有限的推荐 Agent 场景，可优先做运行时工程而非升级模型

  - 做对照实验时用 timing-matched sham 和 generic verification 排除“额外提示/更多思考”的混淆，确认是定向纠正行为在起作用；业务团队可借鉴该
  RCT 设计来验证策略有效性'
score: 7
source: arxiv-cs.CL
depth: abstract
---

动机：LM agents 经常在找到可行方案后却无法稳定交付，例如服务随 shell 退出、错误修改证据等；需要不改模型权重或用户提示的可靠性层。
方法：提出 FIRE 运行时策略：从失败轨迹中定位失败前状态，生成针对性自然语言指令与动作拒绝，由 agent harness 在该状态注入；保持能力不变，只提升重复成功率。
结果：在 Terminal-Bench 2.1 87 任务上，两次尝试，三个 GPT-5.6 tier 的 pass^2 分别从 50.6%→54.0% (Luna)、55.2%→60.9% (Terra)、64.4%→73.6% (Sol)；Sol 的 best-of-two 仅变化 1.2 点而 pass^2 提升 9.2，表明主要将可达方案转为可靠交付。在 14 任务上，Terra 加策略达 71.4%，优于无辅助 Sol 的 64.3%，成本约一半。随机五臂实验：真实策略 61%，无策略 39%，timing-matched sham 36%，通用验证/再考虑 39-43%；定向纠正行为在 24 次编码尝试中出现 22 次，远超其他臂。
