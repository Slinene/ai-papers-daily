---
title: 'Looping Is Not Reliability: State-Bound Evidence and Typed Revision Contracts
  for Agentic Code Repair'
title_zh: 循环不代表可靠：状态绑定证据与类型化修订契约实现代理代码修复
authors:
- Xueping Gao
- Jianwei Yang
- Qiang Yang
affiliations:
- Alibaba Cloud
arxiv_id: '2607.24604'
url: https://arxiv.org/abs/2607.24604
pdf_url: https://arxiv.org/pdf/2607.24604
published: '2026-07-27'
collected: '2026-07-28'
category: Agent
direction: Agent 可靠性保障 · 状态绑定证据与修订契约
tags:
- coding agents
- reliability
- verification
- revision loops
- stopping policies
- agent auditing
one_liner: 揭示代码修复循环中正确补丁易丢失，提出状态绑定证据和类型化契约以保障代理可靠性
practical_value: '- 代理迭代时保存“已验证状态”检查点，避免后续修订破坏已正确结果，电商搜索中的查询改写或排序策略迭代同样适用

  - 引入类型化修订契约，强制每次修订后基于最新状态验证，而非依赖陈旧反馈，提升代理行为稳定性

  - 设计审计接收凭据（auditable admission receipts），对代理关键动作（如投放决策、推荐生成）进行追溯和可靠性监控

  - 评估代理时区分“曾经正确”与“最终正确”，避免将中途正确但最终破坏的情况误判为可靠'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：生成-测试-修订循环在编码代理中广泛应用，但重复迭代不足以保证可靠性——正确补丁可能被后续修订破坏，或陈旧反馈导致误判。需要揭示这一缺陷并提出保障机制。

**方法关键点**：
- 实验设计：在 HumanEval 修复任务上，进行 900 条三修订轨迹分析，发现强制修订下正确率从一次修订后的 0.820 降至两次后的 0.673，但“曾经正确”率升至 0.847，表明正确答案易丢失。
- 普通状态研究：利用 2,430 条分支消除后处理风险集偏差，证实陈旧轨迹（stale traces）对已正确开始的任务危害显著（34/135 受损 vs 4/135，22.2 个百分点差异）。
- 提出状态绑定证据和类型化循环契约：将验证器证据绑定到确切代码状态，保存已验证检查点，发出可审计的“接收凭据”，从机制上分离准入、保留、认证等环节。
- 实现参考规范，不声称提升修复能力，但提供可执行的可靠性保障规约。

**关键结果数字**：
- 强制修订下，最终正确率 0.673 远低于曾经正确率 0.847。
- 陈旧轨迹导致正确起点受损率显著增加（22.2 个百分点，Holm p=0.0337）。
- 前瞻性策略虽消除正确起点伤害，但降低错误起点修复，未能满足联合准则。
- 仓库实验中暴露地板效应和组件异质性，未达显著水平。
