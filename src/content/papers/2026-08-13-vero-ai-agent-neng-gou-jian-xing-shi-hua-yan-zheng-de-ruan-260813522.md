---
title: 'Vero: Can AI Agents Build Formally Verified Software Repositories?'
title_zh: Vero：AI Agent 能构建形式化验证的软件仓库吗
authors:
- Zhe Ye
- Hantao Lou
- Yuechun Sun
- Peiyang Song
- Zhengxu Yan
- Timothe Kasriel
- Qingyang Zhang
- Kaiyu Yang
- Soonho Kong
- Jingxuan He
affiliations:
- UC Berkeley
- University of Chicago
- California Institute of Technology
- Stanford University
- Amazon Web Services
arxiv_id: '2608.13522'
url: https://arxiv.org/abs/2608.13522
pdf_url: https://arxiv.org/pdf/2608.13522
published: '2026-08-13'
collected: '2026-08-15'
category: Eval
direction: AI Agent 形式化验证代码生成基准
tags:
- Formal Verification
- Lean 4
- AI Agents
- Code Generation
- Benchmark
one_liner: 首个仓库级实现与证明联合合成的形式化验证基准，当前最强 Agent 仅完全解决 27/43
practical_value: '- 在电商/推荐系统的关键路径（如扣费、库存、ETL 数据一致性）中引入形式化验证 gate：为 API 接口编写 spec 和机器可检查证明，替代或补充单测，避免边界条件下的隐性
  bug。

  - 评估内部 AI coding agent 时，不要仅看测试通过率；可仿照 Vero 设计双模式评测：proof-only（只补证明）和 code-and-proof（实现+证明联合生成），衡量
  agent 能否在多模块上下文中保持规范一致性。

  - 采用 Vero 的审计机制：允许 agent 证明 spec 不可满足或参考实现错误，用于自动发现接口契约或参考代码中的隐含缺陷；迁移到业务中可对服务间契约建立形式化检查，提前暴露集成矛盾。

  - 仓库级验证思维对微服务架构有参考意义：把跨服务数据流、状态迁移约束用 Lean 4 等语言形式化，不仅能保证单个模块正确，还能验证跨模块组合语义，适合交易链路等高可靠场景。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

## 动机
AI coding agents 生成代码普遍缺少正确性保证，单元测试无法覆盖边缘情况。形式化验证代码生成要求同时产出实现和机器可检查的规范证明，是更可靠的路径。但现有基准要么只面向单函数，要么提供实现后只评估证明生成，无法检验 agent 在真实多模块代码库中做出一致的实现与证明选择。

## 方法关键点
Vero 是首个仓库级联合实现与证明合成基准，包含 43 个多模块实例，源自真实 Python、Dafny、Verus、Coq 仓库，覆盖密码协议到分布式系统等领域。每个实例转为多模块 Lean 4 仓库，预定义 API 接口、人工整理的形式化规范和参考实现。支持两种评估模式：proof-only（仅补证明）和 code-and-proof（同时生成实现与证明）。为提升可靠性，Vero 引入审计机制：允许 agent 形式化证明给定规范不可满足或参考实现错误，从而在基准维护过程中暴露并修正潜在错误。

## 关键结果
评估前沿 coding-agent 配置，最强 agent 在 43 个实例中仅完全解决 27 个，在最难仓库上没有任何规范闭合。表明当前 agent 远未达到仓库级验证软件合成的要求，Vero 为此类进展提供了具体测试平台。
