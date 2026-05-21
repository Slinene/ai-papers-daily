---
title: 'Insights Generator: Systematic Corpus-Level Trace Diagnostics for LLM Agents'
title_zh: LLM Agent 大规模轨迹诊断系统 Insights Generator
authors:
- Akshay Manglik
- Apaar Shanker
- Kaustubh Deshpande
- Jason Qin
- Yash Maurya
- Veronica Chatrath
- Vijay S. Kalmath
- Levi Lentz
- Yuan
- Xue
affiliations:
- Scale AI
arxiv_id: '2605.21347'
url: https://arxiv.org/abs/2605.21347
pdf_url: https://arxiv.org/pdf/2605.21347
published: '2026-05-20'
collected: '2026-05-21'
category: Agent
direction: Agent 多智能体诊断与优化
tags:
- Multi-Agent
- Trace Diagnostics
- Corpus-Level Analysis
- Scaffold Optimization
- Agent Debugging
one_liner: 多智能体系统通过迭代假设-验证循环，从海量执行轨迹中自动发现并量化系统性行为模式，生成有证据支撑的诊断报告
practical_value: '- **大规模轨迹分析的工程参考**：将轨迹数据预处理成结构化 Parquet，构建 schema 缓存和向量索引，Agent
  只通过 Python REPL 调用统计工具而非直接读取原始文本，可大幅降低上下文消耗，适用于电商 Agent 日志的海量诊断。

  - **假设-验证分离的 Agent 角色设计**：Scout 负责在小样本中探索模式提出候选假设，Investigator 在全量数据上进行统计验证并计算效应量（p
  值、odd ratio），这种分工可迁移至推荐系统 Agent 的 A/B 实验诊断或行为差异分析。

  - **报告驱动的 scaffold 优化**：人类专家使用 IG 报告后，scaffold 性能提升 30.4 pp（对比无报告基线），且报告深度与证据质量直接影响修改效率；在自动优化循环中，每轮重新生成分析报告可以避免纯
  scaffold 搜索的退化。可借鉴该闭环思想，将生成式推荐或电商 Agent 的离线评估日志自动转化为 prompt 或工具链的改进建议。

  - **评估框架的复用**：提出的四维度评估（覆盖度、配对胜率、质量评分、人工干预提升）可作为自建 Agent 诊断系统效果的度量标准，尤其适合验证诊断报告对工程师开发效率的实际价值。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**
LLM Agent 的执行轨迹通常包含成千上万个 token，单个轨迹的调试无法发现跨轨迹群组的系统性模式，如沉默失败、效率差异或特定条件下的行为退化。这些模式只有在语料库级别进行群体对比时才可见，而现有的单轨迹分析或固定分类法难以自动化地完成此类发现与验证。

**方法关键点**
- **多智能体分工**：Orchestrator 接收诊断问题，调度 Scout（假设生成）和 Investigator（假设验证）。Scout 在约 50-200 条采样轨迹上探索，提出候选假设；Investigator 在全量语料上通过统计计算确认或证伪假设，并输出置信度与效应量。
- **结构化数据层**：所有轨迹预先经 Python 处理成带元数据的 Parquet 存储，Agent 仅通过代码执行工具进行分组、对比、Cramér's V 等分析，避免将原始长文本塞入 LLM 上下文。
- **迭代循环**：Orchestrator 可多轮交替分发 Scout 和 Investigator，根据已确认的发现决定是否补充新假设或提交最终报告，报告包含证据引用、流行度估计和可操作建议。
- **评估体系**：提出四层评估：LLM 裁判的覆盖率/配对胜率/质量评分、人类专家评分报告质量、人类专家基于报告修改 scaffold 的性能提升、以及自动修补循环的收敛效果。

**关键实验与数字**
- **基准**：SpreadsheetBench（296 轨迹）和 HLE（250 轨迹），涵盖电子表格操作和闭卷专业问答。
- **对比系统**：Single-Agent Coding、CC Subagents、Trace2Skill-style、RLM。IG 在配对胜率（77.9%）和机制解释/特异性维度得分上均领先，而覆盖率（91%）与最佳系统接近。
- **人类专家干预**：使用 IG 报告的工程师将 scaffold 准确率提升 30.4 pp（从 27.0% 到 57.4%），远超 CC Subagents 报告的 16.2 pp 提升，编辑改动更精准。
- **自动修补循环**：含 IG 分析的循环可持续提升到 0.84 准确率，而无分析输入的纯修补器在第二轮即退化。

**最值得记住的一句话**
“Insights Generator 的 Scout-Investigator 架构与结构化数据层的结合，使得语料库级别的行为洞察既能覆盖广泛模式，又具备统计严密的证据深度，直接转化为工程师优化 Agent 的显著能力提升。”
