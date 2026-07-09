---
title: Interpretable Uncertainty for Adaptive Retrieval and Reasoning in Question
  Answering
title_zh: 面向可解释 QA 的自适应检索与推理不确定性框架
authors:
- Ritajit Dey
- Iadh Ounis
- Graham McDonald
affiliations:
- University of Glasgow
arxiv_id: '2607.07380'
url: https://arxiv.org/abs/2607.07380
pdf_url: https://arxiv.org/pdf/2607.07380
published: '2026-07-08'
collected: '2026-07-09'
category: RAG
direction: 不确定性估计 · 自适应检索与推理
tags:
- RAG
- Uncertainty Estimation
- LLM
- Interpretability
- Question Answering
one_liner: 利用 LLM 隐藏状态分解不确定性，以单次前向高效估计，按信号自适应触发 RAG 或推理
practical_value: '- **对话式推荐/客服中的自适应检索**：根据用户查询的模型内部不确定性，自动判断是知识不足（触发商品知识库 RAG）还是模糊冲突（启动推理链澄清），避免盲目调用。

  - **低延迟在线服务**：从隐藏状态单次前向计算不确定性，比多步提示或自一致性方法更轻量，适合高并发推荐问答场景。

  - **多策略稳健响应**：区分知识缺失与知识冲突，设计不同分支处理（如“查商品” vs “反问用户”），提升 agent 回答的可靠性。

  - **用户可感知的置信度**：显式的不确定性信号可转化为界面提示（如“正在为你搜索准确信息”），增强用户信任与体验。'
score: 7
source: arxiv-cs.IR
depth: abstract
---

**动机**：LLM 在 QA 中易产生幻觉且决策过程不透明；RAG 可提升事实性，但何时触发检索与推理通常依赖黑盒策略或多步推理，效率低且难以解释。

**方法**：提出一种不确定性感知的自适应 QA 框架，直接从 LLM 内部隐藏状态估计两种互补的不确定性信号——知识不足（应检索）与知识模糊/冲突（应推理）。该方法只需单次前向传播，无需额外提示或多轮；根据阈值得分，系统动态触发 RAG 或加强推理步骤，整个过程基于可解释的显式信号。

**结果**：框架在多种 QA 设置中验证，能有效区分需要检索与需要推理的场景，降低不必要的检索开销，同时提高答案的事实一致性与透明性。具体消融实验表明，分解不确定性比单一不确定性指令能更精准地驱动策略选择。
