---
title: 'Doomed from the Start: Early Abort of LLM Agent Episodes via a Recall-Controlled
  Probe Cascade'
title_zh: 从开始就已注定：基于召回控制探针级联的LLM Agent尽早终止
authors:
- Kai Ruan
- Zihe Huang
- Ziqi Zhou
- Qianshan Wei
- Xuan Wang
- Hao Sun
affiliations:
- Gaoling School of Artificial Intelligence, Renmin University of China
- Institute of Computing Technology, Chinese Academy of Sciences
- Duke University
- Institute of Automation, Chinese Academy of Sciences
- College of Computer Science, Zhejiang University
arxiv_id: '2607.06503'
url: https://arxiv.org/abs/2607.06503
pdf_url: https://arxiv.org/pdf/2607.06503
published: '2026-07-07'
collected: '2026-07-08'
category: Agent
direction: LLM Agent早停与推理节省
tags:
- Early Abort
- LLM Agents
- Probe Cascade
- Recall Control
- Inference Compute Saving
- Failure Prediction
one_liner: 提出召回受控的探针级联，在Agent早期预测失败并终止，节省47%推理计算且保证全局存活率
practical_value: '- 对于线上LLM Agent系统（如购物助手、自动广告投放），可集成轻量探针级联，每轮动态判断是否提前终止，大幅降低无效推理成本（节省约37%-47%）。

  - 采用**分布无关的校准门控**与**联合搜索每轮召回预算**，能提供用户指定的全局召回率保证（如90%），满足业务对成功轨迹存活率的严苛要求，避免单门累积误杀。

  - 探针仅读取隐藏层激活，无需行为特征，工程实现简单；并且实验表明加行为特征无额外收益，确认隐藏状态已包含足够信息，减少特征工程开销。

  - 提供的样本复杂度分析方法，可指导业务方评估数据是否足够支撑高召回目标，避免盲目承诺。'
score: 7
source: arxiv-cs.AI
depth: abstract
---

**动机**：LLM Agent在多步任务中常走入注定失败的轨迹，但会继续消耗大量推理计算直至超时或错误返回。研究发现，失败可在早期（第一轮）从Agent内部表征中预测，而外部行为观测几乎无异于随机。

**方法**：提出一个**召回率受控的探针级联**。每轮训练一个轻量探针（线性分类器）读取隐藏层激活，预测该回合最终是否失败；然后构建级联门控：每轮设置一个校准阈值，只有通过当前门的轨迹继续执行。关键创新在于对每轮召回率进行**联合搜索**，使得所有成功轨迹以用户指定的全局概率（如90%）通过所有门，确保端到端的存活率保证。这门控是分布无关的，无需假设模型分布。

**结果**：在TextCraft任务上，针对Qwen-2.5-7B和Llama-3.2-3B两个Agent，级联可满足90%至97%的召回目标。在90%目标下，Qwen节省47.1%±10.3%推理计算，Llama节省37.2%±8.8%，比最佳单门策略高1.6-1.7倍。仅使用行为特征的级联节省减半，加入行为特征后无额外提升，证明隐藏状态已包含行为信息。最后，论文量化了认证高召回目标的样本复杂度，为实践提供理论指导。
