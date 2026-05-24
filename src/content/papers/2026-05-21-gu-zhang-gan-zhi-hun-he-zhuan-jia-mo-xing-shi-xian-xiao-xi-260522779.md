---
title: 'FAME: Failure-Aware Mixture-of-Experts for Message-Level Log Anomaly Detection'
title_zh: 故障感知混合专家模型实现消息级日志异常检测
authors:
- Huanchi Wang
- Zihang Huang
- Yifang Tian
- Kristina Dzeparoska
- Hans-Arno Jacobsen
- Alberto Leon-Garcia
affiliations:
- University of Toronto
arxiv_id: '2605.22779'
url: https://arxiv.org/abs/2605.22779
pdf_url: https://arxiv.org/pdf/2605.22779
published: '2026-05-21'
collected: '2026-05-24'
category: LLM
direction: 日志异常检测 · 混合专家
tags:
- Log Anomaly Detection
- Mixture-of-Experts
- LLM
- Few-shot
- Message-level
- Lightweight Router
one_liner: 用LLM离线划分故障域并少量标注，训练轻量路由与专家模型，实现高效消息级异常检测。
practical_value: '- **离线LLM + 轻量在线路由**：业务监控中可先用LLM离线分析日志模板、划分故障类别，再将轻量路由器和专家模型部署到线上，实现实时异常检测，避免每次调用LLM的高成本。

  - **少样本标注策略**：每条模板至多标注K条行即可推导二元正常/异常标签，减少76倍标注量，适用于电商系统海量非结构化日志，快速冷启动异常检测。

  - **未见事件ID泛化**：FAME能检测86.3%未见事件ID的异常，解决模板漂移问题，适合动态变化的推荐/Agent系统。

  - **故障域感知路由**：MoE架构将不同故障模式分配给不同专家，可借鉴到电商多子系统下的异常定位，通过路由结果直接显式故障域，加速根因分析。'
score: 6
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有日志异常检测多基于会话或窗口，需人工排查整组日志，粒度过粗。消息级检测可精确到具体行，但面临模板歧义（同一模板即对应正常和异常）、故障来源异构、以及行级标注成本巨大。直接用LLM逐行检测成本过高。

**方法要点**：FAME框架分三步：(1) 用LLM离线分析各事件模板，每条模板至多标注K条行，自动推导二元正常/异常标签并选取典型示例；(2) LLM提出将模板划分到不同故障域，再通过认证步骤验证合理性；(3) 训练轻量路由器与各领域专家模型，仅用少量标注即可，部署时路由器实时选择专家，输出异常预测及故障域标签。

**关键结果**：在BGL数据集上，仅K=100标注下F1达98.16，标注量减少76倍，并检测到86.3%未见事件ID的异常。在Thunderbird上达到F1=99.95，召回率完美。
