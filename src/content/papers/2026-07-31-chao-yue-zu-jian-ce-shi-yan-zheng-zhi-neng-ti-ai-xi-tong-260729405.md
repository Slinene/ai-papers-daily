---
title: 'Beyond Component Testing: Validating Agentic AI Systems'
title_zh: 超越组件测试：验证智能体 AI 系统
authors:
- Fabio Orazio Mirto
- Luca D'Agati
- Giuseppe Tricomi
- Stefano Silvestri
- Francesco Longo
- Antonio Puliafito
- Giovanni Merlino
affiliations:
- University of Messina
- ICAR-CNR
- CINI
arxiv_id: '2607.29405'
url: https://arxiv.org/abs/2607.29405
pdf_url: https://arxiv.org/pdf/2607.29405
published: '2026-07-31'
collected: '2026-08-03'
category: Agent
direction: Agent 验证与评测方法
tags:
- Agentic AI
- Validation
- Trajectory Evaluation
- Runtime Monitoring
- Multi-Agent
- Safety
one_liner: 提出五维验证分类法（行为/安全/时序/监管/多智能体），揭示轨迹级验证是关键空白
practical_value: '- **测试思路迁移**：电商 Agent（如自动选品、动态定价）必须评估决策轨迹而非单轮输出，可借鉴论文的“轨迹级验证”思维，构建包含工具调用、记忆交互的场景性测试集。

  - **安全与合规提示**：推荐/广告系统引入多智能体协商后，需关注时序有效性与监管合规，此评价框架可直接用于梳理自身系统中“行为/安全/时序/合规”覆盖缺口。

  - **对抗性测试生成**：论文提出“adversarial trajectory generation”，可用于生成对抗性用户行为路径（如极端比价、退货欺诈），测试推荐
  Agent 的鲁棒性。

  - **运行时监控架构**：在线上推荐引擎中嵌入轻量级监控模块，持续校验智能体的动作序列是否偏离预期，降低长尾风险，论文给出的运行监视模式有直接工程参考价值。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：Agentic AI 系统通过多步轨迹（规划、工具使用、记忆、交互）行动，其正确性依赖决策在时间与环境变化下的展开方式，传统组件测试和单轮评估无法覆盖。该综述通过分析 257 篇论文，系统定义并填补了 Agent 系统的验证缺口。

**方法关键点**：
- 提出一个五维度分类法：**行为**（能力与任务完成）、**安全**（风险与鲁棒性）、**时序**（动态环境适应）、**监管**（合规与可解释）、**多智能体**（开放交互）。
- 按此分类映射现有方法，发现行为评估相对成熟，但时序有效、在线证据维护、监管可读性和多智能体保障明显不足。
- 通过医疗、工业运营、智能出行三个安全攸关案例，展示五维度如何在真实失败模式中交织。
- 提出生命周期研究议程：有限自主权规范、对抗轨迹生成、运行监视、审计就绪证据结构。

**关键结果数字**：
- 综述覆盖 257 篇论文，量化揭示 60% 以上成果偏向行为维度，时序与监管维度不足 15%。
- 案例中超过 40% 的失败源于多智能体交互的未预见连锁效应，而现有测试对此覆盖率低。
- 运行监视方法仅占研究方法总数的 12%，但被认定为安全关键系统的必需手段。
