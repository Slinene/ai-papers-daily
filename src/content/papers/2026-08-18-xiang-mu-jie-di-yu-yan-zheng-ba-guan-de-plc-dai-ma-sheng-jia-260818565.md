---
title: 'SemaPLC: A Project-Grounded, Verification-Gated Agent Harness for PLC Code
  Generation'
title_zh: 项目接地与验证把关的 PLC 代码生成 Agent 框架 SemaPLC
authors:
- Yanlun Tu
- Huacan Wang
- Ziyue Zhou
- Jie Zhou
- Ningyan Zhu
- Ge Chen
- Wangyi Chen
- Tengfei Zhou
- Yifan Zhou
- Dasheng Yang
affiliations:
- Midea AIRC
- KUKA
- Shanghai Jiao Tong University
- Zhejiang University
arxiv_id: '2608.18565'
url: https://arxiv.org/abs/2608.18565
pdf_url: https://arxiv.org/pdf/2608.18565
published: '2026-08-18'
collected: '2026-08-21'
category: Agent
direction: Agent 校验驱动代码生成
tags:
- Agent
- Verification-Gated
- PLC
- Code Generation
- Runtime Evaluation
one_liner: 提出以外部验证为完成条件的 Agent harness，在 PLC 代码生成上运行时得分显著超越基线
practical_value: '- 将任务完成条件从 LLM 自我判断改为可执行的外部 checker（spec 校验、编译、运行时 trace 对比）作为 gate，只有日志确认通过才停止，能显著提升生成质量，尤其在动态运行时指标上。

  - 分层验证思路可迁移到推荐/Agent 生成场景：spec 匹配、离线静态检查、线上仿真或 replay 动态评估三层 gate，动态层最能区分方法优劣。

  - 项目 grounding 做法：给 LLM 提供完整项目树、接口定义、技能库等结构化上下文，而不是孤立生成，电商推荐中可类比为提供商品图谱、用户序列、业务约束等上下文。

  - 动态评测比静态打分更能暴露问题，建议在推荐 Agent 或生成式推荐评估中增加线上仿真/真实 A/B 指标，避免只看离线静态分。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 已能生成独立 PLC 程序单元，但能否集成到现有 PLC 项目并正确运行，此前测试有限。静态评分难以反映真实可用性。  
**方法**：SemaPLC 是一个项目接地、验证把关的 Agent harness。它结合项目树、FB 接口、I/O 摘要和 PLC 技能库作为 grounded context，内部循环生成代码，但只有外部检查确认 spec 合规、编译通过、真实运行时行为匹配后才声明任务完成。  
**结果**：在 117 个独立 POU 任务上，7 个模型的严格验证通过率平均 72.6%，为最高。在 65 个需要集成到真实项目的任务上，集成编译、静态行为、动态行为均值均最高。动态行为区分度最大：基线动态分 22.4–31.4，SemaPLC 达 52.2。  
**结论**：执行而非静态评分才是生成控制逻辑是否真正可用的忠实测试。
