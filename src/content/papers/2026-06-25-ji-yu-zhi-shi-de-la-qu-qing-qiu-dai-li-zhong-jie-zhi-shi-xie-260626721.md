---
title: 'Knowledge-Based Pull Requests: A Trusted Workflow for Agent-Mediated Knowledge
  Collaboration'
title_zh: 基于知识的拉取请求：代理中介知识协作的可信工作流
authors:
- Xinyu Zhang
- Weiwei Sun
affiliations:
- Fudan University
arxiv_id: '2606.26721'
url: https://arxiv.org/abs/2606.26721
pdf_url: https://arxiv.org/pdf/2606.26721
published: '2026-06-25'
collected: '2026-06-27'
category: Agent
direction: 代理协作中的信任边界与知识传递机制
tags:
- Agent Collaboration
- Trust Boundary
- Knowledge Distillation
- Workflow
- Software Engineering
one_liner: 提出 KPR 工作流，将外部代码视为知识源，由项目内部可信代理重新生成代码，分离知识接纳与实现合并决策
practical_value: '- KPR 的“知识包”抽象可迁移到多智能体推荐系统：外部代理输出的推荐理由、交互轨迹不直接作为最终结果，而是交由内部代理结合业务规则和上下文再次生成，可提升安全性和一致性。

  - 分离“意图理解”与“实现生成”的决策模式，可应用于电商搜索 Agent 系统：用户粗浅意图由外部解析为结构化知识，内部受控代理根据知识包和商品图谱生成精准查询或推荐。

  - 信任边界设计对多供应商模型协作场景有启发：不同模型生成的推荐候选视为知识源，通过合规性检查门禁后在统一环境下重生成，降低集成风险。

  - 主要学术贡献在于软件工程与 Agent 协作流程，业务可借鉴点偏向 Agent 架构模式而非推荐算法细节。'
score: 6
source: arxiv-cs.HC
depth: abstract
---

**动机**：AI 编程代理使得代码生成成本下降，但理解需求、协商范围和长期维护的责任成本依然高昂。传统 PR 中外部代码直接作为合并候选，信任风险高，上下文理解困难。

**方法关键点**：提出 KPR 工作流，将外部协作者提交的本地代码、测试和经清洗的代理交互轨迹视为**知识源**而非合并候选。外部代理的知识提炼为需人工确认的知识包，包含设计备忘录、风险清单、测试计划等。项目内部受信任的编码代理在仓库上下文、工程规范和安全策略下重新生成候选代码。工作流分离两个决策：知识是否应进入项目，以及具体实现是否合并。论文贡献了工作流、候选产物模式、成本核算视图和协作网关架构。

**关键结果**：在 7 个已合并的公开 PR 上进行了最小化受控仿真实验，证明 KPR 包可从真实 PR 材料实例化，并在描述消融、差异消融和投毒补丁等压力测试下经过检验。表明可审计的提取、转换和项目侧重新生成能降低理解和高上下文外部更改的返工成本。
