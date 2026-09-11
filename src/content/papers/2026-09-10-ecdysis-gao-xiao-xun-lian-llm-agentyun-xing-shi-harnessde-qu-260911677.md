---
title: 'Ecdysis: Efficient and Effective Training of Runtime Harnesses for LLM Agents'
title_zh: Ecdysis：高效训练LLM Agent运行时harness的失败诊断驱动框架
authors:
- Ruiqing Yue
- Yu Cui
- Zhuoyu Sun
- Sicheng Pan
- Xianhong Xue
- Tingyu Li
- Ting Li
- Wenzhuo Zhu
- Yi Chen
- Yifei Liu
affiliations:
- Chengdu Institute of Computer Applications, Chinese Academy of Sciences
- University of Chinese Academy of Sciences
- Beijing Institute of Technology
- Beijing University of Technology
- Yangtze Delta Region Institute of Tsinghua University, Zhejiang
arxiv_id: '2609.11677'
url: https://arxiv.org/abs/2609.11677
pdf_url: https://arxiv.org/pdf/2609.11677
published: '2026-09-10'
collected: '2026-09-11'
category: Agent
direction: Agent 运行时自进化 · 失败归因
tags:
- LLM Agents
- Runtime Harness
- Self-Evolution
- Failure Diagnosis
- Multi-Agent
- Training Efficiency
one_liner: 跨任务失败聚合与多角色协作诊断，区分模型适配与系统缺陷，实现训练加速与泛化提升
practical_value: '- 在搜索/推荐 Agent 的 workflow 优化中，不要针对单条失败 case 直接改 prompt 或工具逻辑；先批量收集失败轨迹，按“失败模式”跨任务分组，只对重复出现的模式做系统级修改，能显著减少过拟合和重复修改成本。

  - 把“诊断”与“实施”分离：用 Analyst/Critic/Engineer/Moderator 多角色写结构化修改规范，再交给 coding agent
  改代码。这相当于在修改工作流前加一道评审，能降低无效修改，提升输入 cache 命中率（论文从 89% 升到 96%）。

  - 用诊断价值选训练样本：优先选暴露新交互路径和未知失败机制的任务，而不是全量随机；论文中仅用 1/4 训练失败样本就接近全量效果，可用于电商/广告 bad case
  分析的降本。

  - 监控 model-accommodation ratio：统计修改中有多少是在迁就当前 LLM 的怪癖；若过高，该 workflow/工具链很可能只对当前模型有效，换模型会退化。可把这个指标纳入
  Agent 上线前的回归检查。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

### 动机
现有 LLM Agent 的 runtime harness 自进化方法多依赖逐条失败反馈迭代搜索，既慢又容易过拟合。核心难点在于失败归因：一次失败可能是当前模型的局限，也可能是 harness 的系统缺陷；逐条修复容易导致“模型特定适配”，牺牲跨任务、跨模型的泛化能力。

### 方法关键点
- **批量跨实例失败聚合**：每轮收集多个任务的失败轨迹，按失败模式分组，优先处理至少在两个不同任务中重复出现的模式，将其视为系统 harness 缺陷的更强证据。
- **Failure-Driven Collaborative Refinement (FDCR)**：Analyst、Critic、Engineer 多角色基于共享 transcript 迭代细化修改建议，Moderator 合成结构化修改规范，再交给 coding agent 实施；诊断与实施解耦。
- **候选接受**：只要求整体训练集得分提升，不要求每个任务都变好，避免过度修改。
- **训练数据策展**：选择能暴露新执行路径和失败机制的任务，减少冗余失败信号；实验显示用 1/4 训练失败样本可接近全量性能。

### 关键结果
在 Qwen3-8B/14B/32B、MiniMax-M2.7、Llama-3.1-8B 五个 LLM 和 τ2-Airline、τ2-Retail、AgentBench 上，ECDYSIS(w/ FDCR) 相对 Self-Evolution 平均准确率从 58.67% 提升到 69.56%（+18.56%），Pass^3 提升 55.2%。训练时间最高加速 3.23×（w/o FDCR）和 1.84×（w/ FDCR），API 成本降低 59-70%。推理 token 降低 10-12%，跨模型泛化更好；model-accommodation ratio 从 SE 的 60.0% 降至 45.5%。

### 一句话
失败信号不是统一可行动的；跨任务重复出现的失败才是系统 harness 缺陷的更强证据，应据此修复而非迁就当前模型。
