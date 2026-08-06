---
title: 'Argus: A General-Purpose Agentic Runtime for Long-Horizon Reasoning'
title_zh: Argus：验证引导下可持续进化的通用长程Agent运行时
authors:
- Boxiu Li
- Zimo Wen
- Yijia Fan
- Junxiang Lei
- Sufeng Guo
- Jiaao Wu
- Ruize Tang
- Mukai Li
- Yifei Shen
- Xiaoyu Chen
affiliations:
- Microsoft
- Shanghai Jiao Tong University
- Fudan University
- Nanjing University
- Tsinghua University
arxiv_id: '2608.05144'
url: https://arxiv.org/abs/2608.05144
pdf_url: https://arxiv.org/pdf/2608.05144
published: '2026-08-05'
collected: '2026-08-06'
category: MultiAgent
direction: 多智体协作的持久化研究运行时
tags:
- Agentic Runtime
- Verification-Gated Evolution
- Long-Horizon Reasoning
- Multi-Agent Systems
- SWE-Bench
- Self-Evolution
one_liner: 一种带角色分工与验证门控的Agent运行时，允许目标修正同时防止目标漂移，在固定模型下实现状态自进化
practical_value: '- 在电商搜索推荐Agent系统中，可借鉴“验证-门控”持久状态管理，将用户意图与操作目标分离，允许根据反馈修正目标并记录，避免工作流中断或错误累积。

  - 将长程任务分解为有界任务（missions），由 Manager / Planner / Engineer / Reviewer 角色协作，可迁移到多 Agent
  推荐系统的任务编排，减少模型幻觉导致的错误扩展。

  - 固定模型参数，仅通过验证门控方式进化记忆、技能、验证规则等持久状态，为生产环境中不希望频繁微调的场景提供了一种轻量级 Agent 改进方案。'
score: 8
source: arxiv-cs.AI
depth: full_pdf
---

**动机**：长程推理任务中，初始目标常因缺失信息而不完全准确，允许中途调整目标至关重要。但无约束的目标修正会退化为“目标漂移”，即系统将目标降级到当前能完成的水平。该工作提出一种验证引导的枢转机制，通过证据、角色责任制和可审计记录，使目标修正具备可区分性和可继承性。

**方法关键点**：
- **有界任务与持久状态**：将研究过程划分为一系列有界任务（missions），每个任务对持久项目状态（记忆、技能、工具、验证器、路由规则）产生更新，任务间状态持久化。
- **四角色分工**：Manager 确定目标与阶段转换，Planner 分解任务，Engineer 执行与自评（低风险任务），Reviewer 独立审查并提供完成判决；完成判决严格区分自评与独立审查。
- **验证门控的运行时自进化**：模型参数固定，但通过验证门控将经过角色审核的记忆、技能、验证规则等持续纳入持久状态，使得后续任务可从更成熟的状态启动，实现经验复用与策略改进，而非单调的上下文增长。
- **工作契约模型**：将目标、约束、验证准则与用户意图显式分离，ManagerAdmit 算子控制材料修改，防止隐性目标变更。

**关键结果**：
- SWE-Bench Pro 上准确率约 78%（Direct Copilot 为 59%），总 token 消耗约 1.41 倍。
- 在 SWE-Bench Pro 连续运行中，相比起始阶段，成熟阶段每个任务平均求解 token 减少 21%，有效工作时间减少 15%；观察到 34 次验证器恢复与 22 次严格审查回路挽回。
- 其余六项基准（GPU 内核优化、模型训练、训练速度、AARRI-Bench 研究任务、数学数据合成）均达到或超越当时最优结果。
- 一项多日数学研究活动中保留了一条被证伪的路径与六条定理前沿更新，六条论文生产流水线共执行 254 个任务并完成提交。
- 系统产出的优化后 RWKV6 内核被上游仓库合并，证明了外部署名验证。
