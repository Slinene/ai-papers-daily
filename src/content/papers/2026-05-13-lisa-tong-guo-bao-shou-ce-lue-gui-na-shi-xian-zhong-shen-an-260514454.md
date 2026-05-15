---
title: 'LiSA: Lifelong Safety Adaptation via Conservative Policy Induction'
title_zh: LiSA：通过保守策略归纳实现终身安全适配
authors:
- Minbeom Kim
- Lesly Miculicich
- Bhavana Dalvi Mishra
- Mihir Parmar
- Phillip Wallis
- Bharath Chandrasekhar
- Kyomin Jung
- Tomas Pfister
- Long T. Le
affiliations:
- Google Cloud AI Research
- Seoul National University
- Google
arxiv_id: '2605.14454'
url: https://arxiv.org/abs/2605.14454
pdf_url: https://arxiv.org/pdf/2605.14454
published: '2026-05-13'
collected: '2026-05-15'
category: Agent
tags:
- Guardrail
- Policy Induction
- Memory
- Lifelong Learning
- AI Agents
- Safety
one_liner: 在稀疏、嘈杂反馈下，通过结构化策略记忆与证据感知重用的保守归纳，持续改进AI护栏
score: 8
source: huggingface-daily
depth: full_pdf
---

**动机**：AI 智能体（agent）从聊天界面扩展到访问私密数据、调用工具、执行多步工作流，安全护栏（guardrail）成为关键防线。但静态的通用护栏无法适配部署环境中动态变化的本地隐私规范、组织政策和用户期望，且实际反馈稀疏、嘈杂、不可重复微调。因此，如何让固定护栏从偶然的部署失败中持续提升，而不引入过拒绝或过允许，是一个待解决的难题。

**方法关键点**：
- **Online–offline 终身适配循环**：在线阶段护栏做决策并收集用户修正报告；离线阶段从稀疏报告中归纳策略记忆，不重训模型。
- **结构化策略记忆**：将失败案例抽象成可复用的自然语言策略（broad policy），合并语义重叠的项，避免仅存个案。
- **冲突感知局部策略**：在标签混杂的语义邻域生成精细化局部规则（local policy），解决宽策略的过泛化问题，提供边界线索。
- **基于证据的置信门控重用**：对每条宽策略维护 Beta 后验分布，使用后验下分位数（置信度）作为门控阈值，仅当累积足够证据时才将宽记忆注入推理，防止弱证据记忆过早影响决策。局部规则不受门控，直接作为边界信号。
- 基础设施：基座护栏（Gemini-3.1-flash-lite 或 Claude-Haiku-4.5）固定不变，离线管理由 Gemini-3.1-pro 完成，检索用 Gemini-embedding-001。

**关键实验**：
- 数据集：PrivacyLens+、ConFaide+、AgentHarm，二分类（允许/拒绝）。
- 模拟部署：每日流式输入，仅误判案例获得反馈，定期离线刷新记忆，在固定预留集上评估。
- 基线：纯预测（无适配）、AGrail（清单式更新）、Synapse（检索过往案例）、ReasoningBank（策略抽象记忆）。
- LiSA 最终日宏 F1 平均达 0.962（噪声 0%），优于 ReasoningBank 的 0.936 和其他基线；在 20% 标签翻转噪声下保持 0.917，远超其他方法。
- 消融指出局部规则是性能提升的主要驱动力，置信门控显著降低方差、提升鲁棒性。
- 延迟–性能分析显示，LiSA 附加到轻量护栏上的延迟–F1 前沿超越了放大静态骨干模型的趋势，成本效率更优。

**一句话**：Guardrail 的有效适配不依赖微调或更大的模型，而在于对部署经验进行证据校准的保守重用。
