---
title: 'MODE-RAG: Manifold Outlier Diagnosis and Energy-based Retrieval-Augmented
  Generation Evaluation'
title_zh: MODE-RAG：流形异常诊断与能量检索增强生成评估的多智能体系统
authors:
- Zehang Wei
- Jiaxin Dai
- Jiamin Yan
- Xiang Xiang
affiliations:
- School of Computer Science & Tech, Huazhong University of Science and Technology
- School of AI and Automation, Huazhong University of Science and Technology
arxiv_id: '2606.17449'
url: https://arxiv.org/abs/2606.17449
pdf_url: https://arxiv.org/pdf/2606.17449
published: '2026-06-16'
collected: '2026-06-18'
category: MultiAgent
direction: 多模态RAG幻觉缓解 · 基于能量的多智体评估
tags:
- Multimodal RAG
- Hallucination Mitigation
- Multi-Agent
- Variational Free Energy
- Monte Carlo Tree Search
- Energy-based Model
one_liner: 提出多智能体系统MODE-RAG，利用变分自由能和注意力动态门控，结合MCTS与logit惩罚来缓解多模态RAG幻觉
practical_value: '- **Agent 动态门控机制**：基于内部注意力状态和变分自由能（VFE）的风险评估，可用于电商搜索/推荐Agent的决策路由，对高不确定性查询触发更严格的事实核查，避免复杂推理链中的错误传播。

  - **MCTS 因果推导修正**：在推荐解释生成或对话式推荐中，可借鉴蒙特卡洛树搜索对候选推荐理由进行因果验证，减少编造理由（sycophancy），提升可信度。

  - **Logit 扰动惩罚逢迎**：对于倾向生成迎合用户的虚假解释，通过在解码时施加针对性的logit惩罚，可迁移到对话Agent中抑制讨好性幻觉。

  - **多智体协作流水线**：Correction和Overseer Agent 的分工模式可复用到搜索推荐系统的后处理流程，例如事实核对Agent、格式化稳定Agent，增强最后输出可靠性。'
score: 7
source: arxiv-cs.MM
depth: abstract
---

**动机**：多模态RAG系统在利用外部视觉知识回答复杂问题时，常产生跨模态幻觉、因果虚构和逢迎（sycophancy）。现有缓解方法存在“干预悖论”——刚性规则会破坏正确生成，而不加干预则会导致逻辑错误累积。为此，需要一套能动态评估高风险的机制。

**方法**：提出多智能体系统 MODE-RAG，核心是利用变分自由能（VFE）和模型内部注意力状态作为风险信号，动态决定是否触发干预。高风险查询被路由到五个阶段专属Agent：使用蒙特卡洛树搜索（MCTS）进行严格的因果推导，并在logit层施加扰动以惩罚逢迎行为；Correction Agent 确保输出格式稳定，Overseer Agent 进行事后事实核查。整套流程形成“感知-检索-推理-生成”全生命周期的幻觉抑制。此外，作者从MultiVent数据集衍生出高挑战子集ModeVent，用于客观评估。

**关键结果**：在ModeVent上的实验表明，MODE-RAG能显著降低幻觉率和逻辑虚构现象，提升多模态RAG系统的鲁棒性，且动态门控策略避免了不必要的干预，保留正确生成的能力。
