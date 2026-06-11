---
title: 'SkillHarm: Lifecycle-Aware Skill-Based Attacks via Automated Construction'
title_zh: SkillHarm：面向技能生命周期的 Agent 攻击基准与自动化构建
authors:
- Yuting Ning
- Zhehao Zhang
- Yash Kumar Lal
- Boyu Gou
- Junyi Li
- Weitong Ruan
- Chentao Ye
- Rahul Gupta
- Diyi Yang
- Yu Su
affiliations:
- The Ohio State University
- Amazon AGI
- Stanford University
arxiv_id: '2606.02540'
url: https://arxiv.org/abs/2606.02540
pdf_url: https://arxiv.org/pdf/2606.02540
published: '2026-05-31'
collected: '2026-06-11'
category: Agent
direction: Agent 技能安全 · 自动化攻击基准
tags:
- Agent Security
- Skill Poisoning
- Benchmark
- Attack Taxonomy
- Automated Construction
one_liner: 首个覆盖技能使用生命周期的攻击基准，揭示固定与自变异投毒下 Agent 高达 86.3% 的攻击成功率
practical_value: '- **Agent 技能安全评估框架**：若业务中使用第三方 Agent 技能（例如 MCP tools、自定义插件），可借鉴
  SkillHarm 定义的 12 类风险（数据管线、系统环境、自主决策）和两种投毒场景（FPP/SMP），设计内部红队测试用例。

  - **自变异投毒（SMP）的低噪音特性**：SMP 初始不触发恶意行为，在后续复用中才爆发，与电商推荐中长效特征污染攻击类似，可思考如何在模型更新、特征缓存下设计延迟投毒检测机制。

  - **自动化投毒样本生成管道**：AutoSkillHarm 利用自然语言 harness 驱动 coding agent 批量构造攻击样本，可迁移到业务安全测试中，自动生成针对内部
  Agent 流水线的变异攻击数据。

  - **失败模式提示防御盲区**：论文发现攻击失败多因 Agent 未执行投毒文件而非真正抵抗力，启示工程防御需加强技能加载阶段的静态分析（如 manifest
  检查、沙箱预执行），而非仅依赖运行时行为监控。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：Agent 在工作流中隐式信任并执行第三方技能，形成高危攻击面。现有研究只在单次任务中评估投毒，且风险列表随意，缺乏系统性和生命周期视角。

**方法**：提出 SkillHarm 基准，覆盖技能加载、使用到复用的完整生命周期。定义两类攻击场景：**固定载荷投毒 (FPP)** 直接污染技能包，一旦调用即触发；**自变异投毒 (SMP)** 首次执行静默篡改持久化内容，在后续复用中延时危害。风险分类基于受损 Agent 组件，细化出 12 种类型（数据管线、系统环境、自主性）。为规模化构建，设计了 AutoSkillHarm 管道，用自然语言 harness 指导 coding agent 自动生成攻击样本，最终产出了 879 个覆盖 71 个技能的样本。

**结果**：当前 Agent 在 FPP 下攻击成功率高达 86.3%，SMP 下 69.3%。分析揭示大量攻击失败是因 Agent 未真正加载或未执行投毒文件，而非主动防御；现有防御手段仍无法可靠缓解威胁。
