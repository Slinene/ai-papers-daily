---
title: 'HarnessRisk: A Lifecycle-Oriented Benchmark for Agent Harness Safety'
title_zh: HarnessRisk：面向智能体骨架全生命周期的安全基准
authors:
- Yajing Bai
- Jinhao Duan
- Jie Peng
- Xianfeng Wu
- Sijia Liu
- Song Wang
- Tianlong Chen
affiliations:
- University of North Carolina at Chapel Hill
- University of Central Florida
- Michigan State University
arxiv_id: '2608.17597'
url: https://arxiv.org/abs/2608.17597
pdf_url: https://arxiv.org/pdf/2608.17597
published: '2026-08-17'
collected: '2026-08-20'
category: Eval
direction: Agent harness安全评测
tags:
- Agent Safety
- Benchmark
- Harness
- LLM Agents
- Security Evaluation
one_liner: 提出覆盖六阶段的Agent harness安全基准，发现配置阶段最脆弱且风险识别不保证安全行动
practical_value: '- 在电商搜索/推荐Agent中，将安全评测拆分为配置、扩展、运行、状态持久化、动作控制、恢复六个阶段，可快速定位风险面——尤其配置阶段（权限、工具白名单等）最为脆弱，工程上应默认最小权限并定期审计。

  - 不要只依赖模型的风险识别能力，需在harness层增加强制拦截/审计：论文显示90%以上检测到风险仍可能保持较高攻击成功率，识别与安全行动之间存在显著gap。

  - 构建内部安全回归集时，可采用“良性用户目标+不可信工作流嵌入对抗指令”的构造方式，覆盖不同harness与模型配置，同时统计Utility、ASR、Persistence、Detection多维指标。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：LLM作为Agent部署时，安全依赖Agent harness对工具、状态、权限、外部动作的管理，但现有安全基准只针对单一攻击机制或局部设置，难以全面比较安全失败如何在不同harness职责中涌现。

**方法**：HarnessRisk将Agent harness安全生命周期组织为六个阶段：Harness Configuration、Capability Extension、Runtime Operation、State Persistence、Action Control、Incident Recovery。构建128个沙箱案例，每个案例将良性用户目标与嵌入不可信工作流中的对抗指令配对。采用Utility、Attack Success Rate、Persistence、Detection四个指标评测轨迹。在3个harness、6个语言模型、14种模型与harness配置上实验。

**关键结果**：攻击成功率从12.6%到80.9%，Utility保持在75.0%-97.6%。Harness Configuration是所有三个harness中最脆弱阶段，攻击可通过在授权工作流内修改安全敏感参数成功。显式风险识别不总能导致安全行动：某些配置在超过90%的运行中检测到风险但仍保持较高攻击成功率。结果表明需要跨多个harness职责、在部署的模型和配置层面评估Agent安全。
