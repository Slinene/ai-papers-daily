---
title: Reward-Guided Autoregressive Graph Generation for Efficient Multi-Agent Communication
  Topology Design
title_zh: 奖励引导的自回归图生成实现高效多智能体通信拓扑设计
authors:
- Poomphob Suwannapichat
- Boonyarit Changaival
- Caesar Wu
- Pascal Bouvry
affiliations:
- University of Luxembourg
- King Mongkut's University of Technology Thonburi
arxiv_id: '2608.20099'
url: https://arxiv.org/abs/2608.20099
pdf_url: https://arxiv.org/pdf/2608.20099
published: '2026-08-20'
collected: '2026-08-21'
category: MultiAgent
direction: 奖励引导的多智能体拓扑生成优化
tags:
- Multi-Agent Systems
- Graph Generation
- RLHF
- Token Efficiency
- Topology Design
- GRPO
one_liner: 在ARG-Designer基础上引入奖励引导训练和图级奖励模型，生成更稀疏多智能体拓扑，平均降token 20.5%且保持精度
practical_value: '- 在需要多 agent 协作的业务流程（如搜索意图拆解、选品+文案+审核 pipeline）中，可直接复用「生成拓扑 + 奖励模型
  + Best-of-N 选择」的架构：用已有正确/错误执行记录训练 reward model，在线采样多个候选拓扑选 reward 最高者执行，额外开销很小，但能显著降低
  token 成本。

  - 奖励函数设计采用层级权重：任务完成(0.6) > agent 数量(0.3) > 边数量(0.1)，且各项归一化到 [0,1]，保证正确性优先；对于有明确监督信号、可验证结果的业务任务（如多步骤排序、问答、代码生成）可直接套用这种
  scalar reward。

  - 用 GNN（GraphSAGE）编码拓扑结构：节点特征拼接角色 embedding + query embedding + 结构特征，训练出的 reward
  model 可跨任务/跨角色共享，新 agent role 无需重新训练生成器，适合多业务域快速迁移。

  - 推理阶段引入 Best-of-N 采样选图，只增加拓扑设计器的采样和打分开销，相比 LLM 调用成本可忽略；对高 QPS、成本敏感的场景，这是很实际的 token
  节省手段。'
score: 8
source: arxiv-cs.LG
depth: full_pdf
---

**动机**  
LLM-based Multi-Agent Systems（MAS）靠多 agent 协作提升复杂推理性能，但代价是显著增加的 token 消耗。ARG-Designer 将 MAS 通信拓扑设计重构为自回归图生成，从零构建有向无环图；但其监督似然目标只拟合训练中见过的拓扑，没有显式激励生成更稀疏、更高效的结构。  

**方法关键点**  
- 引入 Reward-Guided Autoregressive Graph Generation（RGA-Designer），借鉴 RLHF/RLVR，用可验证奖励替代人工反馈。  
- 奖励模型：两阶段 GraphSAGE 编码节点特征（角色 embedding + query embedding + 结构特征），全局池化后 MLP 输出标量 reward；奖励函数将任务完成（λc=0.6）、agent 数（λV=0.3）、边数（λE=0.1）归一化到 [0,1]，并用 Bradley-Terry 偏好对训练；pass/pass 偏好对降权至 0.1。  
- 策略优化：在预训练 ARG-Designer 生成器上做 GRPO 在线微调，用群体相对优势，KL 约束靠近参考模型；推理时采用 Best-of-5 采样选 reward 最高的拓扑。  

**关键实验**  
在 GSM8K、AQuA、MultiArith、SVAMP、HumanEval、MMLU 六个基准上，以 Qwen3-4B 为底座，对比 Vanilla、G-Designer、AgentPrune、AgentDropout、ARG-Designer。RGA 平均准确率 87.80±0.60，与 ARG 的 87.55±0.49 基本持平（无显著差异）；平均 token 消耗 3032±205，比 ARG 的 3815±124 降低 20.5%，在五个基准上统计显著，仅 MultiArith 因模板化问题无显著压缩空间。消融表明 full 方法优于去掉 reward model 或 Best-of-N 的变体。  

**最值得记住的一句话**  
将「任务完成 + 结构紧凑」同时编码进可学习的图级奖励模型，能显式引导拓扑生成器在保持精度的前提下压缩多智能体结构，比纯似然目标更有效。
