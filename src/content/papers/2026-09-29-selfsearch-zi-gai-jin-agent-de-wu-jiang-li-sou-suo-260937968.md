---
title: 'SelfSearch: Reward-Free Search for Self-Improving Agents'
title_zh: SelfSearch：自改进 Agent 的无奖励搜索
authors:
- Jungwoo Yang
- In Jin Kong
- Yohan Jo
affiliations:
- Graduate School of Data Science, Seoul National University
arxiv_id: '2609.37968'
url: https://arxiv.org/abs/2609.37968
pdf_url: https://arxiv.org/pdf/2609.37968
published: '2026-09-29'
collected: '2026-09-30'
category: Agent
direction: Agent 自我改进 · 无奖励搜索
tags:
- Self-improving agents
- Reward-free search
- LLM agents
- Agent search
- SWE-bench
- Metacognition
one_liner: 用历史自我改进轨迹取代下游评估信号，驱动 Agent 自我修改并提升任务成功率与执行效率
practical_value: '- 可将业务 Agent（如广告文案、query 改写、选品分析）历次自我修改的 reasoning、工具调用、失败与代码变更沉淀为可检索经验库；在没有线上收益或频繁
  A/B 的情况下，先低成本迭代 scaffolding，再少量验证。

  - 工程上把 runtime 与可编辑 agent repository 分离，固定推理设置、资源预算和轨迹记录，适合电商/广告场景中安全地让 agent 修改工具和规划器，保证可回滚。

  - 借鉴双 lineage + 共享 episode records：capability 方向专注新增可复用工具，adaptive 方向专注失败恢复，避免单一改进路径过拟合，对工作流自动演化尤其有用。

  - 优先建设“面向自我调试的可复用工具”，如带输出上限的 text search、line-range file viewing、call/result 关联；这些工具既能提升任务解决，也会在后续自改进中被复用。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
LLM agent 已经能检查和修改自身指令、工具与执行流程，但现有 evaluation-guided search 需要反复下游评估，成本高且搜索被绑定到评估任务。SelfSearch 关心的是：能否把“自我修改过程本身”当作经验，不依赖下游 reward 信号就能持续改进 agent。

**方法关键点**
- 完全可编辑的 agent repository，模型权重固定；同一个 agent 同时负责下游任务与自我修改。
- 每个 self-improvement episode 中，agent 读取只读的历史 episode records（推理、工具动作、结果、代码变更），决定改什么、编辑并验证自己的实现，产生 successor agent 和新的 episode record。
- 维护 capability / adaptive 两个 lineage，每代只共享上一代 episode records，搜索方向是定性指令，不做评分；不使用下游任务与评估结果。
- runtime 置于可编辑仓库之外，固定模型、reasoning effort、资源限制与轨迹记录，保证自改进过程可控。
- 初始先运行两个方向各一次生成初始 episode records，但丢弃修改实现，两个 lineage 从同一 B0 出发；十代后保留全部候选。

**关键实验与结果**
在两个模型配置（GPT-5.6 Sol/Luna、DeepSeek-V4 Pro/Flash）上评估 SWE-bench Verified、SWE-bench Multilingual 和 Terminal-Bench 2.1。与初始 agent、evaluation-guided linear/archive search、ablations 以及公开九 harness 对比。
- 全部六个 model–benchmark 设置中，population-mean success 均超过初始 agent。
- Terminal-Bench 2.1：GPT capability agent 43.8%→55.1%，DeepSeek 65.2%→73.0%；个体最大提升 11.2 pp。
- SWE-bench Multilingual：GPT +6.7 pp，DeepSeek +5.0 pp；DeepSeek adaptive 在共同成功任务上执行成本下降 38.5%。
- SWE-bench Verified：DeepSeek 两 lineage 从 81.7% 提升到 86.7%。
- 与 evaluation-guided search 相比，SelfSearch 搜索成本低 13.4–53.2%，成功率不输甚至有优势。
- 只用 $4.03 搜索成本，SelfSearch 生成的 harness 在 DeepSeek V4 Flash 上取得 Terminal-Bench 2.1 82.0%，追平 Codex。
- Ablation：去掉 episode records 或固定 improver 均导致 population mean 下降 1.7–2.9 pp，说明两个机制都有贡献。
- 自改进中产生的 text search、line-range viewing 等工具在下游任务中被复用，跨模型迁移也保持提升。

**最值得记住的一句话**
> 自我改进过程的轨迹本身就能成为有效的改进信号，不必每次都用下游评估信号来引导 agent 搜索。
