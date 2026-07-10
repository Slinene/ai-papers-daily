---
title: Who Broke the System? Failure Localization in LLM-Based Multi-Agent Systems
title_zh: 谁破坏了系统？LLM多智体系统故障定位框架
authors:
- Yufei Xia
- Anjun Gao
- Yueyang Quan
- Zhuqing Liu
- Minghong Fang
affiliations:
- University of Louisville
- University of North Texas
arxiv_id: '2607.07989'
url: https://arxiv.org/abs/2607.07989
pdf_url: https://arxiv.org/pdf/2607.07989
published: '2026-07-08'
collected: '2026-07-10'
category: MultiAgent
direction: 多智体故障定位与归因
tags:
- failure localization
- multi-agent systems
- LLM
- agent attribution
- confidence-aware aggregation
- lightweight fine-tuning
one_liner: 提出AgentLocate，通过信心感知的多评估者聚合与轻量微调，精准定位多智能体系统中的故障代理与起始步骤
practical_value: '- **多Agent编排的诊断工具**：在电商搜索、广告投放、推荐决策等多Agent协作场景中，可复用AgentLocate的框架快速定位哪个子Agent出错（如意图解析Agent、召回策略Agent、排序融合Agent）以及最早偏离步骤，加速问题排查与迭代。

  - **轻量微调提升归因准确率**：利用失败轨迹与独立评估者的反馈对LLM评判器进行LoRA微调，业务侧可基于线上Bad Case构建反馈数据，持续优化内部的Agent责任判定模型，降低人工复盘成本。

  - **信心感知的投票策略**：多评估者投票时用信心分数加权聚合，避免低质量评判干扰，可直接借鉴用于业务Agent链路中的监控、校验或A/B实验评估，提升自动评分的可靠性。

  - **轨迹级代码化隔离定位**：论文将故障定位分解为“哪个Agent”和“哪一步”两个子问题，工程上可据此设计Agent执行日志的自动分析模块，结合最终任务成败信号生成诊断报告，嵌入实时预警系统。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：基于LLM的多Agent系统因长周期交互与紧耦合行为，失败时难以追溯责任Agent与导致不可逆偏误的首个关键步骤，传统调试方法效率低下。

**方法**：提出AgentLocate，将故障定位分解为两步：先由LLM评判器初步判定责任Agent，再用多个独立评估者从不同视角（如动作、环境反馈）二次验证，评估结果通过信心感知加权聚合形成最终归因。收集的反馈以LoRA方式轻量微调评判器，迭代提升归因质量。

**关键结果**：在两个覆盖不同任务、Agent配置、轨迹长度的基准上，AgentLocate无论识别责任Agent（F1提升7-12%）还是定位起始故障步骤（步骤准确率提升6-10%）均显著优于现有方法，且Token消耗与运行时间保持高效。
