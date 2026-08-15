---
title: 'Specification-first convergence with an AI coding agent: a case study of dismantling
  a core architectural invariant across 189 files in a 717k-line codebase with no
  test oracle and no human code review'
title_zh: 规格优先：AI编码Agent无人工审查拆除核心架构不变量案例（189文件/71.7万行）
authors:
- Joel Abenhaim
affiliations:
- AI Sovereign Labs, Paris, France
arxiv_id: '2608.12440'
url: https://arxiv.org/abs/2608.12440
pdf_url: https://arxiv.org/pdf/2608.12440
published: '2026-08-11'
collected: '2026-08-15'
category: Agent
direction: AI 编码 Agent 规格化重构
tags:
- AI Coding Agent
- Specification-first
- Refactoring
- Verification Loop
- Case Study
- Agentic Software Engineering
one_liner: 规格优先协议让AI编码Agent在无人工审查和测试oracle下成功重构71.7万行代码，31轮审计收敛201缺陷
practical_value: '- **规格优先协议**：让 Agent 先写正式规格并反复对照源码审计，可迁移到用 Agent 生成推荐系统特征/模型代码时，先规格化业务不变量（如流式生成生命周期、面板状态机），降低幻觉与遗漏。

  - **审计收敛判据**：要求连续两次验证审计零发现才认定完成，避免单次通过假阴性；可用于 Agent 生成的推荐服务代码或配置的验证循环（如参数搜索空间、离线评估脚本）。

  - **原子实现与编译/测试反馈循环**：把大改动拆小，冻结规格后再审计；在推荐系统中用 Agent 重构特征管道或在线服务时，可借鉴“编译测试反馈 + 规格冻结再审计”流程，减少人工
  review 负担。

  - **成本与耗时参考**：三天、2430美元完成无 oracle 的跨文件架构级重构，适合用于长期欠维护的推荐系统模块解耦，但需注意该案例无人工执行前实际运行验证，仍需谨慎评估风险。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：大型代码库架构重构常缺乏测试 oracle，人工审查成本高，增量重构不可行，传统做法倾向重写。本研究探索 AI 编码 Agent 在规格优先协议下完成此类任务。

**方法关键点**：
- 规格优先：Agent 先形式化目标行为规格，经 14 轮细化审计，不断对照源码验证规格准确性。
- 原子实现：冻结规格后一次性实施变更，配合编译/测试反馈循环。
- 验证循环：17 轮审计代码与冻结规格一致性，收敛标准为连续两轮验证审计零发现。
- 全程无人工代码审查，无预存 oracle。

**关键结果数字**：
- 代码库 717,725 行 TypeScript，3,648 文件；任务拆除 UI 面板生存期不变量，使流式生成可关闭后重连不丢失不重复。
- 变更触及 189 文件（31 新增），两 commits 共 288 文件，34,770 插入，16,422 删除。
- 31 轮审计共纠正 201 处缺陷；无人工执行前软件行为符合规格。
- 耗时 3 天，成本 2,430 美元；发布 1,500+ 页完整规格与原始会话日志作为证据。
