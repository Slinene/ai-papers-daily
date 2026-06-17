---
title: 'OPD-Evolver: Cultivating Holistic Agent Evolver via On-Policy Distillation'
title_zh: OPD-Evolver：基于在线策略蒸馏训练整体智能体进化能力
authors:
- Guibin Zhang
- Xun Xu
- Yanwei Yue
- Zikun Su
- Wangchunshu Zhou
- Xiaobin Hu
- Shuicheng Yan
affiliations:
- LV-NUS Lab
- FDU
- PKU
- Bytedance Inc.
arxiv_id: '2606.17628'
url: https://arxiv.org/abs/2606.17628
pdf_url: https://arxiv.org/pdf/2606.17628
published: '2026-06-15'
collected: '2026-06-17'
category: Agent
direction: 整体代理进化 · 在线策略蒸馏
tags:
- On-Policy Distillation
- Self-Evolving Agents
- Memory Management
- Experience Lifecycle
- LLM Agents
one_liner: 提出快慢双环框架，将结果校准的记忆归因与特权后见蒸馏结合，同时训练经验选择、利用、撰写和管理四种进化能力
practical_value: '- **多级记忆分层与选择**：将代理经验按轨迹、技巧、技能、工具分四级存储，并用可学习的 Selector 筛除低价值记忆，可直接用于推荐系统的用户行为记忆或搜索历史管理，避免上下文噪音。

  - **结果校准的归因监督**：用环境反馈（任务成功/失败）校准记忆价值，生成密集后见标签，可迁移到对话推荐或交互式搜索中对历史交互片段的价值评估。

  - **在线策略自蒸馏框架**：让学生在自己生成的状态上模仿特权教师的行为，实现选择、执行、撰写、维护四种能力的联合训练，适用于需要持续进化的推荐代理或商品描述生成代理。

  - **记忆写入的质量控制**：训练代理只生成高未来效用的记忆，避免“记忆污染”，可借鉴到用户标签或知识图谱的自动更新中，确保新增信息对下游任务有正收益。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：现有记忆增强代理能存储轨迹，但缺乏将经验转化为可持续行为改进的整体进化能力。要么只关注检索，要么仅优化记忆写入，各阶段割裂导致长期自主进化困难。本文目标是将代理训练为一个合格的进化者，同时具备选择有用经验、基于经验执行动作、从新轨迹中提取可复用知识以及持续管理记忆仓库的能力。

**方法关键点**：
- 定义智能体进化者需具备四项耦合能力：经验选择、经验基执行、经验撰写、经验管理。
- 设计快慢双环框架：快环负责与四级记忆（轨迹、技巧、技能、工具）在线交互，执行选择、动作与记忆写入，并定期合并/删除维护；慢环利用结果校准的归因将稀疏任务反馈转化为记忆价值信号，通过特权后见进行在线策略自蒸馏，联合训练四个能力。
- 蒸馏用令牌级 KL 散度，学生仅接触公开输入，教师额外观察记忆价值、成功轨迹等后见信息，形成选择、执行、撰写、维护四组蒸馏目标。

**关键实验**：
- 在 LifelongAgentBench、MemoryArena、AMA-Bench、InterCode 等跨领域基准上，OPD-Evolver 在同参数量级下全面超越 ReasoningBank、MemEvolve、EvolveR 等记忆系统，对 ReasoningBank 最高提升 11.5%；相比 Skill0 等训练方法提升约 5.8%。
- OPD-Evolver-9B 在 6/10 子任务上超越 397B 的 QWEN3.5-A17B，包括 AMA-SA (52.92% vs 51.41%)、InterCode-CTF (57% vs 56%)。
- 消融表明去掉慢环或记忆归因导致性能严重下降（平均 38.67%→32.13%）；选择蒸馏将选中记忆的价值中位数从 0.66-0.69 提升至 0.76-0.79；写作蒸馏将生成记忆的价值中位数从 0.80-0.82 升至 0.89-0.91。

**最值得记的话**：要做到真正的自我进化，代理不能只存储记忆，必须学会判选、善用、精写和勤理；通过特权蒸馏将这四种生命周期能力内化进同一个策略，比单纯扩大模型更有效。
