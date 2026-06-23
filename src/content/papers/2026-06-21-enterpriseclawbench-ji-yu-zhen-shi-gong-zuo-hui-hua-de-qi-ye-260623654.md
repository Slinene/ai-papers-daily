---
title: 'EnterpriseClawBench: Benchmarking Agents from Real Workplace Sessions'
title_zh: 'EnterpriseClawBench: 基于真实工作会话的企业智能体基准'
authors:
- Jincheng Zhong
- Weizhi Wang
- Che Jiang
- Kai Tian
- Zhenzhao Yuan
- Junlin Yang
- Dianqiao Lei
- Kaiyan Zhang
affiliations:
- Horizon Research
- Frontis.AI
arxiv_id: '2606.23654'
url: https://arxiv.org/abs/2606.23654
pdf_url: https://arxiv.org/pdf/2606.23654
published: '2026-06-21'
collected: '2026-06-23'
category: Agent
direction: 企业智能体评估 · 多维度基准
tags:
- Agent Benchmark
- Enterprise Agent
- Multi-dimensional Evaluation
- Real-world Sessions
- LLM
- Harness-Model Combination
one_liner: 从真实企业Agent日志构建852个可复现任务的基准，揭示评估必须报告多维度指标而非单一得分
practical_value: '- 评估生产环境Agent时，必须同时上报**成本、运行时间、产物交付质量、视觉质量**等，不能只依赖文本匹配得分，这在推荐系统Agent评估（如自动素材生成、文案产出）中同理。

  - 基准构建采用**从真实日志恢复任务**的方式，可以借鉴到电商/广告Agent的离线评估：从历史操作会话中抽取场景，脱敏后重构可复现的测试集，防止数据泄露。

  - **硬规则（hard rules）与技能子类（skill subclasses）**的标注思路，可用于业务Agent的细分能力诊断，例如区分“商品标题生成”与“广告文案创意”的不同技能域，针对性优化。

  - 工具-模型组合（harness–model combination）的评测模式提醒我们：Agent框架选择（类似推荐系统中的召回/排序通道）对最终效果影响显著，需要联合调优而非单独比拼模型。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：现有Agent评测常在简化基准上进行，无法反映真实企业场景中需要处理异构文件、调用工具、交付业务成果的复杂要求。企业Agent实际运行数据丰富但未被系统利用。

**方法**：收集真实工作场所Agent会话日志，经过清洗、复原环境 fixture、改写提示并标注角色类别、技能子类、硬性规则和语义评分标准，构建包含852个任务的EnterpriseClawBench基准。因涉及企业内部数据，不公开基准本身，而是贡献构造流程与评估协议。评估时采用多种 harness（Codex、ClaudeCode等）与模型（GPT-5.5、Sonnet 4.6等）组合，测量得分、成本、运行时间等维度。

**结果**：在120个任务的Lite子集上，最佳组合（Codex + GPT-5.5）仅获0.663分，平均分48.6%。成本差异巨大（最便宜组合¥14/任务，最贵¥701/任务），运行时间也从1.0分钟到14.0分钟不等。排名显示，提升得分往往伴随高成本，且不同harness对同一模型影响显著，强调多维评估的必要性。
