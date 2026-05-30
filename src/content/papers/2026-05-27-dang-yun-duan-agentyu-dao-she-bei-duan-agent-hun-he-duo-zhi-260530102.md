---
title: 'When Cloud Agents Meet Device Agents: Lessons from Hybrid Multi-Agent Systems'
title_zh: 当云端Agent遇到设备端Agent：混合多智能体系统的实践教训
authors:
- Corrado Rainone
- Davide Belli
- Bence Major
- Arash Behboodi
affiliations:
- Qualcomm AI Research
arxiv_id: '2605.30102'
url: https://arxiv.org/abs/2605.30102
pdf_url: https://arxiv.org/pdf/2605.30102
published: '2026-05-27'
collected: '2026-05-30'
category: MultiAgent
direction: 混合云边多智能体系统 · 架构与成本/能效权衡
tags:
- Hybrid MAS
- Cloud-Edge Inference
- SLM
- LLM Agents
- KV-cache
- Task-dependent Architecture
one_liner: 系统研究混合云边多智能体架构的性能-成本-能效权衡，揭示规划式与建议式架构的任务依赖性及上下文重置对长程执行的关键作用
practical_value: '- **混合部署策略**：将 token 密集型执行放在设备端（Qwen3 4B-32B），云端（GPT-4o）仅作周期性监督，可大幅降低
  API 成本同时保持竞争力，适合电商客服 Agent、商品信息聚合等长程交互场景。

  - **按任务特性选型**：结构化规划（PEVR）在状态空间大且错误不可逆的 UI 操作任务中显著优于建议式（EVA），而深度搜索类任务中建议式更优，启示电商
  Agent 在导购对话（需要严格跟进步骤）和文档检索（需要灵活聚合）场景应采用不同协作模式。

  - **控制监督频率与上下文重置**：过频繁的云端干预会损害性能，合适的验证间隔及干预后的上下文重置可防止 KV-cache 膨胀，让设备端 SLM 能胜任长程任务，适合内存受限的移动端部署。

  - **避免简单路由**：混合 MAS 能解决单纯云或设备端模型独立无法完成的任务子集，因此构建云端-设备协同系统时应考虑动态任务分配而非静态路由，在电商 Agent
  工作流中可据此设计协调整合模块。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：前沿 LLM 推理成本高昂且依赖云 API，设备端 SLM 虽经济但能力有限，尤其是在长上下文和复杂状态追踪上差距显著。混合多智能体系统（云边协同）是潜在平衡方案，但其设计空间复杂，缺乏通用原则，已有工作多为特定领域定制的 ad hoc 集成。本文旨在系统探索云边混合 MAS 的架构选择、模型分配和监督策略对准确率、金钱成本及边缘能耗的影响，为从业者提供可操作的权衡依据。

**方法关键点**：
- 抽象两种代表性云边混合架构：**PEVR**（Plan-Execute-Verify-Replan），由云端 Supervisor 生成初始计划并按固定间隔验证，失败时重新规划；**EVA**（Execute-Verify-Advise），无初始计划，云端定期验证并提供总结与建议，干预时重置执行上下文。
- 执行器均为设备端 Qwen3 系列（4B/8B/14B/32B），监督器为 GPT-4o；通过调整验证间隔（1~16 步）控制云端参与度。
- 能源消耗通过近似模型估算（2N 参数 × token 数 / 硬件效率），成本按 Azure API 定价计算，并追踪最大 KV-cache 内存占用。

**关键实验与结果**：
- 在 HotpotQA、FanOutQA（深度搜索）和 AppWorld（交互式 UI 辅助）三个基准上评估。
- 混合系统总能在准确性上超过纯设备端 agent，且成本显著低于纯云端 agent；在 AppWorld 上，PEVR 的 Test Pass Ratio 最高（0.21 vs EVA 0.14），而在 FanOutQA 上 EVA 的 ROUGE-1 达 0.23 远优于 PEVR。
- 并非云监督越多越好：存在最优验证间隔，过度干预反而降低性能；PEVR 的激进干预策略在深度搜索中造成性能下降。
- 上下文重置使 MAS 的 KV-cache 增长可控（如 Qwen3 32B 在 80 步时仅 7.9 GB vs 纯边缘 13.1 GB），更适合内存受限部署。
- 混合架构能解决其组件单独无法完成的任务子集，表明静态路由无法替代协作机制。

**核心洞察**：最优混合 MAS 架构高度依赖任务类型——规划式适用于状态敏感、错误高代价的 UI 交互，建议式适用于需要轻量级纠正的深度搜索，而合理的监督频率与上下文管理是实现长程可靠性的关键。
