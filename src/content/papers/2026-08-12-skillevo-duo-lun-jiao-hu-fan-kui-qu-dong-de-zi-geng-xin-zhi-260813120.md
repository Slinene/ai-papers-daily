---
title: 'SkillEvo: Self-Renewing Evolution Gradients from Multi-Turn Interaction Feedback'
title_zh: SkillEvo：多轮交互反馈驱动的自更新智能体技能进化
authors:
- Qianxi Yan
- Chunrong Chen
- Jiuzhou Zhao
- Min Zhang
- Yongzhou Xu
- Xiaochuan Xu
affiliations:
- Tencent Cloud Andon
- Zhejiang University
arxiv_id: '2608.13120'
url: https://arxiv.org/abs/2608.13120
pdf_url: https://arxiv.org/pdf/2608.13120
published: '2026-08-12'
collected: '2026-08-22'
category: Agent
direction: Agent Skill 自进化 · 多轮反馈
tags:
- Agent Skills
- Self-Evolution
- Multi-turn Simulation
- Feedback
- Skill Governance
- LLM
one_liner: 把多轮用户模拟从评估终点改为反馈生成器，并用独立治理层主动修复知识退化，使技能进化梯度可持续
practical_value: '- 多轮用户模拟不要只当测试集，要做成持续产出“可修复知识缺口”的反馈器：电商客服/导购 Agent 可从真实工单抽取 intent
  agenda + behavior facts + emotion trajectory，让模拟用户按状态机逐层追问，暴露单轮 QA 看不到的深层缺陷；每轮修复后对话自然进入下一层，梯度可再生。

  - 反馈可信度三条件值得照搬：coverage/accuracy/attributability。用 intent state machine 保覆盖，用 dual-sided
  orthogonal evaluation 区分 simulator 和 agent 责任，用 collective attribution 把失败分成 Knowledge
  Gap / Capability Limit / Evaluation Noise，只把 Knowledge Gap 送入修订。业务里先归因再改知识库，能避免把权限、工具或评测噪声误写成知识。

  - 治理层不要只做标量门禁，要做“结构诊断+主动修复”：对 Skill/知识库做 fact consistency 硬约束（dual anchors 分别抓跨轮知识丢失和本轮新增事实错误）和
  structural consistency 软约束（bloat、断链、过度泛化）。RAG 知识库、policy 文档、推荐策略知识库的多轮更新都适用，能明显抑制膨胀和事实漂移。

  - 版本选择用 dev 集而不是最终标量分数；自动修订不直接上线，保留 human checkpoint。线上 Agent 知识库或策略库的 closed-loop
  更新可以采用同样的工程护栏。'
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**
Agent Skills 是云客服等场景中承载领域知识与处理流程的可移植模块，但现有维护仍靠手工，失败对话无法自动沉淀。已有自进化工作多用单轮 QA 反馈，第一轮修掉可见缺口后梯度就衰减，多轮交互里的深层缺陷不可见，进化停滞。瓶颈不是编辑能力或迭代次数，而是反馈信号能否持续提供可信的进化梯度；治理若只有 scalar gate，也无法定位和修复结构化退化。

**方法关键点**
- **可信反馈生成**：从真实人工 ticket 合成受约束用户，包含 intent agenda、behavior facts、emotion trajectory；intent state machine 跟踪每个 intent 的 raised / addressed 状态，所有 key/minor intents 都被实质处理才允许正常结束，防止漏问和泄答。
- **Dual-sided orthogonal evaluation**：simulator 侧评估 intent coverage cU，coverage < 1 的样本隔离为 eval noise；agent 侧评估 skill hit 与 exposed-intent response accuracy sC，按 key/minor 意图加权。
- **Collective attribution**：失败分为 Knowledge Gap / Capability Limit / Evaluation Noise，仅 Knowledge Gap 被语义合并后作为反馈 L_t 进入修订，其余两类隔离。
- **Bounded editing**：evidence boundary 只补验证过的缺口；reference boundary 以生产基线 S0 为锚，避免新知识覆盖稳定事实。
- **Controllable governance**：fact consistency 作为硬约束，用 S0 和 S_{t-1} 双锚分别检测跨轮知识丢失和本轮新增事实错误；structural consistency 作为软约束，诊断 knowledge bloat、reference breakage、factual over-generalization，并将治理建议合并进下一轮修复。

**关键结果数字**
在腾讯云生产客服场景，覆盖 6 类云服务、9 个生产 Skills、98 个 skill-reference 文件、2000 张 tickets。四轮进化后，SkillEvo 的 TSR 从 30.0 升至 81.8，较原始 Skill 提升 51.8 点，较 self-reflection 提升 23.0 点，较 single-turn QA 提升 15.4 点；去掉 governance 后 TSR 降至 78.6，说明主要增益来自多轮反馈源。可信度方面，intent coverage 98.9%，人工盲评 fidelity 95.3%，agent 已暴露意图准确率 71.1%；治理方面，RegR 从 28.2 降到 21.1，Bloat 有治理时仅 +2.8%，无治理时达 +16.2%。

**最值得记住的一句话**
评价反馈的质量决定技能进化的上限：只有能让对话继续深入的反馈，才会在每轮修复后暴露下一层缺陷，使进化梯度自我更新。
