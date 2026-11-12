---
title: Ensemble Routing for Prompt-Adaptive Cost-Aware LLM Inference
title_zh: 面向提示自适应的成本感知 LLM 集成路由
authors:
- Saul Urso
- Emanuele Carlini
- Patrizio Dazzi
- Matteo Mordacchini
affiliations:
- Institute of Information Science and Technologies, CNR, Italy
- Institute of Informatics and Telematics, CNR, Italy
- University of Pisa, Department of Computer Science, Italy
arxiv_id: '2611.10193'
url: https://arxiv.org/abs/2611.10193
pdf_url: https://arxiv.org/pdf/2611.10193
published: '2026-11-05'
collected: '2026-11-12'
category: LLM
direction: LLM 路由与成本优化
tags:
- LLM Routing
- Cost-Aware Inference
- Ensemble Routing
- Prompt-Adaptive
- Model Selection
- Inference Optimization
one_liner: PISA 用软聚类+能力预测实现提示自适应单模型路由，PISA-E 无需集成训练即可动态选择集成组合并调节成本质量偏好
practical_value: '- 在电商/广告的 LLM 推理场景（商品文案生成、query 改写、对话式推荐）可按 prompt 难度动态路由到不同规模模型，用软聚类+模型能力预测器代替固定路由，节省推理成本并保持质量。

  - PISA-E 的 cost-quality 偏好可在推理时调节且无需重训，适合不同业务场景（高价值用户 vs 低延迟场景）灵活切换质量/成本权衡。

  - 集成路由无需为 ensemble 单独训练，只用可计算的 ensemble-success surrogate 和候选选择，新增模型时工程接入成本低。

  - 可借鉴其评估方式：同时看 cost-performance hypervolume 和 OOD 表现，避免只优化单点指标导致线上泛化差。'
score: 6
source: huggingface-daily
depth: abstract
---

**动机**：LLM 服务需在响应质量与推理成本间做平衡，但传统路由为每个 prompt 只选一个模型，固定集成又无法适配不同请求的成本质量需求。

**方法关键点**：
- PISA 通过软聚类成员关系和模型特定预测器估计各模型在给定 prompt 上的能力，实现提示自适应单模型路由。
- PISA-E 在此基础上联合选择集成组成与基数，引入显式 cost-quality 偏好，且该偏好可在推理时调整而无需重训。
- 提出可计算的 ensemble-success surrogate 和高效候选选择，使集成路由无需集成专属训练。

**关键结果**：
- 在四个 LLM routing benchmark 的 ID/OOD 设置下，PISA 取得单模型路由中最高的 macro-average cost-performance hypervolume。
- 质量优先时，PISA-E 的 macro-average task performance 最高，ID/OOD 分别超出最强集成基线 2.09 和 2.87 个百分点。
- 在低 cost 运行点，PISA-E 仍超过最强集成基线，同时平均推理成本分别降低约 36% 和 25%。
