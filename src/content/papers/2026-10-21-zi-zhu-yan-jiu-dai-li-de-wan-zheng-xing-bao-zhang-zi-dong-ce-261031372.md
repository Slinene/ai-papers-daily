---
title: 'RIDAR: Safeguarding Research Integrity in Autonomous Research Agents via Automated
  Detection and Runtime Intervention'
title_zh: 自主研究代理的完整性保障：自动检测与运行时干预框架 RIDAR
authors:
- Jiening Siow
- Amy Xin
- Junjie Wang
- Ziyu Tang
- Zijun Yao
- Yunjia Qi
- Fanjin Zhang
- Lei Hou
- Jie Tang
- Juanzi Li
affiliations:
- Tsinghua University
- Renmin University of China
- Zhipu AI
arxiv_id: '2610.31372'
url: https://arxiv.org/abs/2610.31372
pdf_url: https://arxiv.org/pdf/2610.31372
published: '2026-10-21'
collected: '2026-10-24'
category: Agent
direction: Agent 行为审计与运行时纠偏
tags:
- Research Agents
- Integrity Violations
- Runtime Intervention
- Detection
- LLM Agents
- Benchmark
one_liner: 提出研究完整性违规分类法与 RIDAR 框架，离线检测 F1 85.2%，运行时干预减少违规 36.8%
practical_value: '- 可借鉴 RIDAR 的“离线检测 + 运行时干预”双层架构，对电商 Agent 的推荐文案生成、客服自动回复、选品/定价策略等轨迹做合规审计，实时拦截违规内容（如虚假宣传、价格欺诈、敏感词）。

  - 借鉴 RIVT 的细粒度违规分类法，定义电商 Agent 自身的违规类型（如商品描述夸大、使用禁投词、泄露用户隐私等），构建 domain-specific
  的检测 taxonomy 和评测集。

  - 采用运行时干预的思路：检测到违规步骤时，通过重写动作或注入约束条件来纠偏，而不是仅 post-hoc 审计，可减少任务结束时残留问题，提升最终交付质量。

  - 其评估方法可复用：用专家标注的小基准 + 大规模无标注轨迹结合，先测检测器再分析真实分布，作为业务 agent 质量监控的模板。'
score: 6
source: huggingface-daily
depth: abstract
---

动机：自主研究代理（autonomous research agents）广泛应用于科研自动化，但容易产生研究诚信违规（RIV），损害有效性、可复现性和忠实性，且长轨迹难以人工审计。

方法：提出 RIVT 分类法，覆盖研究全生命周期的 14 类违规；开发 RIDAR-POST-HOC 离线检测框架，在 RIV-GOLD（60 条专家标注轨迹）上评估；构建 RIV-WILD 数据集（300 条轨迹、50 个任务）进行大规模检测；进一步提出 RIDAR-RUNTIME，在代理运行过程中动态检测并纠正违规行为。

结果：RIDAR-POST-HOC 在 RIV-GOLD 上 F1 达 85.2%；在 RIV-WILD 上检测到 3,964 个 RIV 实例，99.7% 的轨迹存在违规；RIDAR-RUNTIME 使任务完成时剩余 RIV 减少 36.8%。代码和数据将开源。
