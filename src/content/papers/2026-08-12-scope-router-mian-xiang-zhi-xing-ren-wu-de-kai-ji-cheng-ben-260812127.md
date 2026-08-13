---
title: 'SCOPE-Router: Cost-Aware Open-Set VLM Routing for Execution-Oriented Tasks'
title_zh: SCOPE-Router：面向执行任务的开集成本感知 VLM 路由
authors:
- Tao Yu
- Yifei Qu
- Zhiqing Cui
- Pengfei Zhou
- Zhongtian Luo
- Yujia Yang
- Shenghua Chai
- Haopeng Jin
- Zhenghao Zhang
- Xinming Wang
affiliations:
- CASIA
- UCAS
- NUS
- Tencent
arxiv_id: '2608.12127'
url: https://arxiv.org/abs/2608.12127
pdf_url: https://arxiv.org/pdf/2608.12127
published: '2026-08-12'
collected: '2026-08-13'
category: LLM
direction: VLM 路由 · 成本感知训练
tags:
- VLM Routing
- Cost-Aware
- Open-Set
- Calibration
- Execution-Oriented
- CRM+RCCR
one_liner: 提出执行导向 VLM 路由基准、开集双塔路由器和成本感知训练目标 CRM+RCCR，在三个基准上取得最佳 Rank Score
practical_value: '- 成本感知损失设计可直接迁移：将成本编码为连续 relevance target（正确且最低成本为 1，其他正确模型按成本指数衰减，错误为
  0），用 per-pair BCE 替代 softmax CE，避免多正样本梯度稀释。在电商多模型路由（如广告创意生成、商品文案生成）中可直接替换现有分类器 loss，无需改动模型结构。

  - 开集模型接入方案实用：为新模型构造行为 profile（正确性、成本、价值向量、语义汇总向量），只需在约 1024 条校准集上跑一次即可加入路由池，无需重新训练路由器。适合频繁上线新模型/版本的业务场景，如
  LLM API 切换或多模态内容审核模型更新。

  - 混合校准集选择策略可复用：按 50% 随机 + 30% 诊断（模型分歧度 + 成本分布）+ 20% 多样性（聚类质心）采样，有限的标注预算下最大化 profile
  区分度。在自建路由训练数据或评估模型互补性时可以参考。

  - 架构无关的 CRM+RCCR 目标可试用于现有路由系统：论文实证在 RouterDC、ZOOTER、CosineCls、VLC 四个不同架构上 Rank Score
  提升 1.25–6.21 点。若业务已有简单的 query-model 打分器，可将该 loss 嵌入微调，获得成本感知能力。'
score: 8
source: arxiv-cs.CV
depth: full_pdf
---

**动机**
VLM 正从简单 VQA 走向代码生成、工具调用 Agent、多步网络搜索等执行导向任务，但现有 VLM 路由基准仅覆盖传统 VQA，且训练目标忽视成本、开集能力不足（新模型需重训）。论文针对这三个局限提出解决方案。

**方法关键点**
1. **VLM-ExecRouterBench**：首个执行导向 VLM 路由基准，覆盖 Code、Agentic、Search 三域，34k 样本、11 个候选模型，价格跨近两个数量级；每个样本统一为 Routing Input / Execution Context / Verification Rule 三元组。
2. **SCOPE-Router**：双塔路由，query 和模型行为 profile 映射到共享路由空间计算相似度。Profile 由混合校准集（随机 50% + 诊断 30% + 多样性 20%）构建，融合行为向量（正确性、归一化成本、价值向量、汇总统计）和语义向量（正确/错误/高效样本的聚合嵌入）。新模型只需在 1024 条校准集上跑一次即可生成 profile 加入路由，无需重训路由器。
3. **CRM+RCCR 成本感知训练目标**：CRM 定义连续相关性目标 R = 1[正确]·exp(-λ·α·(cost - min_cost))，采用每对独立 BCE 而非 softmax CE，消除多正样本稀释；RCCR 基于路由偏好相似性拉近 query 表示，增强跨 query 泛化。该损失架构无关，可直接替换现有路由器 loss。

**关键结果**
在 VLM-ExecRouterBench、VL-RouterBench、MMR-Bench 三个基准上 Rank Score 均排名第一；OOD 设置下领先第二名 1.84 分，双重 OOD 开集评估领先 6.75 分。CRM+RCCR 应用于 RouterDC、ZOOTER、CosineCls、VLC 四个不同架构，Rank Score 提升 1.25–6.21 点。在 VLM-ExecRouterBench 上，相比最强单一模型基线，成本降低 85%，准确率仅降 5.21 个百分点。

**最值得记住的一句话**：将成本编码进连续 relevance 目标并用 per-pair BCE 取代 softmax，是成本感知路由的关键；开集接入只需校准集 profile，无需重训。
