---
title: 'GUI vs. CLI: Execution Bottlenecks in Screen-Only and Skill-Mediated Computer-Use
  Agents'
title_zh: GUI vs CLI：屏幕交互与技能驱动型智能体执行瓶颈对比研究
authors:
- Xiao Zhou
- Siyue Zhang
- Yilun Zhao
- Jinbiao Wei
- Tingyu Song
- Arman Cohan
- Chen Zhao
affiliations:
- NYU Shanghai
- Yale NLP Lab
- Nanyang Technological University
arxiv_id: '2606.24551'
url: https://arxiv.org/abs/2606.24551
pdf_url: https://arxiv.org/pdf/2606.24551
published: '2026-06-21'
collected: '2026-06-27'
category: Agent
direction: GUI 与 CLI 智能体执行瓶颈对比
tags:
- GUI agents
- CLI agents
- computer-use
- skill-mediated
- benchmark
- execution bottleneck
one_liner: 在匹配任务条件下，GUI 智能体受限于长视距可靠交互，CLI 智能体瓶颈在于技能覆盖，经验证器增强后 CLI 可反超 GUI
practical_value: '- 在构建 GUI Agent 处理长流程自动化（如电商后台操作、多步骤报表生成）时，可引入中间状态验证器或自我校正机制来缓解累积的定位错误，或结合
  CLI 技能对关键步骤进行兜底。

  - 对于基于 API / 技能调用的 Agent（如订单查询、广告投放接口），性能瓶颈往往不在模型推理能力，而在技能接口的覆盖度；可设计自动化的技能发现与补全管线，利用验证器反馈迭代扩充技能库。

  - 混合架构（GUI + CLI）在真实场景中有互补价值：对界面变化频繁的步骤用 GUI 柔性适配，对高频、标准化操作封装为技能，兼顾灵活性与可靠性。

  - 评测 Agent 性能时务必控制任务、初始状态和验证器，否则模态差异会被任务难度混淆；可参考其匹配基准设计思路来做内部 A/B 对比。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：计算机使用智能体（Computer-use Agent）可通过图形界面（GUI）或程序化命令接口（CLI）执行任务，但现有评测常将交互模态与任务、初始状态、验证器等因素混淆，导致无法厘清性能差异的真正来源。

**方法**：构建严格匹配的执行层基准，包含 440 个桌面任务、18 个应用、12 个工作流类别。GUI 智能体仅通过截图观察和鼠标键盘操作；CLI 智能体通过预定义技能调用。两者接受相同的目标、初始环境和最终状态验证器，仅动作空间受限。另引入**验证器引导的技能增强**，利用执行反馈自动补充缺失技能。

**结果**：在受控条件下，最强 GUI 智能体完全通过率为 59.1%，优于原始技能的 CLI 智能体（48.2%）；但经技能增强后 CLI 跃升至 69.3%，表明 CLI 的短板主要是技能覆盖率不足，而非模型能力不够。核心瓶颈差异：GUI 受限于长视距任务中的可靠接地交互（元素定位、操作链稳定性），CLI 受限于技能接口的覆盖性与可扩展性。
