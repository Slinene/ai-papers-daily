---
title: 'Cluster, Route, Escalate: Cascaded Framework for Cost-Aware LLM Serving'
title_zh: 聚类、路由、升级：面向成本感知LLM服务的级联框架
authors:
- Yasmin Moslem
- Magdalena Kacmajor
- Vasudevan Nedumpozhimana
- Ammar Abbas
- Solmaz Panahi
- David Lynch
- Zhuangzhuang Nie
- Alexandros Agapitos
- Aleksandar Milenovic
- Hongmeng Song
affiliations:
- ADAPT Centre, Trinity College Dublin
- Huawei Research
arxiv_id: '2606.27457'
url: https://arxiv.org/abs/2606.27457
pdf_url: https://arxiv.org/pdf/2606.27457
published: '2026-06-24'
collected: '2026-06-30'
category: LLM
direction: LLM级联路由与成本优化
tags:
- cascaded inference
- model routing
- cost-aware serving
- clustering
- quality estimation
- LLM deployment
one_liner: 两阶段级联：先聚类查询并分配最经济的模型，再通过质量估计升级低质量输出，仅用正确性标签实现成本-准确率优化。
practical_value: '- **多规格LLM路由架构**：电商搜索/推荐/Agent场景常有多型号LLM（如7B/70B）。可借鉴其两阶段设计：先用聚类将用户查询按意图分组，如“商品咨询”“售后投诉”“闲聊”，为每组预先分配性价比最高的模型，避免大模型过载。

  - **成本可控的升级机制**：第二阶段质量估计与升级，类似于推荐系统的粗排-精排级联。可为Agent生成的回复或推荐文案设置质量阈值，当小模型输出置信度低时自动升级到大模型重生成，在保证准确率的同时节省平均推理成本。

  - **仅需任务正确性标签，适合快速迭代**：框架无需额外的人工标注偏好或优劣对比，只需业务已有的正确/错误标签（如用户满意度标签、客服解决状态）即可离线调优λ和升级阈值，降低维护成本。

  - **可解释的超参数控制运营权衡**：通过λ显式设定推理成本预算，业务运营可灵活调整“省钱-更准”的天平，无需重新训练或手动配置路由规则，模型池变化时自动适配。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：生产环境中部署LLM面临准确率与成本的权衡。通常做法是固定使用一个模型，要么大模型浪费在简单查询上，要么小模型处理不了复杂案例。现有路由系统往往需要复杂标注，没有在推理成本预算下联合优化路由与后验质量升级。

**方法关键点**：
- **第一阶段：聚类+路由**。对输入查询进行K-means聚类，为每个聚类分配一个成本效益最高的模型。路由决策分数 = 错误率 + λ × 推理成本，λ作为可解释超参数控制成本预算，离线调优。
- **第二阶段：质量估计级联**。对第一阶段输出进行质量评估，若判定为低质量，则自动升级至更强模型重新生成。这确保仅困难或低置信度查询使用昂贵模型。
- 训练仅需任务正确性标签（二值标签），无需偏好标注，且当模型池变化时无需重新配置，只需更新模型特征。

**关键结果**：在多数据集测试中，级联系统保持了最强模型97-99%的准确率，同时显著降低每个输出token的平均时间（TPOT），实现了成本有效的高质量服务。
