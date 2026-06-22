---
title: Efficient and Sound Probabilistic Verification for AI Agents
title_zh: 面向AI代理的高效可靠概率验证
authors:
- Alaia Solko-Breslin
- Pramod Kaushik Mudrakarta
- Mihai Christodorescu
- Somesh Jha
- Krishnamurthy Dj Dvijotham
affiliations:
- Google DeepMind
- Google
- University of Pennsylvania
- University of Wisconsin–Madison
arxiv_id: '2606.20510'
url: https://arxiv.org/abs/2606.20510
pdf_url: https://arxiv.org/pdf/2606.20510
published: '2026-06-18'
collected: '2026-06-22'
category: Agent
direction: Agent 概率安全验证 · 分布鲁棒优化
tags:
- Agent Verification
- Probabilistic Policies
- Distributionally Robust Optimization
- Runtime Monitoring
- Datalog
one_liner: 基于分布鲁棒优化提出概率验证框架，不依赖独立性假设，计算策略违规概率严格上界，安全-效用权衡优于现有方法
practical_value: '- 在推荐/广告Agent中，安全策略常含不确定性（如敏感内容检测器召回率有限），可借鉴其概率谓词建模方法，将组件失败概率纳入形式化策略，并使用分布鲁棒优化计算整体违规风险上界，避免依赖不现实的独立性假设。

  - 工程实现中，可将该框架集成到Agent运行时监控系统：对每个工具调用或状态变迁，实时查询Datalog策略，并用凸优化器高效计算当前风险上界；当上界超过阈值时触发降级动作，实现可量化的安全兜底。

  - 框架不要求各概率事件独立，适合电商推荐Agent多步骤长链路场景（如检索→过滤→排序→文案生成），其中错误可能因上游模型相关而叠加，直接应用该上界计算方法能更真实地评估端到端安全风险。

  - 上界计算的可解释性可用于业务风控：为每个策略规则输出违规概率贡献，帮助安全团队理解风险来源，调整检测器阈值或策略约束，从而在安全性与推荐效果间取得更好的平衡。'
score: 6
source: arxiv-cs.AI
depth: abstract
---

**动机**：AI代理通过直接操作终端、文件系统和API扩展了大模型的能力，但也引入了安全风险（如误发敏感文件）。现有运行时监控方法依赖Datalog等形式化语言制定确定性策略，无法处理现实中的概率性组件（如PII检测器有漏报/误报）。虽然存在概率Datalog推理方法，但普遍假设谓词间独立，而实际代理的多个概率步骤存在未知相关性，导致违规概率被低估。亟需一种在任意相关性下仍能提供可靠上界的验证方法。

**方法**：提出基于**分布鲁棒优化**（Distributionally Robust Optimization）的验证框架。将策略违规概率建模为给定概率谓词边际分布下的最坏情况期望，不依赖独立性假设，通过求解一个凸优化问题得到严格上界。具体地，将Datalog规则转化为逻辑约束，与各谓词观测到的失败概率一致的所有可能联合分布中，最大化违规期望，从而得到鲁棒边界。框架可处理概率谓词和状态转移，并保证界限的可靠性（sound）。

**结果**：在终端代理（如命令执行）和工具调用代理的标准基准上，与现有概率推理方法相比，该方法给出的违规概率上界更紧且可靠，同时提升了安全性-效用权衡。在相同效用下，能保证更低的违规风险，或相同风险下允许更优的效用。框架的计算效率也满足在线监控需求。
