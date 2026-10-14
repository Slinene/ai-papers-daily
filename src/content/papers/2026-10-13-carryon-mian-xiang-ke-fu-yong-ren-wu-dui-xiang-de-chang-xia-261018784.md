---
title: 'Pack Light, CarryOn: Building Object-Oriented Context for Long-Horizon Agents'
title_zh: CarryOn：面向可复用任务对象的长程 Agent 上下文运行时
authors:
- Yuchen Lu
- Julian McAuley
- Lei Zhang
affiliations:
- University of California San Diego
arxiv_id: '2610.18784'
url: https://arxiv.org/abs/2610.18784
pdf_url: https://arxiv.org/pdf/2610.18784
published: '2026-10-13'
collected: '2026-10-14'
category: Agent
direction: 长程 Agent 上下文管理 · 对象化折叠
tags:
- long-horizon agents
- context management
- object-oriented context
- OSWorld
- token efficiency
- agent memory
one_liner: CarryOn 将长程 Agent 上下文组织为可复用任务对象 + 执行上下文 + 近期交互，OSWorld 2.0 和 BrowseComp-Plus
  分别 +5.8%/+7% 并大幅降 token
practical_value: '- 在电商运营/客服长流程 Agent 中，把已完成的商品素材、报表、投放设置等作为 external object carrier，只记录对象路径与使用条件，续接时让
  Agent 直接读对象检查，替代反复携带生产日志。

  - 显式保留 execution context（目标、约束、未完成任务）与 carrier 互补；论文消融显示缺失该组件会使 partial 分数从 55.93
  降至 44.00，实际系统里容易因折叠丢失当前焦点。

  - 采用 fold 机制：当可复用产物形成（如图片导出、报表填充）就折叠历史，验证后原子提交，能将输入 token 稳定在阈值附近，成本优势随轨迹变长而扩大（OSWorld
  上 500 步降本 34.1%）。

  - 信息检索式 Agent（选品调研、竞品分析）可把中间结论存为 information product carrier 并绑定来源，减少重复搜索；论文在 BrowseComp-Plus
  上实现 +7% 准确率且 token 降 22.9%。'
score: 8
source: arxiv-cs.CL
depth: full_pdf
---

**动机**
长程 Agent 在任务推进中会积累大量交互历史，但这些历史多是对已产生结果的冗余描述。例如图片已插入 PPT、数据已填入表格，后续步骤只需检查和修改这些可复用结果，而无需反复处理产生它们的过程。现有压缩/摘要/检索方法仍以历史或重建的进度描述作为续接基础，容易与 Agent 直接操作的真实任务状态脱节。

**方法关键点**
- 上下文视图由三部分组成：continuation carriers（可复用任务对象）、execution context（目标/约束/未解决问题）、live tail（最近折叠以来的原始交互）。
- carriers 分三类：external objects（文件、文档等工作产物，记录对象引用与使用条件）、information products（可复用发现，直接存储带来源的结论）、situated state（仅在特定应用/会话中存在的状态，记录环境锚点与作用域）。
- 通过 fold 机制定期折叠 live tail：Tracker 识别候选 progress → Grounder 对对象做只读环境检查并绑定证据 → Compiler 联合更新 carriers 与 execution context → 验证后原子提交，覆盖交互历史。
- 跨 fold 维护 carrier 记录：受影响记录更新为 successor 版本，未受影响则直接 carried forward，避免每次重建完整表示。约 80% 的 carrier 记录在 fold 后被保留或更新。

**关键结果**
- OSWorld 2.0：partial 分数从 43.9% 提升到 49.7%（+5.8 个百分点），binary 从 15.7% 到 19.4%；总 token 降 51.9%，成本降 35.9%，输入上下文稳定在约 65K tokens（基线超 200K）。
- BrowseComp-Plus：准确率 49% → 56%（+7%），token 降 22.9%，成本降 7.1%。
- 在 40 任务子集上，Sliding Window/Generic Summary 均低于 baseline，CarryOn 达 55.93% partial，高于 CarryOn-Guided Summary 的 50.93%。
- 消融：移除 execution context 或 continuation carriers 都会使 partial 分数降至约 44%，且移除 carriers 后 agent 调用次数 +23.8%。

**最值得记住的一句话**：可复用任务对象应当成为长程续接的“主语”，而不是对它产生过程的冗余叙述。
