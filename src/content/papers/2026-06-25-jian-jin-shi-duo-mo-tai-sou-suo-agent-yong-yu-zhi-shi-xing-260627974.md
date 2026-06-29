---
title: ProMSA:Progressive Multimodal Search Agents for Knowledge-Based Visual Question
  Answering
title_zh: 渐进式多模态搜索 Agent 用于知识型视觉问答
authors:
- ZhengXian Wu
- Hangrui Xu
- Kai Shi
- Zhuohong Chen
- Yunyao Yu
- Chuanrui Zhang
- Zirui Liao
- Jun Yang
- Zhenyu Yang
- Haonan Lu
affiliations:
- OPPO AI Center
- Tsinghua University
- Nanyang Technological University
arxiv_id: '2606.27974'
url: https://arxiv.org/abs/2606.27974
pdf_url: https://arxiv.org/pdf/2606.27974
published: '2026-06-25'
collected: '2026-06-29'
category: Agent
direction: Agent 自适应多模态检索
tags:
- KB-VQA
- Multimodal Agent
- RLHF
- Tool Use
- Retrieval-Augmented
- Progressive Search
one_liner: 提出自适应调用图文检索的 Agent，并通过长度与深度归一化的 RL 优化搜索策略
practical_value: '- **自适应检索流程**：Agent 迭代选择图像搜索、文本搜索或停止，带工具调用预算和去重。在电商商品搜索中，可构建类似 Agent，根据用户意图动态决定查询商品图库还是文本描述库，避免固定
  top-k 带来冗余。

  - **序列级 RL 训练归一化**：TN-GSPO 根据生成长度与工具交互深度归一化更新，缓解冗长交互被过度惩罚的问题。训练推荐对话 Agent 时，可借鉴此目标，平衡回答质量与多轮交互开销。

  - **两阶段训练范式**：先拒绝采样 SFT 学习合法工具调用格式，再 RL 优化。对落地 Agent 很有参考意义：先用人工或规则筛选合法 action 轨迹微调，再线上
  RL 提升策略。

  - **去重机制**：对已检索内容去重，避免重复调用工具。在召回或多路检索场景中，可加入类似历史感知的去重，减少无效请求，提升效率。'
score: 7
source: huggingface-daily
depth: abstract
---

**动机**：知识型视觉问答（KB-VQA）需要结合图像理解与外部知识，但现有方法固定检索流程和 top-k，无法适应不同推理阶段的信息需求。为提高检索效率与最终答案准确率，需要一个能动态决策检索类型与时机、并在预算内工作的 Agent。

**方法**：ProMSA 将 KB-VQA 建模为多模态搜索 Agent。给定图像和问题，Agent 在每个推理步骤可选调用图像搜索、文本搜索或停止，所有工具调用受总预算限制，并引入去重避免重复检索。训练分两步：（1）拒绝采样 SFT：用规则筛选格式正确的工具调用轨迹，微调基座 VLM 学会输出有效动作；（2）TN-GSPO 强化学习：设计序列级 RL 目标，根据生成序列的长度和工具交互深度对梯度更新进行归一化，防止模型偏好过短或过长的交互。

**结果**：在 E-VQA 和 InfoSeek 基准上，ProMSA 相比强 RAG 和 Agent 基线（如 CRaaS、Searcho1）在检索 Recall 和端到端 VQA 准确率上均有一致提升；消融实验验证了动态预算、去重及 TN-GSPO 归一化的有效性。
