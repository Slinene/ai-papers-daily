---
title: 'GRADRAG: Cross-Component Prompt Adaptation for Coordinated Multi-Agent RAG'
title_zh: GRADRAG：跨组件提示自适应实现多智能体RAG协同优化
authors:
- Paolo Pedinotti
- Enrico Santus
affiliations:
- Bloomberg
arxiv_id: '2607.21324'
url: https://arxiv.org/abs/2607.21324
pdf_url: https://arxiv.org/pdf/2607.21324
published: '2026-07-23'
collected: '2026-07-24'
category: RAG
direction: RAG多智能体协同优化
tags:
- RAG
- MultiAgent
- Prompt Optimization
- Cross-Component
- Evaluation Feedback
- Early Stopping
one_liner: 将RAG管线建模为计算图，通过评估反馈反向传播优化上游Agent提示，取得12-15pp偏好提升
practical_value: '- 在搭建电商搜索/问答的Agent管线（检索→证据整理→答案生成→校验）时，可借鉴GRADRAG的**图结构建模与反馈传播**思路：设计一个Evaluator对最终答案和中间证据打分，将结构化反馈反向发送给上游Agent（如检索改写、图谱构建），用少量迭代联合优化全链路，避免各环节独立调优导致的误差累积。

  - **两阶段自适应提示机制**可直接落地：先让Evaluator输出简短评判（太模糊/证据不足），再据此生成具体改进指令，带动检索和生成prompt的自动更新，降低人工设计prompt的成本。

  - **早停策略**对成本敏感的场景很有价值：Evaluator判断答案质量达标即可终止迭代，避免无效重试，平衡效果与推理开销。

  - 该方法与底层检索范式解耦，支持chunk-based和graph-based两种模式，因此无论团队当前用的是语义分块检索还是知识图谱增强，都能叠加GRADRAG提升多步推理效果，适配迁移成本低。'
score: 7
source: arxiv-cs.CL
depth: abstract
---

**动机**：现有RAG系统多采用多智能体协作，但优化往往局限在单个组件（如查询改写、证据过滤或生成自省），缺少跨组件的联合反馈机制。上游错误会向下游传导，单一环节调优难以根除。

**方法关键点**：
- 将RAG管线抽象为**计算图**，节点为自适应Agent（检索器、图谱构建器、回答生成器），边为数据与反馈流。
- 引入**Evaluator**，对下游答案和支撑证据进行评判，输出简短判语和结构化诊断（如“检索信息不完整/实体缺失”）。
- **Prompt Optimizer**根据Evaluator的诊断，生成具体改进指令，迭代更新上游Agent的提示词，实现跨组件协同进化。
- 支持早停：Evaluator判断答案满意后立即终止优化，节省推理资源。
- 适用于两种检索范式：基于chunk的IRCoT式查询精化，以及基于实体-关系图谱的迭代式检索。

**关键结果**：在SQUALITY和QMSUM数据集上，GRADRAG相比仅优化最终生成器的one-step refinement基线，在LLM成对比较中获得**12-15个百分点的净偏好胜率**，且多数收益在**2轮迭代内**实现，收敛迅速。
