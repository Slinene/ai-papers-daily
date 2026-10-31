---
title: 'VeriCUA: Verification as Agentic Exploration for Computer-Using Agents'
title_zh: VeriCUA：通过智能体式探索验证计算机使用智能体
authors:
- Qiushi Sun
- Da Yu
- Alexander Knop
- Amer Sinha
- Lingpeng Kong
- Ben Kao
- Ravi Kumar
- Pritish Kamath
affiliations:
- Google
- The University of Hong Kong
arxiv_id: '2610.40578'
url: https://arxiv.org/abs/2610.40578
pdf_url: https://arxiv.org/pdf/2610.40578
published: '2026-10-29'
collected: '2026-10-31'
category: Agent
direction: Agent 任务完成验证 · 动态证据探索
tags:
- Verification
- Computer-Using Agents
- Agentic Exploration
- VLM
- GUI Checks
- Code Checks
one_liner: 将验证视为动态证据收集与评估，统一在线离线、跨平台 CUA 任务完成验证，提升一致性并更强拒绝误报
practical_value: '- 对电商 RPA、广告投放自动化等 CUA 场景，别只用 VLM 静态判断轨迹或固定生成检查脚本；可引入验证智能体在任务完成后继续探索
  GUI 或执行代码检查，收集互补证据，降低因部分观测导致的假阳性。

  - 先根据任务上下文构建 rubric，再对未满足 requirement 动态选择 GUI/code check，并用显式证据规则合并结论。这个流程可直接迁移到业务
  Agent 的离线评测、数据清洗与 RL 正负样本过滤，尤其适合 hard cases 标注。

  - 在线部署时，当 Agent 宣称完成，再触发一轮验证探索能更强拒绝 false completion claim，适合客服、订单处理等高风险场景，防止未保存编辑或部分完成被当成成功。

  - 平台无关的统一验证流程能减少为 Web/App/桌面不同端定制 verifier 的工程成本，可用于多端电商 Agent 的统一评估 pipeline。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：计算机使用智能体（CUA）的任务完成验证对数据采集、评测和 RL 都关键。典型做法是让 VLM 判断轨迹，或生成程序检查应用状态；但二者都只依赖局部视图，可能漏掉决定性证据，例如未保存的编辑或不可见故障。不同平台和访问方式还要单独定制 verifier，工程成本高。

**方法关键点**：VeriCUA 将验证定义为共享流程中的动态证据收集与评估，在线/离线、跨平台/模态通用。第一步检查可用上下文并构建任务 rubric；第二步针对尚未解决的要求，选择 GUI 检查或代码检查来补证；第三步按显式证据规则合并检查结果，得到完成判定。验证器不是被动观察，而是 agentic exploration。

**关键结果**：在多种设置下与参考标签一致性优于基线；离线 hard cases 增益最大，在线对假完成声明的拒绝更强。分析表明提升来自互补证据与 test-time exploration。摘要未披露具体准确率数值。
