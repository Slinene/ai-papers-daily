---
title: 'AgentDebugX: An Open-Source Toolkit for Failure Observability, Attribution,
  and Recovery in LLM Agents'
title_zh: 'AgentDebugX: LLM Agent 闭环调试与根因修复工具包'
authors:
- Kunlun Zhu
- Xuyan Ye
- Zhiguang Han
- Yuchen Zhao
- Bingxuan Li
- Weijia Zhang
- Muxin Tian
- Xiangru Tang
- Pan Lu
- James Zou
affiliations:
- University of Illinois Urbana-Champaign
- University of Toronto
- Google
- Stanford University
arxiv_id: '2607.18754'
url: https://arxiv.org/abs/2607.18754
pdf_url: https://arxiv.org/pdf/2607.18754
published: '2026-07-20'
collected: '2026-07-23'
category: Agent
direction: Agent 调试 · 根因分析与修复
tags:
- agent debugging
- failure attribution
- DeepDebug
- recovery loop
- observability
- open-source
one_liner: 提出闭环调试框架AgentDebugX，其多轮根因诊断方法DeepDebug在Who&When上严格归因准确率28.8%优于单次方案21.7%，在GAIA上单次重试修复13/73失败任务。
practical_value: '- **闭环植入推荐Agent质量保障**：可将Detect-Attribute-Recover-Rerun流程嵌入推荐系统的Agent执行链路（如多轮对话推荐、商品搜索Agent），自动检测表象失败并回溯到真正决策错误步骤，将根因分析作为线上兜底策略。

  - **根因分析用于模型迭代**：DeepDebug的多轮全局扫描、结构引导探查与交叉验证机制可直接迁移，用于诊断推荐失败（如错误召回源头、排序打分支离），产出带证据的诊断报告，替代人工日志分析，加速Bad
  Case修复。

  - **可移植轨迹表示降本增效**：框架无关的AgentTrajectory格式支持跨LangGraph、CrewAI等常用Agent框架，适合多团队共享同一诊断工具；Error
  Hub可积累推荐Agent的失败-诊断-修复三元组，形成团队知识库，用于回归测试和长尾错误模式发现。

  - **成本可控的渐进诊断**：采用“简单规则→单次LLM读取→多轮DeepDebug”的成本递增路径，可根据任务复杂度动态选择诊断深度；对于推荐Agent，高频短链任务用轻量检查，长链多跳任务用DeepDebug避免定位偏差，工程上易于落地。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
LLM Agent 行动链长、组件多，故障发生时表征步骤往往不是根因所在：例如最终答案错误可能源于早期规划缺失、记忆过时或多Agent交接错误。现有观测工具仅重放轨迹，缺乏根因定位能力；故障分类基准孤立存在，未能与修复闭环打通。为此，这项工作将调试定义为一个可操作的闭环。

**方法关键点**
1. **闭环流水线**：Detect（检测表象失败）→ Attribute（回溯根因步骤）→ Recover（根据根因生成修复指令）→ Rerun（从检查点重试并对比）。所有阶段共用可移植的AgentTrajectory格式，解耦具体Agent框架。
2. **DeepDebug 多轮诊断代理**：针对单次全轨迹扫描易锚定下游症状、逐步扫描丢失全局上下文的问题，设计了四阶段读足迹流程：全局扫描初判→结构引导二次探查（多Agent则逆移交链回溯，单Agent则二分查找）→交叉审裁分歧假设→输出包含责任代理、确切步骤、证据引述和一条具体修复建议的审计报告。
3. **复用与扩展机制**：Error Hub存储脱敏后的轨迹-诊断-修复三元组，作为团队记忆供检索和回归测试；可扩展故障模式分类法，支持从残留错误中自动候选新模式并人工审批。

**关键实验**
- 在Who&When基准（184条多Agent轨迹）上，DeepDebug (qwen3.5-9b) 取得28.8%严格代理-步骤联合准确率，显著优于最强单次基线All-at-Once的21.7%；该优势集中在长度>40事件的长轨迹上（8% vs 22%）。
- 在GAIA验证集上，先用普通Agent执行165任务，失败73例，仅对失败轨迹进行单次重试修复：DeepDebug的根因引导修复成功13/73（+7.9个点整体准确率），而三种解耦自纠正基线仅修复4-6例。
- 资源开销：DeepDebug多轮总Token量仅为单次全轨迹读取的1.6倍，通过分级路由可控制在低成本水平。

**核心洞察**：将根因定位转化为两阶段假设生成与交叉验证，比单一长上下文阅读更能分辨长轨迹中的因果关系；该定位信息直接转换为修复指令，修复效率成倍提升。
