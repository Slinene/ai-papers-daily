---
title: Learning the Cost of Reliable Inference
title_zh: 学习可靠推理成本：LLM采购路由机制
authors:
- Dimitrios Rontogiannis
- Ander Artola Velasco
- Manuel Gomez Rodriguez
affiliations:
- Max Planck Institute for Software Systems
arxiv_id: '2609.28322'
url: https://arxiv.org/abs/2609.28322
pdf_url: https://arxiv.org/pdf/2609.28322
published: '2026-09-23'
collected: '2026-09-24'
category: Other
direction: LLM 采购路由 · 拍卖机制设计
tags:
- LLM routing
- reverse auction
- cost estimation
- quality threshold
- marketplace
one_liner: 设计基于反向第二价格拍卖的LLM路由平台，在保证质量阈值下动态选择成本最优供应商，节省10%-71%成本
practical_value: '- 在电商/广告多模型路由中，可借鉴“质量阈值+成本竞标”框架：平台先定义业务质量指标（如转化率、准确率），各模型/供应商按成本投标，路由时只选满足阈值且报价最低的，避免固定价格浪费。

  - 反向第二价格拍卖的激励相容设计可迁移到内部多模型/多服务核算：让各团队或供应商按真实边际成本报价，平台按次低价结算，能诱导真实成本暴露，优化全局预算分配。

  - 实验结果（价差10-71%）说明按任务动态选择比固定定价省大量成本，可在推理网关/Agent工具调用中维护模型质量估计与成本表，实时切换。

  - 注意：平台需在线学习质量，可采用Bandit或贝叶斯更新，将质量不确定性与成本竞标结合，不能仅靠一次性评估。'
score: 7
source: arxiv-cs.LG
depth: abstract
---

**动机**：现有LLM平台按token固定收费，但提供商服务成本与用户获得质量高度依赖具体任务，固定价格无法反映竞争，用户难以获得最优价格。

**方法关键点**：设计采购平台，通过反向第二价格拍卖顺序路由查询；提供商按平均服务成本投标，第二价格机制激励真实报价；平台在线学习各提供商质量，逐步将查询路由给满足质量阈值且成本最低的供应商。

**结果**：在Llama和Qwen多模型、数学推理与问答基准上，最具成本竞争力供应商的定价边际在10%–71%之间，表明现有固定价格市场存在显著低效，平台能帮用户实现最大节省。
